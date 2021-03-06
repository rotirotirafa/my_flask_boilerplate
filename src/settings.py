import os
from src.config import Development, Production


ENVIRONMENT = os.getenv("ENVIRONMENT", default="local")


def get_environment() -> object:
    if ENVIRONMENT == 'local':
        return Development
    return Production


SECRET = 'segredo'

ABSOLUTE_PATH = os.path.abspath(__file__)

ROOT = os.path.dirname(ABSOLUTE_PATH)

BASE_DIR = os.path.dirname(ROOT)

DEBUG = os.getenv("DEBUG", default=True)

HOST = os.getenv("HOST", default="0.0.0.0")
PORT = os.getenv("PORT", default=8080)

BASE_PATH = os.getenv("BASE_PATH", default="boilerplate")

VERSION_PREFIX = 'v1'

""" Um dia em Segundos = 86400."""
ONE_DAY = 86400

""" Uma hora em Segundos = 3600 """
ONE_HOUR = 3600
