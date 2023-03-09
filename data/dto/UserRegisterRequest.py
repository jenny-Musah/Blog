class UserRegisterRequest:

    def __int__(self, first_name: str, last_name: str, email_address: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email_address(self):
        return self.email_address

    def get_password(self):
        return self.password
