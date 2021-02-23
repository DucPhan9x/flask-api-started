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


    # def send_simple_message(self):
    #     return requests.post(
    #         "https://api.mailgun.net/v3/sandboxd8ea675e402444de81ade49809e91f17.mailgun.org/messages",
    #         auth=("api", "c775d486eef6f5b35b8db0f23a67ba7d-6e0fd3a4-45152b39"),
    #         data={"from": "Excited User <mailgun@sandboxd8ea675e402444de81ade49809e91f17.mailgun.org>",
    #             "to": ["ducphan.24hdev@gmail.com", "duc@sandboxd8ea675e402444de81ade49809e91f17.mailgun.org"],
    #             "subject": "Hello",
    #             "text": "Testing some Mailgun awesomness!"})
    
