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
