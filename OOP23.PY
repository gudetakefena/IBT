#class and object 

class bankAccount:
    bank_name="CBE BANK"  #CLASS variable
    # class variable vs instance variable
    def init(self,owner,balance=0): 
            self.owner=owner # instance viable
            self.balance=balance # instance viable
    # method modifies or access the atribites  
    def returnOwnerName(self):
         return self.owner
    def deposit(self,amont):
          if amont<500:
             print("you need to deposit to open new bank account ")   
          else:
            self.balance += amont  
            print(f"you you add {amont} to your account , current balance is {self.balance}")
    def withdraw(self,amount):
        if self.balance<amount:
            print("insufficient balace ")
        else:
            self.balance-=amount
            print(f"your current balance is {self.balance}") 



acc1=bankAccount("hena",1000)
# print class variable 
print(bankAccount.bank_name)
print(type(acc1))

# print instance variable
print(f"{acc1.owner}  {acc1.balance}")

# change class variable for all object or instances
acc1.deposit(2500)
print(f"{acc1.owner}  {acc1.balance}")

acc1.withdraw(10000)
acc1.withdraw(1000)

# method
ownerName=acc1.returnOwnerName()
print(ownerName)

# encapsulation attributies are accessed or chanhed using getter or setter function 

class Encapsulation :
    def init(self,name):
        self.name=name
    def getter(self):
        return self.__name
    def setter(self,name):
        self.__name=name
        print(f"your name is changed to {self.__name}")
name=Encapsulation("henok")

# direct access is not allow as before in the back example like acc1.owner 

# print(name.__name) # this is an AttributeError  
# instead use getter to access private attributies.

getName=name.getter()

print(f"your name is {getName}")

# private atribities can't be changed directly like this 

# name.__name="chanege name" # this is an AttributeError

# print(name.__name)

settName=name.setter("slaseheran")

print(f"your name is {getName}")


# inheritance, overriding ,polymorphism , abstraction , dunk 

# inheritance
class vehicle ():
    def __init(self,brand,fromclass):
        self.brand=brand
        self.fromclass=fromclass
    def info(self,brand):
        print(f"this is {self.brand} form {self.fromclass} ")
class car(vehicle):
    def init(self,brand,fromclass,child):
        super().init(brand,fromclass)
        self.brand=brand
        self.fromclass=fromclass
        print (f"{self.brand} from {self.fromclass} ")


parent=vehicle("bmw","parent")
# parent.info("bmw")
child=car("toyota","child")