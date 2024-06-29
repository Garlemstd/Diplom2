
class Header:
    def __init__(self, token):
        self.header_key = "Authorization"
        self.token = token

    def authorization_header(self):
        return {self.header_key: self.token}
