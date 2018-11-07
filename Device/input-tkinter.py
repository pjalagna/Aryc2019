#!/usr/bin/python
# file input1-tkinter
# from https://www.tutorialspoint.com/python/python_gui_programming.htm
""" <<section-0>> """

from Tkinter import *
""" <<section-1>> """

def Insert():
	name = text.get()
	name2 = text2.get()
	global t3, text3
	# t3.set( text.get()	)
	t3.set("here")
	text3.delete(0,END) # clear
	text3.insert(INSERT, text.get())
	list.insert(END, name)
	list.insert(END, name2)
	text2.delete(0,END)
	text.delete(0,END)
	
""" <<section-2>> """
root = Tk()
root.geometry('200x210+350+70')

second = Tk()
second.geometry('300x210+350+70')

""" <<section-3>> """
text = Entry(root, bg = 'white')
text2 = Entry(root, bg = 'white')
button = Button(root, text = "press me", command = Insert)
list = Listbox(root, bg = 'blue', fg = 'yellow')

# global t3 , text3
t3 = StringVar()
text3 = Entry(second, textvariable=t3)

""" <<section-4>> """
text.pack()
text2.pack()
button.pack(padx = 4, pady = 4, anchor= E)
list.pack()

text3.pack()

""" <<section-5>> """

# start loops at bottom
second.mainloop()
root.mainloop()

""" from Tkinter import *

root = Tk()

var = StringVar()
label = Message( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()
"""
nop = """
from Tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)

E1.pack(side = RIGHT)

top.mainloop()
"""
nop = """
main():
   # open tk screen ask iam, to, cmd
   # write to store (t=message, c=[iam,etc] , r=output1)
   # trigger output1-tkinter
   # die
#end
"""
nop = """
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
"""
"""
from Tkinter import *

def Pressed():                          #function
        print 'buttons are cool'

root = Tk()                             #main window
button = Button(root, text = 'Press', command = Pressed)
button.pack(pady=20, padx = 20)
#Pressed()
root.mainloop()
"""

""" command line args
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
"""
   
