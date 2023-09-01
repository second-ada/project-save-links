from typing import
from flask import Flask
from werkzeug.exceptions import HTTPException
from app.routes import api


class Router:
    def __init__(self, app: Flask) -> None:
        app.register_error_handler(404, self.not_found)
        app.register_error_handler(422, self.unprocessable_entity)
        app.register_blueprint(api.bp)

    def not_found(self, e: HTTPException):
        return {
            "error": "Oops!  The current endpoint is not found.",
            "status": "404 Not Found"
        }, 404

    def unprocessable_entity(self, e: HTTPException):
        return {
            'error': e.description,
            'status': '422 Unprocessable Entity'
        }, 422
