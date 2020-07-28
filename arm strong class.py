class arm:
    
    def __init__(self,lower,upper):
                
        self.lower = lower
        self.upper = upper

    def armstrongnumber(lower,upper):
         for num in range(lower, upper + 1):
             #initialize sum
             sum = 0
             #find  the sum of cube of each digit
             temp = num
             while temp > 0:
                 digit=temp%10
                 sum += digit **3
                 temp //= 10
                 if num == sum:
                     print(num)

    lr=int(input("enter the lower bound"))
    up=int(input("enter upper bound"))
    a=armstrongnumber(lr,up)
    print(a)

lr=""
ur=""
obj=arm(lr,ur)
                
