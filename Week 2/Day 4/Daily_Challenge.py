# matrix_string = """7ii
# Tsx
# h%?
# i #
# sM 
# $a 
# #t%
# ^r!"""

# matrix = [list(row) for row in matrix_string.split('\n')]
# transposed_matrix = list(zip(*matrix))
# decrypted_message = ""
# for column in transposed_matrix:
#     alphanumeric_found = False
#     current_group = ""
#     for char in column:
#         if char.isalnum():
#             alphanumeric_found = True
#             current_group += char
#         elif alphanumeric_found:
#             decrypted_message += current_group + " "
#             current_group = ""
#             alphanumeric_found = False
#     if alphanumeric_found:
#         decrypted_message += current_group + " "

# # Print the decrypted message
# print("Decrypted message:")
# print(decrypted_message.strip())
