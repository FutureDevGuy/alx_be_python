# Prompt the user for the current weather condition
# .lower() is used to convert the input to lowercase for case-insensitive comparison
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations based on the input using if, elif, and else statements
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    # Handle unexpected input
    print("Sorry, I don't have recommendations for this weather.")
