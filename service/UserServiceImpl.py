from data.dto.UserLoginRequest import UserLoginRequest
from data.model.User import User
from data.repository import UserRepository
from data.repository.UserRepositoryImpl import UserRepositoryImpl
from service.UserService import UserService
from data.dto import UserRegisterRequest
from utils.Mapper import convertRegisterRequest_to_userModel, mapping_email_from_request, mapping_password_from_request

global user_repositoryImpl


class UserServiceImpl(UserService):

    def __init__(self):
        global user_repositoryImpl
        user_repositoryImpl = UserRepositoryImpl()

    def register(self, user_register_request: UserRegisterRequest):
        user: User = User()
        convertRegisterRequest_to_userModel(user_register_request, user)
        return user_repositoryImpl.save(user)

    def login(self, user_login_request: UserLoginRequest):
        user: User = user_repositoryImpl\
            .find_user_by_email(mapping_email_from_request(user_login_request))
        if user is None:
            return "Incorrect login detail"
        elif user.password != mapping_password_from_request(user_login_request):
            return "Incorrect login details"
        return "Login successful"
