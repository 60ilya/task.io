class Table:
    id = None
    private = None
    description = None
    title = None
    user_id = None

    def __init__(self, private, description, title):
        self.private = private
        self.description = description
        self.title = title

    