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

# # Exercise 8
# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]

# def take_quiz(questions):
#     correct_answers = 0
#     incorrect_answers = 0
#     wrong_answers = []

#     for question_data in questions:
#         question = question_data["question"]
#         correct_answer = question_data["answer"]
        
#         user_answer = input(question + "\nYour answer: ").strip()

#         if user_answer.lower() == correct_answer.lower():
#             print("Correct!")
#             correct_answers += 1
#         else:
#             print("Incorrect!")
#             incorrect_answers += 1
#             wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

#     return correct_answers, incorrect_answers, wrong_answers

# def display_results(correct_answers, incorrect_answers, wrong_answers):
#     print("\nQuiz Results:")
#     print("Number of correct answers:", correct_answers)
#     print("Number of incorrect answers:", incorrect_answers)

#     if incorrect_answers > 0:
#         print("\nQuestions answered incorrectly:")
#         for wrong_answer in wrong_answers:
#             print("Question:", wrong_answer["question"])
#             print("Your answer:", wrong_answer["user_answer"])
#             print("Correct answer:", wrong_answer["correct_answer"])
#             print()

# def play_quiz():
#     correct_answers, incorrect_answers, wrong_answers = take_quiz(data)
#     display_results(correct_answers, incorrect_answers, wrong_answers)
    
#     if incorrect_answers > 3:
#         print("You had more than 3 wrong answers. Please play again.")
#         play_quiz()

# # Start the quiz
# play_quiz()
