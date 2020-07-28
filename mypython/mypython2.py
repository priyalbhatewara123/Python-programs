Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: C:/Users/Dell/Desktop/python programs/mypython2.py =========
[20, 30, 40, 50]
>>> num[0]
20
>>> num[-1:3]
[]
>>> num[-1:-3]
[]
>>> num[-1]
50
>>> num.append(23)
>>> num
[20, 30, 40, 50, 23]
>>> num.insert(2,90)
>>> num
[20, 30, 90, 40, 50, 23]
>>> num.pop(90)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    num.pop(90)
IndexError: pop index out of range
>>> num.pop(2)
90
>>> num
[20, 30, 40, 50, 23]
>>> num.clear()
>>> num
[]
>>> del nums[2:]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    del nums[2:]
NameError: name 'nums' is not defined
>>> 
>>> del num[2:]
>>> num
[]
>>> num.extend([20,'priyal' , 2001, 4,"march"])
>>> num
[20, 'priyal', 2001, 4, 'march']
>>> min(num)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    min(num)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> #min max sum functins can be used with integer list
>>> 