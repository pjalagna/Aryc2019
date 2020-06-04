"""
file p7.py xsd/xml parse
pja 5/19/2020 removed ATV
--- redid KRID to include provenance and value to make GUID
pja 5/18/2020 edits and test
-- needs work isPrimitive(needle) 
(X)) rename ":-:" to ":-:" allows csv text wrap
(X)) need p2pix
-- need snowflake
------'PHASE2' p2pix
---------ATN,ReferentalParentIRI,iri 
-------- "FOR" ReferentID 
-------- USING ReferentIRI,iri2

pja 5/17/2020
-- notes
---- fix DeN in ctl4 
pja 5/16/2020
-- notes
(X)- breaks in ctl1 at eof ctil <
(X)--- fix ftill in fioiClass to ret -1 
(X)------if beyond fsz
--- change k6 to k7 file,v1-v5, ds (in SnowflakeRtns.py)
---- change all SF calls to add file
--- rename name to iri (xml standard name)
--- rename NAME to IRI
--- rename DEFID to DEFID
(X))- rename pickup to position
(X))- rename PICKUP to POSITION
--- for "type" == data (xml list from see xml standard doc ) 
----- if "ref" ie <element ref='iri'..
------- SF ReferentalParentIRI=iri,"ReferentIRI:ID",iri,**phase2**
-----/
---/
----- if "type" not data
------- SF TypingParentIRI=iri,"TypedIRI:ID",iri2,**phase2**
---------- iri2 is value of attr[type]
-----/
---/
--- create phase2 array from na1=va1 for na2 using na3=va3
---- like 
------from ReferentalParentIRI=iri 
------for ReferentID 
------using ReferentIRI=iri2
----/
--- endchain's are serilization problem for phase2
---- endchain is BNF 
------ yes first create spo records (see kRecord2BNF.txt )
--- have to add method of inheritance 
------to provenance 
----- like:
--------*,schema:-:=>,tagx0:-:CS,tagx1,{CSID} 
---------- :-:REF,tagx2:-:CS,tagx3,{CSID}:-:END 
--- on all values use namer to find [industrialAcromym,industry]
--- on all values use regxFinder to find [patternName,clip]
---- like '---- http://---.com----' to find (URL,"http://---.com")
pja 5/15/2020 
--notes 
---- need to add defaults min max Occurs for elements named "element"
------ default min=1 max=1 as per xml standard doc 
---- rename 'PConcordia' to 'ConcordiaKRID'
------ after KRID formed 
---- rename 'CHAIN' to 'KRIDCHAIN'
------ add to ATN for KRID
---- create 'PConcordiaPU' for all parentsPU 
------ forming PUCHAIN pu:-:pu in me:-:dad:-:grandpa
------ at ctl1 for all r0
pja 5/14/2020 added getDeN at ctl1
(X)--SF atn DeN DeN position pu
(X)--SF position pu atn DeN DeN
pja 5/13/2020 captured atx,ax w/o xmlns for skos 
---- prepu to string
---- main takes filename
---- previous vs parent
---- commented out spoPlus(---
pja 5/12/2020 changed KRI to KRID -why KRI when you can KR-ID
pja 5/10/2020 added id types for xsd
pja 5/7/2020 p7.main return spo
pja 5/5/2020 rewrite
pja 5/4/2020 added spo structures
pja 5/3/2020

test as 
import useLib
import p7
import p7xRtns 
sp1,mxsd = p7.main('StratML.xsd')

sp2,mxml = p7.main('example.xml')

sp3,stratml = p7.main('StratML.xsd')

import SnowflakeRtns
csvs = SnowflakeRtns.snowflake2csv(mxsd)
csvs2 = SnowflakeRtns.snowflake2csv(mxml)
fh = open('txOut.csv','w')
fh.write(csvs)
fh.close()




1-get < to > to r1 ; pu++ 
if eof?
--y => -22
--n first 2 rx fan
--<? => 1
--<! => 1
--</ => 4
--other  => 5

4 </tag>
getname[1:-1] #position '/'
previous,pre,atn PU,pu
position, pu,atn,pu,pu
=sequence?
--y sequenceMode=0 
----popParent popPU 
----masterPKI='',masterPU=''
----=>1
=choice?
--y chooseMode=0 
----popParent popPU 
----masterPKI='',masterPU=''
----=> 1
==other?
// endchain
-- popParent popPU => 1
-- => 1


5 <tag{SP atn=atv}lx2(*>,/>)
has space - has = as d60
00 <x> getname[1:-1] to DeN 
-- pushParent(DeN) => 100
01 er -200
10 er -200
11 getnaSP pushParent pushPU => 100

100 
--if tag = "element" 
--- getattr  get2< 
--- KRID
** element input types lookup added to getattr

--- sequenceMode=1? or choiceMode=1
------y 
--------seq++ attr+[seq] 
--------attr+[masterPKI] 
--------spo => 1000
------n spo => 1000
-if tag = complexType 
-- attr+[masterPKI]=perentkri attr[masterPU]=parentPosition  
-- if d60=00 => 1000
-- if d60=11 getattr  get< 
-- KRID spo => 1000

-if tag = sequence 
-- attr+[masterPKI] 
-- attr+[masterPU]
-- seq=0 
-- sequenceMode=1
---getattr()  
---spoAttr()
---=> 1000

- if tag = choice
-- attr+[masterPKI] attr+[masterPU]
-- seq=1 
-- ChooseMode=1
---getattr()  
---spoAttr()
---=> 1000

-if tag= other
-- getattr  get2< KRID
-- spo => 1000

1000 last 2 l2x
lx2--=/> popParent popPU 
--------endchain()
--------=> 1
----*>  => 1

(X)endchain
------- record end of provenance chain as 
snowflakeRtns.ProfilePlus(
---------"ENDCHAIN" last parent kri,PROVENANCE,chain

my parent kri 
==parentPosition[len(parentPosition)-1]


-------"ENDCHAIN" last parent kri,"IRI",elementName

elementName = DeN

-------"ENDCHAIN" last parent kri,"masterPKI",masterPKI
-------"masterPKI",masterPKI,"ENDCHAIN" last parent kri,
#


attr+ note 
---- element has type of input?
------y attr+[SKOSKRID]=kri
------n skip
input types (strip mxlns) cdata,string


((first,KRID)) => kri
((IRI,<atn>)) => kri
((IRI,<atv>) => kri
((parentKRID,<pki> ))=> kri
((position,<#>)) => kri
((ATN,<(atn=atv)> => kri
((ATV,<(atv=atn)> => kri
((kri) ATN)) => <(atn=atv)> 
((kri) ATV) <(atv=atn)> ))
((kri) parentKRID ) pki ))
((kri) FILE ) filename ))
((kri,<atn>)) => <atv>
(("ENDCHAIN" last parent kri)) => "masterPKI",masterPKI
(("ENDCHAIN" last parent kri)) => "IRI",elementName
(("ENDCHAIN" last parent kri)) => PROVENANCE,chain
(("masterPKI",masterPKI,)) => "ENDCHAIN" last parent kri,

support
((UID,kri))
#

notes
"endchain" sigma(mykri) "endname:krid" myname mykrid
-- for endchain xml->xsd.kri "endname:krid" documentation 
-----> krid of documentation

need 6 point array for snowflake database (see SnowflakeDatabase.txt)
segments
ATN atn atv
ATV atv atn
KRID kri
UID value ** no dups

PARENTDeN pDeN CHILDDeN DeN
DeN,DeN,'parentDeN' pDeN
parentKRID parentkri KRID:SEQ kri seq
parentKRID parentkri KRID:PEER kri peer
FIRST kri
KRIDCONCORDIA pkri chain:-: ** no dups for every pkri in chain




notes
(X) uri:name process on element,sequence,choice,complexType
(X)follow parentKRID
(X)trim DeN,atn,atv
(X) DeNftsw spo('first',"KRID",kri)
(X)on complexType add hold parentPosition in masterPU
(X) seq numbers on sequence or xsd:sequence


"""
import spoRtns
spoPlus = spoRtns.spoPlus
getspo = spoRtns.getspo
spoInit = spoRtns.spoInit
import SnowflakeRtns
global snowflakeRtns
snowflakeRtns = SnowflakeRtns

