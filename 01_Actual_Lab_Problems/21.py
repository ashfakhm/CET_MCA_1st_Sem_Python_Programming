"""Add 'ing' to a string, or 'ly' if it already ends with 'ing'."""


text = input("Enter a string: ")

if text.endswith("ing"):
    result = text + "ly"
else:
    result = text + "ing"

print("Result:", result)
