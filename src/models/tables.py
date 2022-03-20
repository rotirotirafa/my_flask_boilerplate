from time import time

import jwt
from passlib.context import CryptContext

from src.database.connection import db
from src.settings import ONE_HOUR, SECRET


class User(db.Model):
    __tablename__ = "users"
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    user_type = db.Column(db.String)

    def __init__(self, email: str, user_type: str, password: str = None):
        self.email = email
        self.user_type = user_type
        self.password = self.get_password_hash(password)

    def to_dict(self):
        return {
            'user_id': self._id,
            'email': self.email,
            'user_type': self.user_type
        }

    def get_password_hash(self, password):
        password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
        return password_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
        return password_context.verify(plain_password, hashed_password)

    @classmethod
    def login_with_email(cls, email):
        user = cls.query.filter_by(email=email).one()
        if user:
            return user.to_dict()
        return None

    @classmethod
    def create_instance_with_id(cls, _id):
        return cls.query.filter_by(_id=_id).first()

    @classmethod
    def find_by_id(cls, _id):
        user = cls.query.filter_by(_id=_id).first()
        if user:
            return user.to_dict()
        return None

    @classmethod
    def find_all(cls):
        users = cls.query.all()
        if users:
            return cls.transform_class_objects_to_list(users)
        return None

    @classmethod
    def transform_class_objects_to_list(cls, users):
        data = []
        for user in users:
            data.append(user.to_dict())
        return data

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, email, user_type):
        self.email = email
        self.user_type = user_type
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
