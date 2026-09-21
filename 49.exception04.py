class Login:

    try:
        password = input("Enter password: ")

        if password != "admin":
            raise ValueError
        else:
            print("Login successful")

    except ValueError:
        print("Invalid password")

    finally:
        print("Thank you for using the system")