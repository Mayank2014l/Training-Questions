def void():
    try:
        age = int(input("Enter your age: "))
        if age<18:
            raise ValueError
        else:
            print("You are eligible for vote")

    except ValueError:
        print("You are not eligible for vote")
void()