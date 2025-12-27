from menu_item import MenuItem

class Menu:
    def __init__(self):
        self.items = []

    def load_menu(self):
        self.items.append(MenuItem(1, "Coffee", 200))
        self.items.append(MenuItem(2, "Tea", 100))
        self.items.append(MenuItem(3, "Sandwich", 150))
        self.items.append(MenuItem(4, "Fish Puff", 200))
        self.items.append(MenuItem(5, "Donut", 250))
        self.items.append(MenuItem(6, "HotDog", 350))

    def display(self):
        print("\t\t**Saditha's Cafe Menu** ")
        for item in self.items:
            print(item)

    def get_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None
