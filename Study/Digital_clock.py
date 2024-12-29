from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Clock")

def present_time():
    # %p - to display AM/PM
    # %S - to display seconds
    # %M - to display minutes
    # %I - to display time in 12h period
    # %H - to display time in 24h period
    display_time = time.strftime("%H:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200, present_time)

digi_clock = Label(root, font=("arial", 150), bg="white", fg="black")
digi_clock.pack()

present_time()
root.mainloop()