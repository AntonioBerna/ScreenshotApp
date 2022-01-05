from tkinter import *
from mss import mss

root = Tk()
root.title("Screen Shot App - Clever Code")
root.geometry("500x200")

def shot():
    with mss() as sct:
        # Designate the filename
        
        # https://python-mss.readthedocs.io/examples.html#basics
        # mon=1 -> first monitor
        # mon=2 -> second monitor
        # mon=-1 -> all monitor
        filename = sct.shot(mon=-1, output="screen.png")

        # Confirm message
        my_label.config(text="Screen Shot Has Been Saved!")

my_button = Button(root, text="Take A Screenshot!", font=("Helvetica", 24), command=shot)
my_button.pack(pady=40)

my_label = Label(root, text="")
my_label.pack(pady=10)

root.mainloop()
