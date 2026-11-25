"""Use the graphics package with different import statements."""

import importlib

from graphics import rectangle
from graphics.circle import *


cuboid = importlib.import_module("graphics.3D-graphics.cuboid")
sphere = importlib.import_module("graphics.3D-graphics.sphere")

length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))
circle_radius = float(input("Enter circle radius: "))

cuboid_length = float(input("Enter cuboid length: "))
cuboid_breadth = float(input("Enter cuboid breadth: "))
cuboid_height = float(input("Enter cuboid height: "))
sphere_radius = float(input("Enter sphere radius: "))

print("Rectangle area:", rectangle.area(length, breadth))
print("Rectangle perimeter:", rectangle.perimeter(length, breadth))
print("Circle area:", area(circle_radius))
print("Circle perimeter:", perimeter(circle_radius))
print(
    "Cuboid surface area:",
    cuboid.area(cuboid_length, cuboid_breadth, cuboid_height),
)
print(
    "Cuboid total edge length:",
    cuboid.perimeter(cuboid_length, cuboid_breadth, cuboid_height),
)
print("Sphere surface area:", sphere.area(sphere_radius))
print("Sphere great-circle perimeter:", sphere.perimeter(sphere_radius))
