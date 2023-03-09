from datetime import date


class Article:

    def __int__(self, title : str, body : str):
        self.title = title
        self.body = body
        self.date = date.today()

