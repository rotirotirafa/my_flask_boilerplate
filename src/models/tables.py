from datetime import datetime

import jwt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from sqlalchemy.orm.exc import NoResultFound

from src.database.connection import db


class User(db.Model):
    __tablename__ = "users"
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    user_type = db.Column(db.String)

    def __init__(self, email, password, user_type):
        self.email = email
        self.password = self.get_password_hash(password)
        self.user_type = user_type

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

    def update(self, email, password):
        self.email = email
        self.password = self.get_password_hash(password)
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'sub': user_id
            }
            return jwt.encode(
                payload,
                'teste-key',
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
            payload = jwt.decode(auth_token, 'teste-key')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class Driver(db.Model):
    __tablename__ = "drivers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    police_check = db.Column(db.String)
    driver_licence = db.Column(db.String)
    vehicle_plate_number = db.Column(db.String)
    vehicle_model = db.Column(db.String)
    user_id = db.Column(db.Integer, ForeignKey(User._id))

    def __init__(self, name, gender, age, police_check, driver_licence, vehicle_plate_number, vehicle_model,  user_id):
        self.name = name
        self.gender = gender
        self.age = age
        self.police_check = police_check
        self.driver_licence = driver_licence
        self.vehicle_plate_number = vehicle_plate_number
        self.vehicle_model = vehicle_model
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'police_check': self.police_check,
            'driver_licence': self.driver_licence,
            'vehicle_plate_number': self.vehicle_plate_number,
            'vehicle_model': self.vehicle_model,
            'user_id': self.user_id,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Traveler(db.Model):
    __tablename__ = "travelers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    police_check = db.Column(db.String)
    user_id = db.Column(db.Integer, ForeignKey(User._id))

    def __init__(self, name, gender, age, police_check, user_id):
        self.name = name
        self.gender = gender
        self.age = age
        self.police_check = police_check
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'police_check': self.police_check,
            'user_id': self.user_id,
            # 'email': self.email
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        travelers = []
        rows = db.session.query(Traveler, User).filter(User._id == Traveler.user_id).all()
        for row in rows:
            travelers.append({
                'id': row.Traveler.id,
                'name': row.Traveler.name,
                'gender': row.Traveler.gender,
                'age': row.Traveler.age,
                'police_check': row.Traveler.police_check,
                'user_id': row.Traveler.user_id,
                'email': row.User.email
            })
        return travelers

    @classmethod
    def find_by_id(cls, traveler_id):
        row = db.session.query(Traveler, User).filter(User._id == traveler_id).one()
        if row:
            return {
                'id': row.Traveler.id,
                'name': row.Traveler.name,
                'gender': row.Traveler.gender,
                'age': row.Traveler.age,
                'police_check': row.Traveler.police_check,
                'user_id': row.Traveler.user_id,
                'email': row.User.email
            }
        return None


class Trip(db.Model):
    __tablename__ = "trips"
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, ForeignKey(Driver.id))
    destination_a = db.Column(db.String)
    destination_b = db.Column(db.String)

    def __init__(self, driver_id, destination_b, destination_a):
        self.driver_id = driver_id
        self.destination_b = destination_b
        self.destination_a = destination_a

    def to_dict(self):
        return {
            'id': self.id,
            'driver_id': self.driver_id,
            'destination_b': self.destination_b,
            'destination_a': self.destination_a
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls, driver_id):
        trips = []
        rows = db.session.query(Trip, Driver).filter(Driver.id == driver_id).all()
        for row in rows:
            trips.append({
                'trip_id': row.Trip.id,
                'destination_a': row.Trip.destination_a,
                'destination_b': row.Trip.destination_b,
                'driver_id': row.Trip.driver_id,
                'driver_name': row.Driver.name
            })
        return trips

    @classmethod
    def find_all_trips(cls):
        trips = []
        rows = db.session.query(Trip, Driver).filter(Driver.id == Trip.driver_id).all()
        for row in rows:
            trips.append({
                'trip_id': row.Trip.id,
                'destination_a': row.Trip.destination_a,
                'destination_b': row.Trip.destination_b,
                'driver_id': row.Trip.driver_id,
                'driver_name': row.Driver.name,
                'vehicle_model': row.Driver.vehicle_model,
                'vehicle_plate_number': row.Driver.vehicle_plate_number
            })
        return trips


    #driver = relationship('Driver', remote_side='Driver._id', foreign_keys='driver.id')


class Match(db.Model):
    __tablename__ = "matches"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver_id = db.Column(db.Integer, ForeignKey(Driver.id))
    traveler_id = db.Column(db.Integer, ForeignKey(Traveler.id))
    trip_id = db.Column(db.Integer, ForeignKey(Trip.id))

    def __init__(self, driver_id, traveler_id, trip_id):
        self.driver_id = driver_id
        self.traveler_id = traveler_id
        self.trip_id = trip_id

    def to_dict(self):
        return {
            'id': self.id,
            'driver_id': self.driver_id,
            'traveler_id': self.traveler_id,
            'trip_id': self.trip_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        matches = []
        rows = db.session.query(Trip, Traveler, Driver, Match).filter(
            Trip.id == Match.trip_id,
            Traveler.id == Match.traveler_id,
            Driver.id == Match.driver_id
        ).all()
        for row in rows:
            matches.append({
                'match_id': row.Match.id,
                'trip_id': row.Trip.id,
                'driver_id': row.Driver.id,
                'driver_name': row.Driver.name,
                'driver_car_model': row.Driver.vehicle_model,
                'driver_plate_number': row.Driver.vehicle_plate_number,
                'destination_a': row.Trip.destination_a,
                'destination_b': row.Trip.destination_b,
                'traveler_id': row.Traveler.id,
                'traveler_name': row.Traveler.name
            })
        return matches

    @classmethod
    def find_all_by_driver_id(cls, driver_id):
        matches = []
        rows = db.session.query(Trip, Traveler, Driver, Match).filter(
            Trip.id == Match.trip_id,
            Traveler.id == Match.traveler_id,
            Driver.id == driver_id
        ).all()
        for row in rows:
            matches.append({
                'match_id': row.Match.id,
                'trip_id': row.Trip.id,
                'driver_id': row.Driver.id,
                'driver_name': row.Driver.name,
                'driver_car_model': row.Driver.vehicle_model,
                'driver_plate_number': row.Driver.vehicle_plate_number,
                'destination_a': row.Trip.destination_a,
                'destination_b': row.Trip.destination_b,
                'traveler_id': row.Traveler.id,
                'traveler_name': row.Traveler.name
            })
        return matches

    @classmethod
    def find_all_by_traveler_id(cls, traveler_id):
        matches = []
        rows = db.session.query(Trip, Traveler, Driver, Match).filter(
            Trip.id == Match.trip_id,
            Traveler.id == traveler_id,
            Driver.id == Match.driver_id
        ).all()
        for row in rows:
            matches.append({
                'match_id': row.Match.id,
                'trip_id': row.Trip.id,
                'driver_id': row.Driver.id,
                'driver_name': row.Driver.name,
                'driver_car_model': row.Driver.vehicle_model,
                'driver_plate_number': row.Driver.vehicle_plate_number,
                'destination_a': row.Trip.destination_a,
                'destination_b': row.Trip.destination_b,
                'traveler_id': row.Traveler.id,
                'traveler_name': row.Traveler.name
            })
        return matches
