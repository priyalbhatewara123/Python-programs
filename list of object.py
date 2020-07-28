class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
#creating blank list
#inserting values ...
list = []
#appending instances to list
list.append(student("rewanngi",2))
list.append(student("priyal" , 12))
list.append(student("riya",13))
#print these values...
for obj in list:
    print(obj.name, obj.roll,sep = " ")
