from data.dto.UserLoginRequest import UserLoginRequest
from data.model.User import User
from data.repository.UserRepository import UserRepository


def convertRegisterRequest_to_userModel(registerRequest, user: User):
    user.password = registerRequest.get("password")
    user.last_name = registerRequest.get("lastName")
    user.first_name = registerRequest.get("firstName")
    user.email_address = registerRequest.get("emailAddress")


def mapping_email_from_request(request):
    email = request.get("emailAddress")
    return email


def mapping_password_from_request(request):
    password = request.get("password")
    return password
