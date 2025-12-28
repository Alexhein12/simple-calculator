# Simple Calculator Program
# Created by: Your Name

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def calculator():
    """Main calculator function"""
    print("=" * 40)
    print("     SIMPLE CALCULATOR")
    print("=" * 40)
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select 1-5")


if __name__ == "__main__":
    calculator()
