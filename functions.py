import math


def square_area(side_length):
    """Calculate the area of a square."""
    return side_length**2


def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius**2


# Example usage:
side = 5
radius = 3

print("Area of square with side length", side, ":", square_area(side))
print("Area of circle with radius", radius, ":", circle_area(radius))
