from flask_restful import Resource


class HealthCheck(Resource):

    @classmethod
    def get(cls):
        return 'im aaaaAlive', 200

    @classmethod
    def post(cls):
        return 'you post something', 200
