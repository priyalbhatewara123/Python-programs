list = [11 , 12 , 13 , 15]
print(list[0])

print(len(list))

#adding new values in list
#append adds the value at the end while insert can add value at any index.
list.append(98)
print(list)
list.insert(2,90)
print(list)

if (len(list) == 6):
    print("correct")

else:
    print("wrong")
