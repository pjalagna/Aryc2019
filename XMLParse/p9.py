"""
file p9.py
usage main(filename{,trace}) renders to ontology fileName.onto
trace == "on" will print progress
"""
"""
pja 9/8/2020 add namespace to all roles (tag,attributeName,refValue,typeValue)
pja 9/6/2020 fixed genx
pja 7/8/2020 recorded (relates) <item>name, <item>nds  
--- to full item at refid of item
--- also tagName contains / if endname
pja 7/4/2020 if complextype has name 
--- then it is the master element
pja 6/9/2020 changed collectAttributes 
--- to allow space inside attribute values
--- added proc70 special pickup for <![cdata]
pja 6/7/2020 
-- added log of r1 in proc8
-- added atn provenance, 
-- atn tag at </
---- deleted seq++ 105,106,107
-- added SQin for 'r1' collections *free text value
pja 6/6/2020 added call105,106,107 spacial attribute processing

test as
import p9
file = 'StratML.xsd'
p9.fresh(file)
p9.main(file,'on')



notes
<attribute process
-- attaches attribute to element
--- allows optional usage
simpleType process
--- allows restrictions
--- allows emumeration

space inside a quoted string is allowed.
<tag/[space/atn=q-q]
not [space/atn=-first space]
atn value xx is protected with SQin and will need
-- SQout for reading/searching

phase 2 notes
attach <documentation>.value
-- to first gpa of tag=element 
---- at endpoint </documentation>
"""
nds = {}
pkg = {}
def logg(txt):
    """
    prints txt if nds['logg'] is =="ON"
    """
    global nds
    if (nds['trace'] == 'on'):
        print("log: " + txt)
    #endif
#logg
def getnds():
    global nds
    return(nds)
#
def getpkg():
    global pkg
    return(pkg)
#
def main(fn,trace=''):
    """
    usage main(fileName)
    renders to ontology fileName.onto
    """
    global nds,pkg
    nds = {}
    pkg = {}
    nds = getnds()
    pkg = getpkg()	
    nds['trace'] = trace
    # umbrella ctl
    ctl = 1
    while (0 < ctl):
        logg('head: ctl=('+ctl.__str__() +')')
        if (ctl == 1): #
            ctl = init(fn,trace) # "
        elif (ctl == 2): #
            logg(proc2.__doc__)
            ctl = proc2() # "
        elif (ctl == 4): #
            logg(proc4.__doc__)
            ctl = proc4() # "
        elif (ctl == 5): #
            logg(proc5.__doc__)
            ctl = proc5() # "
        elif (ctl == 8): #
            logg(proc8.__doc__)
            ctl = proc8() # "
        elif (ctl == 9): #
            logg(proc9.__doc__)
            ctl = proc9() # "
        elif (ctl == 16): #
            logg(proc16.__doc__)
            ctl = proc16() # 
        elif (ctl == 32): #
            logg(proc32.__doc__)
            ctl = proc32() # "
        elif (ctl == 33): #
            logg(proc33.__doc__)
            ctl = proc33() # "
        elif (ctl == 34): #
            logg(proc34.__doc__)
            ctl = proc34() # "
        elif (ctl == 35): #
            logg(proc35.__doc__)
            ctl = proc35() # "
        elif (ctl == 36): #
            logg(proc36.__doc__)
            ctl = proc36() # "
        elif (ctl == 40): #
            logg(proc40.__doc__)
            ctl = proc40() # "
        elif (ctl == 41): #
            logg(proc41.__doc__)
            ctl = proc41() # "
        elif (ctl == 50): #
            logg(proc50.__doc__)
            ctl = proc50() # "
        elif (ctl == 51): #
            logg(proc51.__doc__)
            ctl = proc51() # "
        elif (ctl == 52): #
            logg(proc52.__doc__)
            ctl = proc52() # "
        elif (ctl == 53): #
            logg(proc53.__doc__)
            ctl = proc53() # "
        elif (ctl == 54): #
            logg(proc54.__doc__)
            ctl = proc54() # "
        elif (ctl == 55): #
            logg(proc55.__doc__)
            ctl = proc55() # "
        elif (ctl == 56): #
            logg(proc56.__doc__)
            ctl = proc56() # "
        elif (ctl == 57): #
            logg(proc57.__doc__)
            ctl = proc57() # "
        elif (ctl == 58): #
            logg(proc58.__doc__)
            ctl = proc58() # "
        elif (ctl == 60): #
            logg(proc60.__doc__)
            ctl = proc60() # "
        elif (ctl == 62): #
            logg(proc62.__doc__)
            ctl = proc62() # "
        elif (ctl == 70): #
            logg(proc70.__doc__)
            ctl = proc70() # "
        else:
            print('error ctl ('+ctl.__str__()+')')
            ctl = -1
        #endif
    #wend
