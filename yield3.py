def countdown(x):
    while x>0:
        if x%2 ==0 :
            yield x
        x -= 1

for i in countdown(10):
    print(i)   

def make_word():
    word = " "
    for w in "spam":
        word += w
        yield word

list1 = list(make_word())
print(list1)