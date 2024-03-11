# l1 = [1, 2, 3, 4, 5, 6]
# l1.append(3)
# l1.append([7, 8, 9])
# l1.extend([6, 7, 8])
# print(l1)

# l1=[1, 2, 3, 4, 5, 6]
# l1.insert(0, 6)
# print(l1)
# l2 = [1, 2, 3, 4, 5, "a", "a", "b", 1, 2, 4]
# s = l2.count('a')
# print(s)

# a = ["b", "g", "a", "d", "f", "c", "h", "e"]
# x = sorted(a)
# print("a after sorted function")
# print(a)
# print(x)
# b = [1, 2, 5, 8, 3]
# b.sort()
# print(b)

# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst[0:4])
# print(lst[::])
# print(lst[::-1])

# lst = [1, 2, 3, 4, 5, 6, 7]
# # lst.pop(0)
# # print(lst)
# print(lst)
# # lst.remove(1)
# # print(lst) 
# lst.clear()
# print(lst)

# t = (1, 2, 3, 4, 5, "a", "b", "c")
# t1 = 1, 2, 3, 4, "g", "l"
# print(t)
# print(t1)
# print(len(t))
# t2 = t+t1
# print(t2)

# t = (1, 2, 3, 4, 5)
# print(t)
# print("Minimum element in the tuple",min(t))
# print("Maximum element in the tuple",max(t))

# dict = {
#         1:'a',
#         2:'b',
#         5:'c',
#         4:'d'
#         }

# print(dict)
# print(dict[5])
# print("Maximum element in the tuple",max(dict))

cubes = {
        1: 1,
        2: 8,
        3: 27,
        4: 64,
        5: 125
        }

# print(cubes.pop(4))
# print(cubes)
# print(cubes.popitem())
# print(cubes)


# d = {
#     1:'10',
#     2:'20',
#     3:'30',
#     4:'40',
#     5:'50'
#     }

# l1 =list(d.keys())
# print("the key values are:")
# print(l1)
# l2 = list(d.values())
# print("The values are of dictionary is")
# print(l2)
# l3 = list(d.items())
# print("the list items are")
# print(l3)
# def display_board(board):
#     """
#     Function to display the Tic Tac Toe board.
#     """
#     print(board[0] + ' | ' + board[1] + ' | ' + board[2])
#     print('--|---|--')
#     print(board[3] + ' | ' + board[4] + ' | ' + board[5])
#     print('--|---|--')
#     print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# def player_input(player):
#     """
#     Function to get the position from the player.
#     """
#     position = int(input(f"Player {player}, enter your position (1-9): ")) - 1
#     return position


# def check_win(board, player):
#     """
#     Function to check whether there is a winner or not.
#     """
#     win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
#                       (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                       (0, 4, 8), (2, 4, 6)]

#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
#             return True
#     return False


# def play():
#     """
#     The main function, which calls all the functions created above.
#     """
#     board = [' ' for _ in range(9)]
#     current_player = 'X'

#     while True:
#         display_board(board)
#         position = player_input(current_player)

#         if board[position] == ' ':
#             board[position] = current_player

#             if check_win(board, current_player):
#                 print(f"Player {current_player} wins!")
#                 display_board(board)
#                 break

#             if ' ' not in board:
#                 print("It's a tie!")
#                 display_board(board)
#                 break

#             current_player = 'O' if current_player == 'X' else 'X'
#         else:
#             print("That position is already taken. Try again.")

# play()

# def say_hello(username):
#     print("Hello, World!"+username)
    

# say_hello(" Rick")
# say_hello(" Morty")

# def say_hello(username, language):
#     if language == "EN":
#         print("Hello " + username)
#     elif language == "FR":
#         print("Bonjour " + username)
#     else:
#         print("This language is not supported: " + language)

# say_hello(" Rick", "daz")
# def say_hello(username, language):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     else:
#         print("This language is not supported: " + language)

# say_hello("FR","Rick") # Won't work 
# say_hello("John's","EN")


# name = input("What is your name? ")
# day = input("What is your day of the week? ")
# def number_by_three(name, day):
#     sentence = 'Hello {}! Today is {}.'.format(name, day)
#     print(sentence)

# number_by_three(name, day)

# def get_formatted_name(first_name, last_name):
#     "Return a full name, neatly formatted."
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# # musician = get_formatted_name('jimi', 'hendrix') 
# # print(musician)
# print(get_formatted_name('jimi', 'hendrix'))


# def divided_by_three(number):
#     return number / 3
    
# print(divided_by_three(9.1))

# my_tuple = (1, 2, 3, 4, 5, 6)
# a,b,c,d,e,f = my_tuple
# print(a,b,c,d,e,f)
# print(a+b+c+d+e+f)
# print(a*b*c*d*e*f)
# print(a//b//c//d//e//f)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)


# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# def format_name(first_name, last_name):
#     return (first_name.title(), last_name.title())

# print(format_name(first_name, last_name))


# def calculation(addition, subtraction):
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     addition = a + b
#     subtraction = a - b
#     return addition, subtraction
# print(calculation(0, 0))

# def greet_users(users):             # users should be a list
#     for user in users:              # Because it's a list, we can loop through it
#         print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

# usernames = input("Enter a list of user names: ") 
# greet_users(usernames)


# def my_f1():
#     print("Hello")

# def my_f2():
#     print("Word")

# def my_f3():
#     print("This is Rick!")

# list_of_functions = [my_f1, my_f2, my_f3]

# for function in list_of_functions:
#     function()


# def print_models(unprinted_designs, completed_models):
#     """    
#     Simulate printing each design until none are left.    
#     Move each design to completed_models after printing.    
#     """

#     while unprinted_designs:        
#         current_design = unprinted_designs.pop()            

#         # Simulate creating a 3D print from the design.        
#         print("Printing model: " + current_design)        
#         completed_models.append(current_design)        

# def show_completed_models(completed_models):    
#     """
#     Show all the models that were printed.
#     """    
#     print("\nThe following models have been printed:")   
#     for completed_model in completed_models:        
#         print(completed_model)        

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


