"""
Calculator library containing basic math operations.
"""

def add(first_term, second_term):
    """Return the sum of the inputs."""
    return first_term + second_term

def subtract(first_term, second_term):
    """Return the difference of the inputs."""
    return first_term - second_term

def calculator():
    """Define calculator usage"""
    while True:
        print("\nWelcome to Simple Calculator")
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ['1', '2']:
            print("Invalid choice. Please enter a valid option.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")

if __name__ == "__main__":
    calculator()
    