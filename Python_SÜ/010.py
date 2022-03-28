'''
Functions in python
Phillip
21.3.22
'''
import random

a_list = []
#define a function
def check_input(a_list,ui):
    #check range of number
    if (ui < 0 or ui > 10):
        return False
    #check if number is already in list
    if (ui in a_list):
        return False
    return True


### main programm
for x in range(10):
    ui = int(input("Bitte eine eindutige Zahl zwischen 0 und 10 eingeben ->"))

    if (check_input(a_list,ui) == False):
        print("Falscher Input, bitte nochmal !")
        continue
    else:
        a_list.append(ui)
        print(a_list)