def main(fn):
    xInit(fn)
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
def xInit(fn):
    global s,pu,fsz,ftsw,DeNftsw,sequenceMode,chooseMode,masterPKI,masterPU,seq,snowflakeRtns,parentPosition,previousPosition,p2pix
    p2pix = 0 # phase 2 index
    previousPosition = 0
    snowflakeRtns.ProfileInit()
    seq = 0
    masterPKI=0
    masterPU = 0
    sequenceMode = 0
    chooseMode = 0
    import fioiClass
    s = fioiClass.fio(fn)
    #filesize to fsz
    import os
    ffn = os.getcwd() + '/' + s.fh.name
    fsz = os.path.getsize(ffn)
    DeNftsw = 0 # ftsw for first kri
    pu = 0
    s.fioxSet(0)
    parentInit()
    parentPlus('')
    parentPosition.append(0)
    attrInit()
    ftsw=0
    spoInit()
    parentKRID = ''
#
def rets():
    global s
    return(s)
#

def ctl1():
    #trim to <rx--> fan on rx
    global s,m,r0,r1,rx,pu,l2x,fsz,ftsw,parent,attr,previousPosition,DeN,l1x
    print('\n\n ctl1 begin ')
    attr = {} #blank 
    r1 = ''
    r0 = ''
    df = s.fioxGet()
    print("ctl1 fsz=(" + fsz.__str__() + ")")
    print("ctl1 iox=(" + df.__str__() + ")")
    if (fsz <= s.fioxGet()):
       ctl = -100
    else:
        print('status sequenceMode=(' + sequenceMode.__str__() + ')')
        print('status chooseMode=(' + chooseMode.__str__() + ')')
        print('ctl1 dump parent')
        print(parent)
        print('ctl1 end dump parent\n')
        s.fwhite()
        m=s.f2tkn('>',1)
        previousPosition = pu
        attr['previousPosition'] = pu
        pu = pu +1
        attr['position'] = pu.__str__()
        DeN = getDeN(m[0])
        print('ctl1 DeN=(' + DeN.__str__() + ')')
        print('ctl1 dump parentPosition')
        print(parentPosition)
        print('ctl1 end dump parentPosition\n')
        # endchainPU  in me:-:dad:-:grandpa
        psx = len(parentPosition)-1
        #previous,pre,atn PU,pu
        snowflakeRtns.ProfilePlus('previousPosition', previousPosition.__str__(),'ATN','position',pu.__str__())
        #position, pu,atn,pu,pu
        snowflakeRtns.ProfilePlus('POSITION', pu.__str__(),"ATN",'previousPosition',previousPosition.__str__())
        # position pu atn DeN DeN
        snowflakeRtns.ProfilePlus('POSITION', pu.__str__(), "ATN",'DeN',DeN)
        # atn DeN DeN position pu
        snowflakeRtns.ProfilePlus('ATN','DeN',DeN, 'POSITION',pu.__str__())
        #store rdf
        r0 = m[0]
        print("ctl1 r0=(" + r0.__str__() + ")")
        print("ctl1 current PU" + pu.__str__() + ")")
        print("ctl1 previousPosition" + previousPosition.__str__() + ")")
        l1x = r0[:1] # first 2
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

