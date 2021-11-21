# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config 

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
      SECRET_KEY='dev'
    )
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:adminadmin@database.cpzfde8y7eey.ap-northeast-2.rds.amazonaws.com:3306/database"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy()
    db.init_app(app)

    # flask 서버 확인
    @app.route('/hello')
    def hello():
      return "hello"

    return app
