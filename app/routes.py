from flask import jsonify, request, current_app

from app.auth_service import (
    register_user,
    login_user,
    list_usernames,
    change_password,
    delete_user,
)


def register_routes(app):
    """Attach all routes to the given Flask app instance."""

    @app.route("/")
    def index_page():
        # Serve app/frontend/index.html via Flask's static mechanism
        return app.send_static_file("index.html")

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json(silent=True) or {}
        username = data.get("username")
        password = data.get("password")

        users = current_app.config["USERS"]
        body, status = register_user(users, username, password)
        return jsonify(body), status

    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json(silent=True) or {}
        username = data.get("username")
        password = data.get("password")

        users = current_app.config["USERS"]
        body, status = login_user(users, username, password)
        return jsonify(body), status

    @app.route("/users", methods=["GET"])
    def users_list():
        users = current_app.config["USERS"]
        body, status = list_usernames(users)
        return jsonify(body), status

    @app.route("/change-password", methods=["PUT"])
    def change_password_route():
        data = request.get_json(silent=True) or {}
        username = data.get("username")
        old_password = data.get("old_password")
        new_password = data.get("new_password")

        users = current_app.config["USERS"]
        body, status = change_password(users, username, old_password, new_password)
        return jsonify(body), status

    @app.route("/delete-user", methods=["DELETE"])
    def delete_user_route():
        data = request.get_json(silent=True) or {}
        username = data.get("username")
        password = data.get("password")

        users = current_app.config["USERS"]
        body, status = delete_user(users, username, password)
        return jsonify(body), status
