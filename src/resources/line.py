from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import LineRepository
from util import parse_params


class LineResource(Resource):
    @staticmethod
    def get(line_id):
        try:
            line = LineRepository.get(line_id=line_id)
        except:
            return jsonify({"line": "No line found", "status": 400})
        return jsonify({"line": line.json, "status": 200})

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
