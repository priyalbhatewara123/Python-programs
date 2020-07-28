#function to find square of a number
f = lambda a: a*a
print(f(10)) 
#alternate way to write lambda function
f = (lambda a: a*a)(10)
print(f)

#function to add two numbers
l = lambda a,b : a+b
print(l(2,3))

#3rd function
def test(func,arg):
    return func(arg)

print(test(lambda x:2*x,10))

#normal function
def normal(x):
    return x**2 + 8*x +10
print(normal(2))
#lambda function
print((lambda x: x**2 + 8*x + 10)(2))
