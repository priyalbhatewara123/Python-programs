#try block
try:
    a=int(input("enter numerartor number:"))
    b=int(input("enter denominator number:"))
    print("result of division:"+str(a/b))
except(ValueError,ZeroDivisionError):
        print("Please check the input value: It should be an interger greater than 0")
