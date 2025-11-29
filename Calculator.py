def calculator():
    print("Simple Python Calculator")
    print("-------------------------")

    # Get user inputs
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input!")
        return

    # Perform operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    # Display result
    print(f"Result: {result}")


# Run the calculator
calculator()
