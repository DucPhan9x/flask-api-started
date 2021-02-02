from flask import Blueprint
from flask_restful import Api

from resources import SiteResource

SITE_BLUEPRINT = Blueprint("site", __name__)
Api(SITE_BLUEPRINT).add_resource(SiteResource, "/site/<string:site_id>")
