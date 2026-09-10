"""
Number Expression

This program accepts a number n and calculates the value of
n + nn + nnn.
"""


def calculate_expression(number):
    """Return the value of n + nn + nnn."""
    number_string = str(number)

    n = int(number_string)
    nn = int(number_string * 2)
    nnn = int(number_string * 3)

    return n + nn + nnn


# Get input from the user
number = int(input("Enter a number: "))

# Calculate the expression
result = calculate_expression(number)

# Display the result
print(f"Result of n + nn + nnn: {result}")
