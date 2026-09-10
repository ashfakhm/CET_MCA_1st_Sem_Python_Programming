"""
Greatest Common Divisor (GCD)

This program takes two integers from the user and uses a function
to calculate and return their greatest common divisor.
"""


def find_gcd(first_number, second_number):
    """Return the GCD of two numbers."""
    while second_number != 0:
        first_number, second_number = (second_number, first_number % second_number)

    return first_number


# Get input from the user
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Calculate the GCD
gcd = find_gcd(first_number, second_number)

# Display the result
print(f"GCD of {first_number} and {second_number}: {gcd}")