#main
def fresh(fn,trace=''):
    """
    :: fresh(filename)
    initilize and clear all tables in ontology sqlite database
    
    """
    global pkg
    init(fn,trace)
    pkg['ontology'].db.SQX('delete from v20;')
    pkg['ontology'].db.SQX('delete from GUID;')
#
def init(fn,trace=''):
    global pkg,nds
    print('initilizing')
    nds['trace'] = trace
    nds['file'] = fn
    import useLib
    import gennV
    pkg['genX'] = gennV
    import fioiClass
    pkg['fioi'] = fioiClass.fio(fn)
    import useOnto
    import SQSQ # encryption for protection 
    pkg['SQin'] = SQSQ.SQin
    pkg['SQout'] = SQSQ.SQout
    import OntologyClass
    pkg['ontology'] = OntologyClass.Ontology(fn + '.onto',str(nds['trace']))
    #preset modes
    nds['sequenceMode'] = 0
    nds['chooseMode'] = 0
    #pickup position
    nds['pu'] = 0
    nds['prevPu'] = 0
    # parent list
    nds['parent'] = [] # logical parent list
    nds['parent'].append(0)
    #attr
    nds['attr'] = {}
    #first
    nds['first']=''
    return(2)
#init


def proc2():
    """
    white till "<"-1 == 4 or eof ==>5
    """
    global pkg,nds
    pc1 = 0
    while (pc1 == 0):
        m = pkg['fioi'].fioi()
        if (m == "<"):
            pkg['fioi'].fioo() # backup 1
            pc1 = -1 # break
            ctl = 4
        elif (m=='@eofeof'):
            ctl = 5
            pc1 = -1
        else:
            loop = 1
        #endif
    #wend
    return(ctl)
#proc2

def proc4():
    """
    proc4:
    create refid for <-->
    collect from iox ("<") till ">" into r0 ==> 8 or 
    eof ==> 5
    """
    global pkg,nds
    logg('proc4 seqMode=('+str(nds['sequenceMode'])+ ")")
    logg('proc4 chMode=('+str(nds['chooseMode'])+ ")")
    ans = pkg['fioi'].fioi() # current "<"
    pc4 = 0
    while (pc4==0):
        tt = pkg['fioi'].fioi()
        if (tt == '@eofeof'):
            pc4 = -3
            ctl = 5
        if (tt=='>'): 
            nds['r0'] = ans + tt # <-->
            
            nds['refid'] = pkg['genX'].gennX()
            pc4 = -1
            ctl = 8
        else:
            ans = ans + tt
            loop = 1
        #endif
    #wend
    cc = pkg['fioi'].fioxGet()
    logg('proc4 char count=('+str(cc)+')')
    logg('proc4 r0=('+nds['r0']+')')
    return(ctl)
#proc4

def  proc5():
    """proc5: "DONE" ==> -1 """  
    print('DONE')
    return(-1)
#end 5"

def proc8(): # 
    """ proc8:
    optional collect iox(>) till next "<"-1 
    ;set r1 ==>16 eof ==> 16
    """
    global pkg,nds
    ans = ''
    pc8 = 0
    while (pc8==0):
        tt = pkg['fioi'].fioi()
        if (tt == '<'):
            pkg['fioi'].fioo() # backup 1
            nds['r1'] = ans
            pc8 = -1
            ctl = 16
        elif (tt == '@eofeof'):
            nds['r1'] = ans
            pc8 = -2
            ctl = 16
        else:
            ans = ans + tt
            loop = 1
        #endif
    #wend
    logg("proc8: r1=(" + str(nds['r1'])+ ")")        
    return(ctl)
