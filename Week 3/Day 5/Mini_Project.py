# class AnagramChecker:
#     def __init__(self, word_list_file):
#         with open(word_list_file, 'r') as file:
#             self.word_list = set(word.strip().lower() for word in file)

#     def is_valid_word(self, word):
#         word = word.strip().lower()
#         return word in self.word_list

#     def is_anagram(self, word1, word2):
#         word1 = word1.lower()
#         word2 = word2.lower()
#         return sorted(word1) == sorted(word2)

#     def get_anagrams(self, word):
#         word = word.lower()
#         return [w for w in self.word_list if self.is_anagram(w, word) and w != word]


# def input_word():
#     while True:
#         word = input("Enter a word (or type 'exit' to quit): ").strip()
#         if word.lower() == 'exit':
#             return None
#         if ' ' in word:
#             print("Error: Only one word is allowed.")
#             continue
#         if not word.isalpha():
#             print("Error: Only alphabetic characters are allowed.")
#             continue
#         return word


# def main():
#     anagram_checker = AnagramChecker('words.txt')
#     print("Welcome to the Anagram Checker!")
#     while True:
#         word = input_word()
#         if word is None:
#             print("Goodbye!")
#             break
#         if anagram_checker.is_valid_word(word):
#             print(f"Your word: \"{word}\"")
#             print("This is a valid English word.")
#             anagrams = anagram_checker.get_anagrams(word)
#             if anagrams:
#                 print("Anagrams for your word:", ', '.join(anagrams))
#             else:
#                 print("No anagrams found for your word.")
#         else:
#             print(f"\"{word}\" is not a valid English word.")


# if __name__ == "__main__":
#     main()
