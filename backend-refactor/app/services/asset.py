"""Asset service layer."""
from typing import List, Dict, Any
from app.db.asset import load_assets
from app.db.signal import load_signals

class AssetService:
    def get_all_assets(self) -> List[Dict[str, Any]]:
        """Get all assets with their signals."""
        assets_raw = load_assets()
        signals_raw = load_signals()
        
        return self._merge_assets_and_signals(assets_raw, signals_raw)

    def post_asset(self) -> List[Dict]:
        """Placeholder for posting an asset."""
        # Implementation would go here
        return []

    def _merge_assets_and_signals(self, assets: List[Dict], signals: List[Dict]) -> List[Dict]:
        """Internal helper method to handle the business logic."""
        # 1. Group signals by AssetId for O(1) lookup
        signals_lookup = {}
        for sig in signals:
            aid = sig.get("AssetId")
            if aid not in signals_lookup:
                signals_lookup[aid] = []
            
            signals_lookup[aid].append({
                "id": sig.get("SignalId"),
                "global_id": sig.get("SignalGId"),
                "name": sig.get("SignalName"),
                "unit": sig.get("Unit")
            })

        # 2. Map signals back to assets (Filtering out "Ghost Assets")
        result = []
        for asset in assets:
            asset_id = asset.get("AssetID")
            result.append({
                "asset_id": asset_id,
                "signals": signals_lookup.get(asset_id, [])
            })
            
        return result
