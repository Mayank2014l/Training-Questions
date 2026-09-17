#def keyword is used to declared function

def show():
    print("hello")
show()

def sum(a,b):
    print(a+b)
sum(10,20)

#global variable
a = int(input("Enter number: "))
b = int(input("Enter number: "))
def add():
    print(a+b)
def sub():
    print(a-b)
def multi():
    print(a*b)
def div():
    print(a/b)