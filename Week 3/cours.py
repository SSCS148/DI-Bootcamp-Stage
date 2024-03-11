# class Dog():
#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)

# shelter_dog = Dog(name_of_the_dog="Rex")
# # or
# shelter_dog = Dog("Rex")

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

first_person = Person("John", 36)

print(first_person.name)
print(first_person.age)