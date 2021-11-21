# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
      SECRET_KEY='dev'
    )
    
    # flask 서버 확인
    @app.route('/hello')
    def hello():
      return "hello"

    return app
