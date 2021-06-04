from tkinter import *
import random


def Generate():
    x = random.sample(range(1,42),6)
    lab1.config(text = x[0])
    lab2.config(text = x[1])
    lab3.config(text = x[2])
    lab4.config(text = x[3])
    lab5.config(text = x[4])
    lab6.config(text = x[5])


window = Tk()
window.title("demo3")
window.geometry("500x500+50+50")
window.config(bg="#ccddee")


lab1 = Label(window, text="0", width=26, height=3, bg="#aabbcc")
lab1.pack()

lab2 = Label(window, text="0", width=23, height=3, bg="#bbccdd")
lab2.pack()

lab3 = Label(window, text="0", width=20, height=3, bg="#aabbcc")
lab3.pack()

lab4 = Label(window, text="0", width=17, height=3, bg="#bbccdd")
lab4.pack()

lab5 = Label(window, text="0", width=13, height=3, bg="#aabbcc")
lab5.pack()

lab6 = Label(window, text="0", width=10, height=3, bg="#bbccdd")
lab6.pack()


genBtn = Button(window, text="Generate", command=Generate, width=7, height=3)
genBtn.pack()

exitBtn = Button(window, text="Exit", command=window.destroy, width=4, height=3)
exitBtn.pack()


window.mainloop()