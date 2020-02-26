m = """
file scV.py
uses BV1.py
adds screen tkinter to basii
sc0(p): # sc0 (,,) opens screen
scL(p): # scL (txt,row,col,,) inserts lable into window
scE(p): # scE (name,txt,row,col,,) inserts entry field into window
scEx(p): # scEx (name,txt,row,col,width,,) inserts extended entry field into window
sload(p) # sload (text,index,,) load text into entry fields 
scGo(p): # scGo (,,) executes window
## on exit of window (,,0,[val,field-name]) from screen

"""
"""
    drb = p['sy']['pop']()
    dra.update(drb)
    p['sy']['push'](dra)
    p['sy']['push'](p['OK'])


"""
def main(p,m=m):
    p['package']['screen'] = ''
    p['help']['screen'] = m
    p['sy']['sc0']= sc0 
    p['help']['sc0']= "sc0 (,,) opens screen" 
    p['sy']['sload']= sload 
    p['help']['sload']= "(text,index,,) load text into entry fields "
    p['sy']['scL']= scL 
    p['help']['scL']= "scL (txt,row,col,,) inserts lable into window"
    p['sy']['scE']= scE 
    p['help']['scE']= "scE (name,txt,row,col,,) inserts entry field into window "
    #entryX
    p['sy']['scEx']= scEx 
    p['help']['scEx']= "scE (name,txt,row,col,width,,) inserts extended entry field into window "
    p['sy']['scGo']= scGo 
    p['help']['scGo']= "scGo (,,) executes window"
    return(p)
#
def sload(p): # sload (text,index,,) load text into entry fields 
    ix = int(p['sy']['pop']())
    txt = p['sy']['pop']()
    p['sy']['BVC'].sload(txt,ix)
    p['sy']['push'](p['OK'])
#
def scEx(p):
    W = p['sy']['pop']()
    COL = p['sy']['pop']()
    ROW = p['sy']['pop']()
    name = p['sy']['pop']()
    p['sy']['BVC'].entryX(name,ROW,COL,W)
    p['sy']['push'](p['OK'])
#
def sc0(p): # sc0 (,,) opens screen
    import BV1
    p['sy']['BVC'] = BV1
    p['sy']['BVC'].BVmain()
    p['sy']['push'](p['OK'])
#
 
def scL(p): # scL (txt,row,col,,) inserts lable into window
    COL = p['sy']['pop']()
    ROW = p['sy']['pop']()
    txt = p['sy']['pop']()
    p['sy']['BVC'].slab(txt,ROW,COL)
    p['sy']['push'](p['OK'])
#
def scE(p): # scE (name,txt,row,col,,) inserts entry field into window
    COL = p['sy']['pop']()
    ROW = p['sy']['pop']()
    name = p['sy']['pop']()
    p['sy']['BVC'].entry(name,ROW,COL)
    p['sy']['push'](p['OK'])
#
def scGo(p): # scGo (,,ch0,[val,name]) executes window
    mx = p['sy']['BVC'].sgo()
    print('on exit')
    j = mx.__len__()
    x = 0
    p['sy']['push'](chr(0))
    while (x < j): # push in cv0 format
        p['sy']['push'](mx[x+1].get()) # value
        p['sy']['push'](mx[x]) #name
        x = x+2
    #wend
    p['sy']['push'](p['OK'])
#

## on exit of window (,,0,[val,field-name]) from screen


 