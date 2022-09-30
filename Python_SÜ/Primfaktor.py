'''
Dings Primzahlen
'''
import tkinter.messagebox, tkinter.simpledialog, tkinter.ttk, tkinter as tk

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

while True:
    num = tk.simpledialog.askinteger("Prime Number Factorisation", "Please enter your number")
    num_finish = prime_factors(num)
    tkinter.messagebox.showinfo("Prime Number Factorisation", "Your number is composed of " + str(num_finish))
    repeate= tkinter.messagebox.askyesno("Prime Number Factorisation", "Do you want to try again?")
    if repeate == False:
        break
