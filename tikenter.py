import tkinter as tk
master = tk.Tk()
tk.Label(master,text="First Number").grid(row=0)
tk.Label(master,text="Last Number").grid(row=1)
tk.Label(master,text="result").grid(row=3)
def clicked():
    get(e1,e2)
    set(e1+e2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
btn =Button(master,text='click here',command=clicked)
btn.grid(column=1,row=10)


master.mainloop()
