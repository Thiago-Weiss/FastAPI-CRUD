from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes= ["bcrypt"], deprecated= "auto")


class Hash():
    @staticmethod
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(password: str, password_hash: str):
        return pwd_cxt.verify(password, password_hash)