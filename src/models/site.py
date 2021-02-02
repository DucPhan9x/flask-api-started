from . import db
from .abc import BaseModel, MetaBaseModel


class Site(db.Model, BaseModel, metaclass=MetaBaseModel):

    __tablename__ = "site"

    site_id = db.Column(db.String(50), primary_key=True)
    address = db.Column(db.String(100))
    site_name = db.Column(db.String(100))
    ems_id = db.Column(db.String(10))
    lines = db.relationship(
        "Line", backref="site", cascade="all, delete, delete-orphan", single_parent=True
    )

    def __init__(self, site_id, address, site_name, ems_id):
        self.site_id = site_id
        self.address = address
        self.site_name = site_name
        self.ems_id = ems_id
