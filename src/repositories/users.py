from src.models.tables import User


class UsersRepository:

    user_model = User

    def create_user(self, data):
        user = User(email=data.get('email'), password=data.get('password'), user_type=data.get('user_type'))
        user.save()
        return user.to_dict()

    def list_users(self):
        users = self.user_model.find_all()
        return users

    def list_user(self, user_id: int):
        user = User.find_by_id(user_id)
        return user

