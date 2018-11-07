#!/usr/bin/python
# file EventSelectionPage.py
# pja 02-15-2017 orig from Bundle page
# imports
from Tkinter import *
import ndsClass
gl = ndsClass.nds('gl')
import StrnumClass
cv = StrnumClass.strnum()
import SQClass
db = SQClass.SQC('berta')

# support functions
def loadEvent(box):
    # load from database
    ab = db.SQReadAll('select * from Event;') # EID,cold,ready
    abmax = ab.__len__() 
    print('abmax='+abmax.__str__())
    for j in range( 0 , abmax):
        EID = ab.__getitem__(j)
        box.insert(END,EID)
    #end for
#end def

def LoadUID(uid,uids):
    print('load uid')
    uids.set("PJA")
# end
def LoadSDate(SDate,SDates):
    print('load SDate')
    SDates.set ('12/12/1212')
#end 

# callback functions
def EExit():
    print('EExit')
    exit()
#end
def ESet():
    print('ESet')
    bn = EList.curselection()
    bna = EList.get(bn[0])
    bna0 = bna[0]
    if (bna.__str__() == "(none)"):
        print('bna=(' + bna.__str__() + ")")
        # clear sticky.((user,"EID"))
        sq = "insert into sticky values( '" + uids.get() + "' , 'EID' , '' );"
        try:
            print("sq="+ sq)
            db.SQX(sq)
        except:
            sq = "update sticky set user= '" + uids.get() + "' , na = 'EID' , vval='' " +  "where user='" + uids.get() + "' and na = 'EID' ;"
            print("sq="+ sq)
            db.SQX(sq)
            
        finally:
            nop = -1
        #end
    else:
        print('bna0=(' + bna0 + ")")
        # set sticky.((user,"EID") bna0 )
        sq = "insert into sticky values( '" + uids.get() + "' , 'EID' , '" + bna0 + "' );"
        try:
            print("sq="+ sq)
            db.SQX(sq)
            
        except:
            sq = "update sticky set user= '" + uids.get() + "' ,na ='EID' , vval='" + bna0 + "' where user='" + uids.get() + "' and na = 'EID' ;"
            print("sq="+ sq)
            db.SQX(sq)
        finally:
            nop = -1
        #end
    #endif
    
    
#end

def NewB():
    print('NewB')
    sq = "insert into sticky values( '" + newstr.get() + "' , 'EID' , '' );"
    try:
		print("sq="+ sq)
		db.SQX(sq)
    except:
		sq = "update sticky set user= '" + newstr.get() + "' , na = 'EID' , vval='' " +  "where user='" + uids.get() + "' and na = 'EID' ;"
		print("sq="+ sq)
		db.SQX(sq)
    finally:
		nop = -1
	#end
	# add to Event
    sq = "insert into Event values( '" + newstr.get() + "' , 'n' , 'n' );"
    try:
		print("sq="+ sq)
		db.SQX(sq)
    except:
		sq = "update Event set EID= '" + newstr.get() + "' , cold='n' , ready='n' " +  "where EID='" + newstr.get() + "' ;"
		print("sq="+ sq)
		db.SQX(sq)
    finally:
		nop = -1
	#end

#paint
page = Tk()
#               wide,len
page.geometry('600x400+350+70')

ROW = 0
Label(page, text='Event Selection Page').grid(row=ROW,column=1)
Button(page,text='Exit',command=EExit).grid(row=ROW,column=3)

ROW = 1
Label(page, text='uid').grid(row=ROW,column=1)
Label(page, text='Event List').grid(row=ROW,column=2)
Label(page, text='Screen Date').grid(row=ROW,column=3)

ROW=2
uids = StringVar()
uid = Entry(page,textvariable=uids).grid(row=ROW,column=1)
LoadUID(uid,uids)

SDates = StringVar()
SDate = Entry(page, textvariable=SDates).grid(row=ROW,column=3)
LoadSDate(SDate, SDates)

ROW=3
EList = Listbox(page)
EList.grid(row=ROW,column=2)
EList.insert(END,'(none)')
loadEvent(EList)

ROW=4
Button(page,text='SET',command=ESet).grid(row=ROW,column=2)
newstr = StringVar()
newe = Entry(page, textvariable=newstr).grid(row=ROW,column=3)

ROW=5
Button(page,text='NEW',command=NewB).grid(row=ROW,column=3)

page.mainloop()
