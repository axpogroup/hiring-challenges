"""Utility helpers for assets."""
from typing import List, Dict

def format_asset_response(asset_data: Dict) -> Dict:
    """Format asset data for response."""
    return {
        "asset_id": asset_data.get("asset_id"),
        "signals": asset_data.get("signals", [])
    }

def FormatAssetResponse(data: Dict) -> Dict:
    """PascalCase version."""
    return format_asset_response(data)

def transform_asset(asset: Dict) -> Dict:
    """Transform asset to API format."""
    return {
        "asset_id": asset["asset_id"],
        "signals": asset["signals"]
    }

def process_asset_data(asset_info: Dict) -> Dict:
    """Process asset data."""
    # This does the same as format_asset_response but with extra steps
    aid = asset_info.get("asset_id")
    sigs = asset_info.get("signals", [])
    return {"asset_id": aid, "signals": sigs}
