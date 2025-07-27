# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main execution block for user interaction
if __name__ == "__main__":
    print("Temperature Conversion Tool")
    
    # Prompt user for temperature input
    temp_input = input("Enter the temperature value: ")
    
    try:
        temperature = float(temp_input) # Convert input to a float
    except ValueError:
        # Handle non-numeric input error
        print("Invalid temperature. Please enter a numeric value.")
        exit() # Exit the script if input is invalid

    # Prompt user for unit
    unit = input("Enter the unit (Celsius or Fahrenheit): ").strip().lower()

    if unit == 'celsius':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F") # Format to 2 decimal places
    elif unit == 'fahrenheit':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C") # Format to 2 decimal places
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'Celsius' or 'Fahrenheit'.")
        