def ctl4(): # </tag>
    global r0,parent,parentPosition,sequenceMode,chooseMode,pu,previousPosition
    snowflakeRtns.ProfilePlus("ENDPOINT",pu.__str__())
    tagname = r0[1:-1] #</name> name== /tag
    tagname = getDeN(m[0])
    #trim
    tagname = tagname.rstrip(' \t\r\n')
    tagname = tagname.lstrip(' \t\r\n')
    print("ctl4 tagname=("+ tagname+")")
    #strip xmlns
    d4 = tagname.find(':')
    if (d4 == -1):
        tagname = r0[1:-1]
    else:
        tagname = '/' + tagname[d4+1:]
    #endif
    print("ctl4 tagname=("+ tagname + ")")
    if (tagname.upper() == "/SEQUENCE"):
        sequenceMode = 0
        masterPKI = ''
        masterPU = ''
        seq = 0
        #endchain() #ctl4 </ DeN = sequence
        parent.pop()
        parentPosition.pop()
        ctl = 1
    elif (tagname.upper() == "/CHOICE"):
        chooseMode = 0
        seq = 0
        masterPKI = ''
        masterPU = ''
        #endchain() #clt4 </ DeN = choice
        parent.pop()
        parentPosition.pop()
        ctl = 1
    else:
        #endchain() #ctl4 </ DeN = other
        parent.pop()
        parentPosition.pop()
        ctl = 1
    #endif
    return(ctl)
