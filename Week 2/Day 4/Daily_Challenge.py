matrix_string = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# Convert the matrix string into a 2D list
matrix = [list(row) for row in matrix_string.split('\n')]

# Transpose the matrix to read columns from left to right
transposed_matrix = list(zip(*matrix))

# Initialize an empty string to store the decrypted message
decrypted_message = ""

# Iterate through each column of the transposed matrix
for column in transposed_matrix:
    # Initialize a flag to check if an alphanumeric character has been found
    alphanumeric_found = False
    # Initialize an empty string to store the characters in the current group
    current_group = ""
    # Iterate through each character in the column
    for char in column:
        # Check if the character is alphanumeric
        if char.isalnum():
            # If an alphanumeric character is found, set the flag to True and add it to the current group
            alphanumeric_found = True
            current_group += char
        # If the character is not alphanumeric and a previous alphanumeric character has been found,
        # replace the current group with a space
        elif alphanumeric_found:
            decrypted_message += current_group + " "
            current_group = ""
            alphanumeric_found = False
    # After iterating through all characters in the column, add the last group to the decrypted message
    if alphanumeric_found:
        decrypted_message += current_group + " "

# Print the decrypted message
print("Decrypted message:")
print(decrypted_message.strip())
