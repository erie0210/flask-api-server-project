import pytest
# from utils import create_app
from flask_sqlalchemy import SQLAlchemy
from config import TestingConfig

from flask import Flask
from apps import auth
from apps import balance

def create_testing_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(TestingConfig)

    db = SQLAlchemy()
    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(balance.bp)
    app.add_url_rule('/', endpoint='index')

    return app


@pytest.fixture(scope='session')
def app():
    app = create_testing_app()
    return app


@pytest.fixture 
def client(app):
    client = app.test_client()
    return client


def test_get_user(client):
    response = client.get('/')
    assert response.status_code == 302
    # assert response.json == { 'users': [{'id': 1, 'name':'user1'}] } 