#end ctl4


def ctl5(): #<name{atr}|/>,>
    global r0,d60,DeN,parent,parentPosition,attr,r1
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
        DeN = r0[1:-1]
        parent.append(DeN)
        parentPosition.append(pu)
        attr['DeN'] = DeN
        attr['position'] = pu
        ctl = 100
    elif (d60 ==3):
        DeN = r0[1:a1]
        r1 = r0[a1:]
        parent.append(DeN)
        attr['DeN'] = DeN
        parentPosition.append(pu)
        attr['position'] = pu
        ctl = 100
    else:
        raw_input('ctl1 error d60=' + d60.__str__() + '=')
        ctl = -200
    #
    return(ctl)
#ctl5
        
#
def ctl100():
    global DeN,tnx,sequenceMode,chooseMode,masterPKI,masterPU,seq
    #scrub xmlns
    s100 = DeN.find(':')
    if (s100 <> -1):
        tnx = DeN[s100+1:]
    else:
        tnx = DeN
    #endif
    print('ctl100 tnx=('+ tnx.upper() +')')
    if (tnx.upper() == 'ELEMENT'):
        #if element has input type attr+[skos]
        if (sequenceMode==1):
            attr['masterPKRID'] = masterPKI
            attr['masterPosition'] = masterPU
            seq = seq+1
            attr['seq'] = seq
            snowflakeRtns.ProfilePlus('POSITION',pu.__str__(),'relationship',"CS",masterPU.__str__())
            snowflakeRtns.ProfilePlus('POSITION',pu.__str__(),"ATN","seq",seq.__str__())
            getAttr()
            spoAttr()
            ctl = 1000
        elif (chooseMode == 1):
            attr['masterPKRID'] =masterPKI
            attr['masterPosition'] = masterPU
            seq = seq+1
            attr['seq'] = seq
            snowflakeRtns.ProfilePlus('POSITION',pu.__str__(),'relationship',"CCH",masterPU.__str__())
            #phase2
            snowflakeRtns.ProfilePlus('POSITION',pu.__str__(),"ATN","seq",seq.__str__())
            getAttr()
            spoAttr()
            ctl = 1000
        else:
            getAttr()
            spoAttr()
            ctl = 1000
        #endif
    elif (tnx.upper() == 'COMPLEXTYPE'):
        masterPU = parentPosition[len(parentPosition)-2]
        masterPKI = getKRID4PU(masterPU)
        getAttr()
        spoAttr()
        ctl = 1000
    elif (tnx.upper() == 'SEQUENCE'):
        attr['masterPKRID'] = masterPKI
        attr['masterPosition'] = masterPU
        seq = 0
        sequenceMode = 1
        getAttr()
        spoAttr()
        ctl = 1000
    elif (tnx.upper() == 'CHOICE'):
        attr['masterPKRID'] = masterPKI
        attr['elementPosition'] = masterPU
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
    global l2x,parent,parentPosition
    if (l2x == '/>'):
        #endchain() # ctl1000 l2x = />
        snowflakeRtns.ProfilePlus('ENDPOINT',pu.__str__())
        parent.pop()
        parentPosition.pop()
        ctl = 1
    else:
        ctl = 1
    #endif
    return(ctl)
