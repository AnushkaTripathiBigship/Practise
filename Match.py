print("Simple Calculator")
print("Options: add, subtract, multiply, divide")
operation = input("Enter the operation: ").strip().lower()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

match operation:
    case "add":
        print(f"Result: {num1 + num2}")
    case "subtract":
        print(f"Result: {num1 - num2}")
    case "multiply":
        print(f"Result: {num1 * num2}")
    case "divide":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operation")
