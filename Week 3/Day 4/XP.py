# # # Exercise 1

# # import random

# # def get_words_from_file(wordlist):
# #     with open("wordlist.txt", 'r') as file:
# #         words = file.read().splitlines()
# #     return words

# # def get_random_sentence(length, words):
# #     random_words = random.sample(words, length)
# #     random_sentence = ' '.join(random_words)
# #     return random_sentence.lower()

# # def validate_length_input(input_str):
# #     try:
# #         length = int(input_str)
# #         if length < 2 or length > 20:
# #             return False
# #         return True
# #     except ValueError:
# #         return False

# # def main():
# #     print("Welcome to the Random Sentence Generator!")
# #     words = get_words_from_file("word_list.txt")
    
# #     while True:
# #         length_input = input("How long do you want the sentence to be (between 2 and 20)? ")
        
# #         if validate_length_input(length_input):
# #             length = int(length_input)
# #             sentence = get_random_sentence(length, words)
# #             print("Generated Sentence:", sentence)
# #             break
# #         else:
# #             print("Invalid input. Please enter an integer between 2 and 20.")

# # if __name__ == "__main__":
# #     main()

# # Exercise 2

# import json

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# data = json.loads(sampleJson)

# salary = data["company"]["employee"]["payable"]["salary"]
# print("Salary:", salary)

# data["company"]["employee"]["birth_date"] = "1990-01-01"  # Example birth date

# with open("modified_json.json", "w") as file:
#     json.dump(data, file, indent=4)

# print("JSON saved to file 'modified_json.json'")
