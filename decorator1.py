#decorators
def div(a,b):
    print(a/b)

def smart_div(func):  #decorative function
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div) #first changing the behaviour of div
div(2,4)             #then calling div   
