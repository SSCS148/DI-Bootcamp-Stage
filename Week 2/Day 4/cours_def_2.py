# def check_arguments(*args):
#     print(f"These are the arguments {args}")
# check_arguments(1, 2, 'hey',1, 23, 'hey')

# def check_tuple(a,b):
#     # Returns the sum of 'a' and 'b'
#     return sum((a,b))

# print(check_tuple(10,30))

# def check_tuple(*args):
#     return sum((args))

# print(check_tuple(10,30,34,56,34))

# def  check_keyworded_arguments(**kwargs):
#     print(kwargs)

# check_keyworded_arguments(name="Sarah", age=24)


# def check_keyword_arguments(**kwargs):
#     for key, value in kwargs.items():
#         print(key,":",value)

# check_keyword_arguments(name="Sarah", age=24)

# def check_keywordedarguments(**kwargs):
#     return kwargs

# print(check_keywordedarguments(fruit='apple', ordered= 2))

# def check_arguments_keywordedarguments (required_arg, *args, **kwargs):
#     print(required_arg)
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)

# check_arguments_keywordedarguments("required argument")
# check_arguments_keywordedarguments("required argument", 1, 2, 'hey')
# check_arguments_keywordedarguments("required argument", 1, 2, 'hey', name="Sarah", age=24)

# def check_arguments_keywordedarguments(*args,**kwargs):
#     print('*args', args)
#     print('**kwargs', kwargs)

# check_arguments_keywordedarguments(10,20,30,name='John',surname='Doe',2)

# def check(a, *numbers, **person):
#     print('Greetings : ', a)

#     for num in numbers:
#         print('num - ', num)

#     for key, value in person.items():
#         print(key + ': ' + value)
        
# check("hello", "oh yeah", 1,2,3,name = "John", surname = "Doe",  nickname = "Sachinka")

# def upper_string(string):
#     return string.upper()

# fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'peach']
# # map_objet = map(upper_string, fruits)
# # print(list(map_objet))
# upper_fruits = list(map(upper_string, fruits))
# print(upper_fruits)


# the below code fragment can be found in:
# def starts_with_A(s):
#     return s[1] == "a"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange","Architect"]
# filtered_object = filter(starts_with_A, fruit)
# print(list(filtered_object))

# from functools import reduce    
# def add(a, b):
#     return a + b

# my_list = [1, 3, 2, 5, 6, 4]
# reduced_list = reduce(add, my_list)
# print(reduced_list)

# my_function = lambda s: s.upper()
# # This is the same as doing: 
# def my_function(s):
#     return s.upper()

# print(my_function("hello"))

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(lambda s: s.upper(), fruit)
# print(list(map_object))


# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filtered_object = filter(lambda s: s[0] == "A", fruit)
# print(list(filtered_object))

# from functools import reduce
# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# reduced_list = reduce(lambda first, second: first+second, my_list)
# print(reduced_list)

def hello(string):
    return "Hello " + string

if string.items()<= 4:
    print(f"Hello {string}")
    print(people)

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
print(list(map(hello, people)))

names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank']
short_names = filter(lambda name: len(name) <= 4, names)
greetings = map(lambda name: f"Hello, {name}!", short_names)

for greeting in greetings:
    print(greeting)
