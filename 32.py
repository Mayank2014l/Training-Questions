class Test:
    count = 0
    def __init__(self,name):
        self.name = name
        Test.count += 1
t1 = Test("Ravi")
t2 = Test("Mukesh")
t3 = Test("Rahul")
print("Number of employees ",Test.count)
