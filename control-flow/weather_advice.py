# weather_advice.py

# Prompt the user to enter the current weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Check if the weather is "sunny"
if weather == "sunny":
    # Recommend clothing for sunny weather
    print("Wear a t-shirt and sunglasses.")

# Check if the weather is "rainy"
elif weather == "rainy":
    # Recommend clothing for rainy weather
    print("Don't forget your umbrella and a raincoat.")

# Check if the weather is "cold"
elif weather == "cold":
    # Recommend clothing for cold weather
    print("Make sure to wear a warm coat and a scarf.")

# Handle any unexpected or unrecognized input
else:
    print("Sorry, I don't have recommendations for this weather.")