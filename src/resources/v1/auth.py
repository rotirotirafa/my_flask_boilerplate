from flask_restful import Resource


class Auth(Resource):

    @classmethod
    def post(cls):
        return 'you want POST something', 200

