class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@127.0.0.1:3306/test"
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'SECRET-KEY'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@127.0.0.1:3306/test"
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'SECRET-KEY'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@127.0.0.1:3306/test"
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'SECRET-KEY'