# Prompt the user to input a positive integer for the pattern size
# Use int() to convert the input to an integer
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows (for the while loop)
row_count = 0

# Use a while loop to iterate through each row of the pattern
while row_count < size:
    # Use a for loop to print asterisks (*) side by side for the current row
    for _ in range(size): # The underscore '_' is used when the loop variable is not needed
        print("*", end="") # print without a newline
    
    # After completing each row, print a newline character to move to the next row
    print() # This prints a newline

    # Increment the row counter
    row_count += 1
