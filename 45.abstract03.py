from abc import ABC, abstractmethod

class Test1(ABC):
    @abstractmethod
    def m1():
        pass

class Test2(ABC):
    @abstractmethod
    def m2():
        pass

class Test(Test1, Test2):
    def m1(self):
        print("m1")

    def m2(self):
        print("m2")

t = Test()
t.m1()
t.m2()