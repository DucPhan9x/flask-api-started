from . import db
from .abc import BaseModel, MetaBaseModel


class Account(db.Model, BaseModel, metaclass=MetaBaseModel):

    __tablename__ = "account"

    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(300))

    def __init__(self, uid, user_name, password):
        self.uid = uid
        self.user_name = user_name
        self.password = password
