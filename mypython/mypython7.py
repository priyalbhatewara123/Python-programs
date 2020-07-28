Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #assiging values to two varaibles at the same time
>>> a,b = 2,3
>>> a
2
>>> b
3
>>> a<5 and b>1
True
>>> a<5 && b>1
SyntaxError: invalid syntax
>>> a<5 & b>1
False
>>> x = True
>>> x
True
>>> not x
False
>>> 
>>> #number system conversion in python
>>> bin(25)
'0b11001'
>>> #0b is used to represent that the number is in binary format
>>> 0b0101
5
>>> oct(25)
'0o31'
>>> hex(25)
'0x19'
>>> hex(10)
'0xa'
>>> 0xa
10
>>> #swapping 2 numbers
>>> a = 8
>>> b = 9
>>> temp = a
>>> b = a
>>> a = 10
>>> b = 9
>>> a = a+b
>>> b = a-b
>>> a = a-b
>>> a
9
>>> b
10
>>> #swapping using XOR operator
>>> a = 12
>>> b = 11
>>> a = a^b
>>> b = a^b
>>> a = a^b
>>> a
11
>>> b
12
>>> bin(12)
'0b1100'
>>> bin(11)
'0b1011'
>>> #another way to swap in a single line
>>> a = 9
>>> b = 8
>>> a,b = b,a
>>> a
8
>>> b
9
>>> #bitwise operators
>>> ~12
-13
>>> 90&43
10
>>> bin(90)
'0b1011010'
>>> bin(43)
'0b101011'
>>> bin(10)
'0b1010'
>>> 12<<2
48
>>> bin(12)
'0b1100'
>>> 0b110000
48
>>> 