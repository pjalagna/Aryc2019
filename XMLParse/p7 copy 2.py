"""
file p7.py xsd/xml parse
pja 5/7/2020 p7.main return spo
pja 5/5/2020 rewrite
pja 5/4/2020 added spo structures
pja 5/3/2020

import useLib
import p7
box = p7.main()

1-get < to > to r1 ; pu++ 
if eof?
--y => -22
--n first 2 rx fan
--<? => 1
--<! => 1
--</ => 4
--other  => 5

4
getname[1:-1] 
=sequence?
--y sequenceMode=0 popParent popPU 
elementHold='',elementHoldPU=''
=> 1
=choice?
--y chooseMode=0 popParent popPU 
elementHold='',elementHoldPU=''
=> 1
--n popParent popPU => 1

5
has space - has = as d60
00 <x> getname[1:-1] to cnx 
-- pushParent(cnx) => 100
01 er -200
10 er -200
11 getnaSP pushParent pushPU => 100

100 
--if tag = element 
--- getattr  get2< 
--- KRI
--- sequenceMode=1? or choiceMode=1
----y seq++ attr=seq attr-hold 
-----spo => 1000
----n spo => 1000

-if tag = complexType 
-- attr=holdParent attr=holdPU  
-- if d60=00 => 1000
-- if d60=11 getattr  get< 
-- KRI spo => 1000

-if tag = sequence 
-- attr=holdParent attr=holdPU 
-- seq=1 
-- sequenceMode=1
-- if d60=00 => 1000
-- if 11 getattr  get< KRI spo => 1000

- if tag = choice
-- attr=holdParent attr=holdPU 
-- seq=1 
-- ChooseMode=1

-- if d60=00 => 1000
-- if 11 getattr  get< KRI spo => 1000

-if tag= other
-- getattr  get2< KRI
-- spo => 1000

1000 last 2 l2x
---/> popParent popPU => 1
----*> => 1


((first,KRI)) => kri
((NAME,<atn>)) => kri
((NAME,<atv>) => kri
((parentKRI,<pki> ))=> kri
((pickup,<#>)) => kri
((ATN,<(atn=atv)> => kri
((ATV,<(atv=atn)> => kri
((kri) ATN)) => <(atn=atv)> 
((kri) ATV) <(atv=atn)> ))
((kri) parentKRI ) pki ))
((kri) FILE ) filename ))
((kri,<atn>)) => <atv>

notes
need 6 point array for snowflake database (see SnowflakeDatabase.txt)
segments
ATN atn atv
ATV atv atn
KRI kri
UID value ** no dups

PARENTCNX pcnx CHILDCNX cnx
CNX,cnx,'parentCNX' pcnx
PARENTKRI parentkri KRI:SEQ kri seq
PARENTKRI parentkri KRI:PEER kri peer
FIRST kri
KRICONCORDIA pkri chain:: ** no dups for every pkri in chain




notes
(X) uri:name process on element,sequence,choice,complexType
(X)follow parentKRI
(X)trim cnx,atn,atv
(X) cnxftsw spo('first',"KRI",kri)
(X)on complexType add hold parentPU in elementHoldPU
(X) seq numbers on sequence or xsd:sequence


"""
import spoRtns
spoPlus = spoRtns.spoPlus
getspo = spoRtns.getspo
spoInit = spoRtns.spoInit
import SnowflakeRtns
global snowflakeRtns
snowflakeRtns = SnowflakeRtns

def main():
    xInit()
    global ctl
    ctl = 1
    while (0 < ctl):
        print("ctl=(" + ctl.__str__() + ")")
        if (ctl == 1):
            ctl = ctl1()
        elif (ctl == 4):
            ctl = ctl4()
        elif (ctl == 5):
            ctl = ctl5()
        elif (ctl == 100):
            ctl = ctl100()
        elif (ctl == 1000):
            ctl = ctl1000()
        else:
            raw_input('unknown ctl('+ctl.__str__() + ')')
            ctl = 0
        #endif
    #wend
    return(getspo(),snowflakeRtns.getProAr())
