import pickle

from data.model.User import User
from data.repository.UserRepository import UserRepository


def move_to_file():
    with open('user_db.pkl', 'wb') as user_data:
        pickle.dump(user_db, user_data)


def get_data():
    with open('user_db.pkl', 'rb') as user_data:
        data = pickle.load(user_data)
        user_db.update(data)


counter = 0
user_db = {}


class UserRepositoryImpl(UserRepository):

    def save(self, user: User) -> User:
        user_id = self.generate_id()
        user.set_id(user_id)
        user_db[user_id] = user
        return user

    def generate_id(self) -> int:
        return counter + 1

    def find_user_by_email(self, email: str) -> User:
        for value in user_db.values():
            if value.email_address == email:
                return value

    def load_db(self):
        user_db.update()