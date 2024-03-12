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