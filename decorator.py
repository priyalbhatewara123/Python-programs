#Inner Functions:
def parent():
    print("this is from parent class")
    def first_child():
        print("this is from first child")
    def second_child():
        print("this is from second child")

    second_child()
    first_child()
parent()

#Returning functions from functions
def par(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child   #you are returning first_child without the parentheses.
                             #this means that you are returning a reference to the function first_child. 
    else:
        return second_child
var = par(1)
print(var)     