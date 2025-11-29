import json
from pathlib import Path

# Path to the users.json file located in the project root directory
DATA_FILE = Path(__file__).resolve().parents[1] / "users.json"


def load_users() -> dict:
    """
    Load users from users.json.
    If the file does not exist, is empty, or contains invalid JSON,
    return an empty dictionary.
    """
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return {}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If the JSON file is corrupted, start fresh with an empty dict
        return {}


def save_users(users: dict) -> None:
    """Save the users dictionary into the users.json file."""
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)
