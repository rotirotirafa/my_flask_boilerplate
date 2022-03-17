import os

BASE_DIR = os.path.abspath('.')


class Production(object):
    DEBUG = False
    DEVELOPMENT = False


class Homolog(object):
    DEBUG = True


class Development(object):
    FLASK_ENV = 'development'
    ENV = 'development'
    DEBUG = True
    DEVELOPMENT = True
    DB_USER = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_HOST = '127.0.0.1'
    DB_PORT = 5432
    DB_NAME = 'postgres'
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


