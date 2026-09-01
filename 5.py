"""
Python Dictionary Practice

This program demonstrates common operations performed on dictionaries:
1. Create a dictionary using input from the user.
2. Insert a key-value pair into a dictionary.
3. Print the value of a user-input key.
4. Delete a value from the dictionary.
5. Remove a key from the dictionary.
6. Remove all values from the dictionary.
7. Return all values from the dictionary.
8. Update a key with another value.
9. Return all keys from the dictionary.
10. Merge two dictionaries.
11. Swap two numbers.
12. Swap two numbers without using a temporary variable.
13. Sort a dictionary.
14. Create a one-dimensional (1D) matrix.
15. Create a two-dimensional (2D) matrix and perform addition.
16. Create a three-dimensional (3D) matrix and perform transpose.
"""

# 1. Input from user and create a dictionary
name = input("Enter your name: ")
age = int(input("Enter your age: "))

person = {"name": name, "age": age}

print(f"Dictionary: {person}")


# 2. Insert a key-value pair into the dictionary
key = input("Enter a key: ")
value = input("Enter a value: ")

person[key] = value

print(f"Dictionary after insertion: {person}")


# 3. Print the value of a user-input key
search_key = input("Enter a key to search: ")

if search_key in person:
    print(f"Value: {person[search_key]}")
else:
    print(f"Key '{search_key}' does not exist.")


# 4. Delete a value from the dictionary
delete_key = input("Enter the key whose value you want to delete: ")

if delete_key in person:
    person[delete_key] = None
    print(f"Dictionary after deleting the value: {person}")
else:
    print(f"Key '{delete_key}' does not exist.")


# 5. Remove a key from the dictionary
remove_key = input("Enter the key to remove: ")

if remove_key in person:
    removed_value = person.pop(remove_key)
    print(f"Removed value: {removed_value}")
    print(f"Dictionary after removing the key: {person}")
else:
    print(f"Key '{remove_key}' does not exist.")


# 6. Remove all values from the dictionary
person.clear()

print(f"Dictionary after removing all values: {person}")


# 7. Return all values from the dictionary
student = {"name": "Ash", "age": 20, "course": "Computer Science"}

values = student.values()

print(f"All values: {list(values)}")


# 8. Update a key with another value
student["age"] = 21

print(f"Dictionary after updating age: {student}")


# 9. Return all keys from the dictionary
keys = student.keys()

print(f"All keys: {list(keys)}")


# 10. Merge two dictionaries
first_dictionary = {"name": "Ash", "age": 20}

second_dictionary = {"course": "Computer Science", "college": "ABC College"}

merged_dictionary = first_dictionary | second_dictionary

print(f"Merged dictionary: {merged_dictionary}")


# 11. Swap two numbers
first_number = 10
second_number = 20

first_number, second_number = second_number, first_number

print(f"First number: {first_number}")
print(f"Second number: {second_number}")


# 12. Swap two numbers without a temporary variable
first_number = 10
second_number = 20

first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print(f"First number: {first_number}")
print(f"Second number: {second_number}")


# 13. Sort a dictionary
scores = {"John": 75, "Alex": 90, "David": 60, "Sam": 85}

sorted_scores = dict(sorted(scores.items()))

print(f"Original dictionary: {scores}")
print(f"Sorted dictionary: {sorted_scores}")


# 14. Create a 1D matrix
matrix_1d = [10, 20, 30, 40, 50]

print(f"1D matrix: {matrix_1d}")


# 15. Create a 2D matrix and perform addition
first_matrix = [[1, 2], [3, 4]]

second_matrix = [[5, 6], [7, 8]]

result_matrix = [
    [first_matrix[i][j] + second_matrix[i][j] for j in range(len(first_matrix[0]))]
    for i in range(len(first_matrix))
]

print(f"First matrix: {first_matrix}")
print(f"Second matrix: {second_matrix}")
print(f"Result after addition: {result_matrix}")
for row in result_matrix:
    print(row)


# 16. Create a 3D matrix and perform transpose
matrix_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Transpose by reversing axes (equivalent to np.transpose without axes)
# Original shape (2, 2, 2) -> Transposed shape (2, 2, 2) where transposed[i][j][k] = original[k][j][i]
d0, d1, d2 = len(matrix_3d), len(matrix_3d[0]), len(matrix_3d[0][0])
transposed_matrix = [
    [[matrix_3d[k][j][i] for k in range(d0)] for j in range(d1)] for i in range(d2)
]

print(f"Original 3D matrix: {matrix_3d}")
print(f"Transposed 3D matrix: {transposed_matrix}")
