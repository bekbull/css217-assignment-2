from .Item import Item

class Magazine(Item):
    def __init__(self, title, author, item_id, issue):
        super().__init__(title, author, item_id)
        self.issue = issue
        self.in_library = True
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ID: {self.item_id}")
        print(f"Issue: {self.issue}")
        print(f"In Library: {self.in_library}")
    