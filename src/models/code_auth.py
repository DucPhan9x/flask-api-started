from . import db
from .abc import BaseModel, MetaBaseModel

class CodeAuth(db.Model, BaseModel, metaclass=MetaBaseModel):

    __tablename__ = "code_auth"

    uid = db.Column(db.String(255), primary_key=True)
    code = db.Column(db.String(6))

    def __init__(self, uid, code):
        self.uid = uid
        self.code = code