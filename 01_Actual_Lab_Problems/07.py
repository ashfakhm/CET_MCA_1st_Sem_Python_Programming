n = int(input("Enter The Number You Want To Find Factorial of: "))
fact = 1
for i in range(1, n + 1):
    fact *= i

print(f"Factorial of {n} is {fact}")
