from functools import wraps

import jwt
from flask import request, jsonify

from src.settings import SECRET


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, SECRET, algorithms=["HS256"])
        except Exception as ex:
            return jsonify({'message': 'token is invalid'})

        return f(*args, **kwargs)

    return decorator
