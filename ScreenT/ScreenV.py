m = """
file ScreenV.py
pja 02-24-2020 added scList, scList!
pja 02-18-2020

complies with object profile - see objectProfile.txt

sc0(p): # sc0 (screenName,,) opens screen
scLab(p): # scLab (ScreenName,LabelName,txt,row,col,,) inserts lable into window
scEntry(p): # scEntry (ScreenName,name,row,col,,) inserts entry field into window
scEntryX(p): # scEntryX (ScreenName,name,row,col,width,,) inserts extended entry field into window
scLoad(p) # sload (ScreenName,text,entryName,,) load text into entry fields 
scList(p) # scList (ScreenName,ListName,ROW,COL) creates listbox
scList!(p) # (ScreenName,ListName,text,,)
scReturns(p) # (ScreenName,,0[cv]) all values from screen
scGo(p): # scGo (,,) executes window



"""
"""
common 
    drb = p['sy']['pop']()
    p['sy']['push'](dra)
    p['sy']['push'](p['OK'])

"""


"""
#test as
import useLib
import bbox
bbox.main('bmain')
bbox.start()

push
obV
takeV
push
ScreenV
takeV
push
Screen1
sc0
push
Screen1
push
Lab1
push
hello
push
1
push
1
scLab
push
Screen1
push
Lab2
push
First Name
push
3
push
3
scLab
push
Screen1
push
FName
push
4
push
3
push
20
scEntryX




"""



global myp
myp = ''
def main(p):
    try:
        nop = p['object'].keys()
    except:
        print('please take obV first')
    finally:
        nop = -1
    #
    p['package']['ScreenV'] = ''
    p['help']['ScreenV'] = m
    p['sy']['sc0']= sc0 #(val,index,[],,[])
    p['help']['sc0']= "(oname,,) starts window"
    p['sy']['scLab']= scLab #(val,index,[],,[])
    p['help']['scLab']= "label (oname,labName,txt,ROW,COL,,)"
    p['sy']['scEntryX']= scEntryX #(val,index,[],,[])
    p['help']['scEntryX']= "entry box (oname, name,ROW,COL,W,,)"
    #scGo(oname,,)
    p['sy']['scList']= scList #(val,index,[],,[])
    p['help']['scList']= "creates listbox (oname,ListName,ROW,COL,,)"
    #scListBang(p)
    p['sy']['scList!']= scListBang #(val,index,[],,[])
    p['help']['scList!']= "(oname,ListName,text,,) adds text to list"
    p['sy']['scGo']= scGo #(val,index,[],,[])
    p['help']['scGo']= "executes window (oname,,)"
    #scReturns(p) # (oname,,0[cv])
    p['sy']['scReturns']= scReturns #(val,index,[],,[])
    p['help']['scReturns']= "(oname,,0[cv] returns all collected values"
    global myp
    myp = p
    return(p)
#
def onselect(evt):
    """
    Note here that Tkinter passes an event object to onselect()
    need to get p into this rtn
    """ 
    global myp
    p = myp
    w = evt.widget
    name = w.__str__()
    ListName = name[1:] # remove "."
    oname = p['object']['revcall'][ListName]
    print('ListName is ' + ListName )
    print('oname is ' + oname )
    index = int(w.curselection()[0])
    value = w.get(index)
    print 'You selected item %d: "%s"' % (index, value)
    # use named receiver
    p['object'][oname]['element'][ListName]['value'].set( value )
    
#

