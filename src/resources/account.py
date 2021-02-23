from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import AccountRepository
from util import parse_params
from flask import request
import jwt
import config
class AccountResourceAuth(Resource):

    @staticmethod
    def post():
        if request.is_json:
            data = request.get_json()
            account = AccountRepository.logIn(user_name=data['user_name'], password=data['password'])
            if account:
                return {"message": "Login successfully","data": {"account": {"uid":account.uid,"user_name": account.user_name}, "token": account.encode_auth_token(account.uid)}, "status": 200}
            else:
                return {"message": "Username or password does not exists", "status": 400}
        else:
            return {"error": "The request failed"}


    @staticmethod
    def get():
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
            accounts = AccountRepository.getAll()
            results= [
                {
                "uid": account.uid,
                "user_name": account.user_name,
                } for account in accounts]
        except Exception as e:
            print(e)
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
            accounts=AccountRepository.getAll()
            for user in accounts:
                if data['user_name']==user.user_name:
                    return {"message": f"Username {data['user_name']} already exists.", "status": 400}
            account = AccountRepository.create(user_name=data["user_name"], password=data['password'])
            auth_token=account.encode_auth_token(account.uid)
            return {"message": f"Account {account.user_name} has been registered successfully.","auth_token": auth_token,"status": 200}
        else:
            return {"error": "The request payload is not in JSON format"}
