n = int(input("enter a number"))
for i in range(2,n//2):
    if n % i == 0:
        print("number is not a prime number")
        break

else:
    print("number is prime number")