#end ctl1000
"""======="""
def getDeN(m0):
    m0 = m0.rstrip(' \t\n\r')
    m0 = m0.lstrip(' \t\n\r')
    lx1 = m0[:2]
    lx2 = m0[len(m0)-2:]
    sp = m0.find(' ')
    casesw = 0
    if (lx1 == "</"):
        casesw = casesw + 1
    #endif
    if (lx2 == "/>"):
        casesw = casesw + 2
    #endif
    if (sp <> -1):
        casesw = casesw + 4
    #endif
    #case
    if (casesw ==0):   #<tag>
        DeN = m0[1:-1]
    elif (casesw ==1): # </tag>
        DeN = m0[1:-1] # DeN contains /
    elif (casesw ==2): #<tag/>
        DeN = m0[1:-2]
    elif (casesw == 5): # <tag attr>
        DeN = m0[1:sp]
    elif (casesw == 6): # <tag attr/>
        DeN = m0[1:sp]
    elif (casesw == 4): # <!-- x -->
        DeN = m0[1:sp]
    else:
        print('DeN error m0=('+ m0 + ')')
        print('DeN error casesw=('+ casesw.__str__() + ')')
        DeN = ''
    #
    return(DeN)
#
    
        
    

    
    
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
    # if attr[minOccurs ] not set attr[minOcurs]=1
    try:
        j = attr["minOccurs"]
    except:
        attr["minOccurs"] = 1
    finally:
        nop = 1
    #endtry
    # if attr[minOcurs] not set attr[minOcurs]=1
    try:
        j = attr["maxOccurs"]
    except:
        attr["maxOccurs"] = 1
    finally:
        nop = 1
    #endtry
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
    global DeN,attr,pu,kri,nax,r1,l2x,snowflakeRtns,parent,parentPosition,l1x
    print('--spoP')
    # best kri 
    #add DeN to parents
    parentPlus(DeN)
    #parents spo
    prepu = parent[len(parent)-2]
    prepu = prepu.__str__()
    ######spoPlus(parent[len(parent)-2],'childDeN',DeN)
    snowflakeRtns.ProfilePlus("PARENTDeN",prepu,'childDeN',DeN)
    ######spoPlus(DeN,'parentDeN',prepu)
    snowflakeRtns.ProfilePlus("DeN",DeN,'parentDeN',prepu)
    snowflakeRtns.ProfilePlus("l1x",l1x,"ATN",'position',pu.__str__())
    # /> processing pop from last parent
    if (l2x == "/>"):
        parent.pop()
        parentPosition.pop()
    #
    print("spoP l2x=(" + l2x.__str__() + ")")
    # position pos
    ######spoPlus(DeN,'positionDeN',pu.__str__())
    snowflakeRtns.ProfilePlus("DeN",DeN,'position', pu.__str__())
