from flask import Blueprint
from flask_restful import Api

from resources import AccountResourceAuth
from resources import AccountResourceUnAuth

ACCOUNT_BLUEPRINT_GET_ALL = Blueprint("account_get_all", __name__)
Api(ACCOUNT_BLUEPRINT_GET_ALL).add_resource(AccountResourceAuth, "/accounts/get_all")

ACCOUNT_BLUEPRINT_LOGIN = Blueprint("account_login", __name__)
Api(ACCOUNT_BLUEPRINT_LOGIN).add_resource(AccountResourceAuth, "/account/login")

ACCOUNT_BLUEPRINT_REGISTER= Blueprint("account_register", __name__)
Api(ACCOUNT_BLUEPRINT_REGISTER).add_resource(AccountResourceUnAuth, "/account/register")

