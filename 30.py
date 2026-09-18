class Test:
    #class level variable
    a=10
    def __init__(self):
        #instance variable
        self.b = 20
t = Test()
print(t.a,t.b)
t.a = 11
t.b - 22
print(t.a,t.b)
t1 = Test()
print(t1.a,t1.b) # a,b instance variable
# instance variable is varied from object to object
