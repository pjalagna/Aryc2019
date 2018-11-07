#!/usr/bin/python
# file BundleEntryPage.py
# pja 02-07-2017 orig from html
# imports
from Tkinter import *
import ndsClass
gl = ndsClass.nds('gl')
import StrnumClass
cv = StrnumClass.strnum()
import SQClass
db = SQClass.SQC('berta')

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
uids = StringVar()
uid = Entry(page,textvariable=uids).grid(row=ROW,column=1)
LoadUID(uid,uids)

SDates = StringVar()
SDate = Entry(page, textvariable=SDates).grid(row=ROW,column=3)
LoadSDate(SDate, SDates)

ROW=3
BList = Listbox(page)
BList.grid(row=ROW,column=2)
BList.insert(END,'(none)')
loadBundle(BList)

ROW=4
Button(page,text='SET',command=BSet).grid(row=ROW,column=2)

page.mainloop()
