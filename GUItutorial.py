# GUI tutorial
# import the relevant modules

from tkinter import *
from tkinter import ttk

def calculate(*args): # define a function that gathers my arguments
    try:
        value = float(feet.get())
        meter.set((0.3048 * value * 10000 + 0.5) / 10000) # conversion
    except ValueError:
        pass

root = Tk()
root.title('Feet to Meters')

mainframe = ttk.Frame(root, padding = '3 3 12 12')
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

# create 3 main widgets within the GUI
# 1: user entry for entering the number of feet
# 2: a label where the results appear
# 3: a calculate button
feet = StringVar()
meter = StringVar()
# when displaying the widgets, there are 2 steps
# 1. creating the widget
feet_entry = ttk.Entry(mainframe, width = 7, textvariable = feet) # the input
# 2. place the widget on the screen (.grid method)
# the widgets are the 'children' of the mainframe content window
# they are instances of my Tk widget classes
feet_entry.grid(column = 2, row = 1, sticky = (W, E))
# meter output
ttk.Label(mainframe, textvariable = meter).grid(column = 2, row = 2, sticky = (W, E))
# calculate button
ttk.Button(mainframe, text = 'Calculate', command = calculate).grid(column = 3, row = 3, sticky = W)

# create static labels in the user interface
ttk.Label(mainframe, text = 'feet').grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = 'is equivalent to').grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = 'meters').grid(column = 3, row = 2, sticky = W)

# let's add some padding around the children widgets
# using a for loop to  walk through my children
for child in mainframe.winfo_children(): child.grid_configure(padx = 5, pady = 5)

# to finesse the GUI
# we can set the cursor to start in the field
feet_entry.focus() # focus the cursor
root.bind('<Return>', calculate)

root.mainloop()
