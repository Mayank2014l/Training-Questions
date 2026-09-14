num = int(input("Enter the number: "))

i = 2

while i < num:
    if num % i == 0:
        print("Not a Prime Number")
        break
    i = i + 1
else:
    print("Prime Number")