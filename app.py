# Christmas Gift Tracker
import json

# GiftTracker dictionary
giftTracker = {
    "Bob": {
        "gift": "Watch",
        "price": 200,
        "bought": "No"
    },
    "Amy": {
        "gift": "Perfume",
        "price": 30,
        "bought": "Yes"
    }
}

# Check if the JSON exists or create a new one
try:
    with open("giftTracker.json", "r") as file:
        giftTracker = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    with open("giftTracker.json", "w") as file:
        json.dump(giftTracker, file, indent=4)

def addItem():
    # Read the JSON file
    with open("giftTracker.json", "r") as file:
        giftTracker = json.load(file)

    # Check if gift entry has been added
    try:
        # Grab the entry for the key and each value for user input
        newEntry = input("Enter a name: ").strip()
        giftName = input("Enter a gift: ").strip()
        giftPrice = float(input("Enter a price: ").strip())
        giftBought = input("Has the gift been bought? (yes/no): ").strip().lower()

        if giftBought not in ["yes", "no"]:
            raise ValueError("Error: Please enter yes or no for the status of the gift.")

        # Add a new entry
        giftTracker[newEntry] = {
            "gift": giftName,
            "price": giftPrice,
            "bought": giftBought
        }
        
        # Write the updated Tracker back to the JSON file
        with open("giftTracker.json", "w") as file:
            json.dump(giftTracker, file, indent=4)

        # Show updated dictionary
        print("Updated Gift Tracker:\n")
        showAll()
    
    except ValueError as e:
        print(e)

    finally:
        print("Your Gift Tracker has now been updated!")

def showAll():
    with open("giftTracker.json", "r") as file:
        giftTracker = json.load(file)

    # Loop through giftTracker
    for name, details in giftTracker.items():
        print(f"{name}: Gift: {details['gift']}, Price: {details['price']}, Bought: {details['bought']}")

def deleteItem():
    # Read JSON
    with open("giftTracker.json", "r") as file:
        giftTracker = json.load(file)
    
    try:
        # Delete an item
        delEntry = input("Enter the name you want to delete: ").strip()
        if delEntry in giftTracker:
            giftTracker.pop(delEntry)

            with open("giftTracker.json", "w") as file:
                json.dump(giftTracker, file, indent=4)
            print(f"{delEntry} has successfully been deleted.")
        else:
            print(f"{delEntry} not found in the Gift tracker.")
    
    except Exception as e:
        print(f"Error: {e}")

# Update an item
def updateItem():
    # Read the JSON
    with open("giftTracker.json", "r") as file:
        giftTracker = json.load(file)

    try:
        updateName = input("Enter the name you want to update: ").strip()
        
        # Check if the name exists in the gift tracker
        if updateName in giftTracker:
            # Get new details for the entry
            giftName = input("Enter the new gift name: ").strip()
            giftPrice = input("Enter the new price: ").strip()
            giftBought = input("Has the gift been bought? (yes/no): ").strip().lower()

            if giftBought not in ["yes", "no"]:
                raise ValueError("Error: Please enter yes or no for the status of the bought gift.")

            # Update the existing entry
            giftTracker[updateName] = {
                "gift": giftName,
                "price": giftPrice,
                "bought": giftBought
            }

            print(f"{updateName}'s entry has been updated!")
        else:
            # If the name is not found in the dictionary
            print(f"Error: {updateName} has not been found.")

        # Write back to the JSON file
        with open("gifteTacker.json", "w") as file:
            json.dump(giftTracker, file, indent=4)
    
    except ValueError as e:
        print(f"Error: {e}")

    finally:
        showAll()

def sequence():
    while True:
        print("\nMenu:")
        print("1. Add New Item")
        print("2. Delete an Item")
        print("3. Update an Item")
        print("4. Show All Items")
        print("5. Exit\n")

        opt = input("Please choose an option from (1-5): ").strip()
        
        if opt == "1":
            addItem()
        elif opt == "2":
            deleteItem()
        elif opt == "3":
            updateItem()
        elif opt == "4":
            showAll()
        elif opt == "5":
            print("Exiting the app")
            break  # Exit the loop
        else:
            print("Invalid option. Please select a valid option from 1 to 5.")

# Start the app
sequence()
