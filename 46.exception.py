try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a/b
    print(c)

except ZeroDivisionError:  #ZeroDivisionError instead of this we can use exception as e
    print("Exception Generated")

finally:
    print("Always Executes")