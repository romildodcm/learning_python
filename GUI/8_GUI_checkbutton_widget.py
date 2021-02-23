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

# Adding a button
action = ttk.Button(w, text='Click here!', command=click_me)
action.grid(column=2, row=1)
#action.configure(state='disable')

# New label - Combobox
ttk.Label(w, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar()
# the state parameter readonly restrict the user to only being able to 
# select the values we have programmed  
number_chosen = ttk.Combobox(w, width=12, textvariable=number, state='readonly')
number_chosen['value'] = (1, 2, 4, 42, 787)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Checkbox
chVarDis = tk.IntVar()
# The parameter state = desable will be disable the check button
check1 = tk.Checkbutton(w, text='Disable', variable=chVarDis, state='disable')
check1.select() # Set the initial state of the check button
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(w, text='UnChecked', variable=chVarUn)
check2.deselect() # Set the initial state of the check button
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(w, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


name_entered.focus() # Place the cursor into name entry

w.mainloop()
