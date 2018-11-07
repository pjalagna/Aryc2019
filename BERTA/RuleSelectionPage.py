#!/usr/bin/python
# file RuleSelectionPage.py
# pja 02-20-2017 added sticky fetch for limits (no code)
# pja 02-11-2017 clone from Rule
# pja 02-07-2017 orig from html
#
# rule((RID ) ) 
# imports
from Tkinter import *
import ndsClass
gl = ndsClass.nds('gl')
import StrnumClass
cv = StrnumClass.strnum()
import SQClass
db = SQClass.SQC('berta')

# support functions
def loadRule(box):
    print('load rule')
    # load from database
    ab = db.SQReadAll('select * from rule;') # rid
    abmax = ab.__len__() 
    print('abmax='+abmax.__str__())
    for j in range( 0 , abmax):
        RID = ab.__getitem__(j)
        box.insert(END,RID)
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
def stump():
    print("stump")
#end

def BExit():
    print('Exit')
    exit()
#end

def BSet():
    print('BSet')
    bn = BList.curselection()
    bna = BList.get(bn[0])
    bna0 = bna[0]
    if (bna.__str__() == "(none)"):
        print('bna=(' + bna.__str__() + ")")
        # clear sticky.((user,"RID"))
        sq = "insert into sticky values( '" + uids.get() + "' , 'RID' , '' );"
        try:
            print("sq="+ sq)
            db.SQX(sq)
        except:
            sq = "update sticky set user= '" + uids.get() + "' , na = 'RID' , vval='' " +  "where user='" + uids.get() + "' and na = 'RID' ;"
            print("sq="+ sq)
            db.SQX(sq)
            
        finally:
            nop = -1
        #end
    else:
        print('bna0=(' + bna0 + ")")
        # set sticky.((user,"RID") bna0 )
        sq = "insert into sticky values( '" + uids.get() + "' , 'RID' , '" + bna0 + "' );"
        try:
            print("sq="+ sq)
            db.SQX(sq)
            
        except:
            sq = "update sticky set user= '" + uids.get() + "' ,na ='RID' , vval='" + bna0 + "' where user='" + uids.get() + "' and na = 'RID' ;"
            print("sq="+ sq)
            db.SQX(sq)
        finally:
            nop = -1
        #end
    #endif
    
    
#end

def NewB():
    print('NewB')
    sq = "insert into sticky values( '" + newstr.get() + "' , 'RID' , '' );"
    try:
		print("sq="+ sq)
		db.SQX(sq)
    except:
		sq = "update sticky set user= '" + newstr.get() + "' , na = 'RID' , vval='' " +  "where user='" + uids.get() + "' and na = 'RID' ;"
		print("sq="+ sq)
		db.SQX(sq)
    finally:
		nop = -1
	#end
	# add to Rule
    sq = "insert into Rule values( '" + newstr.get() + "' , 'n' , 'n' );"
    try:
		print("sq="+ sq)
		db.SQX(sq)
    except:
		sq = "update Rule set RID= '" + newstr.get() + "' , cold='n' , ready='n' " +  "where RID='" + newstr.get() + "' ;"
		print("sq="+ sq)
		db.SQX(sq)
    finally:
		nop = -1
	#end

#paint
page = Tk()
#               wide,len
page.geometry('700x500+350+70')

ROW = 0
Label(page, text='Rule Selection Page').grid(row=ROW,column=1)
Button(page,text='Exit',command=BExit).grid(row=ROW,column=3)

ROW = 1
Label(page, text='uid').grid(row=ROW,column=1)
Label(page, text='Rule List').grid(row=ROW,column=2)
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
loadRule(BList)

ROW=4
Label(page, text='Limits').grid(row=ROW,column=1)
Button(page,text='SET',command=stump).grid(row=ROW,column=2)
newstr = StringVar()
newe = Entry(page, textvariable=newstr).grid(row=ROW,column=3)
Button(page,text='NEW',command=NewB).grid(row=ROW,column=4)

ROW=5
Button(page,text='Bundle>',command=stump).grid(row=ROW,column=1)
bstr = StringVar()
newb = Entry(page, textvariable=bstr).grid(row=ROW,column=2)
Button(page,text='<-',command=stump).grid(row=ROW,column=3)


ROW=6
Button(page,text='Test>',command=stump).grid(row=ROW,column=1)
tstr = StringVar()
newt = Entry(page, textvariable=tstr).grid(row=ROW,column=2)
Button(page,text='<-',command=stump).grid(row=ROW,column=3)

ROW=7
Button(page,text='Action>',command=stump).grid(row=ROW,column=1)
astr = StringVar()
newa = Entry(page, textvariable=astr).grid(row=ROW,column=2)
Button(page,text='<-',command=stump).grid(row=ROW,column=3)
page.mainloop()
