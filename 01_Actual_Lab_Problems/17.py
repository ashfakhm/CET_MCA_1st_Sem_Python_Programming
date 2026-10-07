"""Create a list after removing all even numbers."""


numbers = [
	int(value)
	for value in input("Enter numbers separated by spaces: ").split()
]
odd_numbers = [number for number in numbers if number % 2 != 0]

print("List after removing even numbers:", odd_numbers)
