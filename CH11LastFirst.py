"""
    Name: Your name
    Lab: Chapters 11 -Classes, Objects and Inheritance
    Description: This is a program that demonstrate classes and inheritance by creating a vehivle class with constructor and methods and derived classed from it. 
"""
TITLE_LINE = "\nWelcome to Vehicle Description program!\n"
LINE = "-"*50

class Vehicle:

    num = 0

    def __init__(self):
        Vehicle.num += 1
        self.color = ""

    def __del__(self):
        #it reduces the number of vehivles as "del" is called
        Vehicle.num -= 1

    def num_vehicles(self) -> int:
        #this returns the number of vehicles created
        return Vehicle.num

    def __str__(self) -> str:
        return "I am a Vehicle"

    def set_color(self,color: str):
        self.color = color

    def get_color(self):
        return self.color

class Car(Vehicle):

    def __init__(self):
        super(Car,self).__init__()
        self.num_wheels = 4

    def __str__(self):
        type_wheels = f"I am a Car and I have {self.num_wheels} wheels"
        return type_wheels

class Motorcycle(Vehicle):

    def __init__(self):
        super(Motorcycle,self).__init__()
        self.num_wheels = 2

    def __str__(self):
        type_wheels = f"I am a Motorcyle and I have {self.num_wheels} wheels"
        return type_wheels

def main():
    print(TITLE_LINE)

    v = Vehicle()
    print(v)
    v.set_color("I am Black")
    print(v.get_color())
    print(LINE)

    c = Car()
    print(c)
    c.set_color("I am Blue")
    print(c.get_color())
    print(LINE)

    m = Motorcycle()
    print(m)
    m.set_color("I am Green")
    print(m.get_color())
    print(LINE)

    print(f"Total number of vehicles created = {v.num_vehicles()}")
    del m
    print(f"Total number of vehicles remaining = {v.num_vehicles()}")


main()