#final
try:
    num1,num2 = eval(input("enter two numbers,seperated by comma:"))
    result = num1 / num2
    print("result is ",result)
except ZeroDivisionError:
    print("Division by zero is error!!")

except SyntaxError:
    print("Comma is missing.Enter numbers seperated by comma like 1,2")
except:
    print("Wrong input")
else:
    print("No Exceptions")
finally:
    print("This will excute no matter what")
