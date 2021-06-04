from tkinter import *
import random

x=0

def Generate():
    global x
    x = random.randint(1,10000)
    lab1.config(text = x)



window = Tk()
window.title("demo2")
window.geometry("500x500+50+50")
window.config(bg="#aabbcc")


lab1 = Label(window, text="0", width=13, height=3)
lab1.pack()

genBtn = Button(window, text="Generate", command=Generate, width=13, height=3)
genBtn.pack()

exitBtn = Button(window, text="Exit", command=window.destroy, width=13, height=3, bg="yellow")
exitBtn.pack()

window.mainloop()