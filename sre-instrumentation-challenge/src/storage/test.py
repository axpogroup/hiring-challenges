from unittest.mock import patch
from storage import app

import json
import storage


@patch("storage.bucket.data", {})
def test_get_bucket_not_found():
    response = app.test_client().get("/api/buckets/1")
    assert response.status_code == 404

    payload = json.loads(response.data)
    assert payload["error"] == "not found"


@patch("storage.bucket.data", {"1": "hello"})
def test_get_bucket_found():
    with patch("storage.bucket.data", {"1": "hello"}):
        response = app.test_client().get("/api/buckets/1")

        assert response.status_code == 200
        assert response.data == b"hello"


@patch("storage.bucket.data", {})
def test_put_bucket():
    response = app.test_client().put("/api/buckets/1", data="hello")

    assert response.status_code == 200
    assert storage.bucket.data == {"1": b"hello"}


@patch("storage.bucket.data", {})
def test_delete_bucket_not_found():
    response = app.test_client().delete("/api/buckets/1")
    assert response.status_code == 400

    payload = json.loads(response.data)
    assert payload["error"] == "bad request"


# TODO: Add test for test_delete_bucket_found
