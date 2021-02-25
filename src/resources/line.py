from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import LineRepository
from util import parse_params
from flask import request
import jwt

class LineResource(Resource):
    @staticmethod
    def get(line_id):
        try:
            auth_header = request.headers.get('Authorization')
            if auth_header:
                auth_token = auth_header.split(" ")[1]
            else:
                auth_token = ''
            if auth_token:
                try:
                    payload=jwt.decode(auth_token, "secret",algorithms="HS256")
                    resp=payload['sub']
                except jwt.ExpiredSignatureError:
                    return {"message": "Signature expired. Please log in again.", "status": 400}
                except jwt.InvalidTokenError:
                    return {"message": "Invalid token. Please log in again.", "status": 400}
            try:
                line = LineRepository.get(line_id=line_id)
                if line:
                    return ({"line":{"line_id": line.line_id, "site_id": line.site_id, "line_name": line.line_name}, "status": 200})
                return jsonify({"message": "No line found", "status": 400})
            except Exception as e1:
                 print("e1: ", e1)
        except Exception as e:
            print("e: ", e)
            return {"message": "No account found", "status": 400}

    @staticmethod
    def post(line_id, site_id, line_name):
        try:
            line = LineRepository.create(
                line_id=line_id, site_id=site_id, line_name=line_name
            )
        except:
            return jsonify({"line": "No line created", "status": 400})
        return jsonify({"line": line.json, "status": 200})

    @staticmethod
    def put(line_id, site_id, line_name):
        repository = LineRepository()
        try:
            line = repository.update(site_id=site_id, line_name=line_name)
        except:
            return jsonify({"line": "No line updated", "status": 400})
        return jsonify({"line": line.json, "status": 200})
