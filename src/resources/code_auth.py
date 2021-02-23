from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import CodeAuthRepository
from util import parse_params


class CodeAuthResource(Resource):
    @staticmethod
    def get(code):
        try:
            code = CodeAuthRepository.get(code=code)
        except:
            return jsonify({"message": "Verify failed", "status": 400})
        return jsonify({"message": "Verify success", "status": 200})

    @staticmethod
    def post(code):
        try:
            code = CodeAuthRepository.create(
                code=code
            )
        except:
            return jsonify({"message": "No send code authentication", "status": 400})
        return jsonify({"message": "Send code authentication success", "status": 200})

