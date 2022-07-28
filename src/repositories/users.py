from src.models.tables import User
from src.schemas.requests import BodyUserCreateSchema, BodyUserUpdateSchema


class UsersRepository:

    user_model = User

    def create_user(self, data: BodyUserCreateSchema) -> dict:
        user = self.user_model(email=data.email,
                               password=data.password,
                               user_type=data.user_type)
        user.save()
        return user.to_dict()

    def update_user(self, data: BodyUserUpdateSchema, user_id: int):
        user = self.user_model.create_instance_with_id(user_id)
        user.update(data.email, data.user_type)
        return True

    def delete_user(self, user_id: int):
        user = self.user_model.create_instance_with_id(user_id)
        user.delete()
        return True

    def list_users(self):
        users = self.user_model.find_all()
        return users

    def list_user(self, user_id: int):
        user = User.find_by_id(user_id)
        return user

