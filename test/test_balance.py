import pytest
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

def test_get_list(client):
  assert True

def test_create(client):
  assert True

def test_update(client):
  assert True

def test_delete(client):
  assert True

def test_rollback(client):
  assert True