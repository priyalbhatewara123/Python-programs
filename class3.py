'''class student:
    pass

s1 = student()
print(id(s1))   #id func is used to get the address of the object.'''


class student:
    def __init__(self):
        self.name = "Navin"
        self.age = 28
    def compare(self,s2):       #here self points to s1
        if self.age == s2.age:
            return True
        else:
            return False

s1=student()
s2=student()

'''if s1.age == s2.age:
    print("they are same")
else:
    print("they are different")'''

#this can be done with the help of a function compare
if s1.compare(s2):
    print("they are same")
else:
    print("they are different")



