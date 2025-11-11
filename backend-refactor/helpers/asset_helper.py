"""Asset helpers (unused duplicate)."""
from typing import List, Dict

def group_signals_by_asset(signals: List[Dict]) -> Dict[str, List[Dict]]:
    """Group signals by asset ID."""
    grouped = {}
    for signal in signals:
        asset_id = signal.get("AssetId")
        if asset_id not in grouped:
            grouped[asset_id] = []
        grouped[asset_id].append(signal)
    return grouped

def GroupSignalsByAsset(signalList: List[Dict]) -> Dict[str, List[Dict]]:
    """PascalCase version."""
    result = {}
    for sig in signalList:
        aid = sig.get("AssetId")
        if aid not in result:
            result[aid] = []
        result[aid].append(sig)
    return result