#proc8

def  proc9():
    """proc9: bad format no ">" ==> -2 """  
    iox = pkg['fioi'].fioxGet()
    print('ERROR bad xml format no ending ">" at charicter position('+ str(iox) + ')')
    return(-2)
#end 9"


def proc16(): # r0,r1 set collect l1x,l2x from r0 ==> 32 
    """proc16:
    r0,r1 set; collect l1x,l2x from r0;  
    ATN pickup, previous, l1x,l2x
    ==> 32
    """
    global pkg,nds
    nds['refid'] = pkg['genX'].gennX()
    # set pu, prevpu
    nds['prevPu'] =nds['pu']
    nds['pu'] = nds['pu'] +1
    #l1x,l2x 
    nds['l1x'] = nds['r0'][0:2]
    logg('l1x=('+str(nds['l1x'])+')')
    d = len(nds['r0'])
    nds['l2x'] = nds['r0'][d-2:d]
    # special case on l2x if r0 with attribute l2x ends with quote>
    if (nds['l2x'][0] == "'"):
        nds['l2x'] = 'x>'
    #endif
    if (nds['l2x'][0] == '"'):
        nds['l2x'] = 'x>'
    #endif
    logg('l2x=('+str(nds['l2x'])+')')
    # write atn pickup, previous, l1x,l2x
    pkg['ontology'].ATNWrite('pickup',str(nds['pu']), 'refid',str(nds['refid']),str(nds['refid']))
    logg("ATN "+'pickup'+str(nds['pu'])+ 'refid'+ str(nds['refid']))
    pkg['ontology'].ATNWrite('previousPickup',str(nds['prevPu']), 'refid',str(nds['refid']),str(nds['refid']))
    logg("ATN "+'previousPickup'+str(nds['prevPu'])+ 'refid'+str(nds['refid']))
    pkg['ontology'].ATNWrite('l1x',str(nds['l1x']), 'refid',str(nds['refid']),str(nds['refid']))
    logg ("ATN"+ 'l1x'+str(nds['l1x'])+ 'refid'+str(nds['refid']))
    pkg['ontology'].ATNWrite('l2x',str(nds['l2x']), 'refid',str(nds['refid']),str(nds['refid']))
    logg ("ATN"+ 'l2x'+ str(nds['l2x']) + 'refid'+str(nds['refid']))
    pkg['ontology'].ATNWrite('refid',str(nds['refid']), 'refid',str(nds['refid']),str(nds['refid']))
    logg ("ATN"+  'refid'+str(nds['refid'])+'refid'+str(nds['refid']))
    ctl = 32
    return(ctl)
#proc16


def  proc32():
    """proc32: 
    clear attr
    Fan on l1x
      special <!x not <!--
      <? ==> 33  
      <! ==> 34
      </ ==>35
      else ==> 36 """ 
    nds['attr'] ={} # clear attr
    if (nds['l1x']== "<?"):
        ctl = 33
    elif (nds['r0'][0:4] == "<!--"):
        ctl = 34
    elif (nds['l1x']== "<!"):
        ctl = 70
    elif (nds['l1x']== "</"):
        ctl = 35
    else:
        ctl = 36
    #
    return(ctl)
#end 32"
def  proc33():
    """proc33: Goto 4 """  
    return(4)
#end 33"
def  proc34():
    """proc34: Goto 4 """  
    return(4)
#end 34"
def  proc35():
    """proc35: Goto 40 """  
    return(40)
#end 35"
def  proc36():
    """proc36: Goto 50 """  
    return(50)
