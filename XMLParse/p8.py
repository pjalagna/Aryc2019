"""
file p8.py xsd/xml parse
usage main(filename{,trace}) renders to ontology fileName.onto
trace == "on" will print progress

"""
"""
test as



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
        if (ctl==1):
            ctl = init(fn)
        elif (ctl==2): # white till next "<"-1 ; ==> 4 or eof ==> 5
            ctl = proc2()
        elif (ctl==4): # collect till next ">"; set r0 ; ==> 8 or eof ==> 9
            ctl = proc4()
        elif (ctl==5): # eof on white
            ctl = proc5()
        elif (ctl==8): # eof on white
            ctl = proc8()
        elif (ctl==16): # eof on white
            ctl = proc16()
        elif (ctl==32): # eof on white
            ctl = proc32()
        elif (ctl==33): # eof on white
            ctl = proc33()
        elif (ctl==34): # eof on white
            ctl = proc34()
        elif (ctl==35): # eof on white
            ctl = proc35()
        elif (ctl==36): # eof on white
            ctl = proc36()
        else:
            print('error ctl ('+ctl.__str__()+')')
            ctl = -1
        #endif
    #wend
#main
def init(fn):
    print('initilizing')
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
    #refid
    import gennV
    pkg['genx'] = gennV.gennX
    return(2)
#init
def rets():
    global pkg,nds
    return(pkg,nds)
#
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
#proc1
def proc4():
    """
    create refid for <-->
    collect from iox ("<") till ">" ==> 8 or eof ==> 9
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
def proc5(): # eof on white
    print('stump')
    return(0)
#
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
     
#
def proc9(): #
    global pkg,nds 
    print('stump')
    return(0)
#

def proc16(): # r0,r1 set collect l1x,l2x from r0 ==> 32 
    """
    r0,r1 set; collect l1x,l2x from r0; ==> 32 
    ATN pickup, previous, l1x,l2x
    """
    global pkg,nds
    # set pu, prevpu
    nds['prevPu'] =nds['pu']
    nds['pu'] = nds['pu'] +1
    #record atn 
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
    # write atn pickup, previous, l1x
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
    

def proc32(): # fan on l1x 
    """
    l1x = <? ==> 33
    l1x = <! ==> 34
    l1x = </ ==> 35
    else     ==> 36
    """
    global pkg,nds
    if (nds['l1x'] == "<?"):
        ctl = 33
    elif (nds['l1x'] == "<!"):
        ctl = 34
    elif (nds['l1x'] == "</"):
        ctl = 35
    else:
        ctl = 36
    return(ctl)
#
def proc33(): # l1x == <?
    """
    proc33 l1x == <? ==> 4
    """
    logg("proc33 l1x == <? ==> 4")
    return(4)
#  
def proc34(): # 
    """
    proc34 l1x == <! ==> 4
    """
    logg("proc34 l1x == <! ==> 4")
    return(4)
#
def proc35(): # l1x == <?
    """
    proc35 l1x == </ ==> 40
    """
    logg("proc35 l1x == </ ==> 40")
    return(40)
# 
def proc36(): # l1x == <x
    """
    proc36 l1x == <x ==> 50
    """
    logg("proc36 l1x == <x ==> 50")
    return(50)
#     
def proc50(): #
    """
    NOT DONE
    proc50 l1x = <x
    {set first}
    append parent
    collect tag , {//collect attributes}
    fix r1 if len(r1) <> 0 attr[value] = r1
    on mode 
    -- atn with master
    -- seq++
    -- atn seq
    """
    """
    #set/record first = pu
    #parent.append(pu)
    #if r0 has space we have attributes and tag is [1:(sp-1)]
    #-- else 
    #--- if l2x <> />
    #------ tag = [1:-1]
    #----else tag = r0[1:-2]
    attr[] #blank
    // collect attributes from r0 keep ns
    fix r1 (trim l & r)
    if len(r1) <> 0 attr[value] = r1
    // write attributes
    ==> 51
    """
    global pkg,nds
    if (nds['first'] ==''):
        #atn first,pu,'',''
        nds['first'] = nds['pu']
    #endif
#proc50         
        
           
    
"""
dead code 

"""
    
    
    