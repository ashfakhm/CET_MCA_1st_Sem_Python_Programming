"""Construct the specified star pattern using nested loops."""


for row in range(1, 6):
    for _ in range(row):
        print("*", end=" ")
    print()

for row in range(4, 0, -1):
    for _ in range(row):
        print("*", end=" ")
    print()
