# #Exercise 1

# my_fav_numbers = {3, 7, 21, 42}
# my_fav_numbers.add(8)
# my_fav_numbers.add(13)
# my_fav_numbers.remove(13)
# friend_fav_numbers = {5, 11, 19, 23}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(my_fav_numbers)
# print(friend_fav_numbers)
# print(our_fav_numbers)

# #Exercise 2
# NO

# Exercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.pop(0)
# basket.pop(2)
# basket.append('Kiwi')
# basket.insert(0,"Apple")
# appple_count = basket.count("Apple")
# basket.clear()
# print(basket)


# Exercise 4
1# A float is a number that contains a decimal point or is written using scientific notation. ex: 1,-1,
# An integer is a whole number, either positive or negative, without any decimal point. ex: 1,-1,1.23,-1.23

2# list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

3# sequence = []
# i = 1.5
# while i <= 5:
#     sequence.append(i)
#     i += 0.5
# print(sequence)

# Exercise 5

1# for i in range(20):
#     i +=1
#     print(i)

2# for i in range(1,20):
#     if i%2 == 0:
#         print(i)

# Exercise 6
# user_name = 'Sacha'
# ur_name = input('Insert your name :')
# while ur_name != 'Sacha':
#     ur_name = input('Wrong name, try again :\n')
        
# print("Nice")

# Exercise 7

# Ur_favorite_fruits = input('Please. Separate the fruits with a single space : ')
# Favorite_fruits = Ur_favorite_fruits.split()
# Chosen_fruit = input("Now, please enter a fruit name: ")

# if Chosen_fruit in Favorite_fruits:
#     print("Oui")
# else:
#     print("No")

# Exercise 8

# pizza_toppings = []
# while True:
#     topping = input("Enter a pizza topping (type 'quit' to stop): ")
#     if topping.lower() == 'quit':
#         if len(pizza_toppings) == 0:
#             print("No toppings added. Exiting the program.")
#             break 
#         else:
#             print("Exiting the program.")
#             break 
#     print("Adding", topping, "to your pizza.")
#     pizza_toppings.append(topping)

# total_price = 10 + 2.5 * len(pizza_toppings)
# print("\nYour pizza will have the following toppings:")
# for topping in pizza_toppings:
#     print("-", topping)
# print("\nTotal price for your pizza:", total_price)

# Exercise 9
# def calculate_ticket_price(age):
#     if age < 3:
#         return 0
#     elif 3 <= age <= 12:
#         return 10
#     else:
#         return 15

# family_members = int(input("How many family members need tickets? "))
# total_cost = 0

# for _ in range(family_members):
#     age = int(input("Enter the age of the family member: "))
#     total_cost += calculate_ticket_price(age)

# print("Total cost for the family's tickets: $", total_cost)
# teenagers = ["Alice", "Bob", "Charlie", "David", "Emma"]
# teenagers = [name for name in teenagers if 16 <= int(input(f"Enter the age of {name}: ")) <= 21]
# print("Final list of teenagers permitted to watch the movie:", teenagers)

# Exercise 10
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")

# finished_sandwiches = []

# while sandwich_orders:
#     sandwich = sandwich_orders.pop(0)
#     finished_sandwiches.append(sandwich)
#     print("I made your", sandwich.lower())

# print("\nList of sandwiches made:")
# for sandwich in finished_sandwiches:
#     print("-", sandwich)