
def calculate(a, operator, b):
    """Perform an arithmetic operation on two numbers."""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Unsupported operator.")


def main():
    print("=" * 35)
    print("       CLI CALCULATOR")
    print("=" * 35)

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Calculator closed. Goodbye!")
            break

        operators = {
            "1": "+",
            "2": "-",
            "3": "*",
            "4": "/"
        }

        if choice not in operators:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            operator = operators[choice]
            result = calculate(a, operator, b)

            print(f"\nResult: {a:g} {operator} {b:g} = {result:g}")

        except ValueError as error:
            print(f"Input error: {error}")
        except ZeroDivisionError as error:
            print(f"Calculation error: {error}")


if __name__ == "__main__":
    main()
