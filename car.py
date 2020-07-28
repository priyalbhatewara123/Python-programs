class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_des(self):
        long_name = str(self.make + " " + self.year + " " + self.model)
        return long_name

car1 = Car("BMW","B1","2015")
print(car1.get_des())     #it also gets print while running importclass.py file
