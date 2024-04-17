# Part 1: Quizz

# What is a class?

# A class is a blueprint for creating objects (instances) in object-oriented programming. It defines the properties (attributes) and behaviors (methods) that all instances of the class will have.
# What is an instance?

# An instance is a specific realization of a class. It represents a single object created from that class, with its own unique data and behavior.
# What is encapsulation?

# Encapsulation is the bundling of data (attributes) and methods that operate on that data within a single unit (class). It hides the internal state of the object from the outside world and only exposes the necessary interfaces for interacting with it.
# What is abstraction?

# Abstraction is the concept of hiding complex implementation details and showing only the essential features of an object. It allows us to focus on what an object does, rather than how it does it.
# What is inheritance?

# Inheritance is a mechanism in object-oriented programming that allows a class (subclass) to inherit attributes and methods from another class (superclass). It promotes code reusability and establishes a hierarchy of classes.
# What is multiple inheritance?

# Multiple inheritance is a feature of some object-oriented programming languages where a class can inherit attributes and methods from more than one superclass. It allows a subclass to combine features and behaviors from multiple parent classes.
# What is polymorphism?

# Polymorphism is the ability of objects to take on different forms or behaviors based on the context in which they are used. It allows methods to be implemented in different ways in different subclasses, while still maintaining a common interface.
# What is method resolution order or MRO?

# Method Resolution Order (MRO) is the order in which classes are searched to execute a method or access an attribute in Python's inheritance hierarchy. It follows a depth-first, left-to-right traversal of the class hierarchy.

# import random

# class Deck:
#     def __init__(self):
#         self.cards = [(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
#                                       for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]
#         self.shuffle()

#     def shuffle(self):
#         random.shuffle(self.cards)

#     def deal(self):
#         if len(self.cards) == 0:
#             return None
#         return self.cards.pop()

# # Testing the Deck class
# deck = Deck()
# print("Initial deck:", deck.cards)

# print("\nDealing a card...")
# card = deck.deal()
# print("Dealt card:", card)
# print("Remaining cards:", deck.cards)

# print("\nShuffling the deck...")
# deck.shuffle()
# print("Shuffled deck:", deck.cards)
