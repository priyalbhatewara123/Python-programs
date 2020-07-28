f = open('file.txt','w')    
f.write("hello world priyal this side")         
f.close()   

f1 = open('file.txt','r') 
f1 = f1.readlines()   
print(f1)        #it gives the output in form of list

if 'priyal' in f1:
    print("yes")
else:
    print("no")