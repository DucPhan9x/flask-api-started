from flask import Blueprint
from flask_restful import Api

from resources import AccountResource

ACCOUNT_BLUEPRINT = Blueprint("account", __name__)
Api(ACCOUNT_BLUEPRINT).add_resource(AccountResource, "/account/<string:uid>")
