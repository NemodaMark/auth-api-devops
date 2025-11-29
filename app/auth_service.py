from werkzeug.security import generate_password_hash, check_password_hash
from app.storage import save_users


def register_user(users: dict, username: str, password: str):
    """Business logic for registering a new user."""
    if not username or not password:
        return {"error": "username and password are required"}, 400

    if username in users:
        return {"error": "username already exists"}, 400

    password_hash = generate_password_hash(password, method="pbkdf2:sha256")
    users[username] = {"password": password_hash}
    save_users(users)

    return {"message": "user created", "username": username}, 201


def login_user(users: dict, username: str, password: str):
    """Business logic for logging in a user."""
    if not username or not password:
        return {"error": "username and password are required"}, 400

    if username not in users:
        return {"error": "invalid username or password"}, 401

    stored_hash = users[username]["password"]
    if not check_password_hash(stored_hash, password):
        return {"error": "invalid username or password"}, 401

    return {"message": "login successful", "username": username}, 200


def list_usernames(users: dict):
    """Return a list of usernames only (no passwords)."""
    return [{"username": name} for name in users.keys()], 200

def change_password(users: dict, username: str, old_password: str, new_password: str):
    """Business logic for changing a user's password."""
    if not username or not old_password or not new_password:
        return {"error": "username, old_password and new_password are required"}, 400

    if username not in users:
        return {"error": "invalid username or password"}, 401

    stored_hash = users[username]["password"]
    if not check_password_hash(stored_hash, old_password):
        return {"error": "invalid username or password"}, 401

    new_hash = generate_password_hash(new_password, method="pbkdf2:sha256")
    users[username]["password"] = new_hash
    save_users(users)

    return {"message": "password updated", "username": username}, 200


def delete_user(users: dict, username: str, password: str):
    """Business logic for deleting a user."""
    if not username or not password:
        return {"error": "username and password are required"}, 400

    if username not in users:
        return {"error": "invalid username or password"}, 401

    stored_hash = users[username]["password"]
    if not check_password_hash(stored_hash, password):
        return {"error": "invalid username or password"}, 401

    # Delete the user and persist
    users.pop(username)
    save_users(users)

    return {"message": "user deleted", "username": username}, 200
