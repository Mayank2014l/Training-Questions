class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def m1(self):
        self.c = 30
    def m2(self):
        self.d = 40
        self.e = 50
        del self.a
        del self.d

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
t.m2()
print(t.__dict__)
