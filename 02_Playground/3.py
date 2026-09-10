"""
String Methods Practice

This program demonstrates common Python string operations:
1. Input a string.
2. Convert it to capital, lowercase, and camel case.
3. Concatenate another string.
4. Find the number of characters.
5. Extract the 4th character.
6. Extract a substring.
7. Split the string into two parts.
8. Remove leading and trailing whitespace.
9. Replace all occurrences of "a" with "f".
10. Remove all even-indexed characters.
11. Count the occurrences of "a".
12. Find the index of "o".
"""

# Input a string
text = input("Enter a string: ")

# Capital (uppercase), lowercase
print(f"Capital: {text.upper()}")
print(f"Lowercase: {text.lower()}")

# Camel case (safely handle empty or whitespace-only strings)
words = text.split()
camel_case = (
    words[0].lower() + "".join(word.capitalize() for word in words[1:])
    if words
    else ""
)
print(f"Camel case: {camel_case}")

# Concatenate another string
another_string = input("Enter another string: ")
concatenated_string = text + " " + another_string
print(f"Concatenated string: {concatenated_string}")

# Find the number of characters
print(f"Number of characters: {len(text)}")

# Extract the 4th character (check length to prevent IndexError)
if len(text) >= 4:
    print(f"4th character: {text[3]}")
else:
    print("4th character: N/A (string has fewer than 4 characters)")

# Extract a subset of the string aka substring
print(f"Substring: {text[1:5]}")

# Split the string into two parts
midpoint = len(text) // 2
first_part = text[:midpoint]
second_part = text[midpoint:]
# Printing those two parts
print(f"First part: {first_part}")
print(f"Second part: {second_part}")

# Remove leading and trailing whitespace
stripped_text = text.strip()
print(f"Without leading/trailing whitespace: {stripped_text}")

# Replace all occurrences of "a" with "f"
replaced_text = text.replace("a", "f")
print(f'After replacing "a" with "f": {replaced_text}')

# Remove even-indexed characters
odd_indexed_characters = text[1::2]
print(f"After removing even-indexed characters: {odd_indexed_characters}")

# Count the occurrences of "a"
a_count = text.lower().count("a")
print(f'Number of occurrences of "a": {a_count}')

# Find the index of "o"
o_index = text.lower().find("o")
if o_index != -1:
    print(f'Index of "o": {o_index}')
else:
    print('Index of "o": -1 (not found)')
