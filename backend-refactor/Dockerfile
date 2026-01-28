# ---- Base image ----
FROM python:3.11-slim

# ---- Environment ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- Default logging level ----
ENV LOG_LEVEL=WARNING

# ---- Workdir ----
WORKDIR /app

# ---- System dependencies (minimal) ----
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ---- Install Python dependencies ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy application code ----
COPY app ./app

# ---- Expose port ----
EXPOSE 8000

# ---- Run app ----
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
