from tkinter import*
window = Tk()
window.title("welcome to like geeks app")
lbl = Label(window,text="HELLO" ,font=("Arial Bold",50))

lbl.grid(column=0,row=0)


             
btn =Button(window,text="Click Me")
btn.grid(column=10,row=1)
window.mainloop()
