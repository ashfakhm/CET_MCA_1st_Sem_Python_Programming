# Program to create a single string from two strings by swapping characters at the same position
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = ""
for a, b in zip(s1, s2):
    result += b + a

print("Result:", result)
