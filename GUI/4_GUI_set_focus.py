import tkinter as tk
from tkinter import ttk
from typing import Text

w = tk.Tk()
w.title("Text box widget")

def click_me():
    action.configure(text = "Hello " + name.get())

# Changing our label
ttk.Label(w, text="Enter a name: ").grid(column=0, row=0)

# Adding a text box entry widget
name = tk.StringVar()
name_entered = ttk.Entry(w, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Place the cursor into name entry
name_entered.focus()

# Adding a button
action = ttk.Button(w, text='Click here!', command=click_me)
action.grid(column=1, row=1)

w.mainloop()
