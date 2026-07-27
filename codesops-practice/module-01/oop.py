class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class BankCustomer(Person):
    def __init__(self, name, bank):
        super().__init__(name)
        self.bank = bank

    def display_info(self):
        print("Name:", self.name)
        print("Bank:", self.bank)


customer = BankCustomer("gudeta", "Commercial Bank")
customer.display_name()
customer.display_info()
class Users:
    def __init__(self),username,email)
        pass

        





