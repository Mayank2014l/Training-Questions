# Enter product name
# Enter Quantity
# Enter price

# 1. add product
# 2. veiw all product with price
# 3. gst Calculate
# 4. discount >=3000 10% , <=2000 6%
# 5. final bill

Product=[]

while True:
    print("1. add products")
    print("2. veiw all product with price")
    print("3. gst Calculate")
    print("4. discount >=3000 10% , <=2000 6%")
    print("5. final bill")

    ch = int(input("Enter your Choice: "))

    if ch == 1:
        name = input("Enter the name of the product: ")
        Quantity = int(input("Enter the amount of Quantity: "))
        price = int(input("Enter the price: "))
        Product.append([name,Quantity,price])
        print("Product added Successfully")

    elif ch == 2:
        if len(Product) == 0:
            print("No Products Found")
        else:
            for products in Product:
                print("Name:", products[0], "| Price:", products[2])

    elif ch == 3:
        subtotal = 0

        for products in Product:
            subtotal = subtotal + (products[1] * products[2])

        gst = subtotal * 18 / 100

        print("Subtotal:", subtotal)
        print("GST (18%):", gst)
        print("Total after GST:", subtotal + gst)

    elif ch == 4:
        subtotal = 0

        for products in Product:
            subtotal = subtotal + (products[1] * products[2])

        if subtotal >= 3000:
            discount = subtotal * 10 / 100
            print("Discount: 10%")
        elif subtotal <= 2000:
            discount = subtotal * 6 / 100
            print("Discount: 6%")
        else:
            discount = 0
            print("No Discount")

        print("Discount Amount:", discount)
        print("Amount after Discount:", subtotal - discount)

    elif ch == 5:
        subtotal = 0

        for products in Product:
            total = products[1] * products[2]
            subtotal = subtotal + total

            print("Name:", products[0])
            print("Quantity:", products[1])
            print("Price:", products[2])
            print("Product Total:", total)

        if subtotal >= 3000:
            discount = subtotal * 10 / 100
        elif subtotal <= 2000:
            discount = subtotal * 6 / 100
        else:
            discount = 0

        amount_after_discount = subtotal - discount

        gst = amount_after_discount * 18 / 100

        final_amount = amount_after_discount + gst

        print("Subtotal:", subtotal)
        print("Discount:", discount)
        print("Amount after Discount:", amount_after_discount)
        print("GST (18%):", gst)
        print("Final Amount:", final_amount)

    elif ch == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")