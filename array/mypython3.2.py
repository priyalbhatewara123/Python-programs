# delete a value from array without using inbuilt function
from array import *
arr = array('i',[10,20,30,40])
print(arr)
val = int(input("enter a value you want to delete"))
arr2 = array('i',[])
for i in range(0,4):
    if arr[i]==val:
        continue
    else:
        arr2.append(arr[i])


print(arr2)
# to print array in reverse order without using builtin func
arr3 = array('i',[])
for j in range(3,-1):
    arr3.append(arr[j])

print(arr3)
