from typing import Dict
from flask import Blueprint, jsonify, request, Response
from flask.typing import ResponseReturnValue
from prometheus_client import Histogram, Counter, generate_latest, CONTENT_TYPE_LATEST


request_duration_histogram = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration by path, method, and status code',
    ['path', 'method', 'status_code'],
)

request_count = Counter(
    'http_requests_total',
    'Total number of HTTP requests by path and method',
    ['path', 'method'],
)



bucket_blueprint = Blueprint("zones", __name__)

data: Dict[str, bytes] = {}


@bucket_blueprint.route("/buckets/<id>")
def get_bucket(id: str) -> ResponseReturnValue:
    with request_duration_histogram.labels(path="/buckets/<id>", method="GET").time():
        request_count.labels(path="/buckets/<id>", method="GET").inc()
        if id in data.keys():
            return data.get(id), 200, {"Content-Type": "application/octet-stream"}
        
        return jsonify({"error": "not found"}), 404, {"Content-Type": "application/json"}

@bucket_blueprint.route("/buckets/<id>", methods=["PUT"])
def put_bucket(id: str) -> ResponseReturnValue:
    with request_duration_histogram.labels(path="/buckets/<id>", method="PUT").time():
        request_count.labels(path="/buckets/<id>", method="PUT").inc()
        data[id] = request.get_data()
        return "", 200

@bucket_blueprint.route("/buckets/<id>", methods=["DELETE"])
def delete_bucket(id: str) -> ResponseReturnValue:
    with request_duration_histogram.labels(path="/buckets/<id>", method="DELETE").time():
        request_count.labels(path="/buckets/<id>", method="DELETE").inc()
        if id in data.keys():
            data.pop(id, None)
            return "", 500

    return jsonify({"error": "bad request"}), 400, {"Content-Type": "application/json"}

@bucket_blueprint.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
