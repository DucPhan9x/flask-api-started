from models import Account


class AccountRepository:
    @staticmethod
    def get(uid):
        return Account.query.filter_by(uid=uid).one()

    def update(self, user_name, password):
        account = self.get(uid)
        account.user_name = user_name
        account.password = password

        return account.save()

    @staticmethod
    def create(uid, user_name, password):
        account = Account(uid=uid, user_name=user_name, password=password)

        return account.save()
