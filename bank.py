class bank:

    def __init__(self,d,w):
        self.deposit = d
        self.withdrawl = w
    def amount(self):
         if self.withdrawl<=self.deposit:
                print("remaining balance: %d " %(self.deposit - self.withdrawl))
         else:
            print("insufficient balance:")
        
d = int(input("enter the deposit amount:"))
w = int(input("enter the withdrawl amount:"))
    
newbank = bank(d,w)#object
newbank.amount()

