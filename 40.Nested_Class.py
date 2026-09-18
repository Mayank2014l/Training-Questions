class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course

    class Address:
        def __init__(self,city,state):
            self.city = city 
            self.state = state

        def show(self):
            print("City is ",self.city)
            print("State is ",self.state)
s = Student("rahul","java")
a = Student.Address("noida","up")
a.show()
print("Name is ",s.name)
print("Course is ",s.course)
            