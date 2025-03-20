from tkinter import *
from tkinter.ttk import *

import sv_ttk

def main(root):
    root.geometry("675x475")

    mainframe = Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    button = Button(mainframe, text="Hello", command=lambda: print_window_size(mainframe))
    button.grid()
    button1 = Button(mainframe, text="Balls", command=lambda: print_window_size(mainframe))
    button1.grid()


    sv_ttk.use_dark_theme()
   

def print_window_size(widget):
    print(f"{widget.winfo_width()} x {widget.winfo_height()}")


root = Tk(className="Profile Launcher")
if __name__ == "__main__":
    main(root)
root.mainloop()

