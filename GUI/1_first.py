import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()
# Add a Title
win.title("My First Python GUI")
# Disabre resizing the GUI by passing in False/False
#win.resizable(False, False)

# Adding a label
ttk.Label(win, text="A label").grid(column=0, row=0)

# Start the GUI
win.mainloop()