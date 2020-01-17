"""
file slV.py
pja 01-10-2020
N- add help
use with takeV verb in basii
introduces a list process for basii - (s)ingle (l)ist

test with bbox "slV" takeV
"""
def main(p):
    p['sl'] = {}
    # verbs
    p['sy']['.SL'] = dotSL
    p['sy']['.SLD'] = dotSLD
    p['sy']['.SLLD'] = dotSLLD
    p['sy']['SLInit']= SLInit
    p['sy']['SLAdd'] = SLAdd
    p['sy']['SLRead'] = SLRead
    p['sy']['.SLL'] = dotSLL
    return(p)
#end main
def dotSL(p):
    #.SL p['sl'].keys()
    ans = p['sl'].keys()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end dotSL
def dotSLD(p):
    ans = p['sl'].__len__()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end dotSLD 
def dotSLLD(p):
    #.SLLD p['sl']['fox'].__len__() 
    p1 = p['sy']['pop']()
    ans = p['sl'][p1].__len__()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end dotSLLD
def SLInit(p):
    # (name,,) pl['sl'][name] =[]
    p1 = p['sy']['pop']()
    p['sl'][p1] = []
    p['sy']['push'](p['OK'])
#end SLInit 
def SLAdd(p):
    #add (v,name,,) p['sl'][name].append( v )
    name = p['sy']['pop']()
    v = p['sy']['pop']()
    p['sl'][name].append( v )
    p['sy']['push'](p['OK'])
#end SLAdd
def SLRead(p):
    #read (k,name,,val) push( p['sl'][name][k] )
    name = p['sy']['pop']()
    k = p['sy']['pop']()
    # prepare k by type
    tt = SLtype(p,name)
    if (tt=='list'):
        k = int(k)
    #endif
    ans = p['sl'][name][k]
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end SLRead
def dotSLL(p):
    #.SLL (name,,keys/null) on type keys for dict OR Null
    name = p['sy']['pop']()
    tt = SLtype(p,name)
    if (tt=='list'):
        ans = "null"
    else:
        ans = p['sl'][name].keys()
    #endif
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end dotSLL
def SLtype(p,name):
    #not callable not on symbol table
    a = p['sl'][name].__class__
    aa = a.__str__(a)
    aaa = aa.replace("<type '","")
    aaa = aaa.replace("'>",'')
    return(aaa)
#end SLtype
