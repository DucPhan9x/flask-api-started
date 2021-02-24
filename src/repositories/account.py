from models import Account
import uuid
import hashlib
from server import bcrypt

class AccountRepository:
    @staticmethod
    def logIn(user_name, password):
        user=Account.query.filter_by(user_name=user_name).first()
        if user:
            if(bcrypt.check_password_hash(user.password.encode("utf-8").decode('utf8'), password.encode("utf-8").decode('utf8'))):
                return user

    @staticmethod
    def getAll():
        return Account.query.all()

    @staticmethod
    def getUserById(uid):
        return Account.query.filter_by(uid=uid).first()

    @staticmethod
    def getUserByEmail(user_name):
        return Account.query.filter_by(user_name=user_name).first()

    @staticmethod
    def update(uid, password):
        account = Account.query.filter_by(uid=uid).first()
        account.password = bcrypt.generate_password_hash(password.encode("utf-8")).decode('utf8')

        return account.save()

    @staticmethod
    def create(user_name, password):
        account = Account(uid=str(uuid.uuid4()), user_name=user_name, password=bcrypt.generate_password_hash(password.encode("utf-8")).decode('utf8'))

        return account.save()
