# # Exercise 1
# def display_message():
#     print("In this course, I am learning how to write Python functions and improve my programming skills.")

# display_message()

# Exercise 2
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")

# favorite_book("The Great Gatsby")

#Exercise 3
# def describe_city(city, country="Unknown"):
#     print(f"{city} is in {country}")

# describe_city("Reykjavik", "Iceland")
# describe_city("Paris", "France")
# describe_city("Tokyo")

# Exercise 4
# import random

# def compare_numbers(guess):
#     if guess < 1 or guess > 100:
#         print("Please enter a number between 1 and 100.")
#         return
    
#     generated_number = random.randint(1, 100)
    
#     if guess == generated_number:
#         print("Success! You guessed the correct number.")
#     else:
#         print(f"Fail! The generated number was {generated_number}.")
    
#     print(f"Your guess: {guess}")
#     print(f"Generated number: {generated_number}")

# compare_numbers(50)

#Exercise 5
# def make_shirt(size="large", text="I love Python"):
#     print(f"The size of the shirt is {size} and the text is '{text}'.")

# make_shirt()

# make_shirt("medium")

# make_shirt("small", "Hello World!")

# # Bonus: 
# make_shirt(size="extra large", text="Python is fun!")

# # Exercise 6
# def show_magicians(magicians):
#     """Prints the name of each magician in the list."""
#     for magician in magicians:
#         print(magician)

# def make_great(magicians):
#     """Modifies the original list of magicians by adding 'the Great' to each magician's name."""
#     for i in range(len(magicians)):
#         magicians[i] = "the Great " + magicians[i]

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# make_great(magician_names)

# show_magicians(magician_names)

# # Exercise 7
# import random

# def get_random_temp(season):
#     """Returns a random temperature based on the season."""
#     if season.lower() == 'summer':
#         return random.randint(16, 40)
#     elif season.lower() == 'autumn' or season.lower() == 'fall':
#         return random.randint(-10, 23)
#     elif season.lower() == 'winter':
#         return random.randint(-10, 16)
#     elif season.lower() == 'spring':
#         return random.randint(0, 23)
#     else:
#         print("Invalid season. Please enter summer, autumn, winter, or spring.")

# def main():
#     """Generates a random temperature based on the season and provides friendly advice."""
#     season = input("Enter the season (summer, autumn, winter, or spring): ")
#     temperature = get_random_temp(season)
#     print(f"The temperature right now is {temperature} degrees Celsius.")

#     if temperature < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif 0 <= temperature <= 16:
#         print("Quite chilly! Don’t forget your coat.")
#     elif 16 < temperature <= 23:
#         print("It's a moderate temperature. Enjoy your day!")
#     elif 24 <= temperature <= 32:
#         print("Warm weather! Stay hydrated.")
#     elif 32 < temperature <= 40:
#         print("Hot day ahead! Seek shade and stay cool.")

# main()
