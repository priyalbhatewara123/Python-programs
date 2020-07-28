def add_five(x):
    return x+5
def apply_twice(func,arg):
    return func(func(arg))
    
print(apply_twice(add_five , 10))