def countdown(x):
    while x>0:
        yield x
        x-=1

'''for i in countdown(10):
    print(i)  '''

result = countdown(10)
for i in result:
    print(i)          