Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = logspace(1,40,5)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a = logspace(1,40,5)
NameError: name 'logspace' is not defined
>>> from numpy import *
>>> a = logspace(1,40,5)
>>> print(a)
[1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30
 1.00000000e+40]
>>> print(a[0])
10.0
>>> print(a[4])
1e+40
>>> print('%2f' %a[4])
10000000000000000303786028427003666890752.000000
>>> print('%3f' %a[4])
10000000000000000303786028427003666890752.000000
>>> b = zeros(5)
>>> print(b)
[0. 0. 0. 0. 0.]
>>> b = zeros(5,int)
>>> print(b)
[0 0 0 0 0]
>>> c = ones(3)
>>> print(c)
[1. 1. 1.]
>>> 