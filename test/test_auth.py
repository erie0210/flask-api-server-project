from flask import session
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

def test_without_login(client):
    response = client.get('/')
    assert response.status_code == 302

def test_register(client):
  assert client.get('/auth/register')
    
# test 데이터베이스 user 테이블에 {id:1. 'email': 'abc@gmail.com', 'password': 'asdf'} 데이터 존재할 때
def test_login(client):
  assert client.get('/auth/register')
  response = client.post(
    '/auth/login',
    data = {'email': 'abc@gmail.com', 'password': 'asdf'}
  )
  assert response.status_code == 200

def test_logout(client):
  response = client.get('/auth/logout')
  assert response.status_code == 302