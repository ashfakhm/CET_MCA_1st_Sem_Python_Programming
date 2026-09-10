import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        print("There are no real roots.")
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)

        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
