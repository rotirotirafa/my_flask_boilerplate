from flask_pydantic import validate
from flask_restful import Resource

from src.utils.functions import token_required


class BaseResource(Resource):

    method_decorators = [validate(), token_required]

    @classmethod
    def response_success(cls):
        return 'ok', 200

    @classmethod
    def response_error(cls):
        return 'error', 400
