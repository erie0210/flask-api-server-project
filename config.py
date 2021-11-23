import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
  DEBUG = True
  TESTING = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:adminadmin@database.cpzfde8y7eey.ap-northeast-2.rds.amazonaws.com:3306/database?charset=utf8"
  SQLALCHEMY_ECHO = False
  SECRET_KEY = 'SECRET-KEY'


class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:adminadmin@database.cpzfde8y7eey.ap-northeast-2.rds.amazonaws.com:3306/database?charset=utf8"
  SQLALCHEMY_ECHO = False
  SECRET_KEY = 'SECRET-KEY'


class TestingConfig(Config):
  TESTING = True
  SQLALCHEMY_ECHO = False
  SQLALCHEMY_DATABASE_URI =  os.environ.get('TEST_DB_URL')
  SQLALCHEMY_ECHO = False
  SECRET_KEY = 'SECRET-KEY'