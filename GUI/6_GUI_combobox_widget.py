import tkinter as tk
from tkinter import ttk
from typing import Text

w = tk.Tk()
w.title("Text box widget")

def click_me():
    action.configure(text = "Hello " + name.get() + ' ' + number.get())

# Changing our label
ttk.Label(w, text="Enter a name: ").grid(column=0, row=0)

# Adding a text box entry widget
name = tk.StringVar()
name_entered = ttk.Entry(w, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus() # Place the cursor into name entry

# Adding a button
action = ttk.Button(w, text='Click here!', command=click_me)
action.grid(column=2, row=1)
#action.configure(state='disable')

# New label
ttk.Label(w, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(w, width=12, textvariable=number)
number_chosen['value'] = (1, 2, 4, 42, 787)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)


w.mainloop()
