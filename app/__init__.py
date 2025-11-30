import os
from flask import Flask
from app.storage import load_users
from app.routes import register_routes

def create_app() -> Flask:
    app = Flask(
        __name__,
        static_folder="frontend",   # app/frontend
        static_url_path="/static",  # served as /static/*
    )

    # Load users once and keep them in app config
    app.config["USERS"] = load_users()

    # Flag whether the app is running inside Docker
    app.config["RUNNING_IN_DOCKER"] = os.getenv("RUNNING_IN_DOCKER", "0") == "1"

    # Attach routes
    register_routes(app)

    return app
