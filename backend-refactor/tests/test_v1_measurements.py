"""Tests for v1 measurements endpoints."""
from app.services.measurement import MeasurementService

def test_get_measurements_success(client):
    app = client.app
    
    class MockMeasurementService:
        def get_measurements(self, signal_ids, from_date, to_date):
            return [
                {
                    "signal_id": "S1",
                    "timestamp": "2024-01-01T10:00:00",
                    "value": 115.9581,
                    "unit": "kV"
                }
            ]

    app.dependency_overrides[MeasurementService] = MockMeasurementService
    
    # Pass aliases 'from' and 'to' in the query string
    params = {
        "signal_ids": "S1",
        "from": "2024-01-01T00:00:00",
        "to": "2024-01-02T00:00:00"
    }
    response = client.get("/api/v1/measurements", params=params)
    
    assert response.status_code == 200
    assert response.json()[0]["value"] == 115.9581
    app.dependency_overrides.clear()

def test_get_measurements_invalid_range(client):
    # 'from' is after 'to', should trigger the HTTPException in the router
    params = {
        "signal_ids": "S1",
        "from": "2024-01-02T00:00:00",
        "to": "2024-01-01T00:00:00"
    }
    response = client.get("/api/v1/measurements", params=params)
    
    assert response.status_code == 400
    assert "Invalid date range" in response.json()["detail"]

def test_get_signal_stats_success(client):
    app = client.app
    
    class MockStatsService:
        def calculate_signal_stats(self, signal_id, from_date, to_date):
            return {
                "signal_id": signal_id,
                "from_date": from_date.isoformat(),
                "to_date": to_date.isoformat(),
                "count": 2,
                "mean": 20.0,
                "min": 10.0,
                "max": 30.0,
                "median": 20.0,
                "std_dev": 14.14
            }

    app.dependency_overrides[MeasurementService] = MockStatsService
    
    params = {"from": "2024-01-01T00:00:00", "to": "2024-01-02T00:00:00"}
    response = client.get("/api/v1/measurements/stats/S1", params=params)
    
    assert response.status_code == 200
    data = response.json()
    assert data["signal_id"] == "S1"
    assert data["mean"] == 20.0
    app.dependency_overrides.clear()
