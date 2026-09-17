producer = dict()

while True:
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    ch = int(input("Enter your Case: "))

    if ch == 1:
        id = int(input("Enter Producer id: "))
        name = input("Enter the name of producer: ")
        product = input("Enter product: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        producer[id] = {
            "name": name,
            "product": product,
            "quantity": quantity,
            "price": price
        }

        print("Producer added Successfully!!")

    elif ch == 2:
        if producer:
            for id, pro in producer.items():
                print("Producer id:", id)
                print("Producer Name:", pro["name"])
                print("Product:", pro["product"])
                print("Quantity:", pro["quantity"])
                print("Price:", pro["price"])
        else:
            print("No Record found")

    elif ch == 3:
        pid = int(input("Enter id: "))

        if pid in producer:
            pro = producer[pid]

            print("Producer id:", pid)
            print("Producer Name:", pro["name"])
            print("Product:", pro["product"])
            print("Quantity:", pro["quantity"])
            print("Price:", pro["price"])
        else:
            print("Producer not found")

    elif ch == 4:
        pid = int(input("Enter id: "))

        if pid in producer:
            name = input("Enter name: ")
            product = input("Enter product: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            producer[pid] = {
                "name": name,
                "product": product,
                "quantity": quantity,
                "price": price
            }

            print("Producer updated Successfully!!")
        else:
            print("Id Not found")

    elif ch == 5:
        pid = int(input("Enter id: "))

        if pid in producer:
            del producer[pid]
            print("Producer deleted!!")
        else:
            print("Id not found")

    elif ch == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")