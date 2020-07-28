#implemention of super keyword
class Computer():
    def __init__(self, computer,ram,ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd
class Laptop(Computer):
    def __init__(self,computer,ram,ssd,color,weight,model):
        super().__init__(computer,ram,ssd)
        self.model=model
        self.color=color
        self.weight=weight
lenovo1 = Laptop('lenovo',2,512,"Seagreen",6700,'1420')
print('This computer is:',lenovo1.computer)
print("this computer has ram of",lenovo1.ram)
print("this computer has a ssd of",lenovo1.ssd)
print("this computer has a color of",lenovo1.color)
print("this computer has a weight of",lenovo1.weight)
print("this computer has a model of",lenovo1.model)
lenovo2 = Laptop('lenovo',2,523,"yellow",34920,'1220')
print('This computer is:',lenovo2.computer)
print("this computer has ram of",lenovo2.ram)
print("this computer has a ssd of",lenovo2.ssd)
print("this computer has a color of",lenovo2.color)
print("this computer has a weight of",lenovo2.weight)
print("this computer has a model of",lenovo2.model)
