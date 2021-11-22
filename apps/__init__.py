# -*- coding: utf-8 -*-
from flask import Flask
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy

from secret import DB

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
      SECRET_KEY='dev',
      SQLALCHEMY_DATABASE_URI=DB['DATABASE_URI'],
      SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    db = SQLAlchemy()
    db.init_app(app)

    # AUTH: 인증 관련 블루프린트 
    from . import auth
    app.register_blueprint(auth.bp)

    # BALANCE: 가계부 블루프린트
    from . import balance
    app.register_blueprint(balance.bp)
    app.add_url_rule('/', endpoint='index')

    return app
