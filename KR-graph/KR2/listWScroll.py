"""
import listWScroll

"curselection"

"""
"""
each listbox should exist in its own frame to be positioned into the main.

listboxClass:


"""
from tkinter import *
  
  
# Creating the root window 
root = Tk() 
  
# Creating a Listbox and 
# attaching it to root window 
listbox1 = Listbox(root,selectmode=MULTIPLE,height=10) 
  
# Adding Listbox to the left 
# side of root window 
listbox1.pack(side = LEFT, fill = BOTH) 
#listbox1.grid(row=0,column=0,rowspan=3) 
  
# Creating a Scrollbar and  
# attaching it to root window 
scrollbar = Scrollbar(root) 
  
# Adding Scrollbar to the right 
# side of root window 
#scrollbar.pack(side = RIGHT, fill = BOTH)
scrollbar.pack(side = LEFT, fill = BOTH)  
#scrollbar.grid(row=0,column=1,rowspan=3) 
  
# Insert elements into the listbox 
for values in range(100): 
    listbox1.insert(END, values*10) 
      
# Attaching Listbox to Scrollbar 
# Since we need to have a vertical  
# scroll we use yscrollcommand 
listbox1.config(yscrollcommand = scrollbar.set) 
  
# setting scrollbar command parameter  
# to listbox.yview method its yview because 
# we need to have a vertical view 
scrollbar.config(command = listbox1.yview) 

f1 = Frame(root)
f1.pack(side=LEFT)

def hit():
   print('hit was hit')
   print(listbox1.curselection())
   j=listbox1.curselection()
   for m in j:
       print(listbox1.get(m))
   #
   #exit
   root.quit() #doesn't shut window
#
b1 = Button(f1,text='hit', command=hit)
b1.grid(row=3,column=3)
root.mainloop() 