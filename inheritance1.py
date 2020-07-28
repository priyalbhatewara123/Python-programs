class college:
    def name(self):
            print("name :msit")
    
class student(college):
        def no(self):
            print("no :48")
class teacher(student):
    def id(self):
        print("id : 1456","no:48","name:msit")
    
    

tech=teacher( )
tech.name()
tech.no()
tech.id()

