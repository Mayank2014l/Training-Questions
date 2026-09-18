class A:
    def m1(self):
        print("hello")
    def m2(self,a,b):
        print(self.a + self.b)
class B(A):
    pass
b=B()
b.m1()
b.m2()
