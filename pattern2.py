for i in range(1,5):
    for j in range(i,5):
        print(j," " ,end="")
    print()


str1 = "ABCD"
str2 = "PQR"
for i in range(4):
    print(str1[:i+1]+str2[i:])