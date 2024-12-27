from tkinter import *

#a4a4a4 for dark, #c1c1c1 for light

moneyamount = 0
moneylabel = None

def addone():
    global moneyamount, moneylabel
    moneyamount += 1
    if moneylabel:
        moneylabel.destroy()
    moneylabel = Label(root, text=moneyamount)
    moneylabel.pack()


def main():
    #Setup for window
    global root
    root = Tk()
    root.title("Bank")
    root.geometry('860x640')
    root.config(bg='#c1c1c1')

    #Interactive parts
    addmoneybutton = Button(root, text="Add $1", command=addone)
    addmoneybutton.pack()

    root.mainloop()