# Jira Ticket Lister (FastAPI)

This app exposes an endpoint that lists Jira tickets for project `ITHUB` from `https://axpo.atlassian.net`.


> **Security**: 
All API endpoints are fully protected by Entra ID authentication. Every request must include a valid Bearer token issued by the configured tenant. Unauthenticated requests will be rejected with a `401 Unauthorized` response. 
The `/teams/webhook` endpoint is additionally secured with HMAC-SHA256 signature verification, ensuring only genuine requests originating from the configured Teams Outgoing Webhook are accepted.

## 1) Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) Configure environment variables

```bash
export JIRA_BASE_URL="https://axpo.atlassian.net"
export JIRA_EMAIL="hub@axpo.com"
export JIRA_API_TOKEN="<your-jira-api-token>"
export JIRA_PROJECT_KEY="ITHUB"
export ENTRA_TENANT_ID="<entra-tenant-id>"
export ENTRA_AUDIENCE="<api-application-id-uri-or-client-id>"
export ENTRA_ISSUER="https://login.microsoftonline.com/<entra-tenant-id>/v2.0"
export DATABASE_URL="sqlite:///./jira_comments.db"
```

Notes:
- `ENTRA_AUDIENCE` must match the `aud` claim in your access token.
- If you omit `ENTRA_ISSUER`, the app derives it from `ENTRA_TENANT_ID`.
- Only SQLite is supported for `DATABASE_URL` right now.

## 3) Run

```bash
uvicorn app.main:app --reload
```

## 4) Test

Get an Entra access token for your API and call `/tickets`:

```bash
curl -H "Authorization: Bearer <entra-access-token>" \
	"http://127.0.0.1:8000/tickets?max_results=20"
```

Create a Jira comment and store it in the local DB audit table:

```bash
curl -X POST \
	-H "Authorization: Bearer <entra-access-token>" \
	-H "Content-Type: application/json" \
	-d '{"body":"This comment was posted via API."}' \
	"http://127.0.0.1:8000/tickets/ITHUB-123/comments"
```

Swagger UI is available at:
- http://127.0.0.1:8000/docs
