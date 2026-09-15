students=[]
while True:
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Students")
    print("4. Find Max Marks with Name")
    print("5. Exit")

    ch = int(input("Enter your Choice: "))

    if ch == 1:
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))
        students.append([name,marks])
        print("Student Added Successfully")
    elif ch == 2:
        if len(students) == 0:
            print("No Students Found")
        else:
            for student in students:
                print("Name:", student[0], "| Marks:", student[1])
    elif ch == 3:
        name = input("Enter the name to search: ")

        for i in students:
            if students[i]==name:
                print(students[i])
            
    elif ch == 4:
        if len(students) == 0:
            print("No Students Found")
        else:
            max_student = students[0]

            for student in students:
                if student[1] > max_student[1]:
                    max_student = student

            print("Student with Maximum Marks:")
            print("Name:", max_student[0])
            print("Marks:", max_student[1])

    elif ch == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")