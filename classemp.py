class employee:
    def __init__(self,f_name,l_name,salary):  #init is a special method where all variables are declared
	        self.f_name = f_name
	        self.l_name = l_name
	        self.salary = salary
    def bonos(self):
		bonous = self.salary/10
		print(f'your bonous is {bonous}')
	        
f_name=input("enter firest name:")
l_name=input("enter last name:")
s=int(input("salary"))
bonous = 0
newemployee = employee(f_name,l_name,s)

print(newemployee.f_name,newemployee.l_name)
newemployee.bonos()
           

