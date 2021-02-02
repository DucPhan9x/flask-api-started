from flask import Blueprint
from flask_restful import Api

from resources import LineResource

LINE_BLUEPRINT = Blueprint("line", __name__)
Api(LINE_BLUEPRINT).add_resource(LineResource, "/line/<string:line_id>")
