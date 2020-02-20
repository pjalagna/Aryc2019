#!/usr/bin/python
m = """file BundleEntryPage.py
pja 02-14-2020 review and edits
# pja 02-07-2017 orig from html

test as
import BundleEntryPage


# imports
"""
from Tkinter import *
import ndsClass
gl = ndsClass.nds('gl')
import StrnumClass
cv = StrnumClass.strnum()
import SQClass
db = SQClass.SQC('berta')
vars = []
# support functions

def LoadUID(uid,uids):
    print('load uid')
    uids.set("PJA")
# end
def LoadSDate(SDate,SDates):
    print('load SDate')
    SDates.set ('12/12/1212')
#end 

# callback functions
def BExit():
    print('BExit')
    exit()
#end
def BSet():
    print ('BSet')
    print(dir(vars[0]))
    print(vars[0].trace_variable())
    #print(uids.__str__() + '-' + uids.get())
    print(vars[0].__str__() + '-' + vars[0].get())
    print(vars[1].__str__() + '-' + vars[1].get())
    #print(SDates.__str__() + '-' + SDates.get())
#end
    
#paint
page = Tk()
#               wide,len
page.geometry('600x400+350+70')

ROW = 0
Label(page, text='Bundle Entry Page').grid(row=ROW,column=1)
Button(page,text='Exit',command=BExit).grid(row=ROW,column=3)

ROW = 1
Label(page, text='uid').grid(row=ROW,column=1)
Label(page, text='Bundle List').grid(row=ROW,column=2)
Label(page, text='Screen Date').grid(row=ROW,column=3)

ROW=2

vars.append( StringVar() )
uid = Entry(page,textvariable=vars[len(vars)-1]).grid(row=ROW,column=1)
LoadUID(uid,vars[len(vars)-1])

vars.append( StringVar() )
SDate = Entry(page, textvariable=vars[len(vars)-1]).grid(row=ROW,column=3)
LoadSDate(SDate, vars[len(vars)-1])

ROW=3
BList = Listbox(page)
BList.grid(row=ROW,column=2)
BList.insert(END,'(none)')
# loadBundle(BList)

ROW=4
Button(page,text='SET',command=BSet).grid(row=ROW,column=2)

page.mainloop()
