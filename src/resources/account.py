from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import AccountRepository
from util import parse_params
from flask import request


class AccountResourceAuth(Resource):

    @staticmethod
    def post():
        if request.is_json:
            data = request.get_json()
            account = AccountRepository.logIn(user_name=data['user_name'], password=data['password'])
            if account:
                return {"message": "Login successfully","account": {"uid":account.uid,"user_name": account.user_name}, "token":"XgbuVEXBU5gtSKdbQRP1Zbbby1i1",
                      "photo_url":"assets/images/avatars/Abbott.jpg" ,"status": 200}
            else:
                return {"message": "No account found", "status": 400}
        else:
            return {"error": "The request failed"}


    @staticmethod
    def get():
        try:
            accounts = AccountRepository.getAll()
            results= [
                {
                "uid": account.uid,
                "user_name": account.user_name,
                } for account in accounts]
        except:
            return {"message": "No account found", "status": 400}
        return ({"accounts": results, "status": 200})

    

    @staticmethod
    def put(user_name, password):
        repository = AccountRepository()
        account = repository.update(user_name=user_name, password=password)
        return jsonify({"account": account.json})


class AccountResourceUnAuth(Resource):

    @staticmethod
    def post():
        if request.is_json:
            data = request.get_json()
            account = AccountRepository.create(user_name=data['user_name'], password=data['password'])
            return {"message": f"account {account.user_name} has been registered successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
