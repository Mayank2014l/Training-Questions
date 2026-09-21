class A:
    def m1(self):
        print("This is Class A")


class B(A):
    def m2(self):
        print("This is Class B")


class C(A):
    def m3(self):
        print("This is Class C")


b = B()
c = C()

b.m1()
b.m2()
c.m1()
c.m3()