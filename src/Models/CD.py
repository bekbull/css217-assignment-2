from .Item import Item


class CD(Item):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.duration = duration
