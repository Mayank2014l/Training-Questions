class A:
    def m1(self):
        print("This is Class A")

class B(A):
    def m2(self):
        print("This is Class B")

class C(B):
    def m3(self):
        print("This is Class C")

c = C()
c.m1()  
c.m2()  
c.m3()  