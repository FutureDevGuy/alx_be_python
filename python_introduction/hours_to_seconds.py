# Define the variable for hours
hours = 2

# Calculate the number of seconds in the given hours (1 hour = 3600 seconds)
seconds = hours * 3600

# Print the result in the specified format
# Use 'hour(s)' to correctly handle singular and plural
if hours == 1:
    print(f"{hours} hour is {seconds} seconds")
else:
    print(f"{hours} hours is {seconds} seconds")