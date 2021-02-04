from models import Account
import uuid
import hashlib
class AccountRepository:
    @staticmethod
    def logIn(user_name, password):
        return Account.query.filter_by(user_name=user_name, password=hashlib.md5(password.encode()).hexdigest()).one()


    @staticmethod
    def getAll():
        return Account.query.all()

    @staticmethod
    def update(self, user_name, password):
        account = self.get(uid)
        account.user_name = user_name
        account.password = password

        return account.save()

    @staticmethod
    def create(user_name, password):
        account = Account(uid=str(uuid.uuid4()), user_name=user_name, password=hashlib.md5(password.encode()).hexdigest())

        return account.save()
