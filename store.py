import csv


class Item:
    # class attribute
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validate received arguments
        assert price >= 0, f"Price {price} should be grater or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} should be grater or equal to 0"

        # The object stuffs
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append all instances of the class
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        # using the pay_rate as class attr will prevent you from setting the instance level pay_rates
        # self.price = self.price * Item.pay_rate
        # What I mean (instance level pay_rate) could be reassign in any object of the class
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()

# print(item1.price)
# item1.apply_discount()
# print(item1.price)
#
# print(item2.price)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# for instance in Item.all:
#     print(instance.name)

print(Item.all)


