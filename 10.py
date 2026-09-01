"""
Fibonacci Series

This program takes the number of terms from the user and uses
a function to generate and print the Fibonacci series.
"""


def fibonacci_series(number_of_terms):
    """Return a Fibonacci series containing the given number of terms."""
    first_number = 0
    second_number = 1
    series = []

    for _ in range(number_of_terms):
        series.append(first_number)
        first_number, second_number = (second_number, first_number + second_number)

    return series


# Get input from the user
number_of_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci series
series = fibonacci_series(number_of_terms)

# Display the result
print(f"Fibonacci series: {series}")
