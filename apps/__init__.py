# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
      SECRET_KEY='dev'
    )
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:adminadmin@database.cpzfde8y7eey.ap-northeast-2.rds.amazonaws.com:3306/database"
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
