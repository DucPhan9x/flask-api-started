from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import SiteRepository
from util import parse_params


class SiteResource(Resource):
    @staticmethod
    def get(site_id):
        try:
            site = SiteRepository.get(site_id=site_id)
        except:
            return jsonify({"site": "No site found", "status": 400})
        return jsonify({"site": site.json, "status": 200})

    @staticmethod
    def post(site_id, address, site_name, ems_id):
        try:
            site = SiteRepository.create(
                site_id=site_id, address=address, site_name=site_name, ems_id=ems_id
            )
        except:
            return jsonify({"site": "No site created", "status": 400})
        return jsonify({"site": site.json, "status": 200})

    @staticmethod
    def put(site_id, address, site_name, ems_id):
        repository = SiteRepository()
        try:
            site = repository.update(
                site_id=site_id, address=address, site_name=site_name, ems_id=ems_id
            )
        except:
            return jsonify({"site": "No site updated", "status": 400})
        return jsonify({"site": site.json, "status": 200})
