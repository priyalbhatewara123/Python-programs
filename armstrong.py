def checkArmstrongNumber(lower,upper):
    for num in range(lower, upper + 1):
        #initialize sum
        sum = 0
        #find  the sum of cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit **3
            temp //= 10
            if num == sum:
                print(num)
#checkArmstrongNumber(100,1000)
                #or
#lower = int(input("enter the lower range:"))
#upper = int(input("enter upper range:"))

#checkArmstrongNumber(lower,upper)
                #or...

def main():
    

    data = ("my data read from the web")
    print(data)
    lower = int(input("enter lower range: "))
    upper = int(input("enter upper range:"))
    modified_data = checkArmstrongNumber(lower,upper)
    print(modified_data)
if __name__ == "__main__":
    main()
    
        
