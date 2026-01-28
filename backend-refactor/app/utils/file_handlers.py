"""Helper to read data from files."""
import csv
import json
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

def load_json_file(file_path: str) -> List[Dict[str, Any]]:
    """Safely load a JSON file from a given path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format in {file_path}: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error loading {file_path}: {e}")
        return []

def load_csv_file(file_path: str, delimiter: str = "|") -> List[Dict[str, Any]]:
    """Safely load a CSV file from a given path."""
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            return [row for row in reader]
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Error reading CSV {file_path}: {e}")
        return []
