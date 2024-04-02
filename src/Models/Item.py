class Item:
    def __init__(self, title, author, item_id, in_library=True):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.in_library = in_library
    
    def check_in(self):
        self.in_library = True
        print(f"{self.title} has been checked in.")
    
    def check_out(self):
        self.in_library = False
        print(f"{self.title} has been checked out.")