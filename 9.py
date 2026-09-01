"""
Character Frequency

This program takes a string from the user and uses a function
to count the frequency of each character in the string.
"""


def character_frequency(text):
    """Return the frequency of each character in a string."""
    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    return frequency


# Get input from the user
text = input("Enter a string: ")

# Calculate character frequency
frequency = character_frequency(text)

# Display the result
print(f"Character frequency: {frequency}")
