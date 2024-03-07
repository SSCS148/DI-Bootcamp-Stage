fruits = input("Enter a list of fruits: ")
storage = fruits.split()
print(fruits)
name_of_fruit = input("Enter a name of fruit: ")
if name_of_fruit in storage:
    print(name_of_fruit + " is already in the list.")
else:
    print(name_of_fruit + " is not in the list.")