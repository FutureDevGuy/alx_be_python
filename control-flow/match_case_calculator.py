# Prompt the user for the first number
# Use float() to allow for decimal numbers
num1 = float(input("Enter the first number: "))

# Prompt the user for the second number
num2 = float(input("Enter the second number: "))

# Ask for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

# Variable to store the result
result = None

# Perform the calculation using a Match Case statement
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        # Handle division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _: # Default case for invalid operation
        print("Error: Invalid operation chosen. Please use +, -, *, or /.")