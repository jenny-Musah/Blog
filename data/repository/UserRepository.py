from data.model.User import User


class UserRepository:

    def save(self, user: User) -> User:
        raise NotImplementedError

    def find_user_by_email(self, email: str):
        raise NotImplementedError
