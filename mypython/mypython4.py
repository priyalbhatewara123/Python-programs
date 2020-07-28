Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dictionary
>>> dic = {1:'priyal' , 2:'rewangi',3:'prachi'}
>>> dic
{1: 'priyal', 2: 'rewangi', 3: 'prachi'}
>>> dic[2]
'rewangi'
>>> dic.get(1)
'priyal'
>>> print(dic.get(1))
priyal
>>>  print(dic.get(4))
 
SyntaxError: unexpected indent
>>> print(dic.get(4))
None
>>> 
KeyboardInterrupt
>>> print(dic.get(5,not found))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(dic.get(5,not found))
NameError: name 'found' is not defined
>>> print(dic.get(5,'not found'))
not found
>>> #dictionary from 2 lists
>>> key = ['priyal','rewangi','pranav']
>>> values = ['march','dec','aug']
>>> data = dict(zip(keys,values))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data = dict(zip(keys,values))
NameError: name 'keys' is not defined
>>> data = dict(zip(key,values))
>>> data
{'priyal': 'march', 'rewangi': 'dec', 'pranav': 'aug'}
>>> data['priyal']
'march'
>>> #to add new values to dictionary
>>> data['monica'] = 'jan'
>>> data
{'priyal': 'march', 'rewangi': 'dec', 'pranav': 'aug', 'monica': 'jan'}
>>> del data['monica']
>>> data
{'priyal': 'march', 'rewangi': 'dec', 'pranav': 'aug'}
>>> 