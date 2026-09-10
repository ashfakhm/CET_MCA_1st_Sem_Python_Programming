number = int(input("Enter a number: "))
n = int(input("How many multiples? "))

for i in range(1, n + 1):
    print(f"{number} x {i} = {number * i}")
