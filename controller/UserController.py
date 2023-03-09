import atexit

import jsons as jsons
from flask import request

from application_bean import return_server
from data.repository.UserRepositoryImpl import  move_to_file, get_data
from service.UserServiceImpl import UserServiceImpl

app = return_server()
user_service: UserServiceImpl = UserServiceImpl()

atexit.register(move_to_file)


@app.before_first_request
def before_app_run():
    get_data()


@app.post('/api/v1/register')
def register():
    user_request = request.get_json()
    try:
        return jsons.dump(user_service.register(user_request))
    except ValueError as e:
        return e


@app.post('/api/v1/login')
def login():
    request_body = request.get_json()
    try:
        return jsons.dump(user_service.login(request_body))
    except ValueError as error:
        return error
