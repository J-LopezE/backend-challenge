import pytest
from app import create_app
from app.models import db

@pytest.fixture
def app():
   yield create_app("testing")

@pytest.fixture
def db_setup(app):
    with app.app_context():
        db.create_all()
        yield 
        db.drop_all()
    

@pytest.fixture
def client(app):
    return app.test_client()