'''
Phillip
get_programm
23.05.22
'''

import tkinter as tk
import tkinter.messagebox
from tkinter import simpledialog, messagebox



def Rges_parallel(list_resistors):
    # calculates the total resistance in the parallel circuit
    count = 1
    Rges_temp = 1 / list_resistors[0]
    while len(list_resistors) != count:
        print(1)
        Rges_temp = Rges_temp + 1 / list_resistors[count]
        count += 1
    # makes the final calculation and returns Rges
    Rges = 1 / Rges_temp
    return Rges


def Rges_serial(list_resistors):
    # calculates the total resistance in the serial circuit
    count = 1
    Rges_temp = list_resistors[0]
    while len(list_resistors) != count:
        Rges_temp = Rges_temp + list_resistors[count]
        count += 1
    # returns Rges
    Rges = Rges_temp
    return Rges


def parallel_U(list_resistors, Iges):
    # calculates the total voltage in the parallel circuit
    Uges = Rges_parallel(list_resistors) * Iges
    return Uges


def parallel_I(list_resistors, Uq):
    # calculates the total current in the parallel circuit
    Iges = Uq / Rges(list_resistors)
    return Iges


def serial_U(list_resistors, Iges):
    # calculates the total voltage in the serial circuit
    Uges = Rges_serial(list_resistors) * Iges
    return Uges


def serial_I(list_resistors, Uq):
    # calculates the total current in the serial circuit
    Iges = Uq / Rges_serial(list_resistors)
    return Iges


'''
##############################################################################
Main Programm
###############################################################################
'''

tk.messagebox.showinfo(title="Get Program", message="Welcome to your own Get Program!")
while True:
    list_resistors = []

    R = simpledialog.askfloat(title="Get Program", prompt="Please enter the value of your first Resistor in \u03A9")
    next = tk.messagebox.askyesno(title="Get Program", message="Do you want to add another Resistor?")
    while next == True:
        list_resistors.append(R)
        R = simpledialog.askfloat(title="Get Program", prompt="Please enter the value of your next Resistor in \u03A9")
        next = tk.messagebox.askyesno(title="Get Program", message="Do you want to add another Resistor?")
    list_resistors.append(R)

    which = messagebox.askquestion(title="Get Program", icon="question",
                                   message="Do you want to calculate the Voltage or the Current?"
                                           " For Voltage click Yes, for Current No", type="yesno")
    which_now = messagebox.askquestion(title="Get Program", icon="question",
                                       message="Is your circuit parallel or serial? For Parallel click Yes, for Serial No",
                                       type="yesno")

    if which == 'yes':
        I = simpledialog.askinteger(title="Get Program", prompt="Please enter the value of your current in A")
        if which_now == 'yes':
            U = parallel_U(list_resistors, I)
        elif which_now == 'no':
            U = serial_U(list_resistors, I)

    if which == 'no':
        U = simpledialog.askfloat(title="Get Program", prompt="Please enter the value of your voltage in V")
        if which_now == 'yes':
            I = parallel_I(list_resistors, U)
        elif which_now == 'no':
            I = serial_I(list_resistors, U)

    tk.messagebox.showinfo(title="Get Program", message="Your result is: \n U = {}V \n I = {}A".format(U, I))

    restart = tk.messagebox.askyesno(title="Get Program", message="Do you wish to calculate another one?")
    if restart == False:
        break
    else:
        continue
