import os

BASE_DIR = os.path.abspath('.')

class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = 'SEGREDO'
    DB_USER = ''
    DB_PASSWORD = ''
    DB_HOST = '127.0.0.1'
    DB_PORT = 5432
    DB_NAME = ''
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Production(Config):
    DEBUG = False
    DEVELOPMENT = False


class Homolog(Config):
    DEBUG = True


class Development(Config):
    FLASK_ENV = 'development'
    ENV = 'development'
    DEBUG = True
    DEVELOPMENT = True
    DB_USER = 'rafael_rotiroti'
    DB_PASSWORD = '123456'
    DB_HOST = '127.0.0.1'
    DB_PORT = 5432
    DB_NAME = 'crud'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/src/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


