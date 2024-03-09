# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez',
#     'age': 30,
#     }

# print(rick_dict['first_name'] + " " + rick_dict['last_name'] + " is " + str(rick_dict['age']) + " years")

# a_dict = {
#             'color': 'blue', 
#             'fruit': 'apple',
#             'pecdsjt': 23,
#             'colcdsor': 'red', 
#             'fruceit': 24,
#             'pecdst': 'dpet',
# }
# for key, value in a_dict.items():
#     print(key, '------>', value)

# my_dog = {
#     'name': 'Rufus',
#     'age': 4,
    
#     'best_friend': {
#     'name': 'Felix',
#     'age': 4.5
#     },
    
#     'favorite_foods': ['steaks', 'sausages', 'shawarma']
# }
# print("My dog's name is", my_dog['name'],"and his best friend's name is", my_dog['best_friend']['name'],"but my dog is", my_dog['age'], "years old and",my_dog['best_friend']['name'],"is",my_dog['best_friend']['age'],"years old.")

# shirts = [
#     {
#     'name': 'Awesomes T-shirt 3000',
#     'size': 'S',
#     'price': 20
#     },
#     {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
#     },
#     {
#     'name': 'Awesomez T-shirt 3000',
#     'size': 'L',
#     'price': 30
#     },
# ]
# print(shirts[1]['name'], '------>', shirts[0]['size'], '------>', shirts[2]['price'])

# sample_dict = { 
#         "class":{ 
#         "student":{ 
#         "name":"Mike",
#         "marks":{ 
#             "physics":70,
#             "history":80
#                 }
#                     }
#                 }
#             }

# x = sample_dict.keys()
# y = sample_dict.values()
# z = sample_dict.items()
# # for key in sample_dict:
# #     print(sample_dict["class"]["student"]["marks"])
# #(modify a value in a key) sample_dict["class"]["student"]["marks"]["history"] = 250
# #(add a value in a key) sample_dict["class"]["student"]["marks"]["history"] = 250, 80
# #(erase a key)del sample_dict["class"]["student"]["marks"]["history"]
# #(a key and a value in a key) sample_dict["class"]["student"]["marks"]["weigth"] = 80
# # print(sample_dict["class"]["student"]["marks"])
# print(x,"\n")
# print(y,"\n")
# print(z)

# sample_dict = {
#     "name": "Kelly",
#     "age":25,
#     "salary": 8000,
#     "city": "New york"
#             }
# del sample_dict["salary"]
# del sample_dict["name"]
# print(sample_dict)

# my_books =  {
#             "title": "Harry Potter",
#             "author": "JK Rowling",
#             }

# for x, y in my_books.items():
#     print("The " + x + " is " + y)

### print(list(range(1, 11, 3)))

# for item in enumerate('Rachel ma femme que j\'aime à la folie'):
#     print(item)

# for (index, letter) in enumerate('Rachel ma femme que j\'aime à la folie'):
#     print('At index {} the letter is {}'.format(index, letter))


# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

# for item in zip(list1, list2, list3):
#     print(item)

# x = 0
# while x < 2:
#     print(f'x is {x}')
#     x += 1
# else:
#     print('x is bigger than 2')

# for letter in 'Leonardo':
#     if letter == 'a':
#         break
#     print(letter,end='') # end='' renders each letter next to the other

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':  
#         break
#     print('Length of the string is', len(s))
# print('Done')

# for letter in 'Leonardo':
#     if letter == 'o':
#         continue
#     print(letter, end='') # dont execute for 'o' letter

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     if len(s) < 3:
#         print('Too small')
#         continue
#     print('Input is of sufficient length')

# my_number = '1234'
# my_list = []

# for num in my_number:
#     my_list.append(num)
# print(my_list)

# my_number = '1234'
# my_list = []

# my_list = [num for num in my_number]
# print(my_list)

# my_list = [x for x in range(0,6)]
# print(my_list)

# my_list = [x**2 for x in range(0,6)] # square
# print(my_list)

# my_list = [x for x in range(0,11) if x%2 == 0] # only even
# print(my_list)

# my_list = []

# for i in [2, 3, 4]:
#     for j in [100, 200, 300]:
#         my_list.append(i*j)

# print(my_list)

# my_list = []
# my_list = [(i*j) for i in [2, 3, 4] for j in [100, 200, 300]]
# print(my_list)

# family_age = {'Lea': 12, 'Mark': 25, 'George': 50}

# new_year = 1

# new_family_age = {name: age+new_year for (name, age) in family_age.items()}

# print(new_family_age)


#XP_Gold

# birthdays = {
#     "Alice": "1990/05/15",
#     "Bob": "1985/09/20",
#     "Charlie": "1992/02/10",
#     "David": "1988/11/25",
#     "Eve": "1995/07/03"
# }

# print("Welcome! You can look up the birthdays of the people in the list!")
# print(birthdays.keys())
# user = input("Enter one name of the list : ")
# while True:
#     if user in birthdays.keys():
#         print(birthdays.get(user))
#     elif user != birthdays.keys():
#         print("Sorry, we don’t have the birthday information for",{user})
#         user = input("Enter one name of the list : ")
    





