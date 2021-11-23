# -*- coding: utf-8 -*-
import os
from flask import Flask
from config import ProductionConfig, DevelopmentConfig, TestingConfig
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

def create_app(test_config=None):

  app = Flask(__name__, instance_relative_config=True)
  swagger = Swagger(app)

  # config
  if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
  elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
  else:
    app_config = DevelopmentConfig
  app.config.from_object(app_config)

  db = SQLAlchemy()
  db.init_app(app)

  # AUTH: 인증 관련
  from . import auth
  app.register_blueprint(auth.bp)

  # BALANCE: 가계부 
  from . import balance
  app.register_blueprint(balance.bp)
  app.add_url_rule('/', endpoint='index')

  return app