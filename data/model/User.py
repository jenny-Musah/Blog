class User:

    def __init__(self):
        self.id = None

    def __int__(self, first_name: str, last_name: str, email_address: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password

    def set_id(self, user_id):
        self.id = user_id

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email_address(self):
        return self.email_address
