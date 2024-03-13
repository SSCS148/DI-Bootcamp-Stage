# class Animal():
#     def __init__(self, type, number_legs, sound,name):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound
#         self.name = name

#     def make_sound(self):
#         print(f"I am an animal, his name is {self.name} and I love saying {self.sound}")

# class Dog(Animal):
#     def fetch_ball(self):
#         print(f"I am a {self.type}, and I love fetching balls")

# rex = Dog('dog', 4,"Wouaf","Georges")
# print('This animal is a:', rex.type)
# rex.make_sound()
# rex.fetch_ball()

# roger = Animal('Roger', 4, "Grr","Georges")

# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle
# print(nc.color)


# class Circle:
#         def __init__(self, diameter):
#             self.diameter = diameter

#         def grow(self, factor=2):
#             """grows the circle's diameter by factor"""
#             self.diameter = self.diameter * factor

# class NewCircle(Circle):
#         def grow(self, factor=2):
#             """grows the area by factor..."""
#             self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)

# nc.grow()

# print(nc.diameter)

# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

# class Dog(Animal):
#     def __init__(self, type, number_legs, sound, fetch_ball):
#         super().__init__(type, number_legs, sound)
#         # Or : Animal.__init__(self,type, number_legs, sound)
#         self.fetch_ball = fetch_ball

# rex = Dog('dog', 4, "wouaf", True)
# print('This animal is a :', rex.type)



# class Computer():

#     def __init__(self):
#         self.name = "Apple Computer" # public
#         self.__max_price = 900 # private

#     def sell(self):            # public method
#         print("Selling Price: {}",{self.__max_price})

#     def __sell(self):          # private method
#         print('This is private method')

#     def set_max_price(self, price):
#         self.__max_price = price

# c = Computer()
# c.sell()


# class Parrot():

#     def fly(self):
#         print("Parrot can fly")

#     def swim(self):
#         print("Parrot can't swim")

# class Penguin():

#     def fly(self):
#         print("Penguin can't fly")

#     def swim(self):
#         print("Penguin can swim")

# def flying_test(bird):
#     bird.fly()

# blu = Parrot()
# peggy = Penguin()

# flying_test(blu)
# flying_test(peggy)


# class Alien():
#     def __init__(self, name, planet):
#         self.name = name
#         self.planet = planet

#     def fly(self):
#         print(self.name, 'is flying!')

#     def sleep(self):
#         print("Aliens don't sleep")

# class Animal():
#     def __init__(self, name):
#         self.name = name

#     def sleep(self):
#         print("zzzZZZZZ")

# class Dog(Animal):
#     def bark(self):
#         print("{} barked, WAF !".format(self.name))

# class AlienDog(Alien, Dog):
#     def bark(self):
#         print("{} barked, 0ul10ul0u (that's how aliens dogs bark..) !".format(self.name))


# my_normal_dog = Dog("Roger")
# my_normal_dog.sleep()

# my_normal_dog.bark()

# my_alien_dog = AlienDog("Rex", "Neptune")
# print(my_alien_dog.planet)

# my_alien_dog.fly()

# my_alien_dog.sleep()

# my_alien_dog.bark()


# class Alien():
#     def __init__(self, name, planet):
#         self.name = name
#         self.planet = planet

#     def fly(self):
#         print(self.name, 'is flying!')

#     def sleep(self):
#         print("Aliens don't sleep")

# class Animal():
#     def __init__(self, name):
#         self.name = name

#     def sleep(self):
#         print("zzzZZZZZ")

# class Dog(Animal):
#     def bark(self):
#         print("{} barked, WAF !".format(self.name))

# class AlienDog(Alien, Dog):
#     def bark(self):
#         print("{} barked, 0ul10ul0u (that's how aliens dogs bark..) !".format(self.name))
#         print("{} barked, 0ul10ul0u (that's how aliens dogs bark..) !".format(self.planet))

# my_normal_dog = Dog("Roger")
# my_normal_dog.sleep()

# my_normal_dog.bark()

# my_alien_dog = AlienDog("Rex", "Neptune")
# print(my_alien_dog.planet)

# my_alien_dog.fly()
# my_alien_dog.sleep()

# my_alien_dog.bark()

# class A():

#     def dothis(self):
#         print("doing this in A")
# class B(A):
#     pass
# class C():
#     def dothis(self):
#         print("doing this in C")
# class D(B, C):
#     pass

# d_instance = D()
# d_instance.dothis() 
# d_instance.dothis() 



# class Book():
#     def __init__(self, title, author, publication_date, price):
#         self.title = title
#         self.author = author
#         self.publication = publication_date
#         self.price = price

#     def present(self):
#         print(f'Title: {self.title}')

# class Fiction(Book):
#     def __init__(self, title, author, publication_date, price, is_awesome):
#         super().__init__(title, author, publication_date, price)
#         self.genre = 'Fiction'
#         self.is_awesome = is_awesome
#         if self.is_awesome:
#             self.bored = False
#             print('Wow this is an awesome book')
#         else:
#             self.bored = True
#             print('I am very bored')

# if __name__ == '__main__':
#     foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
#     foundation.present()
#     print(foundation.price)
#     print(foundation.bored)
#     boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
#     print(boring_book.bored)


# def age():
#     user_age = input("How old are you?\n>>> ")
#     #######
#     try:
#         user_age = int(user_age)
#         print("I AM AFTER USER_AGE")
#     except:
#         print("Your age is not a real age")
#         user_age = 0
#     #######
#     print("Next year, you will be {} years old".format(user_age+1))

# age()


# valid_flag = False
# while not valid_flag:
#     userage = input("How old are you ? ")
#     try:
#         userage = int(userage)
#         valid_flag = True
#     except:
#         print("Please enter a real age")

# print("Next year, your age will be",userage+1)


# valid_flag = False
# while not valid_flag:
#     userage = input("How old are you ? ")
#     try:
#         userage    = int(userage)
#         valid_flag = True
#     except:
#         pass

# print("Next year, your age will be",userage+1)

#Exercise:
# def sum_calculator(my_list):
#     total = 0
#     for integer in my_list:
#         try:
#             total += int(integer)
#         except ValueError:
#             pass
#     return total

# my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
# result = sum_calculator(my_list)
# print(result)

# valid_flag = False
# while not valid_flag:
#     userage = input("How old are you ? ")
#     try:    # TRY THIS
#         userage    = int(userage)
#     except: # IF YOU GOT AN ERROR
#         print("Wrong age!")
#     else:   # ELSE
#         valid_flag = True

# print("Next year, your age will be",userage+1)

# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was {x}'.format(x=x))
# #The error that will appear is your own custom error
# #Traceback (most recent call last):
# #File "pyblog/app.py", line 52, in <module>
# #raise Exception('x should not exceed 5. The value of x was {x}'.format(x=x))
# #Exception: x should not exceed 5. The value of x was 10'
# #Process finished with exit code 1


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    pass

bengal_cat = Bengal("Bengal", 3)
chartreux_cat = Chartreux("Chartreux", 4)
siamese_cat = Siamese("Siamese", 2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]
sara_pets = Pets(all_cats)
sara_pets.walk()

