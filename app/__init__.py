from flask import Flask
from app.storage import load_users
from app.routes import register_routes


def create_app() -> Flask:
    """
    Application factory.
    Creates and configures the Flask app instance.
    """
    app = Flask(
        __name__,
        static_folder="frontend",   # app/frontend
        static_url_path="/static",  # served as /static/*
    )

    # Load users once and keep them in app config
    app.config["USERS"] = load_users()

    # Attach routes
    register_routes(app)

    return app
