def safe_divide(numerator, denominator):
    """
    Performs division, handling potential ZeroDivisionError and ValueError for non-numeric inputs.

    Args:
        numerator (str/int/float): The numerator, expected to be convertible to a float.
        denominator (str/int/float): The denominator, expected to be convertible to a float.

    Returns:
        str: An error message if an error occurs, or the result of the division.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        # Catch ValueError if conversion to float fails (non-numeric input)
        return "Error: Please enter numeric values only."
    
    try:
        # Attempt to perform division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        # Catch ZeroDivisionError if denominator is zero
        return "Error: Cannot divide by zero."
    except Exception as e:
        # Catch any other unexpected errors
        return f"An unexpected error occurred: {e}"
