# file TestSelectionPage.py
"""
pja 02-13-2017 orig
pja 12-31-2017 added imports viz bundle entry

database
r --< r/t >--t
t (( tid ) v1type,op1,v2type,op2,v3type )
t --(v1type)--0< te >-- e
t --(v1type)--0< tl >-- litPool
tv1e (( tid ) eid )
tv1l (( tid ) vval )
litpool (( lid ))

screen
0+"Test Selection"+ -------- + scr. date+ -------- + (exit)  + --------- ++
1+ -------------- + "user"   + [user]   + -------- + ------- + (SAVE)    ++
2+ test list      + -------- + (By Rule)+ rule     + (<-)    +
3+ test list  ctd + -------- + (all)    +
4+ test list  ctd + -------- + (by Element) + element + (<-) +
5+ test list  ctd +
6+ test list  ctd +
7+ (select)       + v1[[[[[[ + op1[[[[[ + v1[[[[[[ + op1[[[[[ + v1[[[[[[ ++
8+ -------------- + type     + -------- + type     + -------  + type     ++
9+ (Element->)    +
10+ (Litteral->)   +
"""
# imports
from Tkinter import *
import ndsClass
gl = ndsClass.nds('gl')
import StrnumClass
cv = StrnumClass.strnum()
import SQClass
db = SQClass.SQC('berta')
# helping functions
# callback functions
def PExit():
    print('Page Exit')
    exit()
#end

#paint
page = tk()
#               wide,len
page.geometry('600x400+350+70')

ROW=0
"""
+"Test Selection"+ -------- + scr. date+ -------- + (exit)  + --------- ++
"""
Label(page, text='Test Selection').grid(row=ROW,column=0)
#Entry-2 =
""" uids = StringVar()
uid = Entry(page,textvariable=uids).grid(row=ROW,column=1)
"""
Button(page,text='Exit',command=PExit).grid(row=ROW,column=4)

ROW=1
"""
+ -------------- + "user"   + [user]   + -------- + ------- + (SAVE)    ++
"""
#Label-1
#Entry-2
#Button-5

ROW = 2
"""
2+ test list      + -------- + (By Rule)+ rule     + (<-)    +
"""
#Listbox-0 =
"""
BList = Listbox(page)
BList.grid(row=ROW,column=2)
BList.insert(END,'(none)')
"""
#Button-2 limitByRule()
#Entry-3 Rule
#Button-4 setRule()

ROW=3
"""
3+ test list  ctd + -------- + (all)    +
"""
#Button-2 limitAll()

ROW = 4
"""
4+ test list  ctd + -------- + (by Element) + element + (<-) +
"""
#Button-2 limitByElement()
#Entry-3 element
#Button-4 getElement

ROW = 7
"""
+ (select)       + v1[[[[[[ + op1[[[[[ + v1[[[[[[ + op1[[[[[ + v1[[[[[[ ++
"""
#Button-0 selectTlist()
#Entry-1 getV1()
#Entry-2 getOP1()
#Entry-3 getV2()
#Entry-4 getOP2()
#Entry-5 getV3()


ROW = 8
"""
+ -------------- + type     + -------- + type     + -------  + type     ++
"""
#Button-1 getV1Type()
#Button-3 getV2Type()
#Button-5 getV3Type()

ROW = 9
"""
+ (Element->)    +
"""
#Button-0 getElement()

ROW = 10
"""
+ (Litteral->)   +
"""
#Button-0 getLitPool()

