list1 = ['dog','cat','owl','dog','cat','lion','cat']
#to remove all cat from the list
while 'cat' in list1:
    list1.remove('cat')
print(list1)

'''to remove duplicate values from the list
we make a dictionary whose key will be the items in the list'''
list1 = list(dict.fromkeys(list1))
print(list1)