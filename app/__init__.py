from flask import Flask
from app.routes import Router


def create_app():
    app = Flask(__name__)

    Router(app)

    return app
