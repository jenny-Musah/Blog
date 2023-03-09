from data.dto import UserRegisterRequest
from data.dto import UserLoginRequest


class UserService:

    def register(self,  user_register_request: UserRegisterRequest):
        raise Exception("Method has no implementation")

    def login(self, user_login_request: UserLoginRequest):
        raise Exception("Method has no implementation")