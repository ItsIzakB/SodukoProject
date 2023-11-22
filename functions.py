from tkinter import *
import numpy as np
import tkinter as tk


def retrieve_info(entry):
    entry_text = entry.get()
    print(entry_text)

#input is the value we are pressing on our keyboard
#entry is the entry that is displayed
def validate_input(input, entry):
    #the logic is that we want our input to only allow numbers and '\b' while only letting the entry be 0 or 1
    #characters long
    if input.isdigit() and len(entry) < 2:
        return True
    elif input == '\b ':
        return True
    else:
        return False


def create_empty_matrix(rows, columns):
    # matrix will be flat filled with 0's
    flat_matrix = np.zeros(rows * columns)

    #then it's made into a matrix with correct dimensions
    matrix=flat_matrix.reshape(rows, columns)

    return matrix


def configure_window(window):
    window.geometry("600x600")
    window.title("Soduko Game")
    window.config(background='#fce1bd')
    window.resizable(0, 0)


def create_labels_in_grid(window, num_rows, num_columns):
    # we need to store the value of the Entry widgets in a matrix
    entries = create_empty_matrix(num_rows, num_columns)

    for row in range(num_rows):
        for column in range(num_columns):
            square = Entry(window,
                           font=('Arial', 40),
                           fg='black',
                           bg='white',
                           relief='solid',
                           bd='1',
                           width=2,
                           cursor='dot',
                           justify="center")
            square.grid(row=row, column=column, sticky= tk.E)
            #This is used to make sure input is only single-digit numbers or '\b'
            reg = window.register(validate_input)
            square.config(validate="key", validatecommand=(reg, '%S', '%P'))





    return entries

def add_bars(window):
    top_bar = tk.Frame(window, height=5, width=window.winfo_reqwidth(), bg="black")
    top_bar.grid(row=0, column=0, columnspan=14)
