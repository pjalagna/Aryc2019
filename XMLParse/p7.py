dd = """<me>
<a1>text<bold><center>here</center></bold>more</a1>
</me>"""


def xInit():
    global s
    fn = raw_input('parse file name? ')
    import fioiClass
    s = fioiClass.fio(fn)
    s.fioxSet(0)
    parentInit()
    parentPlus('')
    attrInit()
    spoInit()
#

def x1():
    global s,m
    ax = 1
    while (ax == 1):
        print('[[ 1 ]] x1' )
        s.fwhite() 
        m=s.f2tkn('>',1)
        print('x1 m=(' + m.__str__() + ')')
        x2()
        ax = raw_input('x1 after x2 0/1' )
    #wend
#x1
    
    
def x2 ():
    global m
    if (m[0][1] == "?"):
        status = 'ok'
    elif (m[0][1] == "!"):
        status = 'ok'
    else:
        x3()
        raw_input('x2 after x3 0/1 ' )
    #
#x2


def x3():
    global m,hs
    try:
        hs = m[0].index(' ')
    except:
        hs = -1
    finally:
        nop = 1
    #
    try:
        es = m[0].index('/',len(m[0])-2)
    except:
        es = -1
    finally:
        nop = 1
    #
    bs = -1
    if (m[0][1]== '/'):
        bs = 1
    #
    ctx=0
    if (hs <> -1):
        ctx = ctx +1
    #
    if (es <> -1):
        ctx = ctx +2
    #
    if (bs <> -1):
        ctx = ctx +4
    #
    print('ctx=(' + ctx.__str__() + ")")
    if (ctx == 0): # <na>
        na = m[0][1:len(m[0])-1]
        parentPlus(na)
        spoPlus(parent[len(parent)-2],'child',na)
        spoPlus(na,'parent',parent[len(parent)-2])
    elif (ctx == 1): # sp no </ or />
        na = m[0][1:hs]
        attrInit()
        attrPlus('en',na)
        getattr(m[0])
        processAttr()
    else:
        print('ctx=(' + ctx.__str__() + ')')
        raw_input("??")
    #endif ctx
#
    
    
    
def getattr(ma):
    global hs
    # clip
    hs2 = 0
    atts = ma[hs:len(m[0])-1]
    atts = atts.lstrip()
    bsw = 0
    while(bsw==0):
        try:
            hs2 = atts.index(' ',hs2+1)
        except:
            hs2 = len(atts)
            bsw = 1
        finally:
            nop = 1
        #
        em = atts.index('=')
        atna = atts[0:em]
        atval = atts[em+2:hs2-1]
        attrPlus(atna,atval)
        atts = atts[hs2:]
        atts = atts.lstrip()
    #wend     
#end getattr

def processAttr():
    global attr,parent
    if (attr['en']=='element'):
        parentPlus(attr['name'] + ":" + attr['id'])
        #parent spo
        nax = attr['name'] + ":" + attr['id']
        spoPlus(parent[len(parent)-2],'child',nax)
        spoPlus(nax,'parent',parent[len(parent)-2])
        # att spo
        for mk in attr:
            spoPlus(nax,'attr',"(" + mk + '=' + attr[mk] + ")")
        #endfor
    else:
        raw_input('processAttr stop')
    #endif
#
    


# support 


def parentInit():
    global parent
    parent = []
#


def parentPlus(strin):
    global parent
    print('parentPlus added (' + strin + ")")
    parent.append(strin)
#


def attrInit():
    global attr
    attr = {}
#


def attrPlus(atna,atval):
    global attr
    print('attrPlus added ' + atna + '[' + atval +']')
    attr[atna] = atval
#

def spoInit():
    global SPO,Thing,pred
    SPO = {} # [subj][has][obj]
    Thing = {}
    pred = {}
#


def spoPlus(sub,predi,obj):
    global SPO,Thing,pred
    #does subject exist?
    print('spoPlus added ' + 'sub=(' + sub + ')')
    print('              ' + 'pred=(' + predi + ')')
    print('              ' + 'obj=(' + obj + ')')
    try:
        tx = SPO[sub]
    except:
        SPO[sub] = {}
        Thing[sub] = ''
    finally:
        nop =1
    #
    #does spo[subject][pred] exist?
    try:
        tx = SPO[sub][predi]
    except:
        SPO[sub][predi] = {}
        pred[predi] = ''
    finally:
        nop =1
    #
    #does spo[subject][pred][obj] exist?
    try:
        tx = SPO[sub][predi][obj]
    except:
        SPO[sub][predi][obj] = ''
        Thing[obj] = ''
    finally:
        nop =1
    #    
#spoPlus 

   