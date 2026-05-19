"""Teams notification module.

Posts an Adaptive Card to a Microsoft Teams channel via an Incoming Webhook URL
every time a Jira comment is successfully created.

Also exposes HMAC validation and message parsing so that replies to the
notification card (via a Teams Outgoing Webhook) can be turned back into
Jira comments through the POST /teams/webhook endpoint.

Required environment variables:
    TEAMS_WEBHOOK_URL              — Incoming Webhook URL from the Teams channel connector.
    TEAMS_OUTGOING_WEBHOOK_SECRET  — Security token shown when you create the Outgoing Webhook
                                     in Teams (used for HMAC-SHA256 request verification).
"""

import base64
import hashlib
import hmac
import os
import re
from typing import Any

import httpx


def _webhook_url() -> str:
    url = os.getenv("TEAMS_WEBHOOK_URL")
    if not url:
        raise RuntimeError("Missing TEAMS_WEBHOOK_URL environment variable.")
    return url


# ---------------------------------------------------------------------------
# Outgoing Webhook helpers
# ---------------------------------------------------------------------------

_ISSUE_KEY_RE = re.compile(r"([A-Z][A-Z0-9_]+-\d+)")
# Expected reply format: "ITHUB-123: your comment text"
_REPLY_RE = re.compile(r"([A-Z][A-Z0-9_]+-\d+)\s*:\s*(.+)", re.DOTALL)


def verify_teams_hmac(authorization_header: str, body: bytes) -> bool:
    """Validate the HMAC-SHA256 signature Teams sends on Outgoing Webhook requests.

    Teams sets the Authorization header to ``HMAC <base64-encoded-signature>``.
    The signature is HMAC-SHA256 of the raw request body using the webhook
    security token as the key (UTF-8 encoded).
    """
    secret = os.getenv("TEAMS_OUTGOING_WEBHOOK_SECRET", "")
    if not secret:
        return False

    if not authorization_header.startswith("HMAC "):
        return False

    provided_sig = authorization_header[5:]
    key = base64.b64decode(secret)
    expected_sig = base64.b64encode(
        hmac.new(key, body, hashlib.sha256).digest()
    ).decode()
    return hmac.compare_digest(provided_sig, expected_sig)


def parse_reply(text: str) -> tuple[str, str] | None:
    """Extract (issue_key, comment) from a Teams reply.

    Accepts ``ITHUB-123: comment text`` anywhere in the message.
    Returns None if the format is not recognised.
    """
    # Strip HTML tags Teams sometimes includes
    cleaned = re.sub(r"<[^>]+>", "", text).strip()
    match = _REPLY_RE.search(cleaned)
    if not match:
        return None
    return match.group(1).strip(), match.group(2).strip()


def _build_card(issue_key: str, comment_body: str, requested_by: str | None) -> dict[str, Any]:
    """Build an Adaptive Card payload for a new Jira comment notification."""
    author = requested_by or "unknown"
    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "body": [
                        {
                            "type": "TextBlock",
                            "size": "medium",
                            "weight": "bolder",
                            "text": f"New comment on Jira issue {issue_key}",
                        },
                        {
                            "type": "FactSet",
                            "facts": [
                                {"title": "Issue", "value": issue_key},
                                {"title": "Posted by", "value": author},
                                {"title": "Reply format", "value": f"{issue_key}: your reply text"},
                            ],
                        },
                        {
                            "type": "TextBlock",
                            "text": comment_body,
                            "wrap": True,
                        },
                    ],
                },
            }
        ],
    }


async def notify_comment(
    issue_key: str,
    comment_body: str,
    requested_by: str | None,
) -> None:
    """Send a Teams notification for a newly created Jira comment.

    Raises RuntimeError if TEAMS_WEBHOOK_URL is not configured.
    Raises httpx.HTTPStatusError on 4xx/5xx webhook responses.
    """
    url = _webhook_url()
    card = _build_card(issue_key, comment_body, requested_by)

    timeout = httpx.Timeout(15.0, connect=10.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(url, json=card)
        response.raise_for_status()
