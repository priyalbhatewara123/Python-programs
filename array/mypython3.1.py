# to get the index of the value in an array
from array import *
arr = array('i',[10,20,30,40])
print(arr)
val = int(input("enter a value"))
for i in range(0,4):
    if arr[i] == val:
        print("index: " , i)
        break

# to print index using inbuilt function
val1 = int(input("enter a value"))
print(arr.index(val1))
