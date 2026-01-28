"""Tests for v1 assets endpoints."""
from app.services.asset import AssetService

def test_get_assets_success(client):
    # 1. Get the app instance from the fixture
    app = client.app
    
    # 2. Create a Mock Service
    class MockAssetService:
        def get_all_assets(self):
            return [{"asset_id": "A1", "signals": []}]

    # 3. Inject the Mock
    app.dependency_overrides[AssetService] = MockAssetService
    
    # 4. Execute request
    response = client.get("/api/v1/assets/")
    
    # 5. Assertions
    assert response.status_code == 200
    assert response.json()[0]["asset_id"] == "A1"
    
    # 6. Clean up
    app.dependency_overrides.clear()

def test_get_assets_empty(client):
    app = client.app
    
    class EmptyAssetService:
        def get_all_assets(self):
            return []
    
    app.dependency_overrides[AssetService] = EmptyAssetService
    
    response = client.get("/api/v1/assets/")
    
    assert response.status_code == 200
    assert response.json() == []
    
    app.dependency_overrides.clear()

def test_get_assets_no_signals(client):
    app = client.app
    
    class NoSignalAssetService:
        def get_all_assets(self):
            return [{"asset_id": "A2", "signals": []}]
    
    app.dependency_overrides[AssetService] = NoSignalAssetService
    
    response = client.get("/api/v1/assets/")
    
    assert response.status_code == 200
    assert response.json()[0]["signals"] == []
    
    app.dependency_overrides.clear()

def test_get_assets_large_dataset(client):
    app = client.app
    
    class LargeAssetService:
        def get_all_assets(self):
            return [{"asset_id": f"A{i}", "signals": []} for i in range(1000)]
    
    app.dependency_overrides[AssetService] = LargeAssetService
    
    response = client.get("/api/v1/assets/")
    
    assert response.status_code == 200
    assert len(response.json()) == 1000
    
    app.dependency_overrides.clear()
