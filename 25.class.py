class Test:
    def __init__(self):
        print(id(self))

t = Test()
print(id(t))



class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
t = Test()
print(t.a)
print(t.__dict__) # is a keyword which is used to acces class attr.



class Test:
    def __init__(self):
        # instance variable
        self.a = 10
        self.b = 20
        # instance method can access instance variable
    def add(self):
        print(self.a+self.b)
t = Test()
t.add()


