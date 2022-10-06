class Customers:
    # Initializer or constructor
    def __init__(self, name, type):
        self._name = name
        self.type = type

    # string method ==> overriding something
    def __str__(self):
        return self._name + ' ' + self.type

    # This is how to access a protected instance attribute
    # remember access kind is getter
    @property
    def name(self):
        return self._name


customers = [Customers('Ben', 'Blue'), Customers('Dela', 'Red'), Customers('Grace', 'Green')]

# for customer in customers:
#     print(customer)
# print('Done')

print(customers[0].name)
print()
