"""
Python List Practice

This program demonstrates common operations performed on lists:
1. Input a list.
2. Sort the list.
3. Reverse the list.
4. Add an element to the list.
5. Remove an element from the list.
6. Remove an element by its position.
7. Remove all elements from the list.
8. Return the number of elements in the list.
9. Extract all digits of a number into a list.
10. Convert a number into its binary representation.
11. Return the square roots of numbers in a list.
12. Copy a list.
13. Reverse a number without using a built-in function.
14. Insert an element at a specific position in a list.
"""

import math

# 1. Input a list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Original list: {numbers}")


# 2. Sort the list
numbers.sort()
print(f"Sorted list: {numbers}")


# 3. Reverse the list
numbers.reverse()
print(f"Reversed list: {numbers}")


# 4. Add an element to the list
element = int(input("Enter an element to add: "))
numbers.append(element)
print(f"List after adding {element}: {numbers}")


# 5. Remove an element from the list
element = int(input("Enter an element to remove: "))

if element in numbers:
    numbers.remove(element)
    print(f"List after removing {element}: {numbers}")
else:
    print(f"{element} is not present in the list.")


# 6. Remove an element by position
position = int(input("Enter the position to remove: "))

if 0 <= position < len(numbers):
    removed_element = numbers.pop(position)
    print(f"Removed element: {removed_element}")
    print(f"List after removing position {position}: {numbers}")
else:
    print(f"Invalid position: {position}")


# 7. Remove all elements from the list
numbers.clear()
print(f"List after removing all elements: {numbers}")


# 8. Return the number of elements in the list
sample_list = [10, 20, 30, 40, 50]
number_of_elements = len(sample_list)
print(f"Number of elements: {number_of_elements}")


# 9. Extract all digits of a number into a list
number = int(input("Enter a number: "))
digits = [int(digit) for digit in str(number)]
print(f"Digits: {digits}")


# 10. Convert a number into its binary representation
number = int(input("Enter a number: "))
binary_number = bin(number)
print(f"Binary representation: {binary_number}")


# 11. Return square roots of numbers in a list
numbers = [4, 9, 16, 25, 36]
square_roots = [math.sqrt(number) for number in numbers]

print(f"Numbers: {numbers}")
print(f"Square roots: {square_roots}")


# 12. Copy a list
original_list = [10, 20, 30, 40]
copied_list = original_list.copy()

print(f"Original list: {original_list}")
print(f"Copied list: {copied_list}")


# 13. Reverse a number without using a built-in function
number = int(input("Enter a number: "))
reversed_number = 0
remaining_number = number

while remaining_number > 0:
    digit = remaining_number % 10
    reversed_number = reversed_number * 10 + digit
    remaining_number //= 10

print(f"Original number: {number}")
print(f"Reversed number: {reversed_number}")


# 14. Insert an element at a specific position
numbers = [10, 20, 30, 40]

element = int(input("Enter an element to insert: "))
position = int(input("Enter the position: "))

numbers.insert(position, element)

print(f"List after inserting {element} at position {position}: {numbers}")
