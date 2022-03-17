from flask_restful import Resource

from src.repositories.users import UsersRepository


class User(Resource):

    user_repository = UsersRepository()

    @classmethod
    def get(cls, user_id: int = None):
        try:
            if user_id:
                return cls.user_repository.list_user(user_id), 200
            return cls.user_repository.list_users(), 200
        except Exception as ex:
            print(ex)

    @classmethod
    def post(cls):
        return 'you want POST something', 200

    @classmethod
    def put(cls, user_id: int):
        return 'you want PUT something', 200

    @classmethod
    def delete(cls, user_id: int):
        return 'you want to DELETE something', 200
