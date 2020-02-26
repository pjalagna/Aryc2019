m = """
file ScreenV.py
pja 02-18-2020

complies with object profile - see objectProfile.txt

sc0(p): # sc0 (,,) opens screen
scL(p): # scL (txt,row,col,,) inserts lable into window
scE(p): # scE (name,txt,row,col,,) inserts entry field into window
scEx(p): # scEx (name,txt,row,col,width,,) inserts extended entry field into window
scLoad(p) # sload (text,entryName,,) load text into entry fields 
scGo(p): # scGo (,,) executes window
## on exit of window (,,0,[val,element-name]) from screen

scList(p) # scList (name,ROW,COL) creates listbox
scListItem(p) # (item,listname,,) adds item to listbox

"""
"""
    drb = p['sy']['pop']()
    dra.update(drb)
    p['sy']['push'](dra)
    p['sy']['push'](p['OK'])


"""


## on exit of window (,,0,[val,field-name]) from screen


#tt? tt = Tkinter == p['object']['Tkinter']
#page? tt.Tk() == p['object'][oname]['call']

"""
#test as
import ScreenV
p = {}
p = ScreenV.init()
p = ScreenV.main(p)
p
ScreenV.push(p,'sc1')
ScreenV.sc0(p)
print(1)

ScreenV.push(p,'sc1')
ScreenV.push(p,'lab1')
ScreenV.push(p,'test text')
ScreenV.push(p,'5')
ScreenV.push(p,'5')
ScreenV.scLab(p)
print(2)

ScreenV.push(p,'sc1')
ScreenV.push(p,'en1')
ScreenV.push(p,'6')
ScreenV.push(p,'5')
ScreenV.push(p,'20')
ScreenV.scEntryX(p)
print(3)


"""
def init(): 
    p = {}
    p['sy']={}
    p['dat'] =[]
    p['sy']['push'] = push
    p['sy']['pop'] = pop
    return(p)
#

def push(p,item):
    p['dat'].append(item)
#


def pop(p):
    return(p['dat'].pop())
#




def main(p):
    p['object'] = {}
    return(p)
#
def sc0(p) : # s0(oname,,)
	oname = p['sy']['pop'](p)
	import Tkinter
	p['object']['Tkinter'] = Tkinter
	p['object'][oname]={}
	p['object'][oname]['element'] = {}
	p['object'][oname]['call'] = p['object']['Tkinter'].Tk()
	p['object'][oname]['call'].title(oname)
	p['object'][oname]['call'].geometry('600x400+350+70')
#


def scLab(p) : # scLab (oname,labName,txt,ROW,COL,,)
	COL = p['sy']['pop'](p)
	ROW = p['sy']['pop'](p)
	txt = p['sy']['pop'](p)
	labName = p['sy']['pop'](p)
	oname = p['sy']['pop'](p)
	## store
	p['object'][oname]['element'][labName]={}
	p['object'][oname]['element'][labName]['name'] = labName
	p['object'][oname]['element'][labName]['value'] = p['object']['Tkinter'].StringVar()
	p['object'][oname]['element'][labName]['value'].set(txt)
	## set
	#tt.Label(page, text=txt).grid(row=ROW,column=COL)
	p['object']['Tkinter'].Label(p['object'][oname]['call'], textvariable=p['object'][oname]['element'][labName]['value'],text=txt).grid(row=ROW,column=COL)
#


def scEntryX(p): #scEntryX (oname, name,ROW,COL,W)
	W = p['sy']['pop'](p)
	COL = p['sy']['pop'](p)
	ROW = p['sy']['pop'](p)
	name = p['sy']['pop'](p)
	oname = p['sy']['pop'](p)

	# tt.Entry(page,textvariable=TV, width = W ).grid(row=ROW,column=COL)
	##store
	p['object'][oname]['element'][name]={}
	p['object'][oname]['element'][name]['name'] = name
	p['object'][oname]['element'][name]['value'] = p['object']['Tkinter'].StringVar()
	##set
	p['object'] ['Tkinter'].Entry( p['object'][oname]['call'], textvariable=p['object'][oname]['element'][name]['value'], width = W ).grid(row=ROW,column=COL)
#


def scGo(p): #scGo(oname,,)
    oname = p['sy']['pop']
    p['object'][oname]['call'].mainloop()
#


# p['object'][oname]['element'][name]['value'].get() #element

#ScList(oname,listName,ROW,COL)
##store
### rcvr text box at row col
### rcvr routine
### button at row+1 col
### listbox at row+2 col
##set
### rcvr text box at row col
### button at row+1 col
### listbox at row+2 col









 