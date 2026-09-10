"""
Star Pattern

This program takes an integer from the user and prints a star pattern.
The pattern increases from one star to the given number and then
decreases back to one star.
"""


def print_star_pattern(number):
    """Print an increasing and decreasing star pattern."""
    for row in range(1, number + 1):
        print(f"{'*' * row}")

    for row in range(number - 1, 0, -1):
        print(f"{'*' * row}")


# Get input from the user
number = int(input("Enter a number: "))

# Print the pattern
print_star_pattern(number)
