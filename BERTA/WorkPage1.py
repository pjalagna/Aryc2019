# file WorkPage1.py
""" berta workpage
pja 02-06-2017 
pja 02-04-2017 org
-- 
"""
# imports
from Tkinter import *
import ndsClass
gl = ndsClass.nds('gl')
tAR = {}
gl.bang('tAR',tAR)
etidAR = {}
gl.bang('etidAR', etidAR)

import StrnumClass
cv = StrnumClass.strnum()
import SQClass
db = SQClass.SQC('berta')
import subprocess

# nds globals
# support functions

def LoadUID(uid,uids):
    print('load uid')
    uids.set("PJA")
# end
def LoadSDate(SDate,SDates):
    print('load SDate')
    import time
    SDates.set (time.asctime())
#end 

#callbacks
def SAVEC():
    print('bundle=' + bids.get())
    print('rule=' + rids.get())
    print('active rows=',tAR.keys())
    # per active row
    for k in  tAR.keys() :
        # test for blanks
        if (tAR[k]['formi'].get() == ''):
            nop = 1
        else:
            print('k=' + k.__str__() + ' formi=' + tAR[k]['formi'].get())
            print('')
        #endif
    #end for
#end 
def stump():
    print("Stump")
#end

def BExit():
    print("BExit")
    exit()
#bexit
def SBundle():
    print("Get Bundle List")
    subprocess.Popen(["nohup", "python", "BundleSelectionPage.py"])
#end
def CBundle():
    print('grab sticky bundle')
    sq = "select vval from sticky where user ='" + uids.get() + "' and na='BID' ;"
    sqc = db.SQReadAll(sq)
    bids.set(sqc[0])
#end

#paint
page = Tk()
page.geometry('1500x400+350+7000')
ROW = 0 # L-pname -- --  "uid"  "sdate"  B-exit
Label(page, text='Work Page 1').grid(row=ROW,column=0)
Label(page, text='UID').grid(row=ROW,column=3)
Label(page, text='Screen Date').grid(row=ROW,column=4)
Button(page,text='Exit',command=BExit).grid(row=ROW,column=5)

ROW = 1 # SAVE -- -- E-uid -- e-sdate -- -- --
Button(page,text='SAVE',command=SAVEC).grid(row=ROW,column=0)
uids = StringVar()
uid = Entry(page,textvariable=uids).grid(row=ROW,column=3)
LoadUID(uid,uids)

SDates = StringVar()
SDate = Entry(page, textvariable=SDates).grid(row=ROW,column=4)
LoadSDate(SDate, SDates)

ROW=2
Label(page, text='Bundle').grid(row=ROW,column=2)
Label(page, text='Rule').grid(row=ROW,column=3)
Label(page, text='Test').grid(row=ROW,column=4)
Label(page, text='Action').grid(row=ROW,column=5)

ROW=3 # b-sbun -> -- e-bun -- -- b-save
Button(page,text='Bundle List',command=SBundle).grid(row=ROW,column=0)
Button(page,text='->',command=CBundle).grid(row=ROW,column=1)
bids = StringVar()
ebid = Entry(page,textvariable=bids).grid(row=ROW,column=2)

ROW=4 # b-rule ->  e-rule -- -- --
Button(page,text='Select rule',command=stump).grid(row=ROW,column=0)
Button(page,text='->',command=stump).grid(row=ROW,column=1)
rids = StringVar()
erid = Entry(page,textvariable=rids).grid(row=ROW,column=3)

ROW=5 # b-sact -> -- -- -- -- e-action -- -- --
Button(page,text='Select Action',command=stump).grid(row=ROW,column=0)
Button(page,text='->',command=stump).grid(row=ROW,column=1)
acids = StringVar()
eacid = Entry(page,textvariable=acids).grid(row=ROW,column=5)

for ROW in range (6 , 18): # b-test -> -- --  e-test 
	Button(page,text='Select Test',command=stump).grid(row=ROW,column=0)
	Button(page,text='->',command=stump).grid(row=ROW,column=1)
	tAR[ROW] = {}
	tAR[ROW]['formi'] = StringVar()
	tAR[ROW]['view'] = Entry(page,textvariable=tAR[ROW]['formi']).grid(row=ROW,column=4,ipadx=50)
#end for


page.mainloop()



   
   
   
