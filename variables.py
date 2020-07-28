#types of variables in oops
class car:
    wheels = 5   #class variable
    def __init__(self):
        self.mil = 10        #instance variable
        self.com = "BMW"

c1 = car()
c2 = car()

c1.mil = 8 #value of instance variable is changed for one object
car.wheels = 5 #value of class variable if changed for both the objects
print(c1.wheels , c1.mil , c1.com)
print(c2.wheels , c2.mil , c2.com)

