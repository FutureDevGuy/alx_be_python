# Prompt the user to input a number
# Use int() to convert the input to an integer
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table using a for loop
# The loop will iterate from 1 up to and including 10
for i in range(1, 11): # range(1, 11) generates numbers from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")