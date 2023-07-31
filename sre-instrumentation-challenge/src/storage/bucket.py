from typing import Dict
from flask import Blueprint, jsonify, request, Response, Flask
from flask.typing import ResponseReturnValue
# Import prometheus_client libraries and some useful stuff
from prometheus_client import Summary, Counter, generate_latest, CONTENT_TYPE_LATEST
import time
import logging


# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


bucket_blueprint = Blueprint("zones", __name__)

data: Dict[str, bytes] = {}

# Define Prometheus metrics for request duration and request count
REQUEST_DURATION = Summary('http_request_duration_seconds', 'HTTP request duration in seconds', ['path', 'method', 'status'])
REQUEST_COUNT = Counter('http_request_count', 'HTTP request count', ['path', 'method', 'status'])

# Helper function to increment request count and record duration
def record_request_metrics(path, method, status, duration):
    REQUEST_COUNT.labels(path, method, str(status)).inc()
    REQUEST_DURATION.labels(path, method, str(status)).observe(duration)



@bucket_blueprint.route("/buckets/<id>")
def get_bucket(id: str) -> ResponseReturnValue:
    start_time = time.time()  # Record the start time of the request
    try:
        if id in data.keys():
            response = Response(data.get(id), 200, {"Content-Type": "application/octet-stream"})
        else:
            response = Response("not found", 404, {"Content-Type": "application/json"})
    except Exception as e:
        logging.error(f"Error while processing GET request: {e}")
        response = Response("internal server error", 500, {"Content-Type": "application/json"})

    # Calculate the request duration and record metrics
    duration = time.time() - start_time
    record_request_metrics(request.path, request.method, response.status_code, duration)

    return response


@bucket_blueprint.route("/buckets/<id>", methods=["PUT"])
def put_bucket(id: str) -> ResponseReturnValue:
    start_time = time.time()  # Record the start time of the request
    data[id] = request.get_data()
    try:
        data[id] = request.get_data()
        logging.info(f"Bucket {id} created")
        response = Response(f"Bucket {id} created", 200)
    except Exception as e:
        logging.error(f"Error while processing PUT request: {e}")
        response = Response("internal server error", 500, {"Content-Type": "application/json"})

    # Calculate the request duration and record metrics
    duration = time.time() - start_time
    record_request_metrics(request.path, request.method, 200, duration)

    return response


@bucket_blueprint.route("/buckets/<id>", methods=["DELETE"])
def delete_bucket(id: str) -> ResponseReturnValue:
    start_time = time.time()  # Record the start time of the request
    try:
        if id in data.keys():
            data.pop(id, None)
            logging.info(f"Bucket {id} deleted")
            response = Response(f"Bucket {id} deleted", 200)
        else:
            response = Response("bad request", 400, {"Content-Type": "application/json"})
    except Exception as e:
        logging.error(f"Error while processing DELETE request: {e}")
        response = Response("internal server error", 500, {"Content-Type": "application/json"})

    # Calculate the request duration and record metrics
    duration = time.time() - start_time
    record_request_metrics(request.path, request.method, response.status_code, duration)

    return response


# Endpoint to expose Prometheus metrics
@bucket_blueprint.route("/metrics")
def metrics():
    return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)
