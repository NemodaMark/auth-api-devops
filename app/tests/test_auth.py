import sys
from pathlib import Path

# Add the project root directory to sys.path so "from app import app" works
ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app import app
from app.storage import save_users


def test_health_endpoint():
    """Verify that the /health endpoint returns status=ok."""
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"


def test_register_creates_user(tmp_path, monkeypatch):
    """Registering a new user should succeed."""

    # Redirect data file to a temporary JSON file (avoids touching real users.json)
    from app import storage as storage_module

    test_file = tmp_path / "users_test.json"
    monkeypatch.setattr(storage_module, "DATA_FILE", test_file)

    # Start with an empty user base
    save_users({})

    client = app.test_client()
    response = client.post(
        "/register",
        json={"username": "testuser", "password": "secret123"},
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "user created"
    assert data["username"] == "testuser"


def test_register_duplicate_username(tmp_path, monkeypatch):
    """Registering an already existing username should fail."""

    from app import storage as storage_module

    test_file = tmp_path / "users_test.json"
    monkeypatch.setattr(storage_module, "DATA_FILE", test_file)

    # Pre-populate with a user that already exists
    save_users({"testuser": {"password": "hash"}})

    client = app.test_client()

    response = client.post(
        "/register",
        json={"username": "testuser", "password": "anotherpass"},
    )

    assert response.status_code == 400
    data = response.get_json()
    assert "username already exists" in data["error"]
