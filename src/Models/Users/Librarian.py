from .User import User


class Librarian(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)

    def manage_catalog(self):
        print(f"{self.name} can add or remove items from the catalog.")
