Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuples
>>> tup = (12,13,14,15)
>>> tup
(12, 13, 14, 15)
>>> tup[3]
15
>>> tup(3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup(3)
TypeError: 'tuple' object is not callable
>>> tup.count(12)
1
>>> tup.index(15)
3
>>> #set
>>> s = {1,2,45,09,3,45}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> s = {1,23,4,12}
>>> s
{1, 4, 12, 23}
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
>>> set = {1,23,4,12,12,1,1}
>>> set
{1, 4, 12, 23}
>>> #it is not necessary that the item will be printed in ascending order only
>>> set.add(11)
>>> set
{1, 4, 11, 12, 23}
>>> set1 = {1,9,3,7,4}
>>> set1.union(set)
{1, 3, 4, 7, 9, 11, 12, 23}
>>> set1.issubset(set)
False
>>> 