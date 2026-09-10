prompt = "Enter Two Numbers You Want to Do Basic Arithmetic Operations"
print(prompt)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

match operation:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operation")