#
def spoAttr():
    global DeN,attr,pu,kri,parent,parentKRID,s,DeNftsw,snowflakeRtns,parentPosition,p2pix
    print('--spoAttr')
    kri = getKRID()
    #attributes spo
    #det best kri id,name,position as [kri]=(atna=atval)
    prepu = parent[len(parent)-2]
    prepu = prepu.__str__()
    ######spoPlus(prepu,'childDeN',DeN)
    #snowflakeRtns.ProfilePlus("PARENTDeN",parent[len(parent)-2], 'childDeN', 'childDeN',DeN)
    ######spoPlus(DeN,'parentDeN',prepu)
    snowflakeRtns.ProfilePlus('DeN',DeN,'parentDeN', parent[len(parent)-2].__str__() )
    print('\ndump of attr')
    print(attr)
    print('END dump of attr\n')
    
    try:
        j = attr[ref] 
        snowflakeRtns.ProfilePlus("POSITION" ,pu.__str__(),"ATN" , "ReferentPosition" ,masterPU.__str__())
        snowflakeRtns.ProfilePlus('PHASE2',p2pix.__str__(), "REFProcessPosition", pu.__str__())
        p2pix = p2pix + 1 
    except:
        nop = 1
    finally:
        nop = 1
    #end try
    #
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
    if (DeNftsw == 0):
        ######spoPlus('first',"KRID",kri)
        snowflakeRtns.ProfilePlus('FIRST',kri)
        DeNftsw = 1
    #endif
    # add KRID to atn profile
    snowflakeRtns.ProfilePlus("KRID",kri,"ATN","KRID",kri)
    ######spoPlus("ATN","("+ "FILE" + '=' + s.fh.name + ")",kri)
    prepu = parentPosition[len(parentPosition)-2]
    prepu = prepu.__str__()
    snowflakeRtns.ProfilePlus("ATN", "parentPosition", prepu, "KRID",kri)
    ###
    ###
    snowflakeRtns.ProfilePlus("KRID",kri,"ATN", "parentPosition", prepu)
    
    
    snowflakeRtns.ProfilePlus("ATN", "FILE",s.fh.name, "KRID",kri)
    ####
    ######spoPlus("ATV","("+ s.fh.name + '=' + "FILE" + ")",kri)
    ######spoPlus(kri,"ATN","("+ "FILE" + '=' + s.fh.name + ")")
    
    snowflakeRtns.ProfilePlus("KRID",kri,"ATN","FILE",s.fh.name)
    ####
    ######spoPlus(kri,"ATV","("+ s.fh.name + '=' + "FILE" + ")")
    puat = getParentKRID()

    ######spoPlus(kri,'parentPickup',parentPosition[len(parentPosition)-2].__str__())
    snowflakeRtns.ProfilePlus("KRID",kri,"ATN","parentKRID", puat)
    snowflakeRtns.ProfilePlus("parentKRID",puat,"KRID:SEQ",kri,seq)
    snowflakeRtns.ProfilePlus("parentKRID",puat,"KRID:PEER",kri,peer)
    ######spoPlus('parentPickup',puat,kri) 
    
    
    
    for x in attr:
        atx = attr[x].__str__()
        ax = x.__str__()
        if (ax == "position"):
            ######spoPlus('position',attr[x],kri)
            snowflakeRtns.ProfilePlus( "POSITION", atx, "KRID",kri)
        #
        #capture all atx,ax w/o xmlns
        atxs = atx.upper()
        atxd = atxs.find(":")
        if (atxd == -1 ):
            nop =1
        else:
            atxs = atxs[atxd+1:]
        #endif
        axs = ax.upper()
        axd = axs.find(":")
        if (axd == -1 ):
            nop =1
        else:
            axs = axs[atxd+1:]
        #endif
        # ax = tag , atx = value 
        # axs= val w/o xmlns , atxs=w/o xmlns uppercase 
        if (axs == "TYPE"):
            if (atxs == "STRING"):
                # skos kri , atn, ax,atx
                snowflakeRtns.ProfilePlus("DEFKRID",kri,"ATN",ax,atx)
                snowflakeRtns.ProfilePlus("ATN",ax,atx,"DEFKRID",kri)
                # kri kri skosATN ax,atx
                snowflakeRtns.ProfilePlus("KRID",kri,"DEFATN",ax,atx)
                snowflakeRtns.ProfilePlus("DEFATN",ax,atx,"KRID",kri)
            #
        #
        ######spoPlus('IRI',ax,kri)
        ######spoPlus('IRI',atx,kri)
        ######spoPlus(kri,ax,atx)
        snowflakeRtns.ProfilePlus("KRID",kri,"ATN",ax,atx)
        ###
        snowflakeRtns.ProfilePlus("ATN",ax,atx,"KRID",kri)
        ####
        ######spoPlus(kri,atx,ax)
        ######spoPlus("ATN","("+ ax + '=' + atx + ")",kri)
        ######spoPlus("ATV","("+ atx + '=' + ax + ")",kri)
        ######spoPlus(kri,"ATN","("+ ax + '=' + atx + ")")
        ######spoPlus(kri,"ATV","("+ atx + '=' + ax + ")")
        ######spoPlus(ax,atx,kri)
        ######spoPlus(atx,ax,kri)
    #endfor
    
    # clear attr for next
    attr = {} 
    r1 = '' # clear
#


# support 
def getParentchain():
    global krid,parent,parentPosition
    # make parent chain in me:-:dad:-:Gpa
    parentchain = ""
    sx = len(parentPosition)-1
    for s1 in range(sx):
        jj = SnowflakeRtns.getPRec('ATN','position',parentPosition[sx-s1].__str__(),'KRID')
        try:
            jj = jj.keys()[0]
        except:
            jj = '0'
        finally:
            nop =1
        #endtry
        print('getParentchain jj=(' + jj.__str__() + ')')
        parentchain = parentchain + '!!' + jj
    return(parentchain)
#

def getKRID4PU(pu):
    global parentPosition
    try:
        puat = SnowflakeRtns.getPRec("ATN",'position',parentPosition[len(parentPosition)-2].__str__(),"KRID").keys()[0]
    except:
        puat = ''
    finally:
        nop = 1
    #end try
    puat = puat.__str__()
    return(puat)
