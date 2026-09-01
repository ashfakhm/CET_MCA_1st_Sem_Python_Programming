"""
Longest Word

This program accepts a list of words and uses a function to
return the length of the longest word.
"""


def longest_word_length(words):
    """Return the length of the longest word in a list."""
    longest_word = max(words, key=len)

    return len(longest_word)


# Get words from the user
words = input("Enter words separated by spaces: ").split()

# Find the length of the longest word
length = longest_word_length(words)

# Display the result
print(f"Length of the longest word: {length}")
