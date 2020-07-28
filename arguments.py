#default parameters
def inform(name,age="18"): #age is default parameter here
    print(name)
    print(age)

inform("priyal",19)
inform("rewu")

#keyword argument
def infor(name,age="18"): 
    print(name)
    print(age)

infor(age="45",name="pravina")

#variable length argument
def add(*b):    #b is a tuple
    c = 0
    for i in b:
        c = c+i
    print(c)
add(4,5,6,7,1,2)        