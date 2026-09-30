while True:
    LoberizaFlavor = input(" Pizza flavour (Pepperoni/Hawaiian): ").lower()
    LoberizaQuantity = int(input("Enter quantity: "))

    price = 0
    LoberizaSize = ""

    match LoberizaFlavor:
        case "pepperoni":
            print("You selected Pepperoni Pizza.")
            LoberizaSize = input(" Size (Small/Medium/Large): ").lower()
            if LoberizaSize == "small":
                price = 250
            elif LoberizaSize == "medium":
                price = 350
            elif LoberizaSize == "large":
                price = 450
            else:
                print("Invalid Size")

        case "hawaiian":
            print("You selected Hawaiian Pizza.")
            LoberizaSize = input(" Size (Small/Medium/Large): ").lower()
            if LoberizaSize == "small":
                price = 250
            elif LoberizaSize == "medium":
                price = 350
            elif LoberizaSize == "large":
                price = 450
            else:
                print("Invalid Size")

        case _:
            print("Invalid Flavor")

    # Only show the order summary if a valid price was set
    if price > 0:
        LoberizaQuantityFinal = LoberizaQuantity * price
        print(f"\n Chose {LoberizaFlavor.title()} Flavored Pizza, size {LoberizaSize.title()}")
        print(f"Amount: PHP {LoberizaQuantityFinal}")
    else:
        print("Order not completed due to invalid input.")

    # Ask if the user wants to order again
    again = input("\nDo you want to order again? (Y/N): ")
    if again.upper() != "Y":
        print("Thank you for ordering!")
        break