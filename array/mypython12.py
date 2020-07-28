# to print array in sorted form
from array import *
arr = array('i',[30,10,50,20,40])
print(sorted(arr))

# to find factorial of a number
n = int(input("enter a number:"))
fact =1
for i in range(1,n+1):
    fact = fact*i

print(fact)
