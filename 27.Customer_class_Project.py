class Customer:
    bname = "HDFC Bank Mohali"
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance = self.balance+amt
        print("After Deposit Balance is: ", self.balance)
    def withdraw(self,amt):
        if self.balance<amt:
            print("Insufficient Balance")
            
        self.balance = self.balance-amt
        print("After Without Balance is: ",self.balance)
name = input("Enter Customer Name: ")
c = Customer(name)
print("Welcome to" , Customer.bname, "Mr.",name)
while True:
    print("d-Depost")
    print("w-Withdraw")
    print("e-Exit")
    ch=input("Enter your choice: ")
    if ch=='d' or ch=="D":
        amt=int(input("Enter amount: "))
        c.deposit(amt)
    elif ch=='w' or ch=='W':
        amt=int(input("Enter amount: "))
        c.withdraw(amt)
    elif ch=='e' or ch=='E':
        print("Thank for using HDFC Bank Mohali")
        break
    else:
        print("Invalid choice")
