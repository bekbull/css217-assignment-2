class LibrarySystem:
    def __init__(self, catalog):
        self.catalog = catalog

    def add_item(self, item_type, *args, **kwargs):
        # Dynamically creating an instance of the specified item_type.
        # The item_type parameter is expected to be a class from the Item hierarchy.
        item = item_type(*args, **kwargs)
        self.catalog.add_item(item)
