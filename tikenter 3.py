import tkinter as tk
from tkinter import messagebox



       
master = tk.Tk()
r=StringVar()

tk.Label(master,text="First Name").grid(row=0)
tk.Label(master,text="Last Name").grid(row=1)
tk.Label(master,text="result",textvariable=r).grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master) 

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
def clicked():
    s=(int(e1.get())+int(e2.get()))
    
    r.set(s)


btn=Button(master,text="ADD",command=clicked)
btn.grid(column=0,row=2)
       

master.mainloop()
