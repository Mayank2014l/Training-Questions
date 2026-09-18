class Demo:
    def msg(self):
        print("bye")
    @classmethod
    def msg1(cls):
        print("Heello")
    @staticmethod
    def disp():
        print("hi")
d=Demo()
# we can access instance method by using object reference
d.msg()
# we can classemthod ny using object reference as well as class name
Demo.show()
d.show()
# we can access staticmethod by using only class name
Demo.disp()