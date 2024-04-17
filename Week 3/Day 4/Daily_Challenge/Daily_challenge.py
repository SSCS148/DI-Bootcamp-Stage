# class Text:
#     def __init__(self, text):
#         self.text = text

#     def word_frequency(self, word):
#         words = self.text.split()
#         count = words.count(word)
#         if count == 0:
#             return f"The word '{word}' is not found in the text."
#         else:
#             return f"The word '{word}' appears {count} times in the text."

#     def most_common_word(self):
#         words = self.text.split()
#         word_counts = {}
#         for word in words:
#             word_counts[word] = word_counts.get(word, 0) + 1
#         most_common_word = max(word_counts, key=word_counts.get)
#         return most_common_word

#     def unique_words(self):
#         words = self.text.split()
#         unique_words = set(words)
#         return list(unique_words)

#     @classmethod
#     def from_file(cls, filename):
#         with open(filename, 'r') as file:
#             text = file.read()
#         return cls(text)

# # Part I: Analyzing a simple string
# simple_text = "A good book would sometimes cost as much as a good house."
# text_obj = Text(simple_text)

# print("Word frequency of 'good':", text_obj.word_frequency('good'))
# print("Most common word:", text_obj.most_common_word())
# print("Unique words:", text_obj.unique_words())

# # Part II: Analyzing a text from an external file
# stranger_text = Text.from_file('the_stranger.txt')
# print("\nWord frequency of 'the':", stranger_text.word_frequency('the'))
# print("Most common word:", stranger_text.most_common_word())
# print("Unique words:", stranger_text.unique_words())
