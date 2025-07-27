def display_menu():
    """Displays the main menu options for the shopping list manager."""
    # THIS IS THE LINE TO ENSURE IS EXACTLY CORRECT
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Manages adding, removing, and displaying items in the shopping list.
    """
    shopping_list = [] # Initialize an empty list to store shopping items

    while True: # Loop continuously until the user chooses to exit
        display_menu() # Show the menu options
        choice = input("Enter your choice: ").strip() # Get user's choice, remove whitespace, and store

        if choice == '1':
            # Option to Add Item
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Option to Remove Item
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue # Go back to the menu
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            else:
                print(f"'{item_to_remove}' not found in the list.")
        elif choice == '3':
            # Option to View List
            if shopping_list:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Enumerate to get numbered list
                    print(f"{i}. {item}")
                print("--------------------------")
            else:
                print("Your shopping list is empty.")
        elif choice == '4':
            # Option to Exit
            print("Goodbye!")
            break # Exit the while loop
        else:
            # Handle Invalid Choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
