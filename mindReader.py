from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox 
import time

running = True
Text = ("Analyzing brainwaves...", "Scanning memories...", "Calculating probabilities...", "Decoding thoughts...")
validInput = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


def checkInput():
    if entrybox.get() in validInput:
        click()
    else:
        messagebox.showerror(title="Invalid Input", message="Please enter an valid input")


def  finalResult():
    window2 = Tk()
    window2.geometry("250x50")
    window2.title("Final Result")
    Label(window2, text = f"You are thinking of the number {entrybox.get()}.").pack(anchor=N)

def textDisplay(num):
    if num in [0, 25, 50, 75]:
        label.config(text=Text[int(num/25)])

def update_progressbar(value):
    bar['value'] = value
    textDisplay(value)
    if value <= 100:
        window1.after(50, update_progressbar, value + 1) # widget.after(delay{in ms}, callback function, *args) 
    else:
        time.sleep(0.1)
        window1.destroy()
        time.sleep(0.1)
        finalResult()

def click():
    global window1
    window1 = Tk()
    window1.geometry("300x100")
    window1.title("Reading your mind")
    global bar
    bar = Progressbar(window1, orient=HORIZONTAL, length=250)
    bar.place(x=25, y=50)
    global label
    label = Label(window1, text="")
    label.pack()
    window1.after(50, update_progressbar, 0)# widget.after(delay{in ms}, callback function, *args)

window = Tk()

Label(window, text="Think of a number between 1 and 10:").place(x=50, y=30)

entrybox = Entry(window, font=("consol", 10))
entrybox.place(x=80, y=60)

Button(window, text="Read my mind", command=checkInput).place(x=100, y=90)

window.title("Mind Reader")
window.geometry("330x150")
window.mainloop()
