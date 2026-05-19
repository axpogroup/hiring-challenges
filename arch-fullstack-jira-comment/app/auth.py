import os
import time
from typing import Any

import httpx
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

bearer_scheme = HTTPBearer(auto_error=True)

_JWKS_CACHE: dict[str, Any] = {"keys": [], "expires_at": 0.0}


def _build_issuer(tenant_id: str) -> str:
    return f"https://login.microsoftonline.com/{tenant_id}/v2.0"


async def _get_jwks() -> list[dict[str, Any]]:
    now = time.time()
    if _JWKS_CACHE["keys"] and _JWKS_CACHE["expires_at"] > now:
        return _JWKS_CACHE["keys"]

    tenant_id = os.getenv("ENTRA_TENANT_ID")
    if not tenant_id:
        raise HTTPException(status_code=500, detail="Missing ENTRA_TENANT_ID environment variable.")

    discovery_url = (
        f"https://login.microsoftonline.com/{tenant_id}/v2.0/.well-known/openid-configuration"
    )

    timeout = httpx.Timeout(20.0, connect=10.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        discovery_response = await client.get(discovery_url)
        if discovery_response.status_code >= 400:
            raise HTTPException(
                status_code=500,
                detail=f"Unable to fetch Entra discovery document: {discovery_response.text}",
            )

        jwks_uri = discovery_response.json().get("jwks_uri")
        if not jwks_uri:
            raise HTTPException(status_code=500, detail="Discovery document missing jwks_uri.")

        jwks_response = await client.get(jwks_uri)
        if jwks_response.status_code >= 400:
            raise HTTPException(
                status_code=500,
                detail=f"Unable to fetch Entra JWKS: {jwks_response.text}",
            )

    keys = jwks_response.json().get("keys", [])
    _JWKS_CACHE["keys"] = keys
    _JWKS_CACHE["expires_at"] = now + 3600
    return keys


async def require_entra_auth(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict[str, Any]:
    token = credentials.credentials
    tenant_id = os.getenv("ENTRA_TENANT_ID")
    audience = os.getenv("ENTRA_AUDIENCE")
    issuer = os.getenv("ENTRA_ISSUER") or (_build_issuer(tenant_id) if tenant_id else None)

    if not tenant_id or not audience or not issuer:
        raise HTTPException(
            status_code=500,
            detail="Missing Entra configuration. Set ENTRA_TENANT_ID, ENTRA_AUDIENCE, and optionally ENTRA_ISSUER.",
        )

    try:
        header = jwt.get_unverified_header(token)
        kid = header.get("kid")
    except jwt.InvalidTokenError as exc:
        raise HTTPException(status_code=401, detail="Invalid bearer token header.") from exc

    keys = await _get_jwks()
    key_data = next((k for k in keys if k.get("kid") == kid), None)
    if not key_data:
        raise HTTPException(status_code=401, detail="Token signing key not found.")

    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key_data)

    try:
        payload = jwt.decode(
            token,
            key=public_key,
            algorithms=["RS256"],
            audience=audience,
            issuer=issuer,
        )
    except jwt.InvalidTokenError as exc:
        raise HTTPException(status_code=401, detail=f"Token validation failed: {exc}") from exc

    return payload
