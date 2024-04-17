# import re

# MATRIX_STRING = "7i3Tsih%xi #sM $a #t%^r!"
# COLUMNS = 3
# ROWS = 8

# matrix = [char for char in MATRIX_STRING]

# matrix = [list(row) for row in zip(*[iter(matrix)]*COLUMNS)]


# no_digits_list = list()

# for col in range(COLUMNS):
#     for row in range(ROWS):
#         if not matrix[row][col].isdigit():
#             no_digits_list.append(matrix[row][col])

# no_digits_string = "".join(no_digits_list)

# print(re.sub('[^A-Za-z0-9]+', ' ', no_digits_string))
