from flask_restful import Api

from src.resources.health_check import HealthCheck
from src.resources.v1.user import User
from src.settings import BASE_PATH, VERSION_PREFIX


URL_PREFIX = f'/{BASE_PATH}/{VERSION_PREFIX}'


def build_urls(app):

    api = Api()
    '''
    To add a new route
    '''
    api.add_resource(User, f'{URL_PREFIX}/users/', f'{URL_PREFIX}/users/<int:user_id>/')
    api.add_resource(HealthCheck, f'/{URL_PREFIX}/health-check/')

    return api.init_app(app)
