# Storage API

This service implements a simple in-memory Storage API to put, get and delete binary data.

## Usage

1. Install dependencies `make prod` or `pip3 install -e .`
2. Run service: `make run` or `python3 run.py`

### Development Setup

1. Install dependencies `make dev` or `pip3 install -e .[dev]`
2. Run tests `make test` or `pytest storage/test.py`
3. Run service: `make watch` or `hupper -m waitress --port 5000 storage:app`

## API

### PUT /api/buckets/:id

Upload binary data for a given id:

```sh
curl --location --request PUT 'http://localhost:5000/api/buckets/1' \
--data-raw '{
    "data": "some json"
}'

```

### GET /api/buckets/:id

Get binary data for a given id:

```sh
curl --location --request GET 'http://localhost:5000/api/buckets/1'
```

### DELETE /api/buckets/:id

Delete binary data for a given id:

```sh
curl --location --request DELETE 'http://localhost:5000/api/buckets/1'
```