#
def xInit():
    global s,pu,fsz,ftsw,cnxftsw,sequenceMode,chooseMode,elementHold,elementHoldPU,seq,snowflakeRtns,parentPU
    snowflakeRtns.ProfileInit()
    seq = 0
    elementHold=0
    elementHoldPU = 0
    sequenceMode = 0
    chooseMode = 0
    fn = raw_input('xsd file name? ')
    import fioiClass
    s = fioiClass.fio(fn)
    #filesize to fsz
    import os
    ffn = os.getcwd() + '/' + s.fh.name
    fsz = os.path.getsize(ffn)
    cnxftsw = 0 # ftsw for first kri
    pu = 0
    s.fioxSet(0)
    parentInit()
    parentPlus('')
    parentPU.append(0)
    attrInit()
    ftsw=0
    spoInit()
    parentKRI = ''
#
def rets():
    global s
    return(s)
#

def ctl1():
    #trim to <rx--> fan on rx
    global s,m,r0,r1,rx,pu,l2x,fsz,ftsw,parent,attr
    attr = {} #blank 
    r1 = ''
    r0 = ''
    df = s.fioxGet()
    print("ctl1 iox=(" + df.__str__() + ")")
    print('status sequenceMode=(' + sequenceMode.__str__() + ')')
    print('status chooseMode=(' + chooseMode.__str__() + ')')
    print('dump parent')
    print(parent)
    print('end dump parent\n')
    if (fsz <= s.fioxGet()):
       ctl = -100
    else:
        s.fwhite()
        m=s.f2tkn('>',1)
        pu = pu +1
        attr['pickup'] = pu.__str__()
        r0 = m[0]
        print("ctl1 r0=(" + r0.__str__() + ")")
        l2x = r0[-2:] # last 2
        print(r0.__str__())
        try:
            rx = m[0][1]
            #rxFan(rx)
            if (1 == 0):
                nop =0
            elif(rx=="?"):
                ctl = 1
            elif(rx=="!"):
                ctl = 1
            elif(rx=="/"):
                ctl = 4
            else:
                ctl = 5
            #endif
        except:
            ctl = -22
        finally:
            nop = 1
        #endtry
    #endif
    return(ctl)
#ctl1

def ctl4(): # </name>
    global r0,parent,parentPU,sequenceMode,chooseMode
    name = r0[2:-1] #</name>
    name = name.rstrip(' \t\r\n')
    name = name.lstrip(' \t\r\n')
    #strip xmlns
    d4 = name.find(':')
    if (d4 == -1):
        nop = 1 
    else:
        name = r0[2:d4]
    #endif
    if (name.upper() == "SEQUENCE"):
        sequenceMode = 0
        seq = 0
        parent.pop()
        parentPU.pop()
        ctl = 1
    elif (name.upper() == "CHOICE"):
        chooseMode = 0
        seq = 0
        parent.pop()
        parentPU.pop()
        ctl = 1
    else:
        parent.pop()
        parentPU.pop()
        ctl = 1
    #endif
    return(ctl)
#end ctl4


def ctl5(): #<name{atr}|/>,>
    global r0,d60,cnx,parent,parentPU,attr,r1
    d60 = 0
    a1 = r0.find(' ')
    if (a1 <> -1):
        d60 = d60 +1
    #
    a2 = r0.find('=')
    if (a2 <> -1):
        d60 = d60 +2
    #
    if (d60 ==0):
        cnx = r0[1:-1]
        parent.append(cnx)
        parentPU.append(pu)
        attr['cnx'] = cnx
        ctl = 100
    elif (d60 ==3):
        cnx = r0[1:a1]
        r1 = r0[a1:]
        parent.append(cnx)
        attr['cnx'] = cnx
        parentPU.append(pu)
        ctl = 100
    else:
        raw_input('ctl1 error d60=' + d60.__str__() + '=')
        ctl = -200
    #
    return(ctl)
