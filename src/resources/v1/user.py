from src.repositories.users import UsersRepository
from src.resources.v1.base import BaseResource
from src.schemas.requests import BodyUserCreateSchema, BodyUserUpdateSchema, QueryUserParamsSchema


class User(BaseResource):

    user_repository = UsersRepository()

    @classmethod
    def get(cls, query: QueryUserParamsSchema):
        try:
            if query.user_id:
                return cls.user_repository.list_user(query.user_id), 200
            return cls.user_repository.list_users(), 200
        except Exception as ex:
            print(ex)
            raise ex

    @classmethod
    def post(cls, body: BodyUserCreateSchema):
        try:
            return cls.user_repository.create_user(body), 200
        except Exception as ex:
            print(ex)
            raise ex

    @classmethod
    def put(cls, body: BodyUserUpdateSchema, user_id: int):
        return cls.user_repository.update_user(body, user_id), 200

    @classmethod
    def delete(cls, user_id: int):
        return cls.user_repository.delete_user(user_id), 200
