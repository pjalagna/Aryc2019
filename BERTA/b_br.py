# file b-br.py
""" disp for bundles the rules
pja 02-06-2017 
pja 02-04-2017 org
-- 
"""
# imports
from Tkinter import *
import ndsClass
gl = ndsClass.nds('gl')
import StrnumClass
cv = StrnumClass.strnum()
import SQClass
db = SQClass.SQC('berta')

# nds globals
RuleAR = {}
ROW = 0
gl.bang('RuleAR' , RuleAR)
gl.bang('ROW',ROW)

# support functions
def loadBundle(box):
    # stump - load from database
    ab = db.SQReadAll('select * from bundle;') # bid,cold,ready
    abmax = ab.__len__() 
    for j in range( 0 , abmax):
        bid = ab.__getitem__(0)
        box.insert(END,bid)
    #end for
#end def


#callbacks
def CallSelect():
    print('CallSelect')
    RuleAR = gl.att('RuleAR')
    ROW = cv.str2int(gl.att('ROW'))
    
    
    
    # rule load
    ## get bundle name
    bn = blist.curselection()
    bna = blist.get(bn[0])
    ## get list from database
    ### per list gen rule row
    ROW = ROW + 1
    gl.bang('ROW',ROW)
    ### drop button
    RuleAR['D'+ cv.num2str(ROW)] = Button(page,text='Drop Rule')
    RuleAR['D'+ cv.num2str(ROW)].grid(row=ROW, column=1)
    ### rule name
    RuleAR['S'+ cv.num2str(ROW)] = "i am rule of " + bna 
    # ruleName paint
    RuleAR['R'+ cv.num2str(ROW)] = Label(page, text=RuleAR['S'+ cv.num2str(ROW)])
    RuleAR['R'+ cv.num2str(ROW)].grid(row=ROW, column=2)
    ### rule link
    ####
    ## save array
    gl.bang("RuleAR",RuleAR)
# end CallSelect

def CallLoadCold():
    print('CallLoadCold')
    print(blist.curselection())
# end CallLoadCold

def CallLoadReady():
    print('CallLoadReady')
# end CallLoadReady

def CallLoadAll():
    print('CallLoadAll')
# end CallLoadAll

#paint
page = Tk()
page.geometry('400x400+350+70')
ROW = 0
Label(page, text='Bundle').grid(row=ROW,column=1)
blist = Listbox(page)
blist.grid(row=ROW,column=2)
# load bundle names
loadBundle(blist)
bSelect = Button(page, text='Select' , command=CallSelect)
bSelect.grid(row=ROW, column=4)
bLoadCold = Button(page, text='Load Cold' , command=CallLoadCold)
bLoadCold.grid(row=ROW, column=6)
bLoadReady = Button(page, text='Load Ready' , command=CallLoadReady)
bLoadReady.grid(row=ROW, column=8)
bLoadAll = Button(page, text='Load All' , command=CallLoadAll)
bLoadAll.grid(row=ROW, column=10)

page.mainloop()



   
   
   
