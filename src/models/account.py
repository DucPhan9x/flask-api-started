from . import db
from .abc import BaseModel, MetaBaseModel
import datetime
import jwt
import config
from flask import request

class Account(db.Model, BaseModel, metaclass=MetaBaseModel):

    __tablename__ = "account"

    uid = db.Column(db.String(255), primary_key=True)
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(300))

    def __init__(self, uid, user_name, password):
        self.uid = uid
        self.user_name = user_name
        self.password = password

    def encode_auth_token(self, uid):
        try:
            payload={
                'exp': datetime.datetime.utcnow()+datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': uid
            }
            return jwt.encode(
                payload,
                'secret',
                algorithm='HS256'
            )
        except Exception as e:
            return e