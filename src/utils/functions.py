from functools import wraps

import jwt
from flask import request

from src.settings import SECRET


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return {'message': 'a valid token is missing'}, 400
        try:
            jwt.decode(token, SECRET, algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            return {'message': 'Signature expired. Please log in again.', 'error': 'expired'}, 401

        except jwt.InvalidTokenError:
            return {'message': 'Invalid token. Please log in again.', 'error': 'invalid'}, 401

        return f(*args, **kwargs)

    return decorator
