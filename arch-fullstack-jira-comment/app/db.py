import os
import sqlite3
from datetime import datetime, timezone

from fastapi import HTTPException


def _database_url() -> str:
    return os.getenv("DATABASE_URL", "sqlite:///./jira_comments.db")


def _database_path() -> str:
    database_url = _database_url()
    prefix = "sqlite:///"
    if not database_url.startswith(prefix):
        raise HTTPException(status_code=500, detail="Only sqlite DATABASE_URL is supported.")
    return database_url[len(prefix):]


def get_conn() -> sqlite3.Connection:
    return sqlite3.connect(_database_path())


def init_db() -> None:
    with get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS jira_comment_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                issue_key TEXT NOT NULL,
                comment_body TEXT NOT NULL,
                jira_comment_id TEXT NOT NULL,
                requested_by TEXT,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


def store_comment_log(
    issue_key: str,
    comment_body: str,
    jira_comment_id: str,
    requested_by: str | None,
) -> int:
    created_at = datetime.now(timezone.utc).isoformat()
    with get_conn() as conn:
        cursor = conn.execute(
            """
            INSERT INTO jira_comment_log (issue_key, comment_body, jira_comment_id, requested_by, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (issue_key, comment_body, jira_comment_id, requested_by, created_at),
        )
        conn.commit()
        if cursor.lastrowid is None:
            raise HTTPException(status_code=500, detail="Failed to store comment log record.")
        return int(cursor.lastrowid)