#end 36"
def  proc40():
    """proc40:
    atn tag
    atn provenance
    "</" Endpoint process   
    ATN endpoint,refid
    pop parent ==>41
    """
    #atn tag
    vtag = nds['r0'][1:-1]
    j = vtag.find(":")
    if (j == -1):
        tagNS = 'xsd:'
        tagName = vtag
    else:
        tagNS = vtag[0:j]
        tagName = "/"+vtag[j+1:]
    #endif
    pkg['ontology'].ATNWrite("tag", str(vtag),'refid',str(nds['refid']),str(nds['refid']))
    #atn provenance
    pkg['ontology'].ATNWrite("provenance", str(nds['parent']),'refid',str(nds['refid']),str(nds['refid']))
    #atn endpoint
    pkg['ontology'].ATNWrite("endpointRefid", str(nds['refid']),'refid',str(nds['refid']),str(nds['refid']))
    nds['parent'].pop()
    #relates for ns,name
    pkg['ontology'].RELATEWrite('tagNS',tagNS,'resolved','nameSpace','tag',vtag,str(nds['refid']))
    pkg['ontology'].RELATEWrite('tagName',tagName,'resolved','name','tag',vtag,str(nds['refid']))
    return(41)
#end 40"
def  proc41():
    """ proc41:
    Special endpoints
    may have ns:
    on /complex do nds.pop(ctpu), pop master
    
    on /seq do nds.pop(sqpu)
    /sequence = sequenceMode = 0
    
    on /choice do nds.pop(chpu)
    /choice = chooseMode = 0
    ==>4 """
    m=  nds['r0'].find(":")
    if (m == -1):
       j =  nds['r0'].upper()
    else:
       j = "</" + nds['r0'].upper()[m+1:]
    #endif
    logg('proc41 j=('+ j +')')
    if (j == "</SEQUENCE>"):
        nds['sequenceMode'] = 0 #off
        nds.pop("sqpu")
    #endif
    if (j == "</CHOICE>"):
        nds['chooseMode'] = 0 #off
        nds.pop("chpu")
    #endif
    if (j == "</COMPLEXTYPE>"):
        nds.pop("ctpu") 
        nds.pop("master")
    #endif
    return(4)
#end 41"

def  proc50():
    """proc50:  Parse tag, 
        attributes
        append pu to parent  
        adjust minOccurs,maxOccurs   
        ATN tag , attr , {val=r1}
        atn provenance
        ==>51 
    """  
    nds['parent'].append(nds['pu'])
    spc = nds['r0'].find(' ')
    if (spc == -1): # <tag> or <tag/>
        if (nds['l2x']== "/>"):
            nds['tag'] = nds['r0'][1:-2]
        else:
            nds['tag'] = nds['r0'][1:-1]
        #endif
        j = nds['tag'].find(":")
        if (j==-1):
            tagNS = 'xsd:'
            tagName = nds['tag']
        else:
            tagNS = nds['tag'][0:j]
            tagName = nds['tag'][j+1:]
        #endif
        pkg['ontology'].ATNWrite('tag',str(nds['tag']), 'refid',str(nds['refid']),str(nds['refid']))
        pkg['ontology'].RELATEWrite('tagNS',str(tagNS),"resolved",'nameSpace','tag',nds['tag'],str(nds['refid']))
        pkg['ontology'].RELATEWrite('tagName',str(tagName),"resolved",'nameSpace','tag',nds['tag'],str(nds['refid']))
        # r1 attribute
        nds['r1'] = nds['r1'].rstrip()
        nds['r1'] = nds['r1'].lstrip()
        if (len(nds['r1']) <> 0):
            logg("ATN "+'value'+str(pkg['SQin'](nds['r1']))+ 'refid'+ str(nds['refid']))
            pkg['ontology'].ATNWrite('value',str(pkg['SQin'](nds['r1'])), 'refid',str(nds['refid']),str(nds['refid']),flags='355')
        #endif r1
    else: # <tag attr (/> or >)
        nds['tag'] = nds['r0'][1:spc]
        logg('470 tag')
        j = nds['tag'].find(":")
        if (j==-1):
           tagNS = 'xsd:'
           tagName = nds['tag']
        else:
           tagNS = nds['tag'][0:j]
           tagName = nds['tag'][j+1:]
        #endif
        pkg['ontology'].ATNWrite('tag',str(nds['tag']), 'refid',str(nds['refid']),str(nds['refid']))
        pkg['ontology'].RELATEWrite( 'tagNS',tagNS,'resolved','nameSpace','tag',str(nds['tag']),str(nds['refid']))
        pkg['ontology'].RELATEWrite( 'tagName',tagName,'resolved','name','tag',str(nds['tag']),str(nds['refid']))        
        #collect & atn attributes; adjust min,max
        collectAttributes()
        # fix r1 if len>0 atn
        # r1 attribute
        nds['r1'] = nds['r1'].rstrip()
        nds['r1'] = nds['r1'].lstrip()
        if (len(nds['r1']) <> 0):
            nds['r1'] = pkg['SQin'](nds['r1'])
            pkg['ontology'].ATNWrite('value',str(nds['r1']), 'refid',str(nds['refid']),str(nds['refid']),flags="367")
        #endif r1
    #endif # <tag attr/> or >
    #atn provenance
    pkg['ontology'].ATNWrite("provenance", str(nds['parent']),'refid',str(nds['refid']),str(nds['refid']))
    return(51)
