# Assets API

A production-ready FastAPI application for monitoring industrial signals and assets. This project has been refactored into a modular, scalable architecture using industry-best practices.

## 🚀 Key Features

- **Modular Architecture**: Application Factory pattern for better lifecycle management.
- **Recursive Routing**: Versioned API paths for seamless legacy support.
- **Dependency Injection**: Decoupled service layer for high testability.
- **Robust Validation**: Pydantic schemas for strict request/response data integrity.
- **Observability**: Structured logging.
- **Containerized**: Optimized Docker build.

---

## 🛠️ Project Structure

```
.
├── app/
│   ├── api/             # API Router Gateway (v1/v2)
│   ├── core/            # Configuration (Pydantic Settings)
│   ├── db/              # Data access layer
│   ├── schemas/         # Pydantic models (DTOs)
│   ├── services/        # Business logic (Service Layer)
│   ├── utils/           # Helper functions
│   ├── factory.py       # FastAPI App Factory
│   └── main.py          # Entry point
├── data/                # Source JSON/CSV data
├── tests/               # Pytest suite
└── Dockerfile           # Docker container build config
```

## ⚙️ Getting Started

**Prerequisites**
- Python 3.10+
- Virtual Environment (recommended)

**Installation**
1. Clone the repository and navigate to the root:
    ```bash
    cd backend-refactor
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Linux/Mac:
    source .venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
**Running the Application**

Start the development server with auto-reload:
```bash
python -m app.main
# OR
uvicorn app.main:app --reload
```

The API documentation will be available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Testing
The project uses `pytest` with `httpx` for integration testing and service mocking.

Run all tests:
```bash
python -m pytest
```
## 🐳 Docker Deployment
To build and run the containerized version of the API:
1. Build the image:
    ```bash
    docker build -t assets-api .
    ```
2. Run the container:
    ```bash
    docker run -p 8000:8000 assets-api
    ```
## 📊 API Endpoints (Quick Reference)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Liveness probe / Health check |
| `GET` | `/api/v1/assets` | List all assets and their signals |
| `GET` | `/api/v1/measurements` | Query signal data with `from`/`to` filters |
| `GET` | `/api/v1/measurements/stats/{id}` | Statistical analysis (mean, std_dev, etc.) |

## ⏱️ Time Spent (≈ 6 hours)

Below is an approximate breakdown of how the time was spent:

| Task | Time |
| :--- | :--- |
| **Project restructuring & cleanup** (nested routers, moving code under `app/`, removing unused modules, naming consistency) | ~2 h |
| **Data access & services** (CSV/JSON loaders, measurement range filtering, stats calculation, unit enrichment) | ~1.0 h |
| **API design & validation** (datetime parameters, router-level validation, schemas) | ~0.75 h |
| **Logging & configuration** (centralized logging, env-based levels, modern AppSettings) | ~0.75 h |
| **Dockerization** (Dockerfile, copying data folder, production defaults) | ~0.5 h |
| **Testing** (pytest setup, API tests for assets and measurements) | ~1 h |

The focus was on **production-readiness and maintainability**, rather than feature volume.

## 📝 Notes & Decisions

- Introduced a nested router architecture to separate system endpoints (`/health`) from versioned APIs (`/api/v1`).

- Kept routers thin and services focused on business logic; file-based access isolated in the db layer.

- Parsed `from` / `to` parameters directly as `datetime` and validated them at the API boundary.

- Centralized logging configuration, made log level environment-driven, and removed duplicated handlers.

- Used integration-style API tests with FastAPI’s `TestClient`.

- Docker defaults favor production-safe behavior, including logging level and bundled data.

Decisions favored **clarity, correctness, and simplicity** over over-engineering.

## ✅ What Could Be Added Next

- Database-backed persistence

- Pagination for measurements

- Caching layer

- CI pipeline (GitHub Actions)