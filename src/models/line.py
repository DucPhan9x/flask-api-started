from . import db
from .abc import BaseModel, MetaBaseModel


class Line(db.Model, BaseModel, metaclass=MetaBaseModel):

    __tablename__ = "line"

    line_id = db.Column(db.String(50), primary_key=True)
    site_id = db.Column(db.String(50), db.ForeignKey("site.site_id"))
    line_name = db.Column(db.String(100))

    def __init__(self, line_id, site_id, line_name):
        self.line_id = line_id
        self.site_id = site_id
        self.line_name = line_name
