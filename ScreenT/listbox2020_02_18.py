#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
file listbox2020_02_18.py
pja 02-18-2020

moves selection from list to a label via a button
available after exit in StringVar attached to label
returns selected and moved value

test as
import listbox2020_02_18
j = listbox2020_02_18.main()
j

"""
def record_selection():
    """ moves selection into label textvar """
    global lb,var1
    value = lb.get(lb.curselection())   
    var1.set(value)  
#

def main():
	import tkinter as tk
 
	window = tk.Tk()
	window.title('My Window') # adds title  
	window.geometry('500x300')
	global lb,var1
	# add variable to label
	var1 = tk.StringVar()
	l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)

	l.pack()

	# transfer button
	b1 = tk.Button(window, text='record selection', width=15, height=2, command=record_selection)

	b1.pack()
 
	var2 = tk.StringVar()
	var2.set((1,2,3,4,100))
	
	lb = tk.Listbox(window, listvariable=var2)
	# listvariable is the complete list 

	list_items = [11,22,33,44] # also added to var2
	for item in list_items:
		lb.insert('end', item)
	#endfor

	lb.insert(1, 'first') # also added to var2
	lb.insert(2, 'second') # also added to var2

	lb.pack()
 
	window.mainloop()
	return(var1.get())
#
