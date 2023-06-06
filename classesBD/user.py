class User():
    id = None
    username = None
    password_hash = None
    first_name = None
    last_name = None
    registered_at = None

    def __init__(self, id, username, password_hash, first_name, last_name, registered_at):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.registered_at = registered_at