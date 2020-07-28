Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> arr = ('i' ,[1,2,3])
>>> arr
('i', [1, 2, 3])
>>> a = [1,5,7,8]
>>> a
[1, 5, 7, 8]
>>> ae = ([1,0,9,8] , int)
>>> ae
([1, 0, 9, 8], <class 'int'>)
>>> #different ways of creating an array
>>> # 1.using array()
>>> from numpy import *
>>> arr = array([1,2,3,4,5])
>>> print(arr)
[1 2 3 4 5]
>>> print(arr.type)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(arr.type)
AttributeError: 'numpy.ndarray' object has no attribute 'type'
>>> print(arr.dtype)
int32
>>> arr1 = array([1,2,3,4,5.3])
>>> print(arr1.type)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(arr1.type)
AttributeError: 'numpy.ndarray' object has no attribute 'type'
>>> print(arr1.dtype)
float64
>>> print(arr1)
[1.  2.  3.  4.  5.3]
>>> arr2 = linspace(0,16,1)
>>> arr2
array([0.])
>>> arr2 = linspace(0,16,16)
>>> arr2
array([ 0.        ,  1.06666667,  2.13333333,  3.2       ,  4.26666667,
        5.33333333,  6.4       ,  7.46666667,  8.53333333,  9.6       ,
       10.66666667, 11.73333333, 12.8       , 13.86666667, 14.93333333,
       16.        ])
>>> arr2 = linspace(0,16,15)
>>> arr2
array([ 0.        ,  1.14285714,  2.28571429,  3.42857143,  4.57142857,
        5.71428571,  6.85714286,  8.        ,  9.14285714, 10.28571429,
       11.42857143, 12.57142857, 13.71428571, 14.85714286, 16.        ])
>>> arr2 = linspace(0,16,17)
>>> arr2
array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12.,
       13., 14., 15., 16.])
>>> arr3 = logspace(1,40,5)
