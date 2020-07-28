# to get array values from user
from array import *
arr = array('i',[])
l = int(input("enter the length of the array"))
for i in range(0,l):
    x = int(input("enter the element of the array"))
    arr.append(x)

print(arr)