def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the given numbers and operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message for division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Handle division by zero gracefully
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        # Handle invalid operation input
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."

# Note: No main execution block here, as this file is meant to be imported.
