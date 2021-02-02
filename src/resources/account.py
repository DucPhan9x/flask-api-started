from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import AccountRepository
from util import parse_params


class AccountResource(Resource):
    @staticmethod
    def get(uid):
        try:
            account = AccountRepository.get(uid=uid)
        except:
            return jsonify({"account": "No account found", "status": 400})
        return jsonify({"account": account.json, "status": 200})

    @staticmethod
    def post(uid, user_name, password):
        account = AccountRepository.create(
            uid=uid, user_name=user_name, password=password
        )
        return jsonify({"account": account.json})

    @staticmethod
    def put(user_name, password):
        repository = AccountRepository()
        account = repository.update(user_name=user_name, password=password)
        return jsonify({"account": account.json})