#ctl5
        
#
def ctl100():
    global cnx,tnx,sequenceMode,chooseMode,elementHold,elementHoldPU,seq
    #scrub xmlns
    s100 = cnx.find(':')
    if (s100 <> -1):
        tnx = cnx[s100+1:]
    else:
        tnx = cnx
    #endif
    print('ctl100 tnx=('+ tnx.upper() +')')
    if (tnx.upper() == 'ELEMENT'):
        
        if (sequenceMode==1):
            attr['elementHold'] = elementHold
            attr['elementHoldPU'] = elementHoldPU
            seq = seq+1
            attr['seq'] = seq
            getAttr()
            spoAttr()
            ctl = 1000
        elif (chooseMode == 1):
            attr['elementHold'] =elementHold
            attr['elementHoldPU'] = elementHoldPU
            seq = seq+1
            attr['seq'] = seq
            getAttr()
            spoAttr()
            ctl = 1000
        else:
            getAttr()
            spoAttr()
            ctl = 1000
        #endif
    elif (tnx.upper() == 'COMPLEXTYPE'):
        elementHold = parent[len(parent)-2]
        elementHoldPU = parentPU[len(parentPU)-2]
        getAttr()
        spoAttr()
        ctl = 1000
    elif (tnx.upper() == 'SEQUENCE'):
        attr['elementHold'] = elementHold
        attr['elementPU'] = elementHoldPU
        seq = 0
        sequenceMode = 1
        getAttr()
        spoAttr()
        ctl = 1000
    elif (tnx.upper() == 'CHOICE'):
        attr['elementHold'] = elementHold
        attr['elementPU'] = elementHoldPU
        seq = 0
        chooseMode = 1
        getAttr()
        spoAttr()
        ctl = 1000
    else:
        getAttr()
        spoAttr()
        ctl = 1000
    #endif
    return(ctl)
#end ctl100

def ctl1000():
    global l2x,parent,parentPU
    if (l2x == '/>'):
        parent.pop()
        parentPU.pop()
        ctl = 1
    else:
        ctl = 1
    #endif
    return(ctl)
#end ctl1000
"""======="""

def getAttr():
    print('--getAttr')
    global s,attr,r1,l2x
    #trim r1
    r1 = r1.rstrip('\r\n\t ')
    r1 = r1.lstrip('\r\n\t ')
    if (len(r1) <> 0):
        x2d = 0
        while (x2d == 0):
            print("getatt r1=(" + r1.__str__() + ")")
            fo = r1.find(' ')
            print("getatt fo=(" + fo.__str__() + ")")
            if (fo == -1):
                x2d = -1 # break
                fo = len(r1)-1
                if (l2x == '/>'):
                   fo = fo -1
                #endif
                # adjust for last 2 /> or x>
                if (r1[len(r1)-2]=='/'):
                    fo = len(r1) -2
                else:
                    fo = len(r1)-1
                #
            r2 = r1[0:fo]
            print("getatt r2=(" + r2.__str__() + ")")
            try:
                atna,atVal = r2.split('=')
                atVal = atVal[1:-1]
            except:
                #if no space and no = we have <tag> or <tag/>
                atna = 'Tag'
                atVal = r1[1:-1]
                if (r1[len(r1)-2]=='/'):
                    atVal = r1[1:-2]
                #endif
            finally:
                nop = 1
            #endtry
        
            #write att
            if (x2d == 0 ):
                r1 = r1[fo+1:]
                r1 = r1.rstrip('\r\n\t ')
                r1 = r1.lstrip('\r\n\t ')
            #endif
            print('gatAttr write')
            attr[atna]=atVal
        #wend
    #endif len(r1)==0
    # get > to < if not \r\tsp add as atna=Value
    vsp = s.fctillor('<')
    print("ctl1 vsp=(" + vsp.__str__() + ")")
    vsp = vsp.rstrip('\r\n\t ')
    vsp = vsp.lstrip('\r\n\t ')
    if (len(vsp) <> 0 ):
        attr['value']= vsp
    #
    return(attr)
