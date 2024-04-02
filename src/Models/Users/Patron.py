from .User import User


class Patron(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
    
    def borrow_items(self):
        print(f"{self.name} can borrow items from the catalog.")

    def check_in(self, item):
        item.check_in()
    
    def check_out(self, item):
        item.check_out()
        