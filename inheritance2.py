class ElectricCar:
    def __init__(self):
        self.battery = Battery()

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print(self.battery_size)

myCar = ElectricCar()
myCar.battery.describe_battery()

