
from app import db
from datetime import datetime

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hformat = db.Column(db.String(255), nullable=False)
    bucketlist = db.relationship('Bucketlist', backref='user', lazy='dynamic',
                                 cascade='all,delete-orphan')

    @property
    def password(self):
        raise AttributeError('password is hashed and cannot be read')

    @password.setter
    def password(self, password):
        self.password_hformat = generate_password_hash(password)

    def auth_password(self, password):
        return check_password_hash(self.password_hformat, password)

    def confirmation_token(self, expiration=40000):
        serial = Serializer(current_app.config['SECRET_KEY'], expiration)
        return serial.dumps({'id': self.id})

    @staticmethod
    def comfirm_token(token):
        serial = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = serial.loads(token)
        except:
            """ Token is not valid"""
            return False
        return data["id"]


class Bucketlist(db.Model):
    __tablename__ = 'bucketlists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime,
                             nullable=False, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime,
                              default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('Item', backref='bucketlist',
                            lazy='dynamic', cascade='all, delete-orphan')


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, nullable= False,
                              default=datetime.utcnow)
    status = db.Column(db.Boolean, default=False)
    bucket_id = db.Column(db.Integer, db.ForeignKey('bucketlists.id'),
                          nullable=False)
