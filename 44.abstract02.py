from abc import ABC, abstractmethod

class Test1(ABC):
    def __init__(self):
        self.a = 10
        self.b = 20
    @abstractmethod
    def show(self):
        pass
class Test2(Test1):
    def show(self):
        print(self.a)
        print(self.b)
t = Test2()
t.show()