#

#
def getParentKRID():
    m = """ get kri from position """
    global parentPosition
    parpu = parentPosition[len(parentPosition)-2]
    parpu = parpu.__str__()
    puat = getKRID4PU(parpu)
    return(puat)
#
def parentInit():
    global parent,parentPosition
    parent = []
    parentPosition = []
#


def parentPlus(strin):
    global parent,pu,parentPosition
    print('parentPlus added (' + strin + ")")
    parent.append(strin)
    parentPosition.append(pu)
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
""" dead code for later
puch = ''
        for sc in range(psx):
            #endchain as i know it now in me:-:dad:-:gpa
            puch = puch + ":-:" + parentPosition[psx-sc].__str__()
        #end for
        # endchainPU, puch , ATN pu , pu
        snowflakeRtns.ProfilePlus('ENDCHAINPU',puch,'ATN', 'position',pu)
        # POSITION  pu endchainPU, puch
        snowflakeRtns.ProfilePlus('POSITION',pu,'ENDCHAINPU', puch)
        # ATN POSITION  pu endchainPU, puch 
        snowflakeRtns.ProfilePlus('ATN','position',pu, 'ENDCHAINPU',puch)
=========
save for phase2
    
def endchain():
    global parentPosition,DeN,masterPKI
    # create provenance chain
    parentchain = getParentchain()
    #get lastparentkri
    lastParentKRID = getKRID4PU(parentPosition[len(parentPosition)-1])
    ElementName = DeN
    #record
    snowflakeRtns.ProfilePlus("ENDCHAIN", lastParentKRID,"PROVENANCE",parentchain)
    snowflakeRtns.ProfilePlus("ENDCHAIN", lastParentKRID,"IRI",ElementName)
    snowflakeRtns.ProfilePlus("ENDCHAIN", lastParentKRID,"masterPKI",masterPKI)
    snowflakeRtns.ProfilePlus("masterPKI",  masterPKI,"ENDCHAIN" ,lastParentKRID)
    parentchainAr = parentchain.split('!!')
    print('dump parentchainAr')
    for arx in range(len(parentchainAr)):
        #"endchain" sigma(mykri) "endname:pu" myname mykrid
        mypu = pu -1
        snowflakeRtns.ProfilePlus('ENDCHAIN',parentchainAr[arx],"ENDIRI:PU",ElementName,mypu.__str__())
    #endfor
    print('end dump parentchainAr')
#
=====
# concordia to kri
    # chain of KRID
    parentchain = getParentchain()
    # per parent
    sx = len(parentPosition)-1
    for s2 in range(sx):
        s4 = getKRID4PU(parentPosition[s2])
        snowflakeRtns.ProfilePlus( 'ConcordiaKRID', s4, "KRIDCHAIN",parentchain)
    #end for
=====


"""
def isPrimitive(needle): # ==> ok/nok
    m = """remove namespace
primitive types ie not type calls
string
boolean
float
double
decimal
duration
dateTime
time
date
gYearMonth
gYear
gMonthDay
gDay
gMonth
hexBinary
base64Binary
anyURI
QName
NOTATION 
"""
#end
def getKRID():
    """ final krid = best name + provenance + value """
    global attr,DeN
    pch = getParentchain()
    # gen best KRID
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
            if (DeN.upper() <> 'ELEMENT'): 
                atn = 'DeN'
                atv = DeN
                look = 1
            #endif
        #endif
    #endtry
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['position'] 
            atn = 'position'
            atv = attr['position']
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    
    try:
        val = str(attr['value'])
    except:
        val = ''
    finally:
        nop =1 
    #end try
    kri = "KRID(" + atn.__str__() +"):(" + atv.__str__() +"):"+":-:"+pch+":-:"+val+":-:"
    #test for unique
    try:
        jk = snowflakeRtns.getPRec('UID',kri)
        #dup
        raw_input("duplicate KRID=("+KRID+")")
    except:
        snowflakeRtns.ProfilePlus('UID',kri)
    finally:
        nop = 1
    #endtry
    #KRIFD is fixed
    return(kri)
#end getKRID   