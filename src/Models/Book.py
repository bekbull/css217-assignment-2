from .Item import Item


class Book(Item):
    def __init__(self, title, author, item_id, isbn, genre):
        super().__init__(title, author, item_id)
        self.isbn = isbn
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ID: {self.item_id}")
        print(f"ISBN: {self.isbn}")
        print(f"Genre: {self.genre}")
