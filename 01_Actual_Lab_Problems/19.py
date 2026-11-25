"""Display the Fibonacci series for the requested number of terms."""


terms = int(input("Enter the number of terms: "))

if terms < 0:
    print("The number of terms cannot be negative.")
else:
    series = []
    first, second = 0, 1

    for _ in range(terms):
        series.append(first)
        first, second = second, first + second

    print("Fibonacci series:", *series)
