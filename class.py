class Student:
    name = "rewangi"
    id = 10
    course = "btech information technology"
    college = "msit"


    def display (self):   #through self we can access variables value.
        #print("Name: %s \nID: %d \ncourse: %s \ncollege: %s"%(self.name,self.id,self.course,self.college))
        print(f"Name: {self.name} \nID: {self.id} \ncourse: {self.course} \ncollege: {self.college}")




stu = Student()
stu.display()
#Student.display(stu)
