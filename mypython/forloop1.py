num = [11,89,7,48,100]
for nums in num:
    if nums % 5 == 0:
        print(nums)
        break
else:
    print("not found")