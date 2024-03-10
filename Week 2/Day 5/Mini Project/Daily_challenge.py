# Exercise 1

def sort_words(input_str):
    words = [word.strip() for word in input_str.split(',')]
    
    sorted_words = sorted(words)
    
    result = ','.join(sorted_words)
    
    return result

input_str = input("Enter a comma-separated sequence of words: ")
sorted_sequence = sort_words(input_str)
print("Sorted sequence:", sorted_sequence)


# Exercise 2

