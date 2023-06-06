class User():
    id = None
    login = None
    password = None
    first_name = None
    last_name = None

    def __init__(self, login, password, first_name, last_name, id=None):
        self.id = id
        self.login = login
        self.password = password
        self.first_name = first_name
        self.last_name = last_name