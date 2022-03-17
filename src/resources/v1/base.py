from flask_pydantic import validate
from flask_restful import Resource


class BaseResource(Resource):

    method_decorators = [validate()]

    @classmethod
    def response_success(cls):
        return 'ok', 200

    @classmethod
    def response_error(cls):
        return 'error', 400
