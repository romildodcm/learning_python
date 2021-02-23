import tkinter as tk
from tkinter import ttk

w = tk.Tk()
w.title("Button Change")

# Adding a label that will be modified
a_label = ttk.Label(w, text="A label")
a_label.grid(column=0, row=0)

# Button click event function
def click_me():
    action.configure(text="** I have been clicked **")
    a_label.configure(foreground='red')
    a_label.configure(text='A red label')

# Adding a button
action = ttk.Button(w, text='Click here!', command=click_me)
action.grid(column=1, row=0)

w.mainloop()