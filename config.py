import os
from decouple import config
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = 'secret'
	DEBUG = False


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = config("DEV_DATABASE_URI")
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = config("DEV_DATABASE_URI")
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = config("PROD_DATABASE_URI")


config_by_name = dict(
	dev=DevelopmentConfig,
	test=TestingConfig,
	prod=ProductionConfig
)
