
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def wheels(self):
        pass

    def description(self):
        return f"This vehicle is made in {self.make} and it is {self.model} model."


class Car(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def wheels(self):
        return "Car has 4 wheels"

    def description(self):
        return f"This car is made in {self.make}, model {self.model}, capacity {self.capacity}"


class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().init(make, model)
        self.capacity = capacity

    def wheels(self):
        return "Truck has 6 wheels"

    def description(self):
        return f"This truck is made in {self.make}, model {self.model}, capacity {self.capacity}"


car = Car("China", "BYD", "25 ton")
print(car.description())
print(car.wheels())

class Product:
    def init(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, new_inventory):
        if new_inventory <= 0:
            return "Restock amount must be greater than 0."

        self.quantity += new_inventory
        return f"New quantity: {self.quantity}"

    def sell(self, sold_goods):
        if sold_goods <= 0:
            return "Sold quantity must be greater than 0."

        if sold_goods > self.quantity:
            return "Not enough stock available."

        self.quantity -= sold_goods
        return f"Remaining quantity: {self.quantity}"


new_product = Product("Brake Pad", 5500, 30)

print(new_product.restock(25))
print(new_product.sell(20))
print(new_product.sell(50))