def f(x):
    return g(x+1),g(x+2)
def g(y):
    return y*10,y+10
print(f(100))



def isphoneno(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False  
    if text[7] != '-':
        return False  
    for i in range(8,12):
        if not text[i].isdecimal():
            return False 
    return True         

message = input("Enter a message: ")
for i in range(len(message)):
    text = message[i:i+12]
    if isphoneno(text):
        print("phone number found" , text)




