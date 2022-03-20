from time import time

import jwt

from src.models.tables import User
from src.settings import ONE_HOUR, SECRET


class AuthRepository:

    user_model = User

    def generate_token(self, user_id: int):
        user = User.find_by_id(user_id)
        token = self.encode_auth_token(user)
        return token

    def encode_auth_token(self, user):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'sub': user,
                'exp': time() + ONE_HOUR
            }
            return jwt.encode(
                payload,
                SECRET,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, SECRET)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return {'message': 'Signature expired. Please log in again.', 'error': 'expired'}
        except jwt.InvalidTokenError:
            return {'message': 'Invalid token. Please log in again.', 'error': 'invalid'}
