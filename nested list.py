#nested list
nested=[[2,56,[-1,-6,-9]],5,[0,23,7],["hello"]]
print(nested[0][1])
print(nested[0][0:2])
nested[0][2][0:2]
print(nested[3][0][1:4])
nested[1]=100





#list comprehension..
#display square root of a number

def square(x):
    return x*x
def iseven(x):
    return(x%2==0)
#square(6)
#iseven(8)
list1=[square(x) for x in range(100)if iseven(x)]
print(list1)
