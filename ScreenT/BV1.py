#!/usr/bin/python
m = """file BV1.py
pja 02-14-2020 split into rtns
review and edits
# pja 02-07-2017 orig from html

# test as
def dood():
    import BV1
    d = BV1
    d.BVmain()
    d.slab("Smack",1,1)
    d.entry("smack",2,1)
    d.sload("wink",1)
    d.slab("Fname",3,5)
    d.entryX("Fname",4,5,100)
    d.sload("Paul",3)
    d.entry("more",5,5)
    # grab button
    d.butt('grab',7,1)
    # exit button
    d.slab("exit (red button) to exit",9,5)
    d.Listb('butter',6,3)
    mx = d.sgo()
    j = mx.__len__()
    x = 0
    ans = []
    ans.append(d.gettt())
    ans.append(d.vars)
    return(ans)
#

rr = dood()

    while (x < j):
        print(mx[x])
        print(mx[x+1].get())
        x = x+2
    #wend
print(mx)
d.fillList('hello',5)
# imports
"""
def BVmain():
    global tt,gl,cv,db,vars,page
    import Tkinter 
    tt = Tkinter
    import ndsClass
    gl = ndsClass.nds('gl')
    import StrnumClass
    cv = StrnumClass.strnum()
    import SQClass
    db = SQClass.SQC('berta')
    vars = []
    page = tt.Tk()
    page.geometry('600x400+350+70') # wdt,leng+?+?
#

# support functions

def LoadUID(uid,uids):
    print('load uid')
    uids.set("PJA")
# end
def LoadSDate(SDate,SDates):
    print('load SDate')
    SDates.set ('12/12/1212')
#end 
def gettt():
    return(tt)
#
def sload(txt,ix):
    global tt,gl,cv,db,vars,page
    vars[ix].set(txt)
# callback functions
"""def BExit():
    print('BExit')
    return()
#end"""
def BSet():
    print ('BSet')
    print(dir(vars[0]))
    print("count vars" + vars.__len__().__str__())
    #print(uids.__str__() + '-' + uids.get())
    ##print(vars[0].__str__() + '-' + vars[1].get())
    ##print(vars[2].__str__() + '-' + vars[3].get())
    ##print(vars[4].__str__() + '-' + vars[5].get())
    #print(SDates.__str__() + '-' + SDates.get())
nop = -1
#end

def s1():
    global tt,gl,cv,db,vars,page   
	#paint
    page = tt.Tk()
    page.geometry('600x400+350+70') # wdt,leng+?+?
#

def slab(txt,ROW,COL):
    global tt,gl,cv,db,vars,page
    tt.Label(page, text=txt).grid(row=ROW,column=COL)
#
def buex(txt,ROW,COL):
    global tt,gl,cv,db,vars,page
    tt.Button(page, text=txt, command=BExit ).grid( row=ROW, column=COL)
#
def butt(txt,ROW,COL):
    global tt,gl,cv,db,vars,page
    tt.Button (page, text=txt, command=BSet).grid( row=ROW, column=COL)
#
def sav1():
	ROW = 1
	Label(page, text='uid').grid(row=ROW,column=1)
	Label(page, text='Bundle List').grid(row=ROW,column=2)
	Label(page, text='Screen Date').grid(row=ROW,column=3)

	ROW=2
#
def entry(name,ROW,COL):
    global tt,gl,cv,db,vars,page
    vars.append( name )
    vars.append( tt.StringVar() )
    uid = tt.Entry(page,textvariable=vars[len(vars)-1]).grid(row=ROW,column=COL)
#
def entryX(name,ROW,COL,W):
    global tt,gl,cv,db,vars,page
    vars.append( name )
    vars.append( tt.StringVar() )
    uid = tt.Entry(page,textvariable=vars[len(vars)-1], width = W ).grid(row=ROW,column=COL)
    
#
def Listb(name,ROW,COL):
    """
    may need a profile in vars for this
    wanted to add to height on insert
    might even adjust width to strlen
    """
    global tt,gl,cv,db,vars,page
    vars.append( name )
    vars.append( tt.StringVar() )
    uid = tt.Listbox(page, height=1, width=20).grid(row=ROW,column=COL)
    
#
"""def fillList(item,index):
    global tt,gl,cv,db,vars,page
    vars[index].insert(END, item)
#"""

def set(vix,txt):
    LoadUID(uid,vars[len(vars)-1])
#
def sav3():
	vars.append( StringVar() )
	SDate = Entry(page, textvariable=vars[len(vars)-1]).grid(row=ROW,column=3)
	LoadSDate(SDate, vars[len(vars)-1])

	ROW=3
	BList = Listbox(page)
	BList.grid(row=ROW,column=2)
	BList.insert(END,'(none)')
	# loadBundle(BList)

	ROW=4
	
def sgo():
    global tt,gl,cv,db,vars,page
    page.mainloop()
    print('after loop')
    return(vars)
#
