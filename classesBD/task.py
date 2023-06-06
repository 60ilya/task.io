class Task:
    id = None
    title = None
    description = None
    checkbox = None
    column_id = None
    user_id = None
    photo = None

    def __init__(self, title, description, checkbox, column_id, user_id):
        self.title = title
        self.description = description
        self.checkbox = checkbox
        self.column_id = column_id
        self.user_id = user_id
        self.photo = photo