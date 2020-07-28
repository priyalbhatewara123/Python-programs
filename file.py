#Here text file and python file are in same place.
#when we want to just read the file

f = open('file.txt','r')    #r specifies that the file is in read state
print(f.read())             #read() module shows the content of the file.
f.close()                   #default mode is set as read

#if we have to modify our file than open the file in write state.
f1 = open('file.txt','w')
f1.write("Hello world!")
f1.close()                 #close save all changes to our file
#all the previous data gets erased.

f2 = open('file.txt','r')
print(f2.read())
f2.close()

#we can open file differently
with open('file.txt') as file:
    print(file.read())

