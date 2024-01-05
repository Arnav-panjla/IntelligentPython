from tkinter import *
from tkinter.ttk import *
import time

running = True

def click():
    window1 = Tk()
    window1.geometry("300x100")
    bar = Progressbar(window1,orient=HORIZONTAL,length=250,)
    bar.place(x=25,y=50)
    while True:
        bar['value'] +=5
        time.sleep(0.1)
        window1.update()
        if bar['value'] == 100:
            time.sleep(0.5)
            break



window = Tk()

Label(window, text="Think of a number between 1 and 10 :").place(x=50, y= 30)

entrybox = Entry(window, font=("consol", 10))
entrybox.place(x=80, y= 60)

Button(window, text="Read my mind", command=click).place(x=100, y= 90)

window.title("Mind Reader")
window.geometry("300x150")
window.mainloop()