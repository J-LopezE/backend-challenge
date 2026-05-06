from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from app.config import config as config_dict
from app.models import db
import os


def create_app(config_name=None):
    app = Flask(__name__)
    config_name = config_name or os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_dict[config_name])
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        from app.routes.health import ns
        from app.routes.users import us

    api = Api(
        app,
        prefix="/api",
        title="Backend Challenge",
        version="1.0",
        description="REST API",
    )
    api.add_namespace(ns)
    api.add_namespace(us)
    return app