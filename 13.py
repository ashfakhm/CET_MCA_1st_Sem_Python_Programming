"""
Area Calculator Using Lambda Functions

This program uses lambda functions to calculate the areas
of a square, rectangle, and triangle.
"""

# Lambda function for the area of a square
square_area = lambda side: side * side

# Lambda function for the area of a rectangle
rectangle_area = lambda length, width: length * width

# Lambda function for the area of a triangle
triangle_area = lambda base, height: 0.5 * base * height


# Get input for the square
side = float(input("Enter the side of the square: "))

# Get input for the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Get input for the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))


# Calculate the areas
square_result = square_area(side)
rectangle_result = rectangle_area(length, width)
triangle_result = triangle_area(base, height)


# Display the results
print(f"Area of square: {square_result:.2f}")
print(f"Area of rectangle: {rectangle_result:.2f}")
print(f"Area of triangle: {triangle_result:.2f}")
