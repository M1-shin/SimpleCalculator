from mimetypes import inited
from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("500x500")

calculation = StringVar()
calculation.set("")

def press(num):
    calculation.set(calculation.get() + str(num))

def clear():
    calculation.set("")

def equal():
    expression = calculation.get()

    if expression != "":
        result = str(eval(expression))
        calculation.set(result)
    else:
        calculation.set("0")

label = Label(window, textvariable=calculation, font=('century', 20), bg="#ffc2d1",  fg="#3a2d2d",  width=19, height=2, anchor="e")

row1 = Frame(window, bg="#fff0f3")
row2 = Frame(window, bg="#fff0f3")
row3 = Frame(window, bg="#fff0f3")
row4 = Frame(window, bg="#fff0f3")
row5 = Frame(window, bg="#fff0f3")

btn7 = Button(row1, text="7", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(7))
btn8 = Button(row1, text="8", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(8))
btn9 = Button(row1, text="9", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(9))
btnclear = Button(row1, text="Clear", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=clear)

btn4 = Button(row2, text="4", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(4))
btn5 = Button(row2, text="5", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(5))
btn6 = Button(row2, text="6", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(6))
btnmultiply = Button(row2, text="*", width=6, height=2, font=20, bg="#ffb3c6", fg="#3a2d2d", command=lambda: press("*"))

btn1 = Button(row3, text="1", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(1))
btn2 = Button(row3, text="2", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(2))
btn3 = Button(row3, text="3", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(3))
btnsubtract = Button(row3, text="-", width=6, height=2, font=20, bg="#ffb3c6", fg="#3a2d2d", command=lambda: press("-"))

btn0 = Button(row4, text="0", width=6, height=2, font=20, bg="#ffe5ec", fg="#3a2d2d", command=lambda: press(0))
btnequal = Button(row4, text="=", width=6, height=2, font=20, bg="#ffccd5", fg="#3a2d2d", command=equal)
btndivide = Button(row4, text="/", width=6, height=2, font=20, bg="#ffb3c6", fg="#3a2d2d", command=lambda: press("/"))
btnadd = Button(row4, text="+", width=6, height=2, font=20, bg="#ffb3c6", fg="#3a2d2d", command=lambda: press("+"))



label.pack(side=TOP)

row1.pack(side=TOP)
row2.pack(side=TOP)
row3.pack(side=TOP)
row4.pack(side=TOP)
row5.pack(side=TOP)

btn7.pack(side=LEFT)
btn8.pack(side=LEFT)
btn9.pack(side=LEFT)
btnclear.pack(side=LEFT)

btn4.pack(side=LEFT)
btn5.pack(side=LEFT)
btn6.pack(side=LEFT)
btnmultiply.pack(side=LEFT)

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btnsubtract.pack(side=LEFT)

btn0.pack(side=LEFT)
btnequal.pack(side=LEFT)
btndivide.pack(side=LEFT)
btnadd.pack(side=LEFT)

window.mainloop()