def scList(p):
	""" creates listbox (oname,ListName,ROW,COL,,) """
	COL = p['sy']['pop']()
	ROW = p['sy']['pop']()
	ListName = p['sy']['pop']()
	oname = p['sy']['pop']()
	p['object'][oname]['element'][ListName]={}
	p['object'][oname]['element'][ListName]['name'] = ListName
	p['object'][oname]['element'][ListName]['ListSet'] = p['object']['Tkinter'].StringVar()
	p['object'][oname]['element'][ListName]['value'] = p['object']['Tkinter'].StringVar()
	p['object'][oname]['return'].append(ListName)
	#call back
	p['object'][oname]['element'][ListName]['callback'] = onselect
	#set
	p['object']['revcall'][ListName] = oname
	p['object'][oname]['element'][ListName]['rcvr'] = p['object']['Tkinter'].Listbox(p['object'][oname]['call'],listvariable=p['object'][oname]['element'][ListName]['ListSet'],name=p['object'][oname]['element'][ListName]['name'])
	p['object'][oname]['element'][ListName]['rcvr'].grid( row=ROW,column=COL)
	#bind event
	#Lb1.bind('<<ListboxSelect>>', onselect)
	p['object'][oname]['element'][ListName]['rcvr'].bind( '<<ListboxSelect>>',p['object'][oname]['element'][ListName]['callback']) 
	p['sy']['push'](p['OK'])
#

def scListBang(p):
    """ (oname,ListName,text,,)"""
    txt = p['sy']['pop']()
    ListName = p['sy']['pop']()
    oname = p['sy']['pop']()
    p['object'][oname]['element'][ListName]['rcvr'].insert('end',txt)
    p['sy']['push'](p['OK'])
   
# 
def sc0(p) : # s0(oname,,)
	oname = p['sy']['pop']()
	import Tkinter
	p['object']['Tkinter'] = Tkinter
	p['object'][oname]={}
	p['object'][oname]['element'] = {}
	p['object'][oname]['return'] = []
	p['object'][oname]['call'] = p['object']['Tkinter'].Tk()
	p['object'][oname]['call'].title(oname)
	p['object'][oname]['call'].geometry('600x400+350+70')
	p['sy']['push'](p['OK'])
#


def scLab(p) : # scLab (oname,labName,txt,ROW,COL,,)
	COL = p['sy']['pop']()
	ROW = p['sy']['pop']()
	txt = p['sy']['pop']()
	labName = p['sy']['pop']()
	oname = p['sy']['pop']()
	## store
	p['object'][oname]['element'][labName]={}
	p['object'][oname]['element'][labName]['name'] = labName
	p['object'][oname]['element'][labName]['value'] = p['object']['Tkinter'].StringVar()
	p['object'][oname]['element'][labName]['value'].set(txt)
	## set
	#tt.Label(page, text=txt).grid(row=ROW,column=COL)
	p['object']['Tkinter'].Label(p['object'][oname]['call'], textvariable=p['object'][oname]['element'][labName]['value'],text=txt).grid(row=ROW,column=COL)
	p['object'][oname]['return'].append(labName)
	p['sy']['push'](p['OK'])
#


def scEntryX(p): #scEntryX (oname, name,ROW,COL,W)
	W = p['sy']['pop']()
	COL = p['sy']['pop']()
	ROW = p['sy']['pop']()
	name = p['sy']['pop']()
	oname = p['sy']['pop']()

	# tt.Entry(page,textvariable=TV, width = W ).grid(row=ROW,column=COL)
	##store
	p['object'][oname]['element'][name]={}
	p['object'][oname]['element'][name]['name'] = name
	p['object'][oname]['element'][name]['value'] = p['object']['Tkinter'].StringVar()
	##set
	p['object'] ['Tkinter'].Entry( p['object'][oname]['call'], textvariable=p['object'][oname]['element'][name]['value'], width = W ).grid(row=ROW,column=COL)
	p['object'][oname]['return'].append(name)
	p['sy']['push'](p['OK'])
#


def scGo(p): #scGo(oname,,)
    oname = p['sy']['pop']()
    p['object'][oname]['call'].mainloop()
    p['sy']['push'](p['OK'])
#
def scReturns(p):
    # push returns in cv
    oname = p['sy']['pop']()
    #push chr(0)
    p['sy']['push'](chr(0))
    for x in range(p['object'][oname]['return'].__len__()):
        name = p['object'][oname]['return'][x]
        p['sy']['push'] ( p['object'][oname]['element'][name]['value'].get() )
        p['sy']['push'](p['object'][oname]['return'][x])
        

        #into p['object'][oname]['element'][name]['value']
    #
    p['sy']['push'](p['OK'])

# 







 