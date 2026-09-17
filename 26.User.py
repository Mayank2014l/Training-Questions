class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def login(self):
        if self.name == 'Techlive' and password == 123:
            print("valid user")
        else:
            print("Invalid User")
name = input("Enter name: ")
password = int(input("Enter Password: "))
u = User(name,password)
u.login()
