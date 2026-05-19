import os
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException, Query, Request
from pydantic import BaseModel, Field

from app.db import init_db, store_comment_log
from app.teams import notify_comment, parse_reply, verify_teams_hmac

app = FastAPI(title="Jira Ticket Lister", version="1.0.0")


@app.on_event("startup")
async def startup_event() -> None:
    init_db()


class JiraClient:
    def __init__(self) -> None:
        self.base_url = os.getenv("JIRA_BASE_URL", "https://axpo.atlassian.net").rstrip("/")
        self.email = os.getenv("JIRA_EMAIL", "hub@axpo.com")
        self.token = os.getenv("JIRA_API_TOKEN", "JWDOIWAJDWD2djaisodjas")
        self.project_key = os.getenv("JIRA_PROJECT_KEY", "ITHUB")

        if not self.email or not self.token:
            raise RuntimeError(
                "Missing Jira credentials. Set JIRA_EMAIL and JIRA_API_TOKEN environment variables."
            )

    async def add_comment(self, issue_key: str, comment_text: str) -> dict[str, Any]:
        url = f"{self.base_url}/rest/api/3/issue/{issue_key}/comment"
        payload = {
            "body": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": comment_text}],
                    }
                ],
            }
        }

        timeout = httpx.Timeout(20.0, connect=10.0)
        async with httpx.AsyncClient(timeout=timeout, auth=(self.email, self.token)) as client:
            response = await client.post(url, json=payload)

        if response.status_code == 401:
            raise HTTPException(status_code=401, detail="Jira authentication failed. Check email/token.")

        if response.status_code >= 400:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Jira API error when adding comment: {response.text}",
            )

        return response.json()

    async def list_tickets(self, max_results: int = 50) -> dict[str, Any]:
        url = f"{self.base_url}/rest/api/3/search/jql"
        params = {
            "jql": f"project = {self.project_key} ORDER BY created DESC",
            "maxResults": max_results,
            "fields": "summary,status,assignee,issuetype,priority,created,updated",
        }

        timeout = httpx.Timeout(20.0, connect=10.0)
        async with httpx.AsyncClient(timeout=timeout, auth=(self.email, self.token)) as client:
            response = await client.get(url, params=params)

        if response.status_code == 401:
            raise HTTPException(status_code=401, detail="Jira authentication failed. Check email/token.")

        if response.status_code >= 400:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Jira API error: {response.text}",
            )

        data = response.json()
        issues = []
        for issue in data.get("issues", []):
            fields = issue.get("fields", {})
            assignee = fields.get("assignee") or {}
            status = fields.get("status") or {}
            issue_type = fields.get("issuetype") or {}
            priority = fields.get("priority") or {}

            issues.append(
                {
                    "key": issue.get("key"),
                    "summary": fields.get("summary"),
                    "status": status.get("name"),
                    "assignee": assignee.get("displayName"),
                    "issue_type": issue_type.get("name"),
                    "priority": priority.get("name"),
                    "created": fields.get("created"),
                    "updated": fields.get("updated"),
                }
            )

        return {
            "project": self.project_key,
            "total": data.get("total", len(issues)),
            "count": len(issues),
            "tickets": issues,
        }


class JiraCommentIn(BaseModel):
    body: str = Field(min_length=1, max_length=10000)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tickets")
async def tickets(
    max_results: int = Query(default=50, ge=1, le=100),
) -> dict[str, Any]:
    try:
        jira = JiraClient()
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return await jira.list_tickets(max_results=max_results)


@app.post("/tickets/{issue_key}/comments")
async def create_jira_comment(
    issue_key: str,
    comment: JiraCommentIn,
) -> dict[str, Any]:
    try:
        jira = JiraClient()
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    jira_response = await jira.add_comment(issue_key=issue_key, comment_text=comment.body)
    jira_comment_id = str(jira_response.get("id", ""))
    if not jira_comment_id:
        raise HTTPException(status_code=502, detail="Jira response missing comment id.")

    requested_by = None

    local_id = store_comment_log(
        issue_key=issue_key,
        comment_body=comment.body,
        jira_comment_id=jira_comment_id,
        requested_by=requested_by,
    )

    try:
        await notify_comment(
            issue_key=issue_key,
            comment_body=comment.body,
            requested_by=requested_by,
        )
        teams_notified = True
    except Exception:
        teams_notified = False

    return {
        "status": "created",
        "issue_key": issue_key,
        "jira_comment_id": jira_comment_id,
        "db_record_id": local_id,
        "teams_notified": teams_notified,
    }


@app.post("/teams/webhook")
async def teams_outgoing_webhook(request: Request) -> dict[str, Any]:
    """Endpoint called by the Teams Outgoing Webhook.

    Teams sends the message to this URL and expects a JSON response with a
    ``type`` and ``text`` field to display as a bot reply.

    Reply format expected from the Teams user:
        ITHUB-123: your comment text
    """
    payload = await request.json()
    raw_text: str = payload.get("text") or ""
    sender: str = (
        (payload.get("from") or {}).get("name")
        or (payload.get("from") or {}).get("aadObjectId")
        or "Teams user"
    )

    parsed = parse_reply(raw_text)
    if not parsed:
        return {
            "type": "message",
            "text": (
                "\u274c Could not parse your reply. "
                "Use the format: `ITHUB-123: your comment text`"
            ),
        }

    issue_key, comment_text = parsed

    try:
        jira = JiraClient()
    except RuntimeError as exc:
        return {"type": "message", "text": f"\u274c Jira config error: {exc}"}

    try:
        jira_response = await jira.add_comment(issue_key=issue_key, comment_text=comment_text)
    except HTTPException as exc:
        return {"type": "message", "text": f"\u274c Failed to post Jira comment: {exc.detail}"}

    jira_comment_id = str(jira_response.get("id", ""))

    store_comment_log(
        issue_key=issue_key,
        comment_body=comment_text,
        jira_comment_id=jira_comment_id,
        requested_by=sender,
    )

    return {
        "type": "message",
        "text": f"\u2705 Comment posted to {issue_key} by {sender}.",
    }
