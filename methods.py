class student:
    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):        #instance method
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is a student class")

s1 = student(34,78,65)
s2 = student(21,90,45)
print(s1.avg())
print(s2.avg())
print(student.getSchool())
student.info()



