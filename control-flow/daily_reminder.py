# Prompt for a single task description with the exact phrasing
task = input("Enter your task: ")

# Prompt for the task's priority (high, medium, low) with the exact phrasing
# Convert to lowercase for case-insensitive comparison
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes or no) with the exact phrasing
# Convert to lowercase for case-insensitive comparison
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message prefix
# This ensures "Reminder: " is always at the start
reminder_prefix = "Reminder: "
reminder_core = "" # This will hold the task and priority part

# Process the task based on priority using a Match Case statement
match priority:
    case 'high':
        reminder_core = f"'{task}' is a HIGH priority task"
    case 'medium':
        reminder_core = f"'{task}' is a MEDIUM priority task"
    case 'low':
        reminder_core = f"'{task}' is a LOW priority task"
    case _: # Default case for invalid priority
        reminder_core = f"'{task}' has an UNKNOWN priority"

# Combine prefix and core message
reminder_message = reminder_prefix + reminder_core

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
