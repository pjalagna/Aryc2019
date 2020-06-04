"""
file p9.py
usage main(filename{,trace}) renders to ontology fileName.onto
trace == "on" will print progress

"""
nds = {}
pkg = {}
def logg(txt):
    """
    prints txt if nds['logg'] is =="ON"
    """
    global nds
    if (nds['trace'] == 'on'):
        print(txt)
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
    nds = {}
    pkg = {}
    nds = getnds()
    pkg = getpkg
    nds['trace'] = trace
    # umbrella ctl
    # decision tree format y = I*2, n= (I*2)+1
    ctl = 1
    while (0 < ctl):
        logg('head: ctl=('+ctl.__str__() +')')
        if (ctl == 1): #
              ctl = init(fn) # "
        elif (ctl == 2): #
              ctl = proc2() # "
        elif (ctl == 4): #
              ctl = proc4() # "
        elif (ctl == 5): #
              ctl = proc5() # "
        elif (ctl == 8): #
              ctl = proc8() # "
        elif (ctl == 9): #
              ctl = proc9() # "
        elif (ctl == 16): #
              ctl = proc16() # 
        elif (ctl == 32): #
              ctl = proc32() # "
        elif (ctl == 33): #
              ctl = proc33() # "
        elif (ctl == 34): #
              ctl = proc34() # "
        elif (ctl == 35): #
              ctl = proc35() # "
        elif (ctl == 36): #
              ctl = proc36() # "
        elif (ctl == 40): #
              ctl = proc40() # "
        elif (ctl == 41): #
              ctl = proc41() # "
        elif (ctl == 50): #
              ctl = proc50() # "
        elif (ctl == 51): #
              ctl = proc51() # "
        elif (ctl == 52): #
              ctl = proc52() # "
        elif (ctl == 53): #
              ctl = proc53() # "
        elif (ctl == 54): #
              ctl = proc54() # "
        elif (ctl == 55): #
              ctl = proc55() # "
        elif (ctl == 56): #
              ctl = proc56() # "
        elif (ctl == 57): #
              ctl = proc57() # "
        elif (ctl == 58): #
              ctl = proc58() # "
        elif (ctl == 60): #
              ctl = proc60() # "
        elif (ctl == 62): #
              ctl = proc62() # "
         else:
            print('error ctl ('+ctl.__str__()+')')
            ctl = -1
        #endif
    #wend
#main
def fresh(fn)
    """
    :: fresh(filename)
    initilize and clear all tables in ontology sqlite database
    
    """
    global pkg
    init(fn)
    pkg['ontology'].SQX('delete from v20;')
    pkg['ontology'].SQX('delete from GUID;')
#
def init(fn):
    print('initilizing')
    nds['file'] = fn
    import useLib
    import fioiClass
    pkg['fioi'] = fioiClass.fio(fn)
    import useOnto
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
    nds['parent'].append('0')
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
        elif (m=='eof'):
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
    create refid for <-->
    collect from iox ("<") till ">" into r0 ==> 8 or eof ==> 9
    """
    global pkg,nds
    ans = pkg['fioi'].fioi() # current "<"
    pc4 = 0
    while (pc4==0):
        tt = pkg['fioi'].fioi()
        if (tt == 'eof'):
            pc4 = -3
            print('bad format no ending ">"')
            ctl = -4
        if (tt=='>'): 
            nds['r0'] = ans + tt # <-->
            nds['refid'] = pkg['genx']()
            pc4 = -1
            ctl = 8
        else:
            ans = ans + tt
            loop = 1
        #endif
    #wend
    return(ctl)
#proc4

def  proc5():
     """ “done” ==> -1 """ 
    print('DONE')
    return(-1)
#end 5"

def proc8(): # 
    """
    optional collect iox(>) till next "<"-1; set r1 ==>16 eof ==> 16
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
        elif (tt == 'eof'):
            nds['r1'] = ans
            pc8 = -2
            ctl = 16
        else:
            ans = ans + tt
            loop = 1
        #endif
    #wend        
    return(ctl)
#proc8

def  proc9():
     """ “bad format no “>” ==> -2 """ 
    iox = pkg['fioi'].fioxGet()
    print('ERROR bad xml format no ending ">" at charicter position('+ iox + ')')
    return(-2)
#end 9"


def proc16(): # r0,r1 set collect l1x,l2x from r0 ==> 32 
    """
    r0,r1 set; collect l1x,l2x from r0; ==> 32 
    ATN pickup, previous, l1x,l2x
    """
    global pkg,nds
    nds['refid'] = pkg['genx']()
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
    pkg['ontology'].ATNWrite('pickup',str(nds['pu']), 'refid',str(nds['refid']))
    logg("ATN "+'pickup'+str(nds['pu'])+ 'refid'+ str(nds['refid']))
    pkg['ontology'].ATNWrite('previousPickup',str(nds['prevPu']), 'refid',str(nds['refid']))
    logg("ATN "+'previousPickup'+str(nds['prevPu'])+ 'refid'+str(nds['refid']))
    pkg['ontology'].ATNWrite('l1x',str(nds['l1x']), 'refid',str(nds['refid']))
    logg ("ATN"+ 'l1x'+str(nds['l1x'])+ 'refid'+str(nds['refid']))
    pkg['ontology'].ATNWrite('l2x',str(nds['l2x']), 'refid',str(nds['refid']))
    logg ("ATN"+ 'l2x'+ str(nds['l2x']) + 'refid'+str(nds['refid']))
    pkg['ontology'].ATNWrite('refid',str(nds['refid']), 'refid',str(nds['refid']))
    logg ("ATN"+  'refid'+str(nds['refid'])+'refid'+str(nds['refid']))
    ctl = 32
    return(ctl)
