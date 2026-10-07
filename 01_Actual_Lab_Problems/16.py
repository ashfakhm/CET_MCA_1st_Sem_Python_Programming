"""Find the greatest common divisor of two integers."""


first_number = abs(int(input("Enter the first number: ")))
second_number = abs(int(input("Enter the second number: ")))

while second_number != 0:
	remainder = first_number % second_number
	first_number = second_number
	second_number = remainder

print("GCD:", first_number)
