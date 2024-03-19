# Read the file line by line
# Read only the 5th line of the file
# Read only the 5 first characters of the file
# Read all the file and return it as a list of strings. Then split each word
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"

f = open("namelist.txt","r")
# for line in f:
#     print(line)

# print(f.read(3))
# f.close()
all_file = f.read()
print(all_file)
with open("namelist.txt") as file:
    for line in file:
        x = line.split()
    
print(x)