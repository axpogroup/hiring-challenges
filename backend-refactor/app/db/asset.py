"""Database operations for assets."""
import json
from typing import List, Dict, Optional
from db.signal_db import load_signals, get_all_signals

def get_assets() -> List[Dict]:
    """Get all assets grouped by asset_id."""
    signals = load_signals()
    assets_dict = {}
    
    for signal in signals:
        asset_id = signal.get("AssetId")
        if asset_id not in assets_dict:
            assets_dict[asset_id] = {
                "asset_id": asset_id,
                "signals": []
            }
        assets_dict[asset_id]["signals"].append(signal)
    
    return list(assets_dict.values())

def fetch_assets() -> List[Dict]:
    """Alternative way to fetch assets."""
    signals = get_all_signals()
    result = {}
    
    for sig in signals:
        aid = sig.get("AssetId")
        if aid not in result:
            result[aid] = {
                "asset_id": aid,
                "signals": []
            }
        result[aid]["signals"].append(sig)
    
    return [v for k, v in result.items()]

def GetAssets() -> List[Dict]:
    """PascalCase version of get_assets."""
    return get_assets()
