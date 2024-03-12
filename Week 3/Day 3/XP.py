# Exercise 1
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         return f"{self.amount} {self.currency}"

#     def __int__(self):
#         return self.amount

#     def __repr__(self):
#         return f"{self.amount} {self.currency}"

#     def __add__(self, other):
#         if isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             else:
#                 return Currency(self.currency, self.amount + other.amount)
#         else:
#             return Currency(self.currency, self.amount + other)

#     def __iadd__(self, other):
#         if isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             else:
#                 self.amount += other.amount
#         else:
#             self.amount += other
#         return self

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1))  
# print(int(c1)) 
# print(repr(c1))  
# print(c1 + 5)  
# print(c1 + c2)  
# print(c1)

# c1 += 5
# print(c1) 

# c1 += c2
# print(c1)  


# Exercise 2
# func.py
# def add_two_numbers(a, b):
#     result = a + b
#     print("The sum is:", result)

# # exercise_one.py

# from func import add_two_numbers

# # Example usage
# add_two_numbers(5, 7)

# # Exercise 3
# import random
# import string

# def generate_random_string(length):
#     characters = string.ascii_letters 

#     random_string = ''.join(random.choice(characters) for _ in range(length))
    
#     return random_string

# random_string = generate_random_string(5)
# print("Random String:", random_string)

# # Exercise 4
# import datetime

# def display_current_date():
#     current_date = datetime.datetime.now().date()
#     print("Current date:", current_date)

# display_current_date()


# Exercise 5
# from datetime import datetime

# def time_until_january_1st():

#     now = datetime.now()

#     january_1st_next_year = datetime(now.year + 1, 1, 1)

#     time_difference = january_1st_next_year - now

#     days = time_difference.days
#     hours, remainder = divmod(time_difference.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)

#     if days == 1:
#         days_string = "1 day"
#     else:
#         days_string = f"{days} days"

#     time_left = f"{days_string} and {hours:02}:{minutes:02}:{seconds:02} hours"
#     print("The 1st of January is in", time_left)

# time_until_january_1st()


# Exercise 6
# from datetime import datetime

# def minutes_lived(birthdate):
    
#     birth_datetime = datetime.strptime(birthdate, '%Y-%m-%d')
    
#     current_datetime = datetime.now()
    
#     minutes_lived = (current_datetime - birth_datetime).total_seconds() / 60
    
#     return int(minutes_lived)

# birthdate = "1990-05-15"
# print("You have lived for approximately", minutes_lived(birthdate), "minutes.")


