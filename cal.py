def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

 def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4): "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if choice == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == 3:
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == 4:
        print(f"{num1} / {num2} = {divide(num1, num2)}")

if __name__ == "__main__":
    calculator()
