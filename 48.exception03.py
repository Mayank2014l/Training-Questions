def check():
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ValueError
        else:
            print("Valid quantity")

    except ValueError:
        print("Invalid quantity")

    finally:
        print("Thank you")


check()