# Parking System in CGC

class Parking:
    pname = "CGC Smart Parking"

    def __init__(self, name, slots=10):
        self.name = name
        self.slots = slots

    def park(self, num):
        if self.slots >= num:
            self.slots = self.slots - num
            print("Vehicle Parked Successfully")
            print("Available Slots:", self.slots)
        else:
            print("Not Enough Parking Slots")

    def remove(self, num):
        self.slots = self.slots + num
        print("Vehicle Removed Successfully")
        print("Available Slots:", self.slots)


name = input("Enter Driver Name: ")

p = Parking(name)

print("Welcome to", Parking.pname, "Mr.", name)

while True:
    print("p - Park Vehicle")
    print("r - Remove Vehicle")
    print("e - Exit")

    ch = input("Enter your choice: ")

    if ch == 'p' or ch == 'P':
        num = int(input("Enter Number of Vehicles: "))
        p.park(num)

    elif ch == 'r' or ch == 'R':
        num = int(input("Enter Number of Vehicles to Remove: "))
        p.remove(num)

    elif ch == 'e' or ch == 'E':
        print("Thank you for using CGC Smart Parking")
        break

    else:
        print("Invalid choice")