employee = dict()
while True:
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    ch = int(input("Enter your Case: "))

    if ch == 1:
        id = int(input("Enter Employee id: "))
        name = input("Enter the name of employee: ")
        post = input("Enter post: ")
        salary = float(input("Enter the salary: "))
        employee[id] = {
            "name":name,
            "post":post,
            "salary":salary
        }
        print("Employee added Successfully!!")
    elif ch == 2:
        if employee :
            for id,emp in employee.items():
                print("Emp id",id)
                print("Emp Name",emp["name"])
                print("Emp Post",emp["post"])
                print("Emp Salary",emp["salary"])
        else:
            print("no Record found")
    elif ch == 3:
        eid = int(input("Enter id: "))
        if eid in employee:
            emp = employee(eid)
            print("Emp id", eid)
            print("Emp Name",emp["name"])
            print("Emp Post",emp["post"])
            print("Emp Salary",emp["salary"])
        else:
            print("Employee not found")
    elif ch == 4:
        eid = int(input("Enter id: "))
        if eid in employee:
            name = input("Enter name: ")
            post = input("Enter post: ")
            salary = int(input("Enter Salary"))
            employee[id]={
                "name" : name,
                "post" : post,
                "salary" : salary
            }
        else:
            print("Id Not foumd")
    elif ch == 5:
        id = int(input("Enter id: "))
        if id in employee:
            del employee[id]
            print("Employee deleted!!")
        else:
            print("Id not found")
            
    elif ch == 6:
        print("Exiting Program...")
        break
    
    else:
        print("Invalid Choice")