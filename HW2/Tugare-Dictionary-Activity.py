cart = {}
cart[0] = "underwear"
cart[1] = "tank top"
cart[2] = "jacket"

print("You have 3 items in the cart\n")

while True:
    choice = input("What would you like to do [C]hange items [R]emove [D]isplay  [S]earch ? ").strip()

    if choice.upper() == "D":
        print("Displaying Values")
        print("Key\tValue")
        for item in sorted(cart):
            print(f"{item}\t{cart[item]}")
        print()

    elif choice.upper() == "S":
        itemName = input("Enter key or item to search: ").strip()
        if itemName == "":
            print("No input given.\n")
            continue

        if itemName.isdigit():
            key = int(itemName)
            if key in cart:
                print("Found", cart[key], "item\n")
            else:
                print("Im sorry, not in the cart.\n")
        else:
            found = False
            lowItemName = itemName.lower()
            for item in cart:
                if cart[item].lower() == lowItemName:
                    print("Found", cart[item], "item\n")
                    found = True
                    break
            if not found:
                print("Im sorry, not in the cart.\n")

    elif choice.upper() == "R":
        itemName = input("Enter key or item to remove: ").strip()
        if itemName.isdigit():
            key = int(itemName)
            if key in cart:
                print("The key", key, "with value", cart[key], "has been deleted.\n")
                del cart[key]
            else:
                print("Key not found.\n")
        else:
            found = False
            lowItemName = itemName.lower()
            for key in list(cart.keys()):
                if cart[key].lower() == lowItemName:
                    print("The key", key, "with value", cart[key], "has been deleted\n")
                    del cart[key]
                    found = True
                    break
            if not found:
                print("Item not found\n")

    elif choice.upper() == "C":
        itemName = input("Enter key or item to change: ").strip()
        if itemName.isdigit():
            key = int(itemName)
            if key in cart:
                print("Found", cart[key], "item")
                new_value = input("Enter value: ").strip()
                if new_value == "":
                    print("No new value entered. Item not changed.\n")
                else:
                    cart[key] = new_value
                    print("Item updated! Key", key, "now has value", new_value, "\n")
            else:
                print("Im sorry, not in the cart.\n")
        else:
            found = False
            lowItemName = itemName.lower()
            for key in cart:
                if cart[key].lower() == lowItemName:
                    print("Found", cart[key], "item")
                    new_value = input("Enter value: ").strip()
                    if new_value == "":
                        print("No new value entered. Item not changed.\n")
                    else:
                        cart[key] = new_value
                        print("Item updated! Key", key, "now has value", new_value, "\n")
                    found = True
                    break
            if not found:
                print("Im sorry, not in the cart.\n")

    elif choice == "*":
        print("Bye.")
        break

    else:
        print("Invalid choice. Try again.\n")

