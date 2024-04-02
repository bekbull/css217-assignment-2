from .Item import Item

class Magazine(Item):
    def __init__(self, title, author, item_id, issue):
        super().__init__(title, author, item_id)
        self.issue = issue