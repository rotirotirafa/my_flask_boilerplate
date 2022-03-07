import os

from decouple import config

ABSOLUTE_PATH = os.path.abspath(__file__)

ROOT = os.path.dirname(ABSOLUTE_PATH)

BASE_DIR = os.path.dirname(ROOT)

APP_SETTINGS = config("APP_SETTINGS", default="config.Development")

DEBUG = config("DEBUG", default=True, cast=bool)

HOST = config("HOST", default="127.0.0.1")
PORT = config("PORT", default=8000, cast=int)

ENVIRONMENT = config("ENVIRONMENT", default="development")

BASE_PATH = config("BASE_PATH", default="boilerplate")

VERSION_PREFIX = 'v1'
