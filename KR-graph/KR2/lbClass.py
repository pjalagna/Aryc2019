"""
file lbClass.py
pja 8-3-2020

from tkinter import *
root = Tk() 
root.geometry(400x400)
import lbClass
j1 = lbClass.lb(root,'l1',lbClass.simpleFill,lbClass.hit)
f1 = j1.getfx()
f1.pack(root,padx=40,pady=40)


"curselection"

"""
"""
each listbox should exist in its own frame to be positioned into the main.

listboxClass:


"""
from tkinter import *
class lb:
    def __init__(self,root,lbname,simpleFill,l1Ex):
        """
        returns frame with listbox and scroll
        """
        
        self.fx = Frame(root)
        self.	
        lbname = Listbox(self.fx,selectmode=MULTIPLE,height=10)
        lbname.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(self.fx)
        scrollbar.pack(side = LEFT, fill = BOTH)
        lbname.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = lbname.yview)
        b1 = Button(fx,text='hit', command=l1Ex)
        b1.pack()
    #
    def getfx(self):
        return(self.fx)
    #
    def run(self):
        root.mainloop() 
    #
#
        
        
  
# Creating the root window 

  
# Creating a Listbox and 
# attaching it to root window 
 
  
# Adding Listbox to the left 
# side of root window 
 
#listbox1.grid(row=0,column=0,rowspan=3) 
  
# Creating a Scrollbar and  
# attaching it to root window 
 
  
# Adding Scrollbar to the right 
# side of root window 
#scrollbar.pack(side = RIGHT, fill = BOTH)
  
#scrollbar.grid(row=0,column=1,rowspan=3) 
  
# Insert elements into the listbox 
def simpleFill():
    for values in range(100): 
        listbox1.insert(END, values*10) 
    #end for
#end simpleFill
      
# Attaching Listbox to Scrollbar 
# Since we need to have a vertical  
# scroll we use yscrollcommand 
 
  
# setting scrollbar command parameter  
# to listbox.yview method its yview because 
# we need to have a vertical view 
 

#f1 = Frame(root)
#f1.pack(side=LEFT)

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

