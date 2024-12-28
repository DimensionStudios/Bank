from tkinter import *

#a4a4a4 for dark, #c1c1c1 for light

moneyamount = 0
moneylabel = None

def addone():
    global moneyamount
    moneyamount += 1
    

def addfive():
    global moneyamount
    moneyamount += 5
    

def display():
    global moneylabel
    if moneylabel:
        moneylabel.destroy()
    moneylabel = Label(root, text="Balance: $" + str(moneyamount))
    moneylabel.pack()

def run1():
    addone()
    display()

def run5():
    addfive()
    display()


def main():
    #Setup for window
    global root
    root = Tk()
    root.title("AuroraBank")
    root.geometry('860x640')
    root.config(bg='#c1c1c1')

    #Interactive parts
    add1moneybutton = Button(root, text="Add $1", command=run1)
    add5moneybutton = Button(root, text="Add $5", command=run5)
    add1moneybutton.pack()
    add5moneybutton.pack()

    root.mainloop()