import csv

class Inventory:
    def __init__(self, filename):
        self.items = []
        self.load_csv(filename)

    def load_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.items = list(reader)

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item['ID'] == item_id:
                return item
        return None

    def search_by_name(self, name):
        return [item for item in self.items if name.lower() in item['Name'].lower()]