#end 50"
def  proc51():
    """proc51:
        set first
        determine Best KRID from attr - may have ns:
    """  
    if (nds['first']==''):
        nds['first']=  nds['pu']
        #atn
        logg("ATN "+'first'+str(nds['pu'])+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('first', str(nds['pu']), 'refid',str(nds['refid']),str(nds['refid']),flags="497")
    #endif
    # id,name,tag,pos
    # add position to attr
    nds['attr']['pos'] = nds['pu']
    # add tag
    nds['attr']['tag'] = nds['tag']
    logg('504'+str(nds['attr']['tag']))
    #
    bestscore = 0
    bestkrid = ''
    for m in nds['attr']:
        #adjust for ns:
        aa = m.find(":")
        if (aa <> -1):
            m1 = m[aa+1:]
        else:
            m1 = m
        #endif
        m1 = m1.upper()
        logg('best krid m1=('+str(m1)+')')
        logg('best krid m=('+str(m)+')')
        logg('best krid vm=('+str(nds['attr'][m])+')')
        if (m1=='ID'):
            bestscore = 99
            bestkrid = m1+":"+nds['attr'][m].__str__()
        elif (m1=='IDENTIFIER'):
            bestscore = 99
            bestkrid = m1+":"+nds['attr'][m].__str__()
        elif (m1=='NAME'):
            if (bestscore < 90):
                bestscore = 90
                bestkrid = m1+":"+nds['attr'][m].__str__()
            #endif
        elif (m1=='TAG'):
            if (bestscore < 80):
                bestscore = 80
                bestkrid = m1+":"+nds['attr'][m].__str__()
            #endif
        elif (m1=='POS'):
            if (bestscore < 70):
                bestscore = 70
                bestkrid = m1+":"+nds['attr'][m].__str__()
            #endif
        else:
            nop = 1 # pos is guaranteed 
        #endif
    #endfor
    #atn
    logg("ATN "+'KRID'+str(bestkrid)+ 'refid'+ str(nds['refid']))
    pkg['ontology'].ATNWrite('KRID',str(bestkrid), 'refid',str(nds['refid']),str(nds['refid']))
    return(52)     
#end 51"
def  proc52():
    """proc52:  Special tag process - might have ns:
  element ==> 53  
complexType ==> 58  
sequence ==> 60  
choice ==> 62
  otherwise ==>53 """  
    tag = nds['tag'].upper()
    if (tag == 'XSD:ELEMENT'):
        ctl = 53
    elif (tag == 'XSD:COMPLEXTYPE'):
        ctl = 58
    elif (tag == 'XSD:SEQUENCE'):
        ctl = 60
    elif (tag == 'XSD:CHOICE'):
        ctl = 62
    else:
        ctl = 53
    #endif
    return(ctl)    
#end 52"
def  proc53():
    """proc53: Element mood process  
        if sequenceMode =1
             ATN master
             seq++
             ATN seq  
        if chooseMode=1
             ATN master
             seq++
             ATN seq
           ==>54     """  
    if (nds['sequenceMode']==1):
        #atn master
        #logg("ATN "+'master'+str(nds['master'])+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('masterPosition',str(nds['master']), 'refid',str(nds['refid']),str(nds['refid']))
        nds['seq'] = nds['seq']+1
        #atn seq
        pkg['ontology'].ATNWrite('seq',str(nds['seq']), 'refid',str(nds['refid']),str(nds['refid']))
    #endif
    if (nds['chooseMode']==1):
        #atn master
        pkg['ontology']. ATNWrite('masterPosition',str(nds['master']), 'refid',str(nds['refid']),str(nds['refid']))
        nds['seq'] = nds['seq']+1
        #atn seq
        pkg['ontology'].ATNWrite('seq',str(nds['seq']), 'refid',str(nds['refid']),str(nds['refid']))
    #endif
    return(54)
#end 53"
def proc54():
    """proc54: Special attribute processing  
        -----+type    +type  + ref   +
        -----+ on list+not   +       +
        -----+--------+------+-------+
             +//106   + //107+// 105 +
        -----+--------+------+-------+
        otherwise ==> 56
         """  
    etypeList = """
"string"
"boolean"
"float"
"int"
"integer"
"double"
"decimal"
"duration"
"dateTime"
"time"
"date"
"gYearMonth"
"gYear"
"gMonthDay"
"gDay"
"gMonth"
"hexBinary"
"base64Binary"
"anyURI"
"QName"
"NOTATION" 
        """
    for m in nds['attr']:
        logg('proc54 m=('+m+')')
        logg('proc54 vm=('+str(nds['attr'][m])+')')
        aa = m.find(":")
        if (aa <> -1):
            m1 = m[aa+1:]
        else:
            m1 = m
        #endif
        logg('proc54 m1=('+str(m1)+')')
        bb = int(str(nds['attr'][m]).find(':'))
        if (bb <> -1):
            mv1 = nds['attr'][m][bb+1:]
        else:
            mv1 = nds['attr'][m]
        #endif
        logg('proc54 mv1=('+str(mv1)+')')
        if (m1=='ref'):
            logg('calling 105')
            call105(m)
        #
        if (m1=='type'):
            if (etypeList.find(mv1)<>-1):
                logg('calling 106')
                call106(m)
            else:
                logg('calling 107')
                call107(m)
            #endif
        #endif
    #for end
    return(56)       
#end 54"

def  proc56():
    """proc56: L2x fan  /> pop parent ==>4  x> ==>4         """  
    if (nds['l2x']=="/>"):
        nds['parent'].pop()
        pkg['ontology'].ATNWrite("endpointRefid", str(nds['refid']),'refid',str(nds['refid']),str(nds['refid']))
    #endif
    return(4)
#end 56"

def  proc58():
    """proc58:  
    a) "<complexType  w/o name= ;"set master= previousparent   ==> 56     
    b) <complextype name= ; set master as me
    """  
    nds['ctpu'] = nds['pu']
    nds['sqpu'] = ''
    j = nds['r0'].find('name=')
    if (j==-1):
        #no name
        lp = len(nds['parent'])
        nds['master'] = nds['parent'][lp-2]
        logg('proc58 master w/o namepu='+str(nds['parent'][lp-2]))
    else:
        nds['master'] = nds['pu']
        logg('proc58 master w/name pu='+str(nds['pu']))
    #endif 
    
    return(56)
#end 58"

def  proc60():
    """proc60: r0="<sequence  " set sequenceMode = 1  set seq=0  ==>56 """  
    nds['sqpu'] = nds['pu']
    nds['seq'] =0
    nds['sequenceMode'] = 1
    return(56)
#end 60"

def  proc62():
    """proc62: r0="<choice  set" seq=0  set chooseMode=1  ==>56     """  
    nds['seq'] =0
    nds['chooseMode'] = 1
    nds['chpu'] = nds['pu']
    return(56)
#end 62"

def proc70():
    """
    proc70 - special backValue process
    if <![cdata text]> proceeds an element this value belongs to the previous element
    relate to pu-1 as 'backValue'
    ==>4
    """
    bv = nds['r0'][2:-1]
    #relate to pu-1 as 'backvalue'
    pkg['ontology'].RELATEWrite('backValue',str(bv),"backValue",'','pickup',str(nds['pu']-1),str(nds['refid']))
    return(4)
    
#end proc70
def collectAttributes():
    """
    collect and atn attributes
    """
    global nds,pkg
    # clip to l2x
    if (nds['l2x'] =="/>"):
        r = nds['r0'].find(nds['l2x'])
        ats = nds['r0'][1:r]
    else:
        r = nds['r0'].find(">")
        ats = nds['r0'][1:r]
    #endif
    #clear attribute list
    nds['attr']={}
    #remove tag
    spc = ats.find(' ')
    nds['tag'] = ats[0:spc]
    ats = ats[spc+1:]
    ixx = 0
    cxc = 0
    while (cxc ==0):
        #collect atn till =
        spc2 = ats.find('=')
        atn = ats[0:spc2]
        atn = atn.rstrip(" \n\t")
        atn = atn.lstrip(" \n\t")
        cx = ats[spc2+1]
        cx2 = ats.find(cx,spc2+2)
        atv = ats[spc2+2:cx2]
        nds["attr"][atn] = atv
        #atn attr
        pkg['ontology'].ATNWrite(atn,str(atv), 'refid',str(nds['refid']),str(nds['refid']))
        # record attributeNS,attributeName
        x = atn.find(":")
        if (x==-1):
           attNS = ''
           attName = atn.rstrip(' \n\t')
           attName = attName.lstrip(' \n\t')
        else:
           attNS = atn[0:x]
           attName = atn[x+1:].rstrip(' \n\t')
           attName = attName.lstrip(' \n\t')
        #endif
        pkg['ontology'].RELATEWrite('attNS',attNS,'resolved','nameSpace','attribute',atn,str(nds['refid']))
        pkg['ontology'].RELATEWrite('attName',attName,'resolved','name','attribute',atn,str(nds['refid']))
        try:
            j = ats[cx2+1]
            ats = ats[cx2+2:]
        except:
            cxc = -1
        finally:
            nop = 1
        #endtry
    #wend
    #default min,max if not in attr might have ns: 
    jj = nds['attr'].keys().__str__()
    if (jj.find('minOccurs')== -1):
        logg("ATN "+'minOccurs'+'1'+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('minOccurs','1', 'refid',str(nds['refid']),str(nds['refid']))
    #endif
    if (jj.find('maxOccurs')== -1):
        logg("ATN "+'maxOccurs'+'1'+ 'refid'+ str(nds['refid'])+str(nds['refid']))
        pkg['ontology'].ATNWrite('maxOccurs','1', 'refid',str(nds['refid']),str(nds['refid']))
    #endif
#end collectAttributes
    
    
"""
sql ReadAll returns  x but x[0][0] is the string

"""

def call105(m):
    """
    call 105:
    "ref" seq mode=1 
    -- relate master, ct-sq , refid
    -- atn master , refid
    -- seq++ , 
    ref chmode=1
    -- relate master, ct-sq , refid
    -- atn master , refid
    -- seq++ , 
    continue
    -- relate parent=, "parent", refid=
    -- relate ref=val, ref, refid=
    """
    logg(call105.__doc__)
    if (nds['sequenceMode']==1):
        relateValue = "ct"+str(nds['ctpu'])+ '::sq'+str(nds['sqpu'])
        pkg['ontology'].RELATEWrite('masterPosition', str(nds['master']),"CS",relateValue,'refid',str(nds['refid']),str(nds['refid']),flags='3')
        pkg['ontology'].RELATEWrite('masterPosition', str(nds['master']), "SEQ",str(nds['seq']),'refid',str(nds['refid']),str(nds['refid']))
        pkg['ontology'].ATNWrite('master', str(nds['master']),'refid',str(nds['refid']),str(nds['refid']))

        #written later
    #endif
    if (nds['chooseMode']==1):
        relateValue = "ct"+str(nds['ctpu'])+ '::ch'+str(nds['chpu'])
        pkg['ontology'].RELATEWrite('masterPosition', str(nds['master']),"CT",relateValue,'refid',str(nds['refid']),str(nds['refid']),flags='3')
        pkg['ontology'].ATNWrite('master', str(nds['master']),'refid',str(nds['refid']),str(nds['refid']))
        pkg['ontology'].RELATEWrite('masterPosition', str(nds['master']), "SEQ",str(nds['seq']),'refid',str(nds['refid']),str(nds['refid']))

        #written later
    #endif
    #continue
    # relate parent=, parent, refid
    pkg['ontology'].RELATEWrite('parent',str(nds['parent'][len(nds['parent'])-2]),'parent','','refid',str(nds['refid']),str(nds['refid']))
    return()
#call105
        
def call106(m):
    """
    call106:
    type; on entry list
    sequenceMode=1
    -- relate master, ctsq, refid
    -- relate type= , entryPoint, refid=

    chooseMode=1
    -- relate master, ctch, refid
    -- relate type= , entryPoint, refid=

    continue
    -- relate parent= , parent , refid
    """
    logg(call106.__doc__)
    # in all cases relate entryType
    # relate type= entryPoint'' , refid
    pkg['ontology'].RELATEWrite( m, str(nds['attr'][m]) ,'entryType',str(nds['attr'][m]),'refid',str(nds['refid']),str(nds['refid']))
    if (nds['sequenceMode']==1):
        relateValue = "ct"+str(nds['ctpu'])+ '::sq'+str(nds['sqpu'])
        pkg['ontology'].RELATEWrite('masterPosition', str(nds['master']),"masterCS",relateValue,'refid',str(nds['refid']),str(nds['refid']),flags='3')
        pkg['ontology'].ATNWrite('master', str(nds['master']),'refid',str(nds['refid']),str(nds['refid']))
    #endif
    if (nds['chooseMode']==1):
        relateValue = "ct"+str(nds['ctpu'])+ '::sq'+str(nds['chpu'])
        pkg['ontology'].RELATEWrite('master', str(nds['master']),"masterCT",relateValue,'refid',str(nds['refid']),str(nds['refid']),flags='3')
        pkg['ontology'].ATNWrite('master', str(nds['master']),'refid',str(nds['refid']),str(nds['refid']))
    #endif
    #continue
    pkg['ontology'].RELATEWrite('parent', str(nds['parent'][len(nds['parent'])-2]),'parent','','refid',str(nds['refid']),str(nds['refid']))
    return()
#end call106

def call107(m):
    """
    call 107:
    type call
    seqenceMode=1
    -- relate master , ctsq, refid
    -- atn master,refid
    -- relate type=typeVal, typeCall,typeVal refid

    chooseMode=1
    -- relate master , ctch, refid
    -- atn master,refid
    -- relate type=typeVal, typeCall,typeVal refid

    continue
    relate parent= , parent, refid
    """
    logg(call107.__doc__)
    #relate type=typeVal, typeCall,typeVal refid
    pkg['ontology'].RELATEWrite(m,str(nds['attr'][m]),'typeCall',str(nds['attr'][m]),'refid',str(nds['refid']),str(nds['refid']))
    if (nds['sequenceMode']==1):
        relateValue = "ct"+str(nds['ctpu'])+ '::sq'+str(nds['sqpu'])
        pkg['ontology'].RELATEWrite('master', str(nds['master']),"master",relateValue,'refid',str(nds['refid']),str(nds['refid']),flags='3')
        pkg['ontology'].ATNWrite('master', str(nds['master']),'refid',str(nds['refid']),str(nds['refid']))
    #endif
    if (nds['chooseMode']==1):
        relateValue = "ct"+str(nds['ctpu'])+ '::ch'+str(nds['chpu'])
        pkg['ontology'].RELATEWrite('master', str(nds['master']),"master",relateValue,'refid',str(nds['refid']),str(nds['refid']),flags='3')
        pkg['ontology'].ATNWrite('master', str(nds['master']),'refid',str(nds['refid']),str(nds['refid']))
    #endif
    #continue
    pkg['ontology'].RELATEWrite('parent',str(nds['parent'][len(nds['parent'])-2]),'parent','','refid',str(nds['refid']),str(nds['refid']))
    return()
#end call107
