# class Dog():
#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)

# shelter_dog = Dog(name_of_the_dog="Rex")
# # or
# shelter_dog = Dog("Rex")

# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# first_person = Person("John", 36)

# print(first_person.name)
# print(first_person.age)

# class Point():
#     def __init__(info, name, age):
#         info.name = name
#         info.age = age
# ## create an instance of the class
# p = Point("Sacha",23)
# ## access the attributes
# print("My name is : ", p.name)
# print("My age is : ", p.age)


# class Dog():
#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

#     def bark(self):
#         print("{} barks ! WAF".format(self.name))

# print(Dog("Rex").bark())

# class Dog():
#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

#     def bark(self):
#         print("{} barks ! WAF".format(self.name))

#     def walk(self, number_of_meters):
#         print("{} walked {} meters".format(self.name, number_of_meters))

# shelter_dog = Dog("Rex")
# shelter_dog.walk(10)

# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

# first_person = Person("John", 36) #Output only the name is John
# first_person.show_details() #No output

# class Computer():
#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()

# Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
# dell_computer.description("Mark")

# class BankAccount:

#     def __init__(self, account_number, balance=0):
#         self.__account_number = account_number
#         self.__balance = balance
#         self.__transactions = []

#     def view_balance(self):
#         self.__transactions.append("View Balance")
#         return f"Balance for account {self.__account_number}: {self.__balance}"

#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Invalid amount")
#         elif amount < 100:
#             raise ValueError("Minimum deposit is 100")
#         else:
#             self.__balance += amount
#             self.__transactions.append(f"Deposit: {amount}")
#             return "Deposit Successful"

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             raise ValueError("Insufficient Funds")
#         else:
#             self.__balance -= amount
#             self.__transactions.append(f"Withdraw: {amount}")
#             return "Withdraw Approved"

#     def view_transactions(self):
#         result = "Transactions:\n-------------\n"
#         for transaction in self.__transactions:
#             result += transaction + "\n"
#         return result

#     def get_account_number(self):
#         return self.__account_number

#     def get_balance(self):
#         return self.__balance

#     def get_transaction_history(self):
#         return self.__transactions


# # Example usage:
# account = BankAccount("12345")
# print(account.deposit(200))  # Deposit Successful
# print(account.withdraw(50))  # Withdraw Approved
# print(account.view_balance())  # Balance for account 12345: 150
# print(account.view_transactions())

# class Cat:
#     def __init__(self, cat_name, cat_age):  
#         self.name = cat_name
#         self.age = cat_age 

# old = Cat("Rex", 2)
# Cat1 = Cat("Rex", 12)
# Cat2 = Cat("Mittens", 7)
# Cat3 = Cat("Felix", 4)

# def find_oldest_cat(cat_list):
#     oldest_cat = None
#     max_age = 0
#     for cat in cat_list:
#         if cat.age > max_age:
#             oldest_cat = cat
#             max_age = cat.age
#     return oldest_cat

# cat_list = [Cat1, Cat2, Cat3]
# oldest_cat = find_oldest_cat(cat_list)
# print(oldest_cat.name, "is the oldest cat, he is ",oldest_cat.age)  


class Dog:
    def __init__(self, name_of_the_dog,height):
        print("A new dog has been initialized!")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog
        self.height = height
    def bark(self):
        print("{} barks! WAF".format(self.name))
    def jump(self):
        print("{} jumps!".format(self.name))
        self.height += 10
        print("He is now {} meters tall".format(self.height))
    
print