#
def spoP():
    global cnx,attr,pu,kri,nax,r1,l2x,snowflakeRtns,parent,parentPU
    print('--spoP')
    # best kri 
    #add cnx to parents
    parentPlus(cnx)
    #parents spo
    spoPlus(parent[len(parent)-2],'childCNX',cnx)
    snowflakeRtns.ProfilePlus("PARENTCNX",parent[len(parent)-2],'childCNX',cnx)
    spoPlus(cnx,'parentCNX',parent[len(parent)-2])
    snowflakeRtns.ProfilePlus("CNX",cnx,'parentCNX',parent[len(parent)-2])
    # /> processing pop from last parent
    if (l2x == "/>"):
        parent.pop()
        parentPU.pop()
    #
    print("spoP l2x=(" + l2x.__str__() + ")")
    # pickup pos
    spoPlus(cnx,'pickupCNX',pu.__str__())
    snowflakeRtns.ProfilePlus("CNX",cnx,'pickupCNX', pu.__str__())
#
def spoAttr():
    global cnx,attr,pu,kri,parent,parentKRI,s,cnxftsw,snowflakeRtns,parentPU
    print('--spoAttr')
    #attributes spo
    #det best kri id,name,pickup as [kri]=(atna=atval)
    spoPlus(parent[len(parent)-2],'childCNX',cnx)
    #snowflakeRtns.ProfilePlus("PARENTCNX",parent[len(parent)-2], 'childCNX', 'childCNX',cnx)
    spoPlus(cnx,'parentCNX',parent[len(parent)-2])
    snowflakeRtns.ProfilePlus('CNX',cnx,'parentCNX', parent[len(parent)-2] )
    print('\ndump of attr')
    print(attr)
    print('END dump of attr\n')
    
    look = 0
    atn = 'unknown'
    atv = 'unknown'
    try:
        if (look == 0):
            jk = attr['identifier'] 
            atn = 'identifier'
            atv = attr['identifier']
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['id'] 
            atn = 'id'
            atv = attr['id']
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['index'] 
            atn = 'index'
            atv = attr['index']
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['ix'] 
            atn = 'ix'
            atv = attr['ix']
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['No.'] 
            atn = 'No.'
            atv = attr['No.']
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['number'] 
            atn = 'number'
            atv = attr['number']
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['name'] 
            atn = 'name'
            atv = attr['name']
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['pickup'] 
            atn = 'pickup'
            atv = attr['pickup']
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
     
    kri = "KRI(" + atn +"):""(" + atv +"):"
    #test for unique
    try:
        jk = snowflakeRtns.getPRec('UID',kri)
        ds = snowflakeRtns.getds()
        kri = kri + '::' + ds
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    snowflakeRtns.ProfilePlus('UID',kri)
    seq = ''
    try:
        seq = attr['seq']
    except:
        attr['seq'] = ''
    finally:
        nop = 1
    #
    peer = ''
    try:
        peer = attr['peer']
    except:
        attr['peer'] = ''
    finally:
        nop = 1
    #
    #spo kri
    if (cnxftsw == 0):
        spoPlus('first',"KRI",kri)
        snowflakeRtns.ProfilePlus('FIRST',kri)
        cnxftsw = 1
    #endif
    spoPlus("ATN","("+ "FILE" + '=' + s.fh.name + ")",kri)
    
    snowflakeRtns.ProfilePlus("ATN", "PARENTKRI", parentPU[len(parentPU)-2], "KRI",kri)
    snowflakeRtns.ProfilePlus("ATV", parentPU[len(parentPU)-2], "PARENTKRI", "KRI",kri)
    snowflakeRtns.ProfilePlus("KRI",kri,"ATV", parentPU[len(parentPU)-2], "PARENTKRI")
    snowflakeRtns.ProfilePlus("KRI",kri,"ATN", "PARENTKRI", parentPU[len(parentPU)-2])
    
    
    snowflakeRtns.ProfilePlus("ATN", "FILE",s.fh.name, "KRI",kri)
    snowflakeRtns.ProfilePlus("ATV",s.fh.name, "FILE", "KRI",kri)
    spoPlus("ATV","("+ s.fh.name + '=' + "FILE" + ")",kri)
    spoPlus(kri,"ATN","("+ "FILE" + '=' + s.fh.name + ")")
    
    snowflakeRtns.ProfilePlus("KRI",kri,"ATN","FILE",s.fh.name)
    snowflakeRtns.ProfilePlus("KRI",kri,"ATV",s.fh.name,"FILE",)
    spoPlus(kri,"ATV","("+ s.fh.name + '=' + "FILE" + ")")
    #parentKRI
    try:
        puat = SnowflakeRtns.getPRec("ATN",'pickup',parentPU[len(parentPU)-2].__str__())
    except:
        puat = ''
    finally:
        nop = 1
    #end try
    puat = puat.__str__()
    spoPlus(kri,'parentPickup',parentPU[len(parentPU)-2].__str__())
    snowflakeRtns.ProfilePlus("KRI",kri,"ATN","PARENTKRI", puat)
    snowflakeRtns.ProfilePlus("PARENTKRI",puat,"KRI:SEQ",kri,seq)
    snowflakeRtns.ProfilePlus("PARENTKRI",puat,"KRI:PEER",kri,peer)
    spoPlus('parentPickup',puat,kri) 
    
    
    for x in attr:
        atx = attr[x].__str__()
        ax = x.__str__()
        if (ax == "pickup"):
            spoPlus('pickup',attr[x],kri)
            snowflakeRtns.ProfilePlus("PICKUP",attr[x],"KRI",kri)
        #
        spoPlus('NAME',ax,kri)
        spoPlus('NAME',atx,kri)
        spoPlus(kri,ax,atx)
        snowflakeRtns.ProfilePlus("KRI",kri,"ATN",ax,atx)
        snowflakeRtns.ProfilePlus("KRI",kri,"ATV",atx,ax)
        snowflakeRtns.ProfilePlus("ATN",ax,atx,"KRI",kri)
        snowflakeRtns.ProfilePlus("ATV",atx,ax,"KRI",kri)
        spoPlus(kri,atx,ax)
        spoPlus("ATN","("+ ax + '=' + atx + ")",kri)
        spoPlus("ATV","("+ atx + '=' + ax + ")",kri)
        spoPlus(kri,"ATN","("+ ax + '=' + atx + ")")
        spoPlus(kri,"ATV","("+ atx + '=' + ax + ")")
        spoPlus(ax,atx,kri)
        spoPlus(atx,ax,kri)
    #endfor
    # make parent chain in me::dad::Gpa
    parentchain = kri
    sx = len(parentPU)-1
    for s1 in range(sx):
        jj = SnowflakeRtns.getPRec('ATN','pickup',parentPU[sx-s1].__str__(),'KRI')
        try:
            jj = jj.keys()[0]
        except:
            jj = '0'
        finally:
            nop =1
        #endtry
        parentchain = parentchain + '!!' + jj
    #
    # concordia to kri
    for s2 in range(sx):
        jj = SnowflakeRtns.getPRec('ATN','pickup',parentPU[sx-s2].__str__(),'KRI')
        try:
            jj = jj.keys()[0]
        except:
            jj = '0'
        finally:
            nop =1
        #endtry
        snowflakeRtns.ProfilePlus('PConcordia',jj, "CHAIN",parentchain)
    #end for
        
    attr = {} 
    r1 = '' # clear
#


# support 


def parentInit():
    global parent,parentPU
    parent = []
    parentPU = []
#


def parentPlus(strin):
    global parent,pu,parentPU
    print('parentPlus added (' + strin + ")")
    parent.append(strin)
    parentPU.append(pu)
#
def getParent():
    global parent
    return( parent)
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


   