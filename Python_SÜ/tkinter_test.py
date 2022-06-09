from tkinter import *
tkFenster = Tk()
def example1():
    tkFenster.title("pack example 01")
    label1 = Label(master=tkFenster, text="eins", bg="red", fg="white")
    label2 = Label(master=tkFenster, text="zwei", bg="green", fg="black")
    label3 = Label(master=tkFenster, text="drei", bg="blue", fg="white")
    label4 = Label(master=tkFenster, text="vier", bg="yellow", fg="black")
    label1.pack()
    label2.pack()
    label4.pack()
    label3.pack()
    tkFenster.mainloop()

def example2():
    tkFenster.title("pack example 02")
    label1 = Label(master=tkFenster, text="eins",
                   bg="red", fg="white")
    label2 = Label(master=tkFenster, text="zwei",
                   bg="green", fg="black")
    label3 = Label(master=tkFenster, text="drei",
                   bg="blue", fg="white")
    label4 = Label(master=tkFenster, text="vier",
                   bg="yellow", fg="black")
    label1.pack(side="right", ipadx=5, ipady=5,
                padx=5, pady=5)
    label2.pack(side="right", ipadx=20, ipady=20,
                padx=20, pady=20)
    label4.pack(side="bottom", ipadx=5, ipady=5,
                padx=5, pady=5)
    label3.pack(side="bottom")
    tkFenster.mainloop()

def example3():
    tkFenster.title("pack example 03")
    label1 = Label(master=tkFenster, text="eins",
                   bg="red", fg="white")
    label2 = Label(master=tkFenster, text="zwei",
                   bg="green", fg="black")
    label3 = Label(master=tkFenster, text="drei",
                   bg="blue", fg="white")
    label4 = Label(master=tkFenster, text="vier",
                   bg="yellow", fg="black")
    label1.pack(fill="x", ipadx=5, ipady=5,
                padx=5, pady=5)
    label2.pack(side="right", ipadx=20, ipady=20,
                padx=20, pady=20)
    label4.pack(side="bottom", ipadx=5, ipady=5,
                padx=5, pady=5)
    label3.pack(fill="both")
    tkFenster.mainloop()

def example4():
    tkFenster.title("pack example 04")
    rahmen1 = Frame(master=tkFenster, bg='magenta')
    rahmen1.pack(side='top', padx ='5', pady ='5')
    rahmen2 = Frame(master=tkFenster, bg='cyan')
    rahmen2.pack(side='bottom', fill = "x", padx ='5',
    pady ='5')
    label1 = Label(master=rahmen1, text="eins",
                   bg="red", fg="white")
    label2 = Label(master=rahmen1, text="zwei",
                   bg="green", fg="black")
    label3 = Label(master=rahmen2, text="drei",
                   bg="blue", fg="white")
    label4 = Label(master=rahmen2, text="vier",
                   bg="yellow", fg="black")
    label1.pack(fill="x", ipadx=5, ipady=5,
                padx=5, pady=5)
    label2.pack(side="right", ipadx=20, ipady=20,
                padx=20, pady=20)
    label4.pack(side="bottom", ipadx=5, ipady=5,
                padx=5, pady=5)
    label3.pack(fill="both")
    tkFenster.mainloop()

def grid_example1():
    tkFenster.title("grid example 01")
    frame1 = Frame(master=tkFenster)
    frame1.pack()
    label1 = Label(master=frame1,
                   text="eins", bg="red", fg="white")
    label2 = Label(master=frame1,
                   text="zwei", bg="green", fg="black")
    label3 = Label(master=frame1,
                   text="drei", bg="blue", fg="white")
    label4 = Label(master=frame1,
                   text="vier", bg="yellow", fg="black")
    label1.grid(column=0)
    label2.grid(row=0, column=1)
    label3.grid(row=1, column=1)
    label4.grid(row=1, column=2)
    tkFenster.mainloop()

def grid_example2():
    tkFenster.title("grid example 02")
    tkFenster.geometry("260x90")
    tkFenster.resizable(False, False)
    frame1 = Frame(master=tkFenster)
    frame1.pack()
    label1 = Label(master=frame1,
                   text="eins", bg="red", fg="white")
    label2 = Label(master=frame1,
                   text="zwei", bg="green", fg="black")
    label3 = Label(master=frame1,
                   text="drei", bg="blue", fg="white")
    label4 = Label(master=frame1,
                   text="vier", bg="yellow", fg="black")
    entry1 = Entry(master=frame1)
    entry2 = Entry(master=frame1)
    # Layout
    label1.grid(row=0, column=0)
    entry1.grid(row=0, column=1)
    label2.grid(row=1, column=0)
    entry2.grid(row=1, column=1)
    label3.grid(row=2, column=1, sticky='e')
    label4.grid(row=5, column=5)
    tkFenster.mainloop()

def auto_resize_example():
    class MyApp(Frame):
        def __init__(self, master):

            super().__init__(master)

    # self.pack(fill=BOTH, expand=True)
    master.geometry("200x200")
    # frame
    self.f1 = Frame(master=master)
    self.f1.pack(fill=BOTH, expand=True)
    # parameter fuer die grid groesse
    self.grid_length = 3
    self.create_buttons()
    # make the grid layout expand
    for x in range(self.grid_length):
        self.f1.columnconfigure(x, weight=1)
    self.f1.rowconfigure(x, weight=1)

    def create_buttons(self):
        for x in range(self.grid_length):
            for y in range(self.grid_length):
                b = Button(master=self.f1,
                       text="{}/{}".format(x, y))

    b.grid(row=y, column=x,
           sticky=N + S + E + W)
    tk_window = Tk()
    tk_window.title("grid expand example")
    app = MyApp(tk_window)
    app.mainloop()

def place_example():
    tkFenster.title("place example 01")
    frame1 = Frame(master=tkFenster)
    frame1.pack()
    label1 = Label(master=frame1,
                   text="Ich bin ein Label",
                   bg="red", fg="white",
                   height=3, width=30)
    b = Button(master=frame1, text="click")
    # Layout
    label1.pack()
    b.place(relx=1, x=-2, y=2, anchor=NE)
    tkFenster.mainloop()




x = int(input("Which example do you want to run? "))

if (x==1):
    example1()
elif (x==2):
    example2()
elif (x==3):
    example3()
elif (x==4):
    example4()
elif (x==5):
    grid_example1()
elif (x==6):
    grid_example2()
elif (x==7):
    auto_resize_example()
elif (x==8):
    place_example()
else:
    print("Wrong input")