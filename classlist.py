class c_list:
    def __init__(self,list):
        self.list = []
        self.list2 = list
    def print_list(self):    #no elements in list
        for i in self.list:
            print(i)
    def print_list2(self):   #list2 will be printed
        for j in self.list2:
            print(j)

list1 = c_list([1 , 2, 3]) 
list1.print_list() 
list1.print_list2()              