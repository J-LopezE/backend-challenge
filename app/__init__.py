from flask import Flask
from flask_restx import Api
from app.routes.health import ns
def create_app():
    app = Flask(__name__)
    api = Api(app, prefix="/api", title="Backend Challenge", version="1.0", description="REST API")
    api.add_namespace(ns)
    return app
