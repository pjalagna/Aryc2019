#!/usr/bin/python
# file BundleSelectionPage.py
# pja 02-11-2017 edits
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
def loadBundle(box):
    # load from database
    ab = db.SQReadAll('select * from bundle;') # bid,cold,ready
    abmax = ab.__len__() 
    print('abmax='+abmax.__str__())
    for j in range( 0 , abmax):
        bid = ab.__getitem__(j)
        box.insert(END,bid)
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
def BExit():
    print('BExit')
    exit()
#end
def BSet():
    print('BSet')
    bn = BList.curselection()
    bna = BList.get(bn[0])
    bna0 = bna[0]
    if (bna.__str__() == "(none)"):
        print('bna=(' + bna.__str__() + ")")
        # clear sticky.((user,"BID"))
        sq = "insert into sticky values( '" + uids.get() + "' , 'BID' , '' );"
        try:
            print("sq="+ sq)
            db.SQX(sq)
        except:
            sq = "update sticky set user= '" + uids.get() + "' , na = 'BID' , vval='' " +  "where user='" + uids.get() + "' and na = 'BID' ;"
            print("sq="+ sq)
            db.SQX(sq)
            
        finally:
            nop = -1
        #end
    else:
        print('bna0=(' + bna0 + ")")
        # set sticky.((user,"BID") bna0 )
        sq = "insert into sticky values( '" + uids.get() + "' , 'BID' , '" + bna0 + "' );"
        try:
            print("sq="+ sq)
            db.SQX(sq)
            
        except:
            sq = "update sticky set user= '" + uids.get() + "' ,na ='BID' , vval='" + bna0 + "' where user='" + uids.get() + "' and na = 'BID' ;"
            print("sq="+ sq)
            db.SQX(sq)
        finally:
            nop = -1
        #end
    #endif
    
    
#end

def NewB():
    print('NewB')
    sq = "insert into sticky values( '" + newstr.get() + "' , 'BID' , '' );"
    try:
		print("sq="+ sq)
		db.SQX(sq)
    except:
		sq = "update sticky set user= '" + newstr.get() + "' , na = 'BID' , vval='' " +  "where user='" + uids.get() + "' and na = 'BID' ;"
		print("sq="+ sq)
		db.SQX(sq)
    finally:
		nop = -1
	#end
	# add to Bundle
    sq = "insert into bundle values( '" + newstr.get() + "' , 'n' , 'n' );"
    try:
		print("sq="+ sq)
		db.SQX(sq)
    except:
		sq = "update Bundle set BID= '" + newstr.get() + "' , cold='n' , ready='n' " +  "where BID='" + newstr.get() + "' ;"
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
Label(page, text='Bundle Selection Page').grid(row=ROW,column=1)
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
newstr = StringVar()
newe = Entry(page, textvariable=newstr).grid(row=ROW,column=3)

ROW=5
Button(page,text='NEW',command=NewB).grid(row=ROW,column=3)

page.mainloop()
