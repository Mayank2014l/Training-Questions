M1 = float(input("Enter the marks: "))
M2 = float(input("Enter the marks: "))
M3 = float(input("Enter the marks: "))
M4 = float(input("Enter the marks: "))

avg_marks = (M1+M2+M3+M4)/4

if (avg_marks>=90):
    print("Grade A")
elif(avg_marks >=75):
    print("Grade B")
elif(avg_marks>=50):
    print("Grade C")
elif(avg_marks>=33):
    print("Grade D")
else:
    print("Grade F")