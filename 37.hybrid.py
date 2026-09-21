class A:
    def m1(self):
        print("This is Class A")


class B(A):
    def m2(self):
        print("This is Class B")


class C(A):
    def m3(self):
        print("This is Class C")


class D(B, C):
    def m4(self):
        print("This is Class D")


d = D()

d.m1()
d.m2()
d.m3()
d.m4()