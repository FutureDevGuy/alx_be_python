# Prompt for a single task description with the exact phrasing
task = input("Enter your task: ")

# Prompt for the task's priority (high, medium, low) with the exact phrasing
# Convert to lowercase for case-insensitive comparison
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes or no) with the exact phrasing
# Convert to lowercase for case-insensitive comparison
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = ""

# Process the task based on priority using a Match Case statement
match priority:
    case 'high':
        reminder_message = f"Reminder: '{task}' is a HIGH priority task"
    case 'medium':
        reminder_message = f"Reminder: '{task}' is a MEDIUM priority task"
    case 'low':
        reminder_message = f"Reminder: '{task}' is a LOW priority task"
    case _: # Default case for invalid priority
        reminder_message = f"Reminder: '{task}' has an UNKNOWN priority"

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == 'yes':
    reminder_message += " that requires immediate attention today!"
elif time_bound == 'no':
    # If not time-bound, just add a general note (optional, but good for clarity)
    reminder_message += " and is not time-sensitive."
else:
    # Handle invalid input for time_bound
    reminder_message += " (Time sensitivity unknown due to invalid input)."


# Print the customized reminder
print(reminder_message)