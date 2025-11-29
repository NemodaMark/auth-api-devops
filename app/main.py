from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash
from app.storage import load_users, save_users

app = Flask(__name__)

# Global users dictionary loaded from JSON file
users = load_users()


@app.route("/health", methods=["GET"])
def health():
    """Simple health-check endpoint to verify the server is running."""
    return jsonify({"status": "ok"}), 200


@app.route("/register", methods=["POST"])
def register():
    """
    Register a new user.
    Expected JSON body:
    {
      "username": "name",
      "password": "password123"
    }
    """
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    password = data.get("password")

    # Basic validation
    if not username or not password:
        return jsonify({"error": "username and password are required"}), 400

    # Reject duplicate username
    if username in users:
        return jsonify({"error": "username already exists"}), 400

    # Hash the password using pbkdf2:sha256
    password_hash = generate_password_hash(password, method="pbkdf2:sha256")

    users[username] = {"password": password_hash}
    save_users(users)

    return jsonify({"message": "user created", "username": username}), 201


@app.route("/users", methods=["GET"])
def list_users():
    """
    Return a list of all registered usernames.
    Password hashes are NOT returned.
    This is mainly an admin/dev endpoint.
    """
    result = [{"username": name} for name in users.keys()]
    return jsonify(result), 200


if __name__ == "__main__":
    # Only used for local development
    app.run(host="0.0.0.0", port=8080, debug=True)
