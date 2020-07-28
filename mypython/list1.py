l = [1,2,3,4,5,6,7,8,9,10,11]
for i in range(0,5):
    print(l[i])

print(l[2:5])
print(l[:5])
print(l[3:])
print(l[3::])
print(l[3::2])
 
#to print the list in reverse order
print(l[10::-1])

l1 = ["priyal", "rewangi", "prachi", "mudita"]
print(l1[2][4])

#split 
names = input("enter the names")
l3 = names.split(" ")
print(l3)

l = list(range(1,11))
for i in l:
    print(i**2)

#an alternate and a small way
l = [i**2 for i in range(1,11)]
print(l)

#title makes the first letter capital
players = ["priyal" , "rewangi" , "prince", "ishika", "somy", "pranav"]
for player in players[0::2]:
    print(player.title())