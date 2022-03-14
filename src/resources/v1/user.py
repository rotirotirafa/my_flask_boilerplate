from flask_restful import Resource


class User(Resource):

    @classmethod
    def get(cls):
        return 'Hello! Im Online!', 200

    @classmethod
    def post(cls):
        return 'you want POST something', 200

    @classmethod
    def put(cls):
        return 'you want PUT something', 200

    @classmethod
    def delete(cls):
        return 'you want to DELETE something', 200
