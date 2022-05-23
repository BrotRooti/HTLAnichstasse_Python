'''
Exploring Python turtle
Julian, Phillip
02.05.2022
'''

#importing classes
import turtle
from turtle import *
import time
import tkinter as tk
from tkinter import simpledialog, messagebox, colorchooser

#
# Functions
#

# Draws a square
def square(size):
    for i in range(4):
        forward(size)
        left(90)

# Draws a rectangle
def rectangle(a, b):
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)

# Moves the turtle without a line behind it
def move(x, y):
    penup()
    turtle.hideturtle()
    goto(x, y)
    setheading(0)
    turtle.showturtle()
    pendown()

# ends fill - changes color - starts new fill
def colorchange(pencolor, fillcolor):
    end_fill()
    color(pencolor, fillcolor)
    begin_fill()

# Draws the House at given coords with given colors
def house(startx, starty, pencolor, fillcolor, scale):
    move(startx, starty)
    colorchange(pencolor, fillcolor)

    speed(1000)
    square(100*scale)

    move(xcor() + 100*scale, ycor() + 100*scale)
    left(135)
    forward(70.711*scale)
    left(90)
    forward(70.711*scale)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 15*scale, ycor() - 30*scale)
    square(20*scale)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 50*scale, ycor())
    square(20*scale)

    colorchange(pencolor, '#593323')
    move(xcor() - 15*scale, ycor() - 70*scale)
    rectangle(20*scale, 40*scale)

    colorchange('#fffb00', '#fffb00')
    move(xcor() + 3*scale, ycor() + 15*scale)
    circle(2.5*scale)

    end_fill()

tk.messagebox.showinfo(title="House Drawing", message="Welcome to the House Drawing Program!")

while(True):
    #messages and input
    X = simpledialog.askinteger(title="House Drawing Program", prompt="Please enter the x-coordinates of the house (-200, 200)")
    Y = simpledialog.askinteger(title="House Drawing Program", prompt="Please enter the y-coordinates of the house (-200, 200)")
    scale = simpledialog.askinteger(title="House Drawing Program", prompt="Please enter the size of the house (1, 10)")
    pen = colorchooser.askcolor(title="House Drawing Program", color="red")
    back = colorchooser.askcolor(title="House Drawing Program", color="purple")

    #change the rgb values to hex
    pencolor = '#%02x%02x%02x' % (pen[0][0], pen[0][1], pen[0][2])
    fillcolor = '#%02x%02x%02x' % (back[0][0], back[0][1], back[0][2])

    #draws the house
    house(X, Y, pencolor, fillcolor, scale)

    #asks if the user wants to draw another house
    repeat = messagebox.askquestion(title="House Drawing Program", icon="question", message="Do you want to draw another house?")

    if (repeat  == 'no'):
        time.sleep(69)
        break
    else:
        continue
