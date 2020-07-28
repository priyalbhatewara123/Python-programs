#when you want to pass a list of values of the argument and also the result in a list
def add_five(x):
    return x+5

nums = [10,20,30,40,50]
ans = list(map(add_five,nums))
print(ans)  

#writing the same using lambda
ans = list(map((lambda x: x+5),nums))
print(ans)

#filter function
ans = list(filter(lambda x: x%3 == 0 , nums))
print(ans)