#proc16


def  proc32():
     """ Fan on l1x
     <? ==> 33 
    <! ==> 34
     </ ==>35
     else ==> 36 """ 
    if (nds['lx1']== "<?"):
        ctl = 33
    elif (nds['lx1']== "<!"):
        ctl = 34
    elif (nds['lx1']== "</"):
        ctl = 35
    else:
        ctl = 36
#end 32"
def  proc33():
     """ Goto 4 """ 
    return(4)
#end 33"
def  proc34():
     """ Goto 4 """ 
    return(4)
#end 34"
def  proc35():
     """ Goto 40 """ 
    return(40)
#end 35"
def  proc36():
     """ Goto 50 """ 
    return(50)
#end 36"
def  proc40():
    """
    "</" Endpoint process  pop parent ==>41
    """
    nds['parent'].pop()
    return(41)
#end 40"
def  proc41():
     """ 
    Special endpoints 
    /sequence = sequenceMode = 0 
    /choice = choiceMode = 0 
    ==>4 """ 
    if (nds['r0'].upper() == "</SEQUENCE>"):
        nds['sequenceMode'] = 0 #off
    #endif
    if (nds['r0'].upper() == "</CHOICE>"):
        nds['choiceMode'] = 0 #off
    #endif
    return(4)
#end 41"

def  proc50():
     """ Parse tag, 
        attributes
         append pu to parent 
        adjust minOccurs,maxOccurs  
        ATN tag , attr , {val=r1}
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
        logg("ATN "+'tag'+str(nds['tag'])+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('tag',str(nds['tag']), 'refid',str(nds['refid']))
        # r1 attribute
        nds['r1'] = nds['r1'].rstrip()
        nds['r1'] = nds['r1'].lstrip()
        if (len(r1) <> 0):
            logg("ATN "+'value'+str(nds['r1'])+ 'refid'+ str(nds['refid']))
            pkg['ontology'].ATNWrite('value',str(nds['r1']), 'refid',str(nds['refid']))
        #endif r1
    else: # <tag attr/> or >
        nds['tag'] = nds['r0'][1:spc]
        #collect & atn attributes; adjust min,max
        collectAttributes()
        # fix r1 if len>0 atn
        # r1 attribute
        nds['r1'] = nds['r1'].rstrip()
        nds['r1'] = nds['r1'].lstrip()
        if (len(r1) <> 0):
            logg("ATN "+'value'+str(nds['r1'])+ 'refid'+ str(nds['refid']))
            pkg['ontology'].ATNWrite('value',str(nds['r1']), 'refid',str(nds['refid']))
        #endif r1
    #endif # <tag attr/> or >
    return(51)
#end 50"
def  proc51():
     """ set first
        Best KRID  from attr - may have ns:
    """ 
    if (nds['first']==''):
        nds['first']=  nds['pu']
        #atn
    #endif
    # id,name,tag,pos
    # add position to attr
    nds['attr']['pos'] = nds['pu']
    # add tag
    nds['attr']['tag'] = nds['tag']
    #
    bestscore = 0
    bestkrid = ''
    for m in nds['attr']:
        #adjust for ns:
        aa = m.find(":")
        if (aa <> -1):
            m = m[aa+1:]
        #endif
        m = m.upper()
        if (m=='ID'):
            bestscore = 99
            bestkrid = nds['attr'][m].__str__()
        elif (m=='IDENTIFIER'):
            bestscore = 99
            bestkrid = nds['attr'][m].__str__()
        elif (m=='NAME'):
            if (bestscore < 90):
                bestscore = 90
                bestkrid = nds['attr'][m].__str__()
            #endif
        elif (m=='TAG'):
            if (bestscore < 80):
                bestscore = 80
                bestkrid = nds['attr'][m].__str__()
            #endif
        elif (m=='POS'):
            if (bestscore < 70):
                bestscore = 70
                bestkrid = nds['attr'][m].__str__()
            #endif
        else:
            nop = 1 # pos is guaranteed 
        #endif
        #atn
        logg("ATN "+'KRID'+str(bestkrid)+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('KRID',str(bestkrid), 'refid',str(nds['refid']))
        return(52)     
#end 51"
def  proc52():
     """ Special tag process - might have ns:
 element ==> 53 
complexType ==> 58 
sequence ==> 60 
choice ==> 62
 otherwise ==>53 """ 
    jj = nds['tag'].find(":")
    if (jj == -1):
        tag = nds['tag'][jj+1:].upper()
    else:
        tag = nds['tag'].upper()
    #endif
    if (tag == 'ELEMENT'):
        ctl = 53
    elif (tag == 'COMPLEXTYPE'):
        ctl = 58
    elif (tag == 'SEQUENCE'):
        ctl = 60
    elif (tag == 'CHOICE'):
        ctl = 62
    else:
        ctl = 53
    #endif
    return(ctl)    
#end 52"
def  proc53():
     """ Element mood process 
        if sequenceMode =1
            ATN master
            seq++
            ATN seq 
        if choiceMode=1
            ATN master
            seq++
            ATN seq
          ==>54   """ 
    if (nds['sequenceMode']==1):
        #atn master
        logg("ATN "+'master'+str(nds['master'])+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('master',str(nds['master']), 'refid',str(nds['refid']))
        nds['seq'] = nds['seq']+1
        #atn seq
        logg("ATN "+'seq'+str(nds['seq'])+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('seq',str(nds['seq']), 'refid',str(nds['refid']))
    #endif
    if (nds['choiceMode']==1):
        #atn master
        logg("ATN "+'master'+str(nds['master'])+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('master',str(nds['master']), 'refid',str(nds['refid']))
        nds['seq'] = nds['seq']+1
        #atn seq
        logg("ATN "+'seq'+str(nds['seq'])+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('seq',str(nds['seq']), 'refid',str(nds['refid']))
    #endif
    return(54)
#end 53"
def  proc54():
     """ Special attribute processing 
        if ref/ns:ref 
        -- ATN ref  
        -- RELATE ref refv predicate=ctpu;sqpu;elpu master,masterpu
        if [entryType]==>55 
        not entry type NOP ==>56   """ 
        for m in nds['attr']:
            aa = m.find(":")
            if (aa == -1):
                m = m[aa+1:]
            #endif
            if (m=='ref'):
                #relate ref refv predicate=ctpu;sqpu;elpu master,masterpu
                relateValue = "ct"+str(nds['ctpu'])+ 'sq'+str(nds['sqpu'])+'el'+str(nds['pu'])
                RELATEWrite( 'ref', str(nds['ref']), "Refered",relateValue,'refid', str(nds['refid']),flags='')
            #endif
        #for end
                
#end 54"
def  proc55():
     """ Entry type attributes 
        ATN defid=krid
         ==>56 """ 
#end 55"
def  proc56():
     """ L2x fan /> pop parent ==>4 x> ==>4     """ 
    if (nds['l2x']=="/>"):
        nds['parent'].pop()
    #endif
    return(4)
#end 56"

def  proc58():
     """ "<complexType "set master= previousPU  ==> 56   """ 
    nds['ctpu'] = nds['pu']
    nds['sqpu'] = ''
    nds['chpu'] = ''
#end 58"

def  proc60():
     """ "<sequence " set sequenceMode = 1 set seq=0 ==>56 """ 
    nds['sqpu'] = nds['pu']
    nds['seq'] =0
    nds['sequenceMode'] = 1
#end 60"

def  proc62():
     """ "<choice set" seq=0 set choiceMode=1 ==>56   """ 
    nds['seq'] =0
    nds['choiceMode'] = 1
    nds['chpu'] = nds['pu']
#end 62"

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
    ats = ats[spc+1:]
    cxc = 0
    while (cxc ==0):
        spc2 = ats.find(' ')
        if (spc2 ==-1):
            #do last
            c1 = ats
            atn,atv = c1.split('=')
            #adjust atv remove quotes if any
            mx = atv.find("'")
            if (mx <> -1):
                atv = atv[1:-1]
            #
            mx = atv.find('"')
            if (mx <> -1):
                atv = atv[1:-1]
            #
            nds['attr'][atn]=atv
            #atn
            logg("ATN "+atn+str(atv)+ 'refid'+ str(nds['refid']))
            pkg['ontology'].ATNWrite(atn,str(atv), 'refid',str(nds['refid']))
            cxc =-1
        else:
            c1 = ats[1:spc2]
            atn,atv = c1.split('=')
            #adjust atv remove quotes if any
            mx = atv.find("'")
            if (mx <> -1):
                atv = atv[1:-1]
            #
            mx = atv.find('"')
            if (mx <> -1):
                atv = atv[1:-1]
            #
            nds['attr'][atn]=atv
            #atn
            logg("ATN "+atn+str(atv)+ 'refid'+ str(nds['refid']))
            pkg['ontology'].ATNWrite(atn,str(atv), 'refid',str(nds['refid']))
            #reduce ats
            ats = ats[spc2+1:]
        #endif
    #wend
    #default min,max if not in attr might have ns: 
    jj = nds['attr'].keys().__str__()
    if (jj.find('minOccurs')== -1):
        logg("ATN "+'minOccurs'+'1'+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('minOccurs','1', 'refid',str(nds['refid']))
    #endif
    if (jj.find('maxOccurs')== -1):
        logg("ATN "+'maxOccurs'+'1'+ 'refid'+ str(nds['refid']))
        pkg['ontology'].ATNWrite('maxOccurs','1', 'refid',str(nds['refid']))
    #endif
#end collectAttributes
    
    
    




