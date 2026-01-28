"""Asset service layer."""
import logging
from typing import List, Dict, Any

from app.db.asset import load_assets
from app.db.signal import load_signals

logger = logging.getLogger(__name__)

class AssetService:
    """Service for managing assets."""

    def get_all_assets(self) -> List[Dict[str, Any]]:
        """Get all assets with their signals."""
        logger.debug("Fetching all assets and signals")

        assets_raw = load_assets()
        signals_raw = load_signals()

        logger.debug(
            "Loaded raw data",
            extra={
                "assets_count": len(assets_raw),
                "signals_count": len(signals_raw),
            },
        )

        result = self._merge_assets_and_signals(assets_raw, signals_raw)

        logger.info(f"Successfully merged {len(result)} assets")

        return result

    def post_asset(self) -> List[Dict]:
        """Placeholder for posting an asset."""
        # Implementation would go here
        return []

    def _merge_assets_and_signals(self, assets: List[Dict], signals: List[Dict]) -> List[Dict]:
        """Internal helper method to handle the business logic."""
        logger.debug("Merging assets and signals")

        # Group signals by AssetId for O(1) lookup
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

        # Map signals back to assets (Filtering out "Ghost Assets")
        result = []
        for asset in assets:
            asset_id = asset.get("AssetID")
            result.append({
                "asset_id": asset_id,
                "signals": signals_lookup.get(asset_id, [])
            })
            
        return result
