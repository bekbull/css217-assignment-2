from .Item import Item


class CD(Item):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.duration = duration
        self.in_library = True
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ID: {self.item_id}")
        print(f"Duration: {self.duration}")
        print(f"In Library: {self.in_library}")
