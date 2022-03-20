from flask_restful import Resource

from src.repositories.auth import AuthRepository


class Auth(Resource):

    auth_repository = AuthRepository()

    @classmethod
    def post(cls, user_id: int):
        return cls.auth_repository.generate_token(user_id), 200

