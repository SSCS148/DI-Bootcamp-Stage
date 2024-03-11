matrix_string = '''7ii Tsx h%? i # sM $a #t% ^r!'''

Column = 3
Rows = 8
rows = matrix_string.split('\n')
row = [row.split(' ') for row in rows]
print(rows)
matrix = []
# for i in range (len(matrix_string)):
#     sublist = list(matrix_string[i:i+Column])
#     matrix.append(sublist)
    
# print(matrix)
for row in rows:
        matrix.append(list(row))
        
matrix = [list(row) for row in matrix]
print(matrix)

transposed_matrix = list(zip(matrix))   
print(transposed_matrix)