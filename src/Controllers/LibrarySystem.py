class LibrarySystem:
    def __init__(self, catalog):
        self.catalog = catalog

    def add_item(self, item_type, *args, **kwargs):
        item = item_type(*args, **kwargs)
        self.catalog.add_item(item)
    
    def remove_item(self, item_id):
        self.catalog.remove_item(item_id)

    def check_out_item(self, item_id):
        item = self.find_item(item_id)
        if item:
            item.check_out()
        else:
            print("Item not found in the catalog.")
    
    def check_in_item(self, item_id):
        item = self.find_item(item_id)
        if item:
            item.check_in()
        else:
            print("Item not found in the catalog.")