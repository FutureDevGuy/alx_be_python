# Prompt the user for the current weather condition
# .lower() is used to convert the input to lowercase for case-insensitive comparison
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations based on the input using if, elif, and else statements
weather = input("What's the weather like? ")

if weather == "sunny":
    print("Wear sunglasses.")
elif weather == "rainy":
    print("Take an umbrella.")
elif weather == "snowy":
    print("Wear a coat and boots.")
else:
    print("Sorry, I don't understand the weather condition.")
    
    # Handle unexpected input
    