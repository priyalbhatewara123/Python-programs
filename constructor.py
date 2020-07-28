class user :
    #variables...
    nm1 = " "
    nm2 = " "

    nm3 = " "
    nm4 = " "
    def __init__(self,p,q,r,s):#instance variables
        self.nm1 = p
        self.nm2 = q
        self.nm3 = r
        self.nm4 = s


    def sayhello(self):
        print("welcome  to you all in sub" + self.nm1+self.nm2+self.nm3+self.nm4)


user1 = user("rewangi","priyal","prachi","ritika")
user1.sayhello()
