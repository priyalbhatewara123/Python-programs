Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #address of variables
>>> num = 2
>>> id(num)
1924458432
>>> num1 = 2
>>> id(num1)
1924458432
>>> num1 = 3
>>> id(num1)
1924458448
>>> id(2)
1924458432
>>> # type of variable
>>> type(num1)
<class 'int'>
>>> num = 10+9i
SyntaxError: invalid syntax
>>> num = 10+9j
>>> type(num)
<class 'complex'>
>>> #conversion between the datatypes
>>> a = 5.6
>>> b = int(a)
>>> b
5
>>> z = float(b)
>>> z
5.0
>>> h = complex(z)
>>> h
(5+0j)
>>> h = z
>>> bool1 = (h=z)
SyntaxError: invalid syntax
>>> bool1 = 10>9
>>> bool1
True
>>> type(bool1)
<class 'bool'>
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(True)
1
>>> int(False)
0
>>> # range
>>> range(10)
range(0, 10)
>>> list(range(10)) #to print what all numbers are included in range we convert range to list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> # to print all odd numbers
>>> list(range(0,11,2))
[0, 2, 4, 6, 8, 10]
>>> list(range(1,10,4))
[1, 5, 9]
>>> list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 