from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from app.config import Config
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        from app import models 

    from app.routes.health import ns
    api = Api(app, prefix="/api", title="Backend Challenge", version="1.0", description="REST API")
    api.add_namespace(ns)
    return app