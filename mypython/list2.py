#adding 2 list
'''l = [1,2,3] + [4,5,6]
print(l)

#printing element more than once
print(["hi"]*3)

#to print non-negative values we use abs
a = list(map(abs,[1,-67,-12,-90]))
print(a)'''

#to print commom elements of 2 list in 3rd list
l1 = [11 , 87 , 56, 34, 90, 23 , 67]
l2 = [11 , 57 , 66, 34, 90, 33 , 60]
l3 = []
for a in l1:
    for b in l2:
        if(a==b):
            l3.append(a)

print(l3)