# program to swap first and last character of a string

s = input("Enter a string: ")

if len(s) >= 2:
    first = s[0]  # first character
    last = s[-1]  # last character
    middle = s[1:-1]  # everything in between

    new_string = last + middle + first
    print("New string:", new_string)
else:
    print("Please enter a string with at least 2 characters.")
