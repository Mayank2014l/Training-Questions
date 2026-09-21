from abc import ABC,abstractmethod
class Demo(ABC):
    @abstractmethod  # pre defined method like save(),fetchALL(),findByID
    def show():
        pass
class Test(Demo):
    def show(self):
        print("Hello")
    def msg(self):
        print("Hi")
t = Test()
t.show()
