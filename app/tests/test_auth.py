import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app import create_app  # type: ignore

app = create_app()


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_register_and_login():
    client = app.test_client()
    app.config["USERS"] = {}

    # Register
    r1 = client.post("/register", json={"username": "testuser", "password": "secret"})
    assert r1.status_code == 201

    # Login with same credentials
    r2 = client.post("/login", json={"username": "testuser", "password": "secret"})
    assert r2.status_code == 200
    assert r2.get_json()["message"] == "login successful"


def test_change_password_and_delete():
    client = app.test_client()
    app.config["USERS"] = {}

    # Register first
    client.post("/register", json={"username": "mark", "password": "oldpass"})

    # Change password
    r_change = client.put(
        "/change-password",
        json={
            "username": "mark",
            "old_password": "oldpass",
            "new_password": "newpass",
        },
    )
    assert r_change.status_code == 200

    # Login with new password works
    r_login = client.post(
        "/login",
        json={"username": "mark", "password": "newpass"},
    )
    assert r_login.status_code == 200

    # Delete user
    r_delete = client.delete(
        "/delete-user",
        json={"username": "mark", "password": "newpass"},
    )
    assert r_delete.status_code == 200
