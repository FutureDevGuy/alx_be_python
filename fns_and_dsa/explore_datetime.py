from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and prints the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.now()
    # Format the datetime object into a string
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and prints it in "YYYY-MM-DD" format.
    """
    try:
        # Prompt user for number of days
        num_days_str = input("Enter the number of days to add: ")
        num_days = int(num_days_str)

        # Get the current date (without time for simpler addition)
        current_date_only = datetime.now().date()

        # Calculate the future date
        # timedelta represents a duration
        future_date = current_date_only + timedelta(days=num_days)

        # Format the future date into a string
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution block
if __name__ == "__main__":
    display_current_datetime()
    print("-" * 30) # Separator for clarity
    calculate_future_date()
