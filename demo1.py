from tkinter import *

x=0

def letBrnAdd():
    global x
    x += 1
    lab1.config(text=(x))

def letBtnSub():
    global x
    x -= 1
    lab1.config(text=(x))

window = Tk()
window.title("demo1")
window.geometry("500x500+50+50")
window.config(bg="#aabbcc")


lab1 = Label(window, text="0", width=13, height=3)
lab1.pack()

addBtn = Button(window, text="Add", command=letBrnAdd, width=13, height=3)
addBtn.pack()

subBtn = Button(window, text="Sub", command=letBtnSub, width=13, height=3)
subBtn.pack()

exitBtn = Button(window, text="Exit", command=window.destroy, width=13, height=3)
exitBtn.pack()

window.mainloop()