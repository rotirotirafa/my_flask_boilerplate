from flask_restful import Api

from src.resources.health_check import HealthCheck
from src.settings import BASE_PATH, VERSION_PREFIX


def build_urls(app):

    api = Api()
    '''
    To add a new route
    '''
    api.add_resource(HealthCheck, f'/{BASE_PATH}/{VERSION_PREFIX}/health-check/')

    return api.init_app(app)
