from models import CodeAuth
import uuid
class CodeAuthRepository:

    @staticmethod
    def update(self, uid, code):
        code = self.get(uid)
        code.code = code
        return code_auth.save()

    @staticmethod
    def create(code):
        code_auth = CodeAuth(uid=str(uuid.uuid4()), code=code)
        return code_auth.save()

    @staticmethod
    def get(code):
        return CodeAuth.query.filter_by(code=code).first()
