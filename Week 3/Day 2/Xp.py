# Exercise 1:
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     pass

# bengal_cat = Bengal("Bengal", 5)
# chartreux_cat = Chartreux("Chartreux", 3)
# siamese_cat = Siamese("Siamese", 2)

# all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# sara_pets = Pets(all_cats)

# sara_pets.walk()


# # Exercise 2:
# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         return f"{self.name} is barking"

#     def run_speed(self):
#         return self.weight / self.age * 10

#     def fight(self, other_dog):
#         self_score = self.run_speed() * self.weight
#         other_score = other_dog.run_speed() * other_dog.weight

#         if self_score > other_score:
#             return f"{self.name} won the fight!"
#         elif self_score < other_score:
#             return f"{other_dog.name} won the fight!"
#         else:
#             return "It's a tie!"

# # Create 3 dogs
# dog1 = Dog("Max", 3, 20)
# dog2 = Dog("Buddy", 5, 25)
# dog3 = Dog("Charlie", 4, 18)

# # Test methods
# print(dog1.bark())
# print(dog2.run_speed())
# print(dog3.fight(dog1))


# # Exercise 3:

# from random import choice
# from dog import Dog

# class PetDog(Dog):
#     def __init__(self, name, age, weight):
#         super().__init__(name, age, weight)
#         self.trained = False

#     def train(self):
#         bark_output = self.bark()
#         self.trained = True
#         return bark_output

#     def play(self, *args):
#         dog_names = ', '.join(args)
#         print(f"{dog_names} all play together")

#     def do_a_trick(self):
#         tricks = [
#             "does a barrel roll",
#             "stands on his back legs",
#             "shakes your hand",
#             "plays dead"
#         ]
#         if self.trained:
#             trick = choice(tricks)
#             return f"{self.name} {trick}"
#         else:
#             return "Dog is not trained yet."

# # Example usage
# if __name__ == "__main__":
#     # Create instances of PetDog
#     pet_dog1 = PetDog("Rex", 4, 30)
#     pet_dog2 = PetDog("Bella", 3, 25)

#     # Train a dog
#     print(pet_dog1.train())

#     # Play with dogs
#     pet_dog1.play("Max", "Buddy", "Charlie")

#     # Do a trick
#     print(pet_dog1.do_a_trick())


# # Exercise 4:

# class Family:
#     def __init__(self, last_name, members):
#         self.last_name = last_name
#         self.members = members

#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print(f"Congratulations! A new child named {kwargs['name']} was born into the {self.last_name} family.")

#     def is_18(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 return member['age'] >= 18
#         return False

#     def family_presentation(self):
#         print(f"Family {self.last_name}:")
#         for member in self.members:
#             print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")


# family_members = [
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
# ]

# # Creating an instance of the Family class
# my_family = Family("Smith", family_members)

# # Calling methods
# my_family.born(name='John', age=0, gender='Male', is_child=True)
# print(my_family.is_18('Michael'))  # Check if Michael is over 18
# my_family.family_presentation()


# # Exercise 5:
# class Family:
#     def __init__(self, last_name, members):
#         self.last_name = last_name
#         self.members = members
    
#     def family_presentation(self):
#         print(f"*Here is the {self.last_name} family*")
#         for member in self.members:
#             print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")

#     def born(self, name, age, gender, is_child):
#         self.members.append({'name': name, 'age': age, 'gender': gender, 'is_child': is_child})


# class TheIncredibles(Family):
#     def __init__(self, last_name, members):
#         super().__init__(last_name, members)
    
#     def use_power(self, member_index):
#         if self.members[member_index]['age'] >= 18:
#             print(f"{self.members[member_index]['name']} can use the power: {self.members[member_index]['power']}")
#         else:
#             raise Exception(f"{self.members[member_index]['name']} is not over 18 years old.")
    
#     def incredible_presentation(self):
#         print(f"*Here is our powerful family {self.last_name} *")
#         super().family_presentation()


# # Creating an instance of TheIncredibles class
# incredibles_members = [
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
# ]
# incredibles = TheIncredibles("Incredibles", incredibles_members)

# # Calling incredible_presentation method
# incredibles.incredible_presentation()

# # Adding Baby Jack using the born method
# incredibles.born("Baby Jack", 0, "Male", True)
# incredibles.members[-1]['power'] = "Unknown Power"

# # Calling incredible_presentation method again
# incredibles.incredible_presentation()
