from models import CodeAuth
import uuid
class CodeAuthRepository:

    @staticmethod
    def create(code, email):
        code_auth = CodeAuth(uid=str(uuid.uuid4()), code=code, email=email)
        return code_auth.save()

    @staticmethod
    def get(code):
        return CodeAuth.query.filter_by(code=code).first()

    @staticmethod
    def getAll():
        return CodeAuth.query.all()