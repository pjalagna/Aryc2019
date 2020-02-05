"""
file arV.py
pja 01-31-2020 added drvx verb 
pja 01-26-2020
array functions for basii




"""
def main(p):
    p['sy']['ar!']= arBang #(val,index,[],,[])
    p['help']['ar!']= "arBang #(val,index,[],,[])"
    p['sy']['ar@']= arAt #(index,[],,val)
    p['help']['ar@']= "arAt #(index,[],,val)"
    p['sy']['ar0']= arZ #(,,[])
    p['help']['ar0']= "arZ #(,,[])"
    p['sy']['ar#'] = arSharp # - depth of array ([],,#)
    p['help']['ar#'] = "arSharp # - depth of array ([],,#)"
    p['sy']['dr!']= drBang #(val,name,{},,{})
    p['help']['dr!']= "drBang #(val,name,{},,{})"
    p['sy']['dr@']= drAt #(name,{},,val)
    p['help']['dr@']= "drAt #(name,{},,val)"
    p['sy']['dr0']= drZ #(,,{})
    p['help']['dr0']= "drZ #(,,{})"
    p['sy']['dr#'] = arSharp # depth of array ({},,#)
    p['help']['dr#'] = "arSharp # depth of array ({},,#)"
    p['sy']['drK'] = drKeys # ({},[keys])
    p['help']['drK'] = " ({},[keys]) "
    p['sy']['dr?'] = drHook # ({},[keys])
    p['help']['dr?'] = "(t,{},,{ans}) {}[t] subset if ok else blank "
    p['sy']['dr+'] = drPlus # ({},[keys])
    p['help']['dr?'] = "({b},{a},,) updates dr{a} with {b} "
    p['sy']['drvx'] = drvx 
    p['help']['drvx'] = "(ch0,val,[names],array,,) for multi depth arrays max depth 6 "
    return(p)
#end main
def drvx(p):
    j = []
    # pop till cho
    j.append(p['sy']['pop']())
    while (j[len(j)-1] != chr(0)):
        j.append(p['sy']['pop']())
    #wend
    print('lenj -' + len(j).__str__())
    m = j[0] # the array
    if (len(j)==4): #(ar,na,v,0)
        m[j[1]] = j[2]
    elif (len(j)==5): #(ar,na1,na2,v)
        try:
            px = m[j[1]]
        except:
            m[j[1]]={}
        finally:
            nop = 1
        #end try
        m[j[1]][j[2]] = j[3]
    elif (len(j)==6): #(ar,na1,na2,na3,v,0)
        try:
            px = m[j[1]]
        except:
            m[j[1]]={}
        finally:
            nop = 1
        #end try
        try:
            px = m[j[1]][j[2]]
        except:
            m[j[1]][j[2]]={}
        finally:
            nop = 1
        #end try
        m[j[1]][j[2]][j[3]]= j[4]
    elif (len(j)==7): #(ar,na1,na2,na3,na4,v,0)
        try:
            px = m[j[1]]
        except:
            m[j[1]]={}
        finally:
            nop = 1
        #end try
        try:
            px = m[j[1]][j[2]]
        except:
            m[j[1]][j[2]]={}
        finally:
            nop = 1
        #end try
        try:
            px = m[j[1]][j[2]][j[3]]
        except:
            m[j[1]][j[2]][j[3]]={}
        finally:
            nop = 1
        #end try
        m[j[1]][j[2]][j[3]][j[4]] = j[5]
    else:
        m = {}
    #endif
    nop = 1
    p['sy']['push'](m)
    p['sy']['push'](p['OK']) 
#end drvx 
 
def drPlus(p):
    dra = p['sy']['pop']()
    drb = p['sy']['pop']()
    dra.update(drb)
    p['sy']['push'](dra)
    p['sy']['push'](p['OK'])
#end dr+
def drHook(p):
    dr = p['sy']['pop']()
    t = p['sy']['pop']()
    try:
        ans = dr[t]
        p['sy']['push'](ans)
        p['sy']['push'](p['OK'])
    except:
        p['sy']['push'](p['NOK'])
    finally:
        nop = 1
    #end try
#end dr?
def arZ(p):
    p['sy']['push']([])
    p['sy']['push'](p['OK'])
#end arZ
def drZ(p):
    p['sy']['push']({})
    p['sy']['push'](p['OK'])
#end drZ
def arBang(p): #(val,index,[],,[])
    ar = p['sy']['pop']()
    index = int(p['sy']['pop']())
    vval = p['sy']['pop']()
    ar.append('')
    ar[index] = vval
    p['sy']['push'](ar)
    p['sy']['push'](p['OK'])
#end arBang
def drBang(p): #(val,name,{},,{})
    ar = p['sy']['pop']()
    name = p['sy']['pop']()
    vval = p['sy']['pop']()
    ar[name] = vval
    p['sy']['push'](ar)
    p['sy']['push'](p['OK'])
#end drBang
def arAt(p): #(index,[],,val)
    ar = p['sy']['pop']()
    index = int(p['sy']['pop']())
    m = ar[index]
    p['sy']['push'](m)
    p['sy']['push'](p['OK'])
#end arAt
def drAt(p): #(name,{},,val)
    ar = p['sy']['pop']()
    name = p['sy']['pop']()
    m = ar[name]
    p['sy']['push'](m)
    p['sy']['push'](p['OK'])
#end drAt
def arSharp(p): 
    ar = p['sy']['pop']()
    m = ar.__len__()
    p['sy']['push'](m)
    p['sy']['push'](p['OK'])
#end arSharp
def drKeys(p): # keys of array ({},[keys]) m.keys()
    ar = p['sy']['pop']()
    m = ar.keys()
    p['sy']['push'](m)
    p['sy']['push'](p['OK'])
#end drKeys
    
    
