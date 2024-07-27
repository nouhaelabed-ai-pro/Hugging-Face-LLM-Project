from flask import Flask
from .routes import main


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Register blueprints
    app.register_blueprint(main)

    return app
