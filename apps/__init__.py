# -*- coding: utf-8 -*-
from flask import Flask
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config['SECRET_KEY'] = 'dev'
    app.config['JSON_AS_ASCII'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:adminadmin@database.cpzfde8y7eey.ap-northeast-2.rds.amazonaws.com:3306/database?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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
