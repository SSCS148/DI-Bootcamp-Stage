# import math

# class Circle:
#     def __init__(self, radius=None, diameter=None):
#         if radius is not None:
#             self.radius = radius
#             self.diameter = radius * 2
#         elif diameter is not None:
#             self.diameter = diameter
#             self.radius = diameter / 2
#         else:
#             raise ValueError("Please provide either radius or diameter")

#     @property
#     def area(self):
#         return math.pi * self.radius ** 2

#     def __str__(self):
#         return f"Circle with radius: {self.radius}"

#     def __add__(self, other):
#         return Circle(radius=self.radius + other.radius)

#     def __lt__(self, other):
#         return self.radius < other.radius

#     def __eq__(self, other):
#         return self.radius == other.radius

#     def draw(self):
#         import turtle
#         turtle.circle(self.radius * 10)
#         turtle.done()

# # Testing the class
# circle1 = Circle(radius=3)
# circle2 = Circle(diameter=8)

# print(circle1)
# print(circle2)
# print("Area of circle1:", circle1.area)
# print("Area of circle2:", circle2.area)

# print("Circle1 < Circle2:", circle1 < circle2)
# print("Circle1 == Circle2:", circle1 == circle2)

# circle3 = circle1 + circle2
# print("Circle3:", circle3)

# # Sorting circles
# circles = [circle2, circle1, circle3]
# circles.sort()
# print("Sorted circles:", [str(circle) for circle in circles])

# # Drawing circles
# # circle1.draw()
# # circle2.draw()
# # circle3.draw()

# import math
# import turtle

# class Circle:
#     def __init__(self, radius=None, diameter=None):
#         if radius is not None:
#             self.radius = radius
#             self.diameter = radius * 2
#         elif diameter is not None:
#             self.diameter = diameter
#             self.radius = diameter / 2
#         else:
#             raise ValueError("Please provide either radius or diameter")

#     @property
#     def area(self):
#         return math.pi * self.radius ** 2

#     def __str__(self):
#         return f"Circle with radius: {self.radius}"

#     def __add__(self, other):
#         return Circle(radius=self.radius + other.radius)

#     def __lt__(self, other):
#         return self.radius < other.radius

#     def __eq__(self, other):
#         return self.radius == other.radius

#     def draw(self, x, y):
#         turtle.penup()
#         turtle.goto(x, y - self.radius * 10)
#         turtle.pendown()
#         turtle.circle(self.radius * 10)

# # Testing the class
# circle1 = Circle(radius=3)
# circle2 = Circle(diameter=8)

# circle3 = circle1 + circle2

# # Sorting circles
# circles = [circle2, circle1, circle3]
# circles.sort()

# # Set up the Turtle screen
# screen = turtle.Screen()
# screen.title("Sorted Circles")

# # Draw the circles
# start_x = -150
# start_y = 0
# for circle in circles:
#     circle.draw(start_x, start_y)
#     start_x += 100

# # Close the Turtle graphics window when clicked
# screen.exitonclick()
