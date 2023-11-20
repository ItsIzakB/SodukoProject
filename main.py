import tkinter
from tkinter import *
import functions
import numpy as np

# instantiate window
window = Tk()
functions.configure_window(window)

# configure grid for Sodoku tile placements
entries = functions.create_labels_in_grid(window, 9, 9)
first_entry = window.grid_slaves(row=0, column=0)[0]

button = tkinter.Button(window,
                        text="Retrieve Info",
                        command= lambda entry=first_entry: functions.retrieve_info(entry))


button.grid()
window.mainloop()
