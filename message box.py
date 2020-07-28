#you can use messagebocx library like this
from tkinter import*
from tkinter import messagebox
window = Tk()
window.title("welcome to like geeks app")
window.geometry('350x200')
def clicked():
    messagebox.showinfo('Message title','Mesaage content')
btn =Button(window,text='Click here',command=clicked)
btn.grid(column=0,row=0)
window.mainloop()
