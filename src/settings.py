import os


ABSOLUTE_PATH = os.path.abspath(__file__)

ROOT = os.path.dirname(ABSOLUTE_PATH)

BASE_DIR = os.path.dirname(ROOT)

APP_SETTINGS = os.getenv("APP_SETTINGS", default="config.Development")

DEBUG = os.getenv("DEBUG", default=True)

HOST = os.getenv("HOST", default="0.0.0.0")
PORT = os.getenv("PORT", default=8080)

ENVIRONMENT = os.getenv("ENVIRONMENT", default="development")

BASE_PATH = os.getenv("BASE_PATH", default="boilerplate")

VERSION_PREFIX = 'v1'
