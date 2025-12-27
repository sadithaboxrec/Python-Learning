class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item,quantity):
        self.items.append((item,quantity))

    def display_order(self):
        print("\t\t** Your Order **")
        for item,quantity in self.items:
            print(f"{item.name} x{quantity} - Rs.{item.price * quantity}")

    def get_total(self):
        return sum(item.price * quantity for item, quantity in self.items)
