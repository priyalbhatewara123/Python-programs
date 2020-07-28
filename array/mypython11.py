# arrays in python
from array import *
vals = array('I',[10,89,76,45])
# print(vals)
print(vals.buffer_info()) # it prints a tuple with address and the number of elements
print(vals.typecode)
vals.reverse() # it does not directly print the reversed array
print(vals)
for i in range(len(vals)):
    print(vals[i])

# to copy an array to another array dynamically:
newarr = array(vals.typecode,(a for a in vals))
print(newarr)
# to copy the square of values in another array
newar = array(vals.typecode,(a*a for a in vals))
print(newar)
# to print with the help of while loop
i = 0
while i<len(newarr):
    print(newarr[i])
    i+=1


