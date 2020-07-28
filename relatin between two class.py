class a: #checking relation between two class
    def calculation(self):
        print(1)
class b:
    def calculation(self):
        print (2)
class c(a,b):
    def calculation(self):
        print(3)

d= issubclass(c,a)
print(d)
e=issubclass(a,b)
print(e)
f=issubclass(b,c)
print(f)
