
#file xsdP.py
#generated for xsdP.basii at Fri Apr 17 20:12:57 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def xbegin_1():
    global p
    logg('xbegin_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xbegin-1 processing verb ( xsdVersion ) ')
    if (r == p['OK']):
        logg('call xsdVersion ')
        p['sy']['xsdVersion'](p)
        logg('after xsdVersion')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xbegin-1 processing verb ( xsdInit ) ')
    if (r == p['OK']):
        logg('call xsdInit ')
        p['sy']['xsdInit'](p)
        logg('after xsdInit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xbegin-1 processing text ')
    logg("""L1""")
    if (r == p['OK']):
        logg('push text ' + """L1""")
        datPush("L1")
        logg('after ' + """L1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xbegin-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xbegin_1')
#end xbegin_1

def xbegin (x):
    global p
    logg('begin xbegin')
    ## point of umbrella
    xbeginCtl = 1 # starting spoke
    while xbeginCtl != 0:
        logg('loop xbeginCtl = ' + xbeginCtl.__str__())
        if (xbeginCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xbeginCtl == 1):
            logg('call xbegin_1')
            xbegin_1()
            logg('after call xbegin_1')
            # test and adjust for new spoke
            xbeginCtl = chk(xbeginCtl)

        else:
            #final
            logg('final xbegin')    
            xbeginCtl = 0 # break
        #endif
    #wend
#end xbegin

def L1_1():
    global p
    logg('L1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for L1-1 processing text ')
    logg("""p1""")
    if (r == p['OK']):
        logg('push text ' + """p1""")
        datPush("p1")
        logg('after ' + """p1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for L1-1 processing verb ( protected ) ')
    if (r == p['OK']):
        logg('call protected ')
        p['sy']['protected'](p)
        logg('after protected')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for L1-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for L1-1 processing text ')
    logg("""L1a1""")
    if (r == p['OK']):
        logg('push text ' + """L1a1""")
        datPush("L1a1")
        logg('after ' + """L1a1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for L1-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final L1_1')
#end L1_1

def L1 (x):
    global p
    logg('begin L1')
    ## point of umbrella
    L1Ctl = 1 # starting spoke
    while L1Ctl != 0:
        logg('loop L1Ctl = ' + L1Ctl.__str__())
        if (L1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (L1Ctl == 1):
            logg('call L1_1')
            L1_1()
            logg('after call L1_1')
            # test and adjust for new spoke
            L1Ctl = chk(L1Ctl)

        else:
            #final
            logg('final L1')    
            L1Ctl = 0 # break
        #endif
    #wend
#end L1

def p1_1():
    global p
    logg('p1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for p1-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for p1-1 processing text ')
    logg("""<""")
    if (r == p['OK']):
        logg('push text ' + """<""")
        datPush("<")
        logg('after ' + """<""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for p1-1 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for p1-1 processing verb ( xioo ) ')
    if (r == p['OK']):
        logg('call xioo ')
        p['sy']['xioo'](p)
        logg('after xioo')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final p1_1')
#end p1_1

def p1_2():
    global p
    logg('p1_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for p1-2 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final p1_2')
#end p1_2

def p1 (x):
    global p
    logg('begin p1')
    ## point of umbrella
    p1Ctl = 1 # starting spoke
    while p1Ctl != 0:
        logg('loop p1Ctl = ' + p1Ctl.__str__())
        if (p1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (p1Ctl == 1):
            logg('call p1_1')
            p1_1()
            logg('after call p1_1')
            # test and adjust for new spoke
            p1Ctl = chk(p1Ctl)

        elif (p1Ctl == 2):
            logg('call p1_2')
            p1_2()
            logg('after call p1_2')
            # test and adjust for new spoke
            p1Ctl = chk(p1Ctl)

        else:
            #final
            logg('final p1')    
            p1Ctl = 0 # break
        #endif
    #wend
#end p1

def L1a1_1():
    global p
    logg('L1a1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for L1a1-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for L1a1-1 processing text ')
    logg("""dl1.1""")
    if (r == p['OK']):
        logg('push text ' + """dl1.1""")
        datPush("dl1.1")
        logg('after ' + """dl1.1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for L1a1-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for L1a1-1 processing text ')
    logg("""fan1""")
    if (r == p['OK']):
        logg('push text ' + """fan1""")
        datPush("fan1")
        logg('after ' + """fan1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for L1a1-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final L1a1_1')
#end L1a1_1

def L1a1 (x):
    global p
    logg('begin L1a1')
    ## point of umbrella
    L1a1Ctl = 1 # starting spoke
    while L1a1Ctl != 0:
        logg('loop L1a1Ctl = ' + L1a1Ctl.__str__())
        if (L1a1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (L1a1Ctl == 1):
            logg('call L1a1_1')
            L1a1_1()
            logg('after call L1a1_1')
            # test and adjust for new spoke
            L1a1Ctl = chk(L1a1Ctl)

        else:
            #final
            logg('final L1a1')    
            L1a1Ctl = 0 # break
        #endif
    #wend
#end L1a1

def fan1_1():
    global p
    logg('fan1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan1-1 processing text ')
    logg("""dl1.1""")
    if (r == p['OK']):
        logg('push text ' + """dl1.1""")
        datPush("dl1.1")
        logg('after ' + """dl1.1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing text ')
    logg("""?""")
    if (r == p['OK']):
        logg('push text ' + """?""")
        datPush("?")
        logg('after ' + """?""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing text ')
    logg("""fan2""")
    if (r == p['OK']):
        logg('push text ' + """fan2""")
        datPush("fan2")
        logg('after ' + """fan2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing text ')
    logg("""schemaChk""")
    if (r == p['OK']):
        logg('push text ' + """schemaChk""")
        datPush("schemaChk")
        logg('after ' + """schemaChk""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing text ')
    logg("""lastChk""")
    if (r == p['OK']):
        logg('push text ' + """lastChk""")
        datPush("lastChk")
        logg('after ' + """lastChk""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan1_1')
#end fan1_1

def fan1_2():
    global p
    logg('fan1_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan1-2 processing text ')
    logg("""dl1.1""")
    if (r == p['OK']):
        logg('push text ' + """dl1.1""")
        datPush("dl1.1")
        logg('after ' + """dl1.1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing text ')
    logg("""!""")
    if (r == p['OK']):
        logg('push text ' + """!""")
        datPush("!")
        logg('after ' + """!""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing text ')
    logg("""procBang""")
    if (r == p['OK']):
        logg('push text ' + """procBang""")
        datPush("procBang")
        logg('after ' + """procBang""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing text ')
    logg("""lastChk""")
    if (r == p['OK']):
        logg('push text ' + """lastChk""")
        datPush("lastChk")
        logg('after ' + """lastChk""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan1_2')
#end fan1_2

def fan1_3():
    global p
    logg('fan1_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan1-3 processing text ')
    logg("""dl1.1""")
    if (r == p['OK']):
        logg('push text ' + """dl1.1""")
        datPush("dl1.1")
        logg('after ' + """dl1.1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-3 processing text ')
    logg("""/""")
    if (r == p['OK']):
        logg('push text ' + """/""")
        datPush("/")
        logg('after ' + """/""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-3 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-3 processing text ')
    logg("""fan4""")
    if (r == p['OK']):
        logg('push text ' + """fan4""")
        datPush("fan4")
        logg('after ' + """fan4""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan1_3')
#end fan1_3

def fan1_4():
    global p
    logg('fan1_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan1-4 processing text ')
    logg("""ParseNodeName""")
    if (r == p['OK']):
        logg('push text ' + """ParseNodeName""")
        datPush("ParseNodeName")
        logg('after ' + """ParseNodeName""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-4 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-4 processing text ')
    logg("""ParseAttributes""")
    if (r == p['OK']):
        logg('push text ' + """ParseAttributes""")
        datPush("ParseAttributes")
        logg('after ' + """ParseAttributes""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-4 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-4 processing text ')
    logg("""fan30""")
    if (r == p['OK']):
        logg('push text ' + """fan30""")
        datPush("fan30")
        logg('after ' + """fan30""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-4 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-4 processing text ')
    logg("""Garbage""")
    if (r == p['OK']):
        logg('push text ' + """Garbage""")
        datPush("Garbage")
        logg('after ' + """Garbage""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan1-4 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan1_4')
#end fan1_4

def fan1 (x):
    global p
    logg('begin fan1')
    ## point of umbrella
    fan1Ctl = 1 # starting spoke
    while fan1Ctl != 0:
        logg('loop fan1Ctl = ' + fan1Ctl.__str__())
        if (fan1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (fan1Ctl == 1):
            logg('call fan1_1')
            fan1_1()
            logg('after call fan1_1')
            # test and adjust for new spoke
            fan1Ctl = chk(fan1Ctl)

        elif (fan1Ctl == 2):
            logg('call fan1_2')
            fan1_2()
            logg('after call fan1_2')
            # test and adjust for new spoke
            fan1Ctl = chk(fan1Ctl)

        elif (fan1Ctl == 3):
            logg('call fan1_3')
            fan1_3()
            logg('after call fan1_3')
            # test and adjust for new spoke
            fan1Ctl = chk(fan1Ctl)

        elif (fan1Ctl == 4):
            logg('call fan1_4')
            fan1_4()
            logg('after call fan1_4')
            # test and adjust for new spoke
            fan1Ctl = chk(fan1Ctl)

        else:
            #final
            logg('final fan1')    
            fan1Ctl = 0 # break
        #endif
    #wend
#end fan1

def schemaChk_1():
    global p
    logg('schemaChk_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing text ')
    logg("""dcfan2""")
    if (r == p['OK']):
        logg('push text ' + """dcfan2""")
        datPush("dcfan2")
        logg('after ' + """dcfan2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing text ')
    logg("""schema""")
    if (r == p['OK']):
        logg('push text ' + """schema""")
        datPush("schema")
        logg('after ' + """schema""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing text ')
    logg("""schema""")
    if (r == p['OK']):
        logg('push text ' + """schema""")
        datPush("schema")
        logg('after ' + """schema""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing text ')
    logg("""parentPlus""")
    if (r == p['OK']):
        logg('push text ' + """parentPlus""")
        datPush("parentPlus")
        logg('after ' + """parentPlus""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing text ')
    logg("""parseAttributes""")
    if (r == p['OK']):
        logg('push text ' + """parseAttributes""")
        datPush("parseAttributes")
        logg('after ' + """parseAttributes""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing text ')
    logg("""writeRecords""")
    if (r == p['OK']):
        logg('push text ' + """writeRecords""")
        datPush("writeRecords")
        logg('after ' + """writeRecords""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for schemaChk-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final schemaChk_1')
#end schemaChk_1

def schemaChk_2():
    global p
    logg('schemaChk_2')
    datPush(p['OK'])

    #final
    logg('final schemaChk_2')
#end schemaChk_2

def schemaChk (x):
    global p
    logg('begin schemaChk')
    ## point of umbrella
    schemaChkCtl = 1 # starting spoke
    while schemaChkCtl != 0:
        logg('loop schemaChkCtl = ' + schemaChkCtl.__str__())
        if (schemaChkCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (schemaChkCtl == 1):
            logg('call schemaChk_1')
            schemaChk_1()
            logg('after call schemaChk_1')
            # test and adjust for new spoke
            schemaChkCtl = chk(schemaChkCtl)

        elif (schemaChkCtl == 2):
            logg('call schemaChk_2')
            schemaChk_2()
            logg('after call schemaChk_2')
            # test and adjust for new spoke
            schemaChkCtl = chk(schemaChkCtl)

        else:
            #final
            logg('final schemaChk')    
            schemaChkCtl = 0 # break
        #endif
    #wend
#end schemaChk

def parseAttributes_1():
    global p
    logg('parseAttributes_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for parseAttributes-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-1 processing text ')
    logg("""dpa""")
    if (r == p['OK']):
        logg('push text ' + """dpa""")
        datPush("dpa")
        logg('after ' + """dpa""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final parseAttributes_1')
#end parseAttributes_1

def parseAttributes_2():
    global p
    logg('parseAttributes_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing text ')
    logg("""dpa""")
    if (r == p['OK']):
        logg('push text ' + """dpa""")
        datPush("dpa")
        logg('after ' + """dpa""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing text ')
    logg(""" """)
    if (r == p['OK']):
        logg('push text ' + """ """)
        datPush(" ")
        logg('after ' + """ """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing text ')
    logg("""getattributeName""")
    if (r == p['OK']):
        logg('push text ' + """getattributeName""")
        datPush("getattributeName")
        logg('after ' + """getattributeName""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing text ')
    logg("""getAttributeValue""")
    if (r == p['OK']):
        logg('push text ' + """getAttributeValue""")
        datPush("getAttributeValue")
        logg('after ' + """getAttributeValue""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing text ')
    logg("""AttributeValue""")
    if (r == p['OK']):
        logg('push text ' + """AttributeValue""")
        datPush("AttributeValue")
        logg('after ' + """AttributeValue""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing text ')
    logg("""attName""")
    if (r == p['OK']):
        logg('push text ' + """attName""")
        datPush("attName")
        logg('after ' + """attName""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing text ')
    logg("""attList""")
    if (r == p['OK']):
        logg('push text ' + """attList""")
        datPush("attList")
        logg('after ' + """attList""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( dr! ) ')
    if (r == p['OK']):
        logg('call dr! ')
        p['sy']['dr!'](p)
        logg('after dr!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing text ')
    logg("""attList""")
    if (r == p['OK']):
        logg('push text ' + """attList""")
        datPush("attList")
        logg('after ' + """attList""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parseAttributes-2 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final parseAttributes_2')
#end parseAttributes_2

def parseAttributes_3():
    global p
    logg('parseAttributes_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for parseAttributes-3 processing verb ( xioo ) ')
    if (r == p['OK']):
        logg('call xioo ')
        p['sy']['xioo'](p)
        logg('after xioo')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final parseAttributes_3')
#end parseAttributes_3

def parseAttributes (x):
    global p
    logg('begin parseAttributes')
    ## point of umbrella
    parseAttributesCtl = 1 # starting spoke
    while parseAttributesCtl != 0:
        logg('loop parseAttributesCtl = ' + parseAttributesCtl.__str__())
        if (parseAttributesCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (parseAttributesCtl == 1):
            logg('call parseAttributes_1')
            parseAttributes_1()
            logg('after call parseAttributes_1')
            # test and adjust for new spoke
            parseAttributesCtl = chk(parseAttributesCtl)

        elif (parseAttributesCtl == 2):
            logg('call parseAttributes_2')
            parseAttributes_2()
            logg('after call parseAttributes_2')
            # test and adjust for new spoke
            parseAttributesCtl = chk(parseAttributesCtl)

        elif (parseAttributesCtl == 3):
            logg('call parseAttributes_3')
            parseAttributes_3()
            logg('after call parseAttributes_3')
            # test and adjust for new spoke
            parseAttributesCtl = chk(parseAttributesCtl)

        else:
            #final
            logg('final parseAttributes')    
            parseAttributesCtl = 0 # break
        #endif
    #wend
#end parseAttributes

def getAttributeValue_1():
    global p
    logg('getAttributeValue_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing verb ( dup ) ')
    if (r == p['OK']):
        logg('call dup ')
        p['sy']['dup'](p)
        logg('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing text ')
    logg("""gas""")
    if (r == p['OK']):
        logg('push text ' + """gas""")
        datPush("gas")
        logg('after ' + """gas""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing text ')
    logg("""=""")
    if (r == p['OK']):
        logg('push text ' + """=""")
        datPush("=")
        logg('after ' + """=""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing text ')
    logg("""""")
    if (r == p['OK']):
        logg('push text ' + """""")
        datPush("")
        logg('after ' + """""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing text ')
    logg("""AttributeValue""")
    if (r == p['OK']):
        logg('push text ' + """AttributeValue""")
        datPush("AttributeValue")
        logg('after ' + """AttributeValue""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing text ')
    logg("""""")
    if (r == p['OK']):
        logg('push text ' + """""")
        datPush("")
        logg('after ' + """""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-1 processing verb ( GAV2 ) ')
    if (r == p['OK']):
        logg('call GAV2 ')
        p['sy']['GAV2'](p)
        logg('after GAV2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final getAttributeValue_1')
#end getAttributeValue_1

def getAttributeValue_2():
    global p
    logg('getAttributeValue_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing text ')
    logg("""expectd = after attribute name got (""")
    if (r == p['OK']):
        logg('push text ' + """expectd = after attribute name got (""")
        datPush("expectd = after attribute name got (")
        logg('after ' + """expectd = after attribute name got (""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing text ')
    logg("""gas""")
    if (r == p['OK']):
        logg('push text ' + """gas""")
        datPush("gas")
        logg('after ' + """gas""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing text ')
    logg(""") instead""")
    if (r == p['OK']):
        logg('push text ' + """) instead""")
        datPush(") instead")
        logg('after ' + """) instead""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing text ')
    logg(""" at """)
    if (r == p['OK']):
        logg('push text ' + """ at """)
        datPush(" at ")
        logg('after ' + """ at """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing text ')
    logg("""xpos""")
    if (r == p['OK']):
        logg('push text ' + """xpos""")
        datPush("xpos")
        logg('after ' + """xpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing text ')
    logg("""abort""")
    if (r == p['OK']):
        logg('push text ' + """abort""")
        datPush("abort")
        logg('after ' + """abort""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getAttributeValue-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final getAttributeValue_2')
#end getAttributeValue_2

def getAttributeValue (x):
    global p
    logg('begin getAttributeValue')
    ## point of umbrella
    getAttributeValueCtl = 1 # starting spoke
    while getAttributeValueCtl != 0:
        logg('loop getAttributeValueCtl = ' + getAttributeValueCtl.__str__())
        if (getAttributeValueCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (getAttributeValueCtl == 1):
            logg('call getAttributeValue_1')
            getAttributeValue_1()
            logg('after call getAttributeValue_1')
            # test and adjust for new spoke
            getAttributeValueCtl = chk(getAttributeValueCtl)

        elif (getAttributeValueCtl == 2):
            logg('call getAttributeValue_2')
            getAttributeValue_2()
            logg('after call getAttributeValue_2')
            # test and adjust for new spoke
            getAttributeValueCtl = chk(getAttributeValueCtl)

        else:
            #final
            logg('final getAttributeValue')    
            getAttributeValueCtl = 0 # break
        #endif
    #wend
#end getAttributeValue

def GAV2_1():
    global p
    logg('GAV2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAV2-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-1 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAV2_1')
#end GAV2_1

def GAV2_2():
    global p
    logg('GAV2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAV2-2 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-2 processing verb ( Q? ) ')
    if (r == p['OK']):
        logg('call Q? ')
        p['sy']['Q?'](p)
        logg('after Q?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-2 processing text ')
    logg("""GAVtillQ""")
    if (r == p['OK']):
        logg('push text ' + """GAVtillQ""")
        datPush("GAVtillQ")
        logg('after ' + """GAVtillQ""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAV2_2')
#end GAV2_2

def GAV2_3():
    global p
    logg('GAV2_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAV2-3 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-3 processing verb ( T? ) ')
    if (r == p['OK']):
        logg('call T? ')
        p['sy']['T?'](p)
        logg('after T?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-3 processing text ')
    logg("""GAVtillT""")
    if (r == p['OK']):
        logg('push text ' + """GAVtillT""")
        datPush("GAVtillT")
        logg('after ' + """GAVtillT""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAV2_3')
#end GAV2_3

def GAV2_4():
    global p
    logg('GAV2_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAV2-4 processing text ')
    logg("""expected quoted string after =  got (""")
    if (r == p['OK']):
        logg('push text ' + """expected quoted string after =  got (""")
        datPush("expected quoted string after =  got (")
        logg('after ' + """expected quoted string after =  got (""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing text ')
    logg(""") instead. """)
    if (r == p['OK']):
        logg('push text ' + """) instead. """)
        datPush(") instead. ")
        logg('after ' + """) instead. """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing text ')
    logg(""" at """)
    if (r == p['OK']):
        logg('push text ' + """ at """)
        datPush(" at ")
        logg('after ' + """ at """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing text ')
    logg("""xpos""")
    if (r == p['OK']):
        logg('push text ' + """xpos""")
        datPush("xpos")
        logg('after ' + """xpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing text ')
    logg("""abort""")
    if (r == p['OK']):
        logg('push text ' + """abort""")
        datPush("abort")
        logg('after ' + """abort""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAV2-4 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAV2_4')
#end GAV2_4

def GAV2 (x):
    global p
    logg('begin GAV2')
    ## point of umbrella
    GAV2Ctl = 1 # starting spoke
    while GAV2Ctl != 0:
        logg('loop GAV2Ctl = ' + GAV2Ctl.__str__())
        if (GAV2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (GAV2Ctl == 1):
            logg('call GAV2_1')
            GAV2_1()
            logg('after call GAV2_1')
            # test and adjust for new spoke
            GAV2Ctl = chk(GAV2Ctl)

        elif (GAV2Ctl == 2):
            logg('call GAV2_2')
            GAV2_2()
            logg('after call GAV2_2')
            # test and adjust for new spoke
            GAV2Ctl = chk(GAV2Ctl)

        elif (GAV2Ctl == 3):
            logg('call GAV2_3')
            GAV2_3()
            logg('after call GAV2_3')
            # test and adjust for new spoke
            GAV2Ctl = chk(GAV2Ctl)

        elif (GAV2Ctl == 4):
            logg('call GAV2_4')
            GAV2_4()
            logg('after call GAV2_4')
            # test and adjust for new spoke
            GAV2Ctl = chk(GAV2Ctl)

        else:
            #final
            logg('final GAV2')    
            GAV2Ctl = 0 # break
        #endif
    #wend
#end GAV2

def GAVtillQ_1():
    global p
    logg('GAVtillQ_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAVtillQ-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-1 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAVtillQ_1')
#end GAVtillQ_1

def GAVtillQ_2():
    global p
    logg('GAVtillQ_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAVtillQ-2 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-2 processing verb ( Q? ) ')
    if (r == p['OK']):
        logg('call Q? ')
        p['sy']['Q?'](p)
        logg('after Q?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAVtillQ_2')
#end GAVtillQ_2

def GAVtillQ_3():
    global p
    logg('GAVtillQ_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAVtillQ-3 processing text ')
    logg("""AttributeValue""")
    if (r == p['OK']):
        logg('push text ' + """AttributeValue""")
        datPush("AttributeValue")
        logg('after ' + """AttributeValue""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-3 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-3 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-3 processing text ')
    logg("""AttributeValue""")
    if (r == p['OK']):
        logg('push text ' + """AttributeValue""")
        datPush("AttributeValue")
        logg('after ' + """AttributeValue""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-3 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillQ-3 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAVtillQ_3')
#end GAVtillQ_3

def GAVtillQ (x):
    global p
    logg('begin GAVtillQ')
    ## point of umbrella
    GAVtillQCtl = 1 # starting spoke
    while GAVtillQCtl != 0:
        logg('loop GAVtillQCtl = ' + GAVtillQCtl.__str__())
        if (GAVtillQCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (GAVtillQCtl == 1):
            logg('call GAVtillQ_1')
            GAVtillQ_1()
            logg('after call GAVtillQ_1')
            # test and adjust for new spoke
            GAVtillQCtl = chk(GAVtillQCtl)

        elif (GAVtillQCtl == 2):
            logg('call GAVtillQ_2')
            GAVtillQ_2()
            logg('after call GAVtillQ_2')
            # test and adjust for new spoke
            GAVtillQCtl = chk(GAVtillQCtl)

        elif (GAVtillQCtl == 3):
            logg('call GAVtillQ_3')
            GAVtillQ_3()
            logg('after call GAVtillQ_3')
            # test and adjust for new spoke
            GAVtillQCtl = chk(GAVtillQCtl)

        else:
            #final
            logg('final GAVtillQ')    
            GAVtillQCtl = 0 # break
        #endif
    #wend
#end GAVtillQ

def GAVtillT_1():
    global p
    logg('GAVtillT_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAVtillT-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-1 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAVtillT_1')
#end GAVtillT_1

def GAVtillT_2():
    global p
    logg('GAVtillT_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAVtillT-2 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-2 processing verb ( T? ) ')
    if (r == p['OK']):
        logg('call T? ')
        p['sy']['T?'](p)
        logg('after T?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAVtillT_2')
#end GAVtillT_2

def GAVtillT_3():
    global p
    logg('GAVtillT_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAVtillT-3 processing text ')
    logg("""AttributeValue""")
    if (r == p['OK']):
        logg('push text ' + """AttributeValue""")
        datPush("AttributeValue")
        logg('after ' + """AttributeValue""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-3 processing text ')
    logg("""dgav2""")
    if (r == p['OK']):
        logg('push text ' + """dgav2""")
        datPush("dgav2")
        logg('after ' + """dgav2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-3 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-3 processing text ')
    logg("""AttributeValue""")
    if (r == p['OK']):
        logg('push text ' + """AttributeValue""")
        datPush("AttributeValue")
        logg('after ' + """AttributeValue""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-3 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAVtillT-3 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAVtillT_3')
#end GAVtillT_3

def GAVtillT (x):
    global p
    logg('begin GAVtillT')
    ## point of umbrella
    GAVtillTCtl = 1 # starting spoke
    while GAVtillTCtl != 0:
        logg('loop GAVtillTCtl = ' + GAVtillTCtl.__str__())
        if (GAVtillTCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (GAVtillTCtl == 1):
            logg('call GAVtillT_1')
            GAVtillT_1()
            logg('after call GAVtillT_1')
            # test and adjust for new spoke
            GAVtillTCtl = chk(GAVtillTCtl)

        elif (GAVtillTCtl == 2):
            logg('call GAVtillT_2')
            GAVtillT_2()
            logg('after call GAVtillT_2')
            # test and adjust for new spoke
            GAVtillTCtl = chk(GAVtillTCtl)

        elif (GAVtillTCtl == 3):
            logg('call GAVtillT_3')
            GAVtillT_3()
            logg('after call GAVtillT_3')
            # test and adjust for new spoke
            GAVtillTCtl = chk(GAVtillTCtl)

        else:
            #final
            logg('final GAVtillT')    
            GAVtillTCtl = 0 # break
        #endif
    #wend
#end GAVtillT

def getattributeName_1():
    global p
    logg('getattributeName_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing text ')
    logg("""""")
    if (r == p['OK']):
        logg('push text ' + """""")
        datPush("")
        logg('after ' + """""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing text ')
    logg("""attName""")
    if (r == p['OK']):
        logg('push text ' + """attName""")
        datPush("attName")
        logg('after ' + """attName""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing text ')
    logg("""""")
    if (r == p['OK']):
        logg('push text ' + """""")
        datPush("")
        logg('after ' + """""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing text ')
    logg("""atc""")
    if (r == p['OK']):
        logg('push text ' + """atc""")
        datPush("atc")
        logg('after ' + """atc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing text ')
    logg("""GAN2""")
    if (r == p['OK']):
        logg('push text ' + """GAN2""")
        datPush("GAN2")
        logg('after ' + """GAN2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing text ')
    logg("""attName""")
    if (r == p['OK']):
        logg('push text ' + """attName""")
        datPush("attName")
        logg('after ' + """attName""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing text ')
    logg("""garbageIn""")
    if (r == p['OK']):
        logg('push text ' + """garbageIn""")
        datPush("garbageIn")
        logg('after ' + """garbageIn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getattributeName-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final getattributeName_1')
#end getattributeName_1

def getattributeName (x):
    global p
    logg('begin getattributeName')
    ## point of umbrella
    getattributeNameCtl = 1 # starting spoke
    while getattributeNameCtl != 0:
        logg('loop getattributeNameCtl = ' + getattributeNameCtl.__str__())
        if (getattributeNameCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (getattributeNameCtl == 1):
            logg('call getattributeName_1')
            getattributeName_1()
            logg('after call getattributeName_1')
            # test and adjust for new spoke
            getattributeNameCtl = chk(getattributeNameCtl)

        else:
            #final
            logg('final getattributeName')    
            getattributeNameCtl = 0 # break
        #endif
    #wend
#end getattributeName

def GAN2_1():
    global p
    logg('GAN2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAN2-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-1 processing text ')
    logg("""atc""")
    if (r == p['OK']):
        logg('push text ' + """atc""")
        datPush("atc")
        logg('after ' + """atc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAN2_1')
#end GAN2_1

def GAN2_2():
    global p
    logg('GAN2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAN2-2 processing text ')
    logg("""atc""")
    if (r == p['OK']):
        logg('push text ' + """atc""")
        datPush("atc")
        logg('after ' + """atc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-2 processing text ')
    logg("""=""")
    if (r == p['OK']):
        logg('push text ' + """=""")
        datPush("=")
        logg('after ' + """=""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-2 processing verb ( xioo ) ')
    if (r == p['OK']):
        logg('call xioo ')
        p['sy']['xioo'](p)
        logg('after xioo')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAN2_2')
#end GAN2_2

def GAN2_5():
    global p
    logg('GAN2_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GAN2-5 processing text ')
    logg("""attName""")
    if (r == p['OK']):
        logg('push text ' + """attName""")
        datPush("attName")
        logg('after ' + """attName""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-5 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-5 processing text ')
    logg("""atc""")
    if (r == p['OK']):
        logg('push text ' + """atc""")
        datPush("atc")
        logg('after ' + """atc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-5 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-5 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-5 processing text ')
    logg("""attName""")
    if (r == p['OK']):
        logg('push text ' + """attName""")
        datPush("attName")
        logg('after ' + """attName""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-5 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GAN2-5 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GAN2_5')
#end GAN2_5

def GAN2 (x):
    global p
    logg('begin GAN2')
    ## point of umbrella
    GAN2Ctl = 1 # starting spoke
    while GAN2Ctl != 0:
        logg('loop GAN2Ctl = ' + GAN2Ctl.__str__())
        if (GAN2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (GAN2Ctl == 1):
            logg('call GAN2_1')
            GAN2_1()
            logg('after call GAN2_1')
            # test and adjust for new spoke
            GAN2Ctl = chk(GAN2Ctl)

        elif (GAN2Ctl == 2):
            logg('call GAN2_2')
            GAN2_2()
            logg('after call GAN2_2')
            # test and adjust for new spoke
            GAN2Ctl = chk(GAN2Ctl)

        elif (GAN2Ctl == 3):
            logg('call GAN2_5')
            GAN2_5()
            logg('after call GAN2_5')
            # test and adjust for new spoke
            GAN2Ctl = chk(GAN2Ctl)

        else:
            #final
            logg('final GAN2')    
            GAN2Ctl = 0 # break
        #endif
    #wend
#end GAN2

def fan30_1():
    global p
    logg('fan30_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan30-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-1 processing text ')
    logg("""dfan30""")
    if (r == p['OK']):
        logg('push text ' + """dfan30""")
        datPush("dfan30")
        logg('after ' + """dfan30""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan30_1')
#end fan30_1

def fan30_2():
    global p
    logg('fan30_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan30-2 processing text ')
    logg("""dfan30""")
    if (r == p['OK']):
        logg('push text ' + """dfan30""")
        datPush("dfan30")
        logg('after ' + """dfan30""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing text ')
    logg("""/""")
    if (r == p['OK']):
        logg('push text ' + """/""")
        datPush("/")
        logg('after ' + """/""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing text ')
    logg("""ParentPlus""")
    if (r == p['OK']):
        logg('push text ' + """ParentPlus""")
        datPush("ParentPlus")
        logg('after ' + """ParentPlus""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing text ')
    logg("""writeRecords""")
    if (r == p['OK']):
        logg('push text ' + """writeRecords""")
        datPush("writeRecords")
        logg('after ' + """writeRecords""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing text ')
    logg("""ParentPop""")
    if (r == p['OK']):
        logg('push text ' + """ParentPop""")
        datPush("ParentPop")
        logg('after ' + """ParentPop""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing text ')
    logg("""lastChk""")
    if (r == p['OK']):
        logg('push text ' + """lastChk""")
        datPush("lastChk")
        logg('after ' + """lastChk""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan30_2')
#end fan30_2

def fan30_3():
    global p
    logg('fan30_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan30-3 processing text ')
    logg("""dfan30""")
    if (r == p['OK']):
        logg('push text ' + """dfan30""")
        datPush("dfan30")
        logg('after ' + """dfan30""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-3 processing text ')
    logg(""">""")
    if (r == p['OK']):
        logg('push text ' + """>""")
        datPush(">")
        logg('after ' + """>""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-3 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-3 processing text ')
    logg("""fctillLT2XN3""")
    if (r == p['OK']):
        logg('push text ' + """fctillLT2XN3""")
        datPush("fctillLT2XN3")
        logg('after ' + """fctillLT2XN3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-3 processing text ')
    logg("""XN3Fan""")
    if (r == p['OK']):
        logg('push text ' + """XN3Fan""")
        datPush("XN3Fan")
        logg('after ' + """XN3Fan""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan30_3')
#end fan30_3

def fan30_4():
    global p
    logg('fan30_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan30-4 processing text ')
    logg("""expected / or > after </name at (""")
    if (r == p['OK']):
        logg('push text ' + """expected / or > after </name at (""")
        datPush("expected / or > after </name at (")
        logg('after ' + """expected / or > after </name at (""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-4 processing text ')
    logg("""xpos""")
    if (r == p['OK']):
        logg('push text ' + """xpos""")
        datPush("xpos")
        logg('after ' + """xpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-4 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-4 processing text ')
    logg(""")""")
    if (r == p['OK']):
        logg('push text ' + """)""")
        datPush(")")
        logg('after ' + """)""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-4 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-4 processing text ')
    logg("""abort""")
    if (r == p['OK']):
        logg('push text ' + """abort""")
        datPush("abort")
        logg('after ' + """abort""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan30-4 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan30_4')
#end fan30_4

def fan30 (x):
    global p
    logg('begin fan30')
    ## point of umbrella
    fan30Ctl = 1 # starting spoke
    while fan30Ctl != 0:
        logg('loop fan30Ctl = ' + fan30Ctl.__str__())
        if (fan30Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (fan30Ctl == 1):
            logg('call fan30_1')
            fan30_1()
            logg('after call fan30_1')
            # test and adjust for new spoke
            fan30Ctl = chk(fan30Ctl)

        elif (fan30Ctl == 2):
            logg('call fan30_2')
            fan30_2()
            logg('after call fan30_2')
            # test and adjust for new spoke
            fan30Ctl = chk(fan30Ctl)

        elif (fan30Ctl == 3):
            logg('call fan30_3')
            fan30_3()
            logg('after call fan30_3')
            # test and adjust for new spoke
            fan30Ctl = chk(fan30Ctl)

        elif (fan30Ctl == 4):
            logg('call fan30_4')
            fan30_4()
            logg('after call fan30_4')
            # test and adjust for new spoke
            fan30Ctl = chk(fan30Ctl)

        else:
            #final
            logg('final fan30')    
            fan30Ctl = 0 # break
        #endif
    #wend
#end fan30

def fctillLT2XN3_1():
    global p
    logg('fctillLT2XN3_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fctillLT2XN3-1 processing text ')
    logg("""""")
    if (r == p['OK']):
        logg('push text ' + """""")
        datPush("")
        logg('after ' + """""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3-1 processing text ')
    logg("""XN3""")
    if (r == p['OK']):
        logg('push text ' + """XN3""")
        datPush("XN3")
        logg('after ' + """XN3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3-1 processing text ')
    logg("""""")
    if (r == p['OK']):
        logg('push text ' + """""")
        datPush("")
        logg('after ' + """""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3-1 processing text ')
    logg("""dxn3""")
    if (r == p['OK']):
        logg('push text ' + """dxn3""")
        datPush("dxn3")
        logg('after ' + """dxn3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3-1 processing text ')
    logg("""fctillLT2XN3a""")
    if (r == p['OK']):
        logg('push text ' + """fctillLT2XN3a""")
        datPush("fctillLT2XN3a")
        logg('after ' + """fctillLT2XN3a""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fctillLT2XN3_1')
#end fctillLT2XN3_1

def fctillLT2XN3 (x):
    global p
    logg('begin fctillLT2XN3')
    ## point of umbrella
    fctillLT2XN3Ctl = 1 # starting spoke
    while fctillLT2XN3Ctl != 0:
        logg('loop fctillLT2XN3Ctl = ' + fctillLT2XN3Ctl.__str__())
        if (fctillLT2XN3Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (fctillLT2XN3Ctl == 1):
            logg('call fctillLT2XN3_1')
            fctillLT2XN3_1()
            logg('after call fctillLT2XN3_1')
            # test and adjust for new spoke
            fctillLT2XN3Ctl = chk(fctillLT2XN3Ctl)

        else:
            #final
            logg('final fctillLT2XN3')    
            fctillLT2XN3Ctl = 0 # break
        #endif
    #wend
#end fctillLT2XN3

def fctillLT2XN3a_1():
    global p
    logg('fctillLT2XN3a_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-1 processing text ')
    logg("""dxn3""")
    if (r == p['OK']):
        logg('push text ' + """dxn3""")
        datPush("dxn3")
        logg('after ' + """dxn3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fctillLT2XN3a_1')
#end fctillLT2XN3a_1

def fctillLT2XN3a_2():
    global p
    logg('fctillLT2XN3a_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-2 processing text ')
    logg("""dxn3""")
    if (r == p['OK']):
        logg('push text ' + """dxn3""")
        datPush("dxn3")
        logg('after ' + """dxn3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-2 processing text ')
    logg("""<""")
    if (r == p['OK']):
        logg('push text ' + """<""")
        datPush("<")
        logg('after ' + """<""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-2 processing verb ( xioo ) ')
    if (r == p['OK']):
        logg('call xioo ')
        p['sy']['xioo'](p)
        logg('after xioo')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fctillLT2XN3a_2')
#end fctillLT2XN3a_2

def fctillLT2XN3a_3():
    global p
    logg('fctillLT2XN3a_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-3 processing text ')
    logg("""XN3""")
    if (r == p['OK']):
        logg('push text ' + """XN3""")
        datPush("XN3")
        logg('after ' + """XN3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-3 processing text ')
    logg("""dxn3""")
    if (r == p['OK']):
        logg('push text ' + """dxn3""")
        datPush("dxn3")
        logg('after ' + """dxn3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-3 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-3 processing text ')
    logg("""XN3""")
    if (r == p['OK']):
        logg('push text ' + """XN3""")
        datPush("XN3")
        logg('after ' + """XN3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-3 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fctillLT2XN3a-3 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fctillLT2XN3a_3')
#end fctillLT2XN3a_3

def fctillLT2XN3a (x):
    global p
    logg('begin fctillLT2XN3a')
    ## point of umbrella
    fctillLT2XN3aCtl = 1 # starting spoke
    while fctillLT2XN3aCtl != 0:
        logg('loop fctillLT2XN3aCtl = ' + fctillLT2XN3aCtl.__str__())
        if (fctillLT2XN3aCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (fctillLT2XN3aCtl == 1):
            logg('call fctillLT2XN3a_1')
            fctillLT2XN3a_1()
            logg('after call fctillLT2XN3a_1')
            # test and adjust for new spoke
            fctillLT2XN3aCtl = chk(fctillLT2XN3aCtl)

        elif (fctillLT2XN3aCtl == 2):
            logg('call fctillLT2XN3a_2')
            fctillLT2XN3a_2()
            logg('after call fctillLT2XN3a_2')
            # test and adjust for new spoke
            fctillLT2XN3aCtl = chk(fctillLT2XN3aCtl)

        elif (fctillLT2XN3aCtl == 3):
            logg('call fctillLT2XN3a_3')
            fctillLT2XN3a_3()
            logg('after call fctillLT2XN3a_3')
            # test and adjust for new spoke
            fctillLT2XN3aCtl = chk(fctillLT2XN3aCtl)

        else:
            #final
            logg('final fctillLT2XN3a')    
            fctillLT2XN3aCtl = 0 # break
        #endif
    #wend
#end fctillLT2XN3a

def XN3Fan_1():
    global p
    logg('XN3Fan_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing text ')
    logg("""XN3""")
    if (r == p['OK']):
        logg('push text ' + """XN3""")
        datPush("XN3")
        logg('after ' + """XN3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing verb ( white ) ')
    if (r == p['OK']):
        logg('call white ')
        p['sy']['white'](p)
        logg('after white')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing text ')
    logg("""XN3""")
    if (r == p['OK']):
        logg('push text ' + """XN3""")
        datPush("XN3")
        logg('after ' + """XN3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing verb ( [[ ) ')
    if (r == p['OK']):
        logg('call [[ ')
        p['sy']['[['](p)
        logg('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing verb ( 2 ) ')
    if (r == p['OK']):
        logg('call 2 ')
        p['sy']['2'](p)
        logg('after 2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing verb ( ]] ) ')
    if (r == p['OK']):
        logg('call ]] ')
        p['sy'][']]'](p)
        logg('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing text ')
    logg("""XN3""")
    if (r == p['OK']):
        logg('push text ' + """XN3""")
        datPush("XN3")
        logg('after ' + """XN3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing verb ( len ) ')
    if (r == p['OK']):
        logg('call len ')
        p['sy']['len'](p)
        logg('after len')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing text ')
    logg("""0""")
    if (r == p['OK']):
        logg('push text ' + """0""")
        datPush("0")
        logg('after ' + """0""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-1 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final XN3Fan_1')
#end XN3Fan_1

def XN3Fan_3():
    global p
    logg('XN3Fan_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing text ')
    logg("""XN3""")
    if (r == p['OK']):
        logg('push text ' + """XN3""")
        datPush("XN3")
        logg('after ' + """XN3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing text ')
    logg("""NodeValue""")
    if (r == p['OK']):
        logg('push text ' + """NodeValue""")
        datPush("NodeValue")
        logg('after ' + """NodeValue""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing text ')
    logg("""NodeValue""")
    if (r == p['OK']):
        logg('push text ' + """NodeValue""")
        datPush("NodeValue")
        logg('after ' + """NodeValue""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing text ')
    logg("""garbageIn""")
    if (r == p['OK']):
        logg('push text ' + """garbageIn""")
        datPush("garbageIn")
        logg('after ' + """garbageIn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing text ')
    logg("""parentPlus""")
    if (r == p['OK']):
        logg('push text ' + """parentPlus""")
        datPush("parentPlus")
        logg('after ' + """parentPlus""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing text ')
    logg("""writeRecords""")
    if (r == p['OK']):
        logg('push text ' + """writeRecords""")
        datPush("writeRecords")
        logg('after ' + """writeRecords""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XN3Fan-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final XN3Fan_3')
#end XN3Fan_3

def XN3Fan (x):
    global p
    logg('begin XN3Fan')
    ## point of umbrella
    XN3FanCtl = 1 # starting spoke
    while XN3FanCtl != 0:
        logg('loop XN3FanCtl = ' + XN3FanCtl.__str__())
        if (XN3FanCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (XN3FanCtl == 1):
            logg('call XN3Fan_1')
            XN3Fan_1()
            logg('after call XN3Fan_1')
            # test and adjust for new spoke
            XN3FanCtl = chk(XN3FanCtl)

        elif (XN3FanCtl == 2):
            logg('call XN3Fan_3')
            XN3Fan_3()
            logg('after call XN3Fan_3')
            # test and adjust for new spoke
            XN3FanCtl = chk(XN3FanCtl)

        else:
            #final
            logg('final XN3Fan')    
            XN3FanCtl = 0 # break
        #endif
    #wend
#end XN3Fan

def procBang_1():
    global p
    logg('procBang_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for procBang-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for procBang-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final procBang_1')
#end procBang_1

def procBang_2():
    global p
    logg('procBang_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for procBang-2 processing text ')
    logg("""!""")
    if (r == p['OK']):
        logg('push text ' + """!""")
        datPush("!")
        logg('after ' + """!""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for procBang-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final procBang_2')
#end procBang_2

def procBang_3():
    global p
    logg('procBang_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for procBang-3 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final procBang_3')
#end procBang_3

def procBang (x):
    global p
    logg('begin procBang')
    ## point of umbrella
    procBangCtl = 1 # starting spoke
    while procBangCtl != 0:
        logg('loop procBangCtl = ' + procBangCtl.__str__())
        if (procBangCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (procBangCtl == 1):
            logg('call procBang_1')
            procBang_1()
            logg('after call procBang_1')
            # test and adjust for new spoke
            procBangCtl = chk(procBangCtl)

        elif (procBangCtl == 2):
            logg('call procBang_2')
            procBang_2()
            logg('after call procBang_2')
            # test and adjust for new spoke
            procBangCtl = chk(procBangCtl)

        elif (procBangCtl == 3):
            logg('call procBang_3')
            procBang_3()
            logg('after call procBang_3')
            # test and adjust for new spoke
            procBangCtl = chk(procBangCtl)

        else:
            #final
            logg('final procBang')    
            procBangCtl = 0 # break
        #endif
    #wend
#end procBang

def fan2_1():
    global p
    logg('fan2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan2-1 processing text ')
    logg("""""")
    if (r == p['OK']):
        logg('push text ' + """""")
        datPush("")
        logg('after ' + """""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2-1 processing text ')
    logg("""dcfan2""")
    if (r == p['OK']):
        logg('push text ' + """dcfan2""")
        datPush("dcfan2")
        logg('after ' + """dcfan2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2-1 processing text ')
    logg("""fan2a""")
    if (r == p['OK']):
        logg('push text ' + """fan2a""")
        datPush("fan2a")
        logg('after ' + """fan2a""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan2_1')
#end fan2_1

def fan2 (x):
    global p
    logg('begin fan2')
    ## point of umbrella
    fan2Ctl = 1 # starting spoke
    while fan2Ctl != 0:
        logg('loop fan2Ctl = ' + fan2Ctl.__str__())
        if (fan2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (fan2Ctl == 1):
            logg('call fan2_1')
            fan2_1()
            logg('after call fan2_1')
            # test and adjust for new spoke
            fan2Ctl = chk(fan2Ctl)

        else:
            #final
            logg('final fan2')    
            fan2Ctl = 0 # break
        #endif
    #wend
#end fan2

def fan2a_1():
    global p
    logg('fan2a_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan2a-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-1 processing text ')
    logg("""dcfan2a""")
    if (r == p['OK']):
        logg('push text ' + """dcfan2a""")
        datPush("dcfan2a")
        logg('after ' + """dcfan2a""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan2a_1')
#end fan2a_1

def fan2a_2():
    global p
    logg('fan2a_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan2a-2 processing text ')
    logg("""dcfan2a""")
    if (r == p['OK']):
        logg('push text ' + """dcfan2a""")
        datPush("dcfan2a")
        logg('after ' + """dcfan2a""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-2 processing text ')
    logg(""" """)
    if (r == p['OK']):
        logg('push text ' + """ """)
        datPush(" ")
        logg('after ' + """ """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-2 processing verb ( xioo ) ')
    if (r == p['OK']):
        logg('call xioo ')
        p['sy']['xioo'](p)
        logg('after xioo')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan2a_2')
#end fan2a_2

def fan2a_3():
    global p
    logg('fan2a_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan2a-3 processing text ')
    logg("""dcfan2a""")
    if (r == p['OK']):
        logg('push text ' + """dcfan2a""")
        datPush("dcfan2a")
        logg('after ' + """dcfan2a""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-3 processing text ')
    logg("""?""")
    if (r == p['OK']):
        logg('push text ' + """?""")
        datPush("?")
        logg('after ' + """?""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-3 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-3 processing verb ( xioo ) ')
    if (r == p['OK']):
        logg('call xioo ')
        p['sy']['xioo'](p)
        logg('after xioo')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan2a_3')
#end fan2a_3

def fan2a_4():
    global p
    logg('fan2a_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan2a-4 processing text ')
    logg("""dcfan2a""")
    if (r == p['OK']):
        logg('push text ' + """dcfan2a""")
        datPush("dcfan2a")
        logg('after ' + """dcfan2a""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-4 processing text ')
    logg(""">""")
    if (r == p['OK']):
        logg('push text ' + """>""")
        datPush(">")
        logg('after ' + """>""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-4 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-4 processing verb ( xioo ) ')
    if (r == p['OK']):
        logg('call xioo ')
        p['sy']['xioo'](p)
        logg('after xioo')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan2a_4')
#end fan2a_4

def fan2a_5():
    global p
    logg('fan2a_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan2a-5 processing text ')
    logg("""dcfan2""")
    if (r == p['OK']):
        logg('push text ' + """dcfan2""")
        datPush("dcfan2")
        logg('after ' + """dcfan2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-5 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-5 processing text ')
    logg("""dcfan2a""")
    if (r == p['OK']):
        logg('push text ' + """dcfan2a""")
        datPush("dcfan2a")
        logg('after ' + """dcfan2a""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-5 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-5 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-5 processing text ')
    logg("""dcfan2""")
    if (r == p['OK']):
        logg('push text ' + """dcfan2""")
        datPush("dcfan2")
        logg('after ' + """dcfan2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-5 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan2a-5 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan2a_5')
#end fan2a_5

def fan2a (x):
    global p
    logg('begin fan2a')
    ## point of umbrella
    fan2aCtl = 1 # starting spoke
    while fan2aCtl != 0:
        logg('loop fan2aCtl = ' + fan2aCtl.__str__())
        if (fan2aCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (fan2aCtl == 1):
            logg('call fan2a_1')
            fan2a_1()
            logg('after call fan2a_1')
            # test and adjust for new spoke
            fan2aCtl = chk(fan2aCtl)

        elif (fan2aCtl == 2):
            logg('call fan2a_2')
            fan2a_2()
            logg('after call fan2a_2')
            # test and adjust for new spoke
            fan2aCtl = chk(fan2aCtl)

        elif (fan2aCtl == 3):
            logg('call fan2a_3')
            fan2a_3()
            logg('after call fan2a_3')
            # test and adjust for new spoke
            fan2aCtl = chk(fan2aCtl)

        elif (fan2aCtl == 4):
            logg('call fan2a_4')
            fan2a_4()
            logg('after call fan2a_4')
            # test and adjust for new spoke
            fan2aCtl = chk(fan2aCtl)

        elif (fan2aCtl == 5):
            logg('call fan2a_5')
            fan2a_5()
            logg('after call fan2a_5')
            # test and adjust for new spoke
            fan2aCtl = chk(fan2aCtl)

        else:
            #final
            logg('final fan2a')    
            fan2aCtl = 0 # break
        #endif
    #wend
#end fan2a

def ParseNodeName_1():
    global p
    logg('ParseNodeName_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ParseNodeName-1 processing text ')
    logg("""Xlabel""")
    if (r == p['OK']):
        logg('push text ' + """Xlabel""")
        datPush("Xlabel")
        logg('after ' + """Xlabel""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final ParseNodeName_1')
#end ParseNodeName_1

def ParseNodeName_2():
    global p
    logg('ParseNodeName_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ParseNodeName-2 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-2 processing text ')
    logg("""dpnn""")
    if (r == p['OK']):
        logg('push text ' + """dpnn""")
        datPush("dpnn")
        logg('after ' + """dpnn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-2 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-2 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final ParseNodeName_2')
#end ParseNodeName_2

def ParseNodeName_3():
    global p
    logg('ParseNodeName_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""dpnn""")
    if (r == p['OK']):
        logg('push text ' + """dpnn""")
        datPush("dpnn")
        logg('after ' + """dpnn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg(""":""")
    if (r == p['OK']):
        logg('push text ' + """:""")
        datPush(":")
        logg('after ' + """:""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""XN1""")
    if (r == p['OK']):
        logg('push text ' + """XN1""")
        datPush("XN1")
        logg('after ' + """XN1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""XMNLS""")
    if (r == p['OK']):
        logg('push text ' + """XMNLS""")
        datPush("XMNLS")
        logg('after ' + """XMNLS""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""Xlabel""")
    if (r == p['OK']):
        logg('push text ' + """Xlabel""")
        datPush("Xlabel")
        logg('after ' + """Xlabel""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""XN1""")
    if (r == p['OK']):
        logg('push text ' + """XN1""")
        datPush("XN1")
        logg('after ' + """XN1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""Xna""")
    if (r == p['OK']):
        logg('push text ' + """Xna""")
        datPush("Xna")
        logg('after ' + """Xna""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""Xna""")
    if (r == p['OK']):
        logg('push text ' + """Xna""")
        datPush("Xna")
        logg('after ' + """Xna""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""garbageIn""")
    if (r == p['OK']):
        logg('push text ' + """garbageIn""")
        datPush("garbageIn")
        logg('after ' + """garbageIn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""XMNLS""")
    if (r == p['OK']):
        logg('push text ' + """XMNLS""")
        datPush("XMNLS")
        logg('after ' + """XMNLS""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""garbageIn""")
    if (r == p['OK']):
        logg('push text ' + """garbageIn""")
        datPush("garbageIn")
        logg('after ' + """garbageIn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""PickupPosition""")
    if (r == p['OK']):
        logg('push text ' + """PickupPosition""")
        datPush("PickupPosition")
        logg('after ' + """PickupPosition""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( @++ ) ')
    if (r == p['OK']):
        logg('call @++ ')
        p['sy']['@++'](p)
        logg('after @++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""PickupPosition""")
    if (r == p['OK']):
        logg('push text ' + """PickupPosition""")
        datPush("PickupPosition")
        logg('after ' + """PickupPosition""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing text ')
    logg("""NodePosition""")
    if (r == p['OK']):
        logg('push text ' + """NodePosition""")
        datPush("NodePosition")
        logg('after ' + """NodePosition""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-3 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final ParseNodeName_3')
#end ParseNodeName_3

def ParseNodeName_4():
    global p
    logg('ParseNodeName_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing text ')
    logg("""XN1""")
    if (r == p['OK']):
        logg('push text ' + """XN1""")
        datPush("XN1")
        logg('after ' + """XN1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing text ')
    logg("""Xna""")
    if (r == p['OK']):
        logg('push text ' + """Xna""")
        datPush("Xna")
        logg('after ' + """Xna""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing text ')
    logg("""Xna""")
    if (r == p['OK']):
        logg('push text ' + """Xna""")
        datPush("Xna")
        logg('after ' + """Xna""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing text ')
    logg("""garbageIn""")
    if (r == p['OK']):
        logg('push text ' + """garbageIn""")
        datPush("garbageIn")
        logg('after ' + """garbageIn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing text ')
    logg("""PickupPosition""")
    if (r == p['OK']):
        logg('push text ' + """PickupPosition""")
        datPush("PickupPosition")
        logg('after ' + """PickupPosition""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing verb ( @++ ) ')
    if (r == p['OK']):
        logg('call @++ ')
        p['sy']['@++'](p)
        logg('after @++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing text ')
    logg("""PickupPosition""")
    if (r == p['OK']):
        logg('push text ' + """PickupPosition""")
        datPush("PickupPosition")
        logg('after ' + """PickupPosition""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing text ')
    logg("""NodePosition""")
    if (r == p['OK']):
        logg('push text ' + """NodePosition""")
        datPush("NodePosition")
        logg('after ' + """NodePosition""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ParseNodeName-4 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final ParseNodeName_4')
#end ParseNodeName_4

def ParseNodeName (x):
    global p
    logg('begin ParseNodeName')
    ## point of umbrella
    ParseNodeNameCtl = 1 # starting spoke
    while ParseNodeNameCtl != 0:
        logg('loop ParseNodeNameCtl = ' + ParseNodeNameCtl.__str__())
        if (ParseNodeNameCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (ParseNodeNameCtl == 1):
            logg('call ParseNodeName_1')
            ParseNodeName_1()
            logg('after call ParseNodeName_1')
            # test and adjust for new spoke
            ParseNodeNameCtl = chk(ParseNodeNameCtl)

        elif (ParseNodeNameCtl == 2):
            logg('call ParseNodeName_2')
            ParseNodeName_2()
            logg('after call ParseNodeName_2')
            # test and adjust for new spoke
            ParseNodeNameCtl = chk(ParseNodeNameCtl)

        elif (ParseNodeNameCtl == 3):
            logg('call ParseNodeName_3')
            ParseNodeName_3()
            logg('after call ParseNodeName_3')
            # test and adjust for new spoke
            ParseNodeNameCtl = chk(ParseNodeNameCtl)

        elif (ParseNodeNameCtl == 4):
            logg('call ParseNodeName_4')
            ParseNodeName_4()
            logg('after call ParseNodeName_4')
            # test and adjust for new spoke
            ParseNodeNameCtl = chk(ParseNodeNameCtl)

        else:
            #final
            logg('final ParseNodeName')    
            ParseNodeNameCtl = 0 # break
        #endif
    #wend
#end ParseNodeName

def fan4_1():
    global p
    logg('fan4_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fan4-1 processing text ')
    logg("""ParseNodeName""")
    if (r == p['OK']):
        logg('push text ' + """ParseNodeName""")
        datPush("ParseNodeName")
        logg('after ' + """ParseNodeName""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( [[ ) ')
    if (r == p['OK']):
        logg('call [[ ')
        p['sy']['[['](p)
        logg('after [[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( 2 ) ')
    if (r == p['OK']):
        logg('call 2 ')
        p['sy']['2'](p)
        logg('after 2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( ]] ) ')
    if (r == p['OK']):
        logg('call ]] ')
        p['sy'][']]'](p)
        logg('after ]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing text ')
    logg("""Xna""")
    if (r == p['OK']):
        logg('push text ' + """Xna""")
        datPush("Xna")
        logg('after ' + """Xna""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing text ')
    logg("""parent""")
    if (r == p['OK']):
        logg('push text ' + """parent""")
        datPush("parent")
        logg('after ' + """parent""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( ar# ) ')
    if (r == p['OK']):
        logg('call ar# ')
        p['sy']['ar#'](p)
        logg('after ar#')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( ar@ ) ')
    if (r == p['OK']):
        logg('call ar@ ')
        p['sy']['ar@'](p)
        logg('after ar@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing text ')
    logg("""parentPop""")
    if (r == p['OK']):
        logg('push text ' + """parentPop""")
        datPush("parentPop")
        logg('after ' + """parentPop""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing text ')
    logg("""lastChk""")
    if (r == p['OK']):
        logg('push text ' + """lastChk""")
        datPush("lastChk")
        logg('after ' + """lastChk""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fan4-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fan4_1')
#end fan4_1

def fan4_3():
    global p
    logg('fan4_3')
    datPush(p['OK'])

    #final
    logg('final fan4_3')
#end fan4_3

def fan4 (x):
    global p
    logg('begin fan4')
    ## point of umbrella
    fan4Ctl = 1 # starting spoke
    while fan4Ctl != 0:
        logg('loop fan4Ctl = ' + fan4Ctl.__str__())
        if (fan4Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (fan4Ctl == 1):
            logg('call fan4_1')
            fan4_1()
            logg('after call fan4_1')
            # test and adjust for new spoke
            fan4Ctl = chk(fan4Ctl)

        elif (fan4Ctl == 2):
            logg('call fan4_3')
            fan4_3()
            logg('after call fan4_3')
            # test and adjust for new spoke
            fan4Ctl = chk(fan4Ctl)

        else:
            #final
            logg('final fan4')    
            fan4Ctl = 0 # break
        #endif
    #wend
#end fan4

def lastChk_1():
    global p
    logg('lastChk_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for lastChk-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-1 processing text ')
    logg("""dlastc""")
    if (r == p['OK']):
        logg('push text ' + """dlastc""")
        datPush("dlastc")
        logg('after ' + """dlastc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final lastChk_1')
#end lastChk_1

def lastChk_2():
    global p
    logg('lastChk_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for lastChk-2 processing text ')
    logg("""dlastc""")
    if (r == p['OK']):
        logg('push text ' + """dlastc""")
        datPush("dlastc")
        logg('after ' + """dlastc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-2 processing text ')
    logg(""">""")
    if (r == p['OK']):
        logg('push text ' + """>""")
        datPush(">")
        logg('after ' + """>""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final lastChk_2')
#end lastChk_2

def lastChk_3():
    global p
    logg('lastChk_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for lastChk-3 processing text ')
    logg("""expected > got """)
    if (r == p['OK']):
        logg('push text ' + """expected > got """)
        datPush("expected > got ")
        logg('after ' + """expected > got """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing text ')
    logg("""dlastc""")
    if (r == p['OK']):
        logg('push text ' + """dlastc""")
        datPush("dlastc")
        logg('after ' + """dlastc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing text ')
    logg(""" instead at position (""")
    if (r == p['OK']):
        logg('push text ' + """ instead at position (""")
        datPush(" instead at position (")
        logg('after ' + """ instead at position (""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing text ')
    logg("""xpos""")
    if (r == p['OK']):
        logg('push text ' + """xpos""")
        datPush("xpos")
        logg('after ' + """xpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing text ')
    logg(""")""")
    if (r == p['OK']):
        logg('push text ' + """)""")
        datPush(")")
        logg('after ' + """)""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing text ')
    logg("""abort""")
    if (r == p['OK']):
        logg('push text ' + """abort""")
        datPush("abort")
        logg('after ' + """abort""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lastChk-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final lastChk_3')
#end lastChk_3

def lastChk (x):
    global p
    logg('begin lastChk')
    ## point of umbrella
    lastChkCtl = 1 # starting spoke
    while lastChkCtl != 0:
        logg('loop lastChkCtl = ' + lastChkCtl.__str__())
        if (lastChkCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (lastChkCtl == 1):
            logg('call lastChk_1')
            lastChk_1()
            logg('after call lastChk_1')
            # test and adjust for new spoke
            lastChkCtl = chk(lastChkCtl)

        elif (lastChkCtl == 2):
            logg('call lastChk_2')
            lastChk_2()
            logg('after call lastChk_2')
            # test and adjust for new spoke
            lastChkCtl = chk(lastChkCtl)

        elif (lastChkCtl == 3):
            logg('call lastChk_3')
            lastChk_3()
            logg('after call lastChk_3')
            # test and adjust for new spoke
            lastChkCtl = chk(lastChkCtl)

        else:
            #final
            logg('final lastChk')    
            lastChkCtl = 0 # break
        #endif
    #wend
#end lastChk

def xsdInit_1():
    global p
    logg('xsdInit_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""xsd file name""")
    if (r == p['OK']):
        logg('push text ' + """xsd file name""")
        datPush("xsd file name")
        logg('after ' + """xsd file name""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ask ) ')
    if (r == p['OK']):
        logg('call ask ')
        p['sy']['ask'](p)
        logg('after ask')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( dup ) ')
    if (r == p['OK']):
        logg('call dup ')
        p['sy']['dup'](p)
        logg('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""xsdfn""")
    if (r == p['OK']):
        logg('push text ' + """xsdfn""")
        datPush("xsdfn")
        logg('after ' + """xsdfn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""fileV""")
    if (r == p['OK']):
        logg('push text ' + """fileV""")
        datPush("fileV")
        logg('after ' + """fileV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( takeV ) ')
    if (r == p['OK']):
        logg('call takeV ')
        p['sy']['takeV'](p)
        logg('after takeV')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""xdb.db""")
    if (r == p['OK']):
        logg('push text ' + """xdb.db""")
        datPush("xdb.db")
        logg('after ' + """xdb.db""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""SQV""")
    if (r == p['OK']):
        logg('push text ' + """SQV""")
        datPush("SQV")
        logg('after ' + """SQV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( takeV ) ')
    if (r == p['OK']):
        logg('call takeV ')
        p['sy']['takeV'](p)
        logg('after takeV')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""TRCV""")
    if (r == p['OK']):
        logg('push text ' + """TRCV""")
        datPush("TRCV")
        logg('after ' + """TRCV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( takeV ) ')
    if (r == p['OK']):
        logg('call takeV ')
        p['sy']['takeV'](p)
        logg('after takeV')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""gennV""")
    if (r == p['OK']):
        logg('push text ' + """gennV""")
        datPush("gennV")
        logg('after ' + """gennV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( takeV ) ')
    if (r == p['OK']):
        logg('call takeV ')
        p['sy']['takeV'](p)
        logg('after takeV')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""arV""")
    if (r == p['OK']):
        logg('push text ' + """arV""")
        datPush("arV")
        logg('after ' + """arV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( takeV ) ')
    if (r == p['OK']):
        logg('call takeV ')
        p['sy']['takeV'](p)
        logg('after takeV')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""xsdfn""")
    if (r == p['OK']):
        logg('push text ' + """xsdfn""")
        datPush("xsdfn")
        logg('after ' + """xsdfn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( f@ ) ')
    if (r == p['OK']):
        logg('call f@ ')
        p['sy']['f@'](p)
        logg('after f@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""cxsdfn""")
    if (r == p['OK']):
        logg('push text ' + """cxsdfn""")
        datPush("cxsdfn")
        logg('after ' + """cxsdfn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( TRCV0 ) ')
    if (r == p['OK']):
        logg('call TRCV0 ')
        p['sy']['TRCV0'](p)
        logg('after TRCV0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( TRCV+ ) ')
    if (r == p['OK']):
        logg('call TRCV+ ')
        p['sy']['TRCV+'](p)
        logg('after TRCV+')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""0""")
    if (r == p['OK']):
        logg('push text ' + """0""")
        datPush("0")
        logg('after ' + """0""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""xfpos""")
    if (r == p['OK']):
        logg('push text ' + """xfpos""")
        datPush("xfpos")
        logg('after ' + """xfpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""0""")
    if (r == p['OK']):
        logg('push text ' + """0""")
        datPush("0")
        logg('after ' + """0""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""pu""")
    if (r == p['OK']):
        logg('push text ' + """pu""")
        datPush("pu")
        logg('after ' + """pu""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ar0 ) ')
    if (r == p['OK']):
        logg('call ar0 ')
        p['sy']['ar0'](p)
        logg('after ar0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""GCL""")
    if (r == p['OK']):
        logg('push text ' + """GCL""")
        datPush("GCL")
        logg('after ' + """GCL""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""0""")
    if (r == p['OK']):
        logg('push text ' + """0""")
        datPush("0")
        logg('after ' + """0""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""GCLix""")
    if (r == p['OK']):
        logg('push text ' + """GCLix""")
        datPush("GCLix")
        logg('after ' + """GCLix""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ar0 ) ')
    if (r == p['OK']):
        logg('call ar0 ')
        p['sy']['ar0'](p)
        logg('after ar0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""parents""")
    if (r == p['OK']):
        logg('push text ' + """parents""")
        datPush("parents")
        logg('after ' + """parents""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""0""")
    if (r == p['OK']):
        logg('push text ' + """0""")
        datPush("0")
        logg('after ' + """0""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""parentIX""")
    if (r == p['OK']):
        logg('push text ' + """parentIX""")
        datPush("parentIX")
        logg('after ' + """parentIX""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""""")
    if (r == p['OK']):
        logg('push text ' + """""")
        datPush("")
        logg('after ' + """""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""parentPlus""")
    if (r == p['OK']):
        logg('push text ' + """parentPlus""")
        datPush("parentPlus")
        logg('after ' + """parentPlus""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( dr0 ) ')
    if (r == p['OK']):
        logg('call dr0 ')
        p['sy']['dr0'](p)
        logg('after dr0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""attList""")
    if (r == p['OK']):
        logg('push text ' + """attList""")
        datPush("attList")
        logg('after ' + """attList""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""0""")
    if (r == p['OK']):
        logg('push text ' + """0""")
        datPush("0")
        logg('after ' + """0""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""epos""")
    if (r == p['OK']):
        logg('push text ' + """epos""")
        datPush("epos")
        logg('after ' + """epos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdInit_1')
#end xsdInit_1

def xsdInit (x):
    global p
    logg('begin xsdInit')
    ## point of umbrella
    xsdInitCtl = 1 # starting spoke
    while xsdInitCtl != 0:
        logg('loop xsdInitCtl = ' + xsdInitCtl.__str__())
        if (xsdInitCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdInitCtl == 1):
            logg('call xsdInit_1')
            xsdInit_1()
            logg('after call xsdInit_1')
            # test and adjust for new spoke
            xsdInitCtl = chk(xsdInitCtl)

        else:
            #final
            logg('final xsdInit')    
            xsdInitCtl = 0 # break
        #endif
    #wend
#end xsdInit

def parentPlus_1():
    global p
    logg('parentPlus_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing text ')
    logg("""parentIX""")
    if (r == p['OK']):
        logg('push text ' + """parentIX""")
        datPush("parentIX")
        logg('after ' + """parentIX""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing text ')
    logg("""parents""")
    if (r == p['OK']):
        logg('push text ' + """parents""")
        datPush("parents")
        logg('after ' + """parents""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing verb ( ar! ) ')
    if (r == p['OK']):
        logg('call ar! ')
        p['sy']['ar!'](p)
        logg('after ar!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing text ')
    logg("""parents""")
    if (r == p['OK']):
        logg('push text ' + """parents""")
        datPush("parents")
        logg('after ' + """parents""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing text ')
    logg("""parentIX""")
    if (r == p['OK']):
        logg('push text ' + """parentIX""")
        datPush("parentIX")
        logg('after ' + """parentIX""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing verb ( @++ ) ')
    if (r == p['OK']):
        logg('call @++ ')
        p['sy']['@++'](p)
        logg('after @++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for parentPlus-1 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final parentPlus_1')
#end parentPlus_1

def parentPlus (x):
    global p
    logg('begin parentPlus')
    ## point of umbrella
    parentPlusCtl = 1 # starting spoke
    while parentPlusCtl != 0:
        logg('loop parentPlusCtl = ' + parentPlusCtl.__str__())
        if (parentPlusCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (parentPlusCtl == 1):
            logg('call parentPlus_1')
            parentPlus_1()
            logg('after call parentPlus_1')
            # test and adjust for new spoke
            parentPlusCtl = chk(parentPlusCtl)

        else:
            #final
            logg('final parentPlus')    
            parentPlusCtl = 0 # break
        #endif
    #wend
#end parentPlus

def abort_1():
    global p
    logg('abort_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for abort-1 processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for abort-1 processing verb ( dumpNDS ) ')
    if (r == p['OK']):
        logg('call dumpNDS ')
        p['sy']['dumpNDS'](p)
        logg('after dumpNDS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for abort-1 processing verb ( .s ) ')
    if (r == p['OK']):
        logg('call .s ')
        p['sy']['.s'](p)
        logg('after .s')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for abort-1 processing text ')
    logg("""0""")
    if (r == p['OK']):
        logg('push text ' + """0""")
        datPush("0")
        logg('after ' + """0""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for abort-1 processing verb ( quit ) ')
    if (r == p['OK']):
        logg('call quit ')
        p['sy']['quit'](p)
        logg('after quit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final abort_1')
#end abort_1

def abort (x):
    global p
    logg('begin abort')
    ## point of umbrella
    abortCtl = 1 # starting spoke
    while abortCtl != 0:
        logg('loop abortCtl = ' + abortCtl.__str__())
        if (abortCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (abortCtl == 1):
            logg('call abort_1')
            abort_1()
            logg('after call abort_1')
            # test and adjust for new spoke
            abortCtl = chk(abortCtl)

        else:
            #final
            logg('final abort')    
            abortCtl = 0 # break
        #endif
    #wend
#end abort

def Xlabel_1():
    global p
    logg('Xlabel_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Xlabel-1 processing text ')
    logg("""""")
    if (r == p['OK']):
        logg('push text ' + """""")
        datPush("")
        logg('after ' + """""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel-1 processing text ')
    logg("""cstr""")
    if (r == p['OK']):
        logg('push text ' + """cstr""")
        datPush("cstr")
        logg('after ' + """cstr""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel-1 processing text ')
    logg("""xfpos""")
    if (r == p['OK']):
        logg('push text ' + """xfpos""")
        datPush("xfpos")
        logg('after ' + """xfpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel-1 processing text ')
    logg("""lfo""")
    if (r == p['OK']):
        logg('push text ' + """lfo""")
        datPush("lfo")
        logg('after ' + """lfo""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel-1 processing text ')
    logg("""Xlabel2""")
    if (r == p['OK']):
        logg('push text ' + """Xlabel2""")
        datPush("Xlabel2")
        logg('after ' + """Xlabel2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel-1 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Xlabel_1')
#end Xlabel_1

def Xlabel (x):
    global p
    logg('begin Xlabel')
    ## point of umbrella
    XlabelCtl = 1 # starting spoke
    while XlabelCtl != 0:
        logg('loop XlabelCtl = ' + XlabelCtl.__str__())
        if (XlabelCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (XlabelCtl == 1):
            logg('call Xlabel_1')
            Xlabel_1()
            logg('after call Xlabel_1')
            # test and adjust for new spoke
            XlabelCtl = chk(XlabelCtl)

        else:
            #final
            logg('final Xlabel')    
            XlabelCtl = 0 # break
        #endif
    #wend
#end Xlabel

def Xlabel2_1():
    global p
    logg('Xlabel2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Xlabel2-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-1 processing text ')
    logg("""lx""")
    if (r == p['OK']):
        logg('push text ' + """lx""")
        datPush("lx")
        logg('after ' + """lx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Xlabel2_1')
#end Xlabel2_1

def Xlabel2_2():
    global p
    logg('Xlabel2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Xlabel2-2 processing text ')
    logg("""lx""")
    if (r == p['OK']):
        logg('push text ' + """lx""")
        datPush("lx")
        logg('after ' + """lx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-2 processing text ')
    logg(""" """)
    if (r == p['OK']):
        logg('push text ' + """ """)
        datPush(" ")
        logg('after ' + """ """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-2 processing text ')
    logg("""XlabelFinal""")
    if (r == p['OK']):
        logg('push text ' + """XlabelFinal""")
        datPush("XlabelFinal")
        logg('after ' + """XlabelFinal""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-2 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Xlabel2_2')
#end Xlabel2_2

def Xlabel2_3():
    global p
    logg('Xlabel2_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Xlabel2-3 processing text ')
    logg("""lx""")
    if (r == p['OK']):
        logg('push text ' + """lx""")
        datPush("lx")
        logg('after ' + """lx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-3 processing text ')
    logg(""":""")
    if (r == p['OK']):
        logg('push text ' + """:""")
        datPush(":")
        logg('after ' + """:""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-3 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-3 processing text ')
    logg("""XlabelFinal""")
    if (r == p['OK']):
        logg('push text ' + """XlabelFinal""")
        datPush("XlabelFinal")
        logg('after ' + """XlabelFinal""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-3 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Xlabel2_3')
#end Xlabel2_3

def Xlabel2_4():
    global p
    logg('Xlabel2_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Xlabel2-4 processing text ')
    logg("""lx""")
    if (r == p['OK']):
        logg('push text ' + """lx""")
        datPush("lx")
        logg('after ' + """lx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-4 processing text ')
    logg("""/""")
    if (r == p['OK']):
        logg('push text ' + """/""")
        datPush("/")
        logg('after ' + """/""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-4 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-4 processing text ')
    logg("""XlabelFinal""")
    if (r == p['OK']):
        logg('push text ' + """XlabelFinal""")
        datPush("XlabelFinal")
        logg('after ' + """XlabelFinal""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-4 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Xlabel2_4')
#end Xlabel2_4

def Xlabel2_5():
    global p
    logg('Xlabel2_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Xlabel2-5 processing text ')
    logg("""lx""")
    if (r == p['OK']):
        logg('push text ' + """lx""")
        datPush("lx")
        logg('after ' + """lx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-5 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-5 processing text ')
    logg(""">""")
    if (r == p['OK']):
        logg('push text ' + """>""")
        datPush(">")
        logg('after ' + """>""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-5 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-5 processing text ')
    logg("""XlabelFinal""")
    if (r == p['OK']):
        logg('push text ' + """XlabelFinal""")
        datPush("XlabelFinal")
        logg('after ' + """XlabelFinal""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-5 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Xlabel2_5')
#end Xlabel2_5

def Xlabel2_6():
    global p
    logg('Xlabel2_6')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Xlabel2-6 processing text ')
    logg("""lx""")
    if (r == p['OK']):
        logg('push text ' + """lx""")
        datPush("lx")
        logg('after ' + """lx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-6 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-6 processing text ')
    logg("""=""")
    if (r == p['OK']):
        logg('push text ' + """=""")
        datPush("=")
        logg('after ' + """=""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-6 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-6 processing text ')
    logg("""XlabelFinal""")
    if (r == p['OK']):
        logg('push text ' + """XlabelFinal""")
        datPush("XlabelFinal")
        logg('after ' + """XlabelFinal""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-6 processing verb ( step ) ')
    if (r == p['OK']):
        logg('call step ')
        p['sy']['step'](p)
        logg('after step')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Xlabel2_6')
#end Xlabel2_6

def Xlabel2_7():
    global p
    logg('Xlabel2_7')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Xlabel2-7 processing text ')
    logg("""cstr""")
    if (r == p['OK']):
        logg('push text ' + """cstr""")
        datPush("cstr")
        logg('after ' + """cstr""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-7 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-7 processing text ')
    logg("""lx""")
    if (r == p['OK']):
        logg('push text ' + """lx""")
        datPush("lx")
        logg('after ' + """lx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-7 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-7 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-7 processing text ')
    logg("""cstr""")
    if (r == p['OK']):
        logg('push text ' + """cstr""")
        datPush("cstr")
        logg('after ' + """cstr""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-7 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Xlabel2-7 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Xlabel2_7')
#end Xlabel2_7

def Xlabel2 (x):
    global p
    logg('begin Xlabel2')
    ## point of umbrella
    Xlabel2Ctl = 1 # starting spoke
    while Xlabel2Ctl != 0:
        logg('loop Xlabel2Ctl = ' + Xlabel2Ctl.__str__())
        if (Xlabel2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (Xlabel2Ctl == 1):
            logg('call Xlabel2_1')
            Xlabel2_1()
            logg('after call Xlabel2_1')
            # test and adjust for new spoke
            Xlabel2Ctl = chk(Xlabel2Ctl)

        elif (Xlabel2Ctl == 2):
            logg('call Xlabel2_2')
            Xlabel2_2()
            logg('after call Xlabel2_2')
            # test and adjust for new spoke
            Xlabel2Ctl = chk(Xlabel2Ctl)

        elif (Xlabel2Ctl == 3):
            logg('call Xlabel2_3')
            Xlabel2_3()
            logg('after call Xlabel2_3')
            # test and adjust for new spoke
            Xlabel2Ctl = chk(Xlabel2Ctl)

        elif (Xlabel2Ctl == 4):
            logg('call Xlabel2_4')
            Xlabel2_4()
            logg('after call Xlabel2_4')
            # test and adjust for new spoke
            Xlabel2Ctl = chk(Xlabel2Ctl)

        elif (Xlabel2Ctl == 5):
            logg('call Xlabel2_5')
            Xlabel2_5()
            logg('after call Xlabel2_5')
            # test and adjust for new spoke
            Xlabel2Ctl = chk(Xlabel2Ctl)

        elif (Xlabel2Ctl == 6):
            logg('call Xlabel2_6')
            Xlabel2_6()
            logg('after call Xlabel2_6')
            # test and adjust for new spoke
            Xlabel2Ctl = chk(Xlabel2Ctl)

        elif (Xlabel2Ctl == 7):
            logg('call Xlabel2_7')
            Xlabel2_7()
            logg('after call Xlabel2_7')
            # test and adjust for new spoke
            Xlabel2Ctl = chk(Xlabel2Ctl)

        else:
            #final
            logg('final Xlabel2')    
            Xlabel2Ctl = 0 # break
        #endif
    #wend
#end Xlabel2

def XlabelFinal_1():
    global p
    logg('XlabelFinal_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for XlabelFinal-1 processing text ')
    logg("""cstr""")
    if (r == p['OK']):
        logg('push text ' + """cstr""")
        datPush("cstr")
        logg('after ' + """cstr""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-1 processing verb ( len ) ')
    if (r == p['OK']):
        logg('call len ')
        p['sy']['len'](p)
        logg('after len')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-1 processing text ')
    logg("""0""")
    if (r == p['OK']):
        logg('push text ' + """0""")
        datPush("0")
        logg('after ' + """0""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-1 processing verb ( <> ) ')
    if (r == p['OK']):
        logg('call <> ')
        p['sy']['<>'](p)
        logg('after <>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-1 processing verb ( xioo ) ')
    if (r == p['OK']):
        logg('call xioo ')
        p['sy']['xioo'](p)
        logg('after xioo')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-1 processing text ')
    logg("""csrt""")
    if (r == p['OK']):
        logg('push text ' + """csrt""")
        datPush("csrt")
        logg('after ' + """csrt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final XlabelFinal_1')
#end XlabelFinal_1

def XlabelFinal_2():
    global p
    logg('XlabelFinal_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for XlabelFinal-2 processing text ')
    logg("""lfo""")
    if (r == p['OK']):
        logg('push text ' + """lfo""")
        datPush("lfo")
        logg('after ' + """lfo""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-2 processing text ')
    logg("""xfpos""")
    if (r == p['OK']):
        logg('push text ' + """xfpos""")
        datPush("xfpos")
        logg('after ' + """xfpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-2 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for XlabelFinal-2 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final XlabelFinal_2')
#end XlabelFinal_2

def XlabelFinal (x):
    global p
    logg('begin XlabelFinal')
    ## point of umbrella
    XlabelFinalCtl = 1 # starting spoke
    while XlabelFinalCtl != 0:
        logg('loop XlabelFinalCtl = ' + XlabelFinalCtl.__str__())
        if (XlabelFinalCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (XlabelFinalCtl == 1):
            logg('call XlabelFinal_1')
            XlabelFinal_1()
            logg('after call XlabelFinal_1')
            # test and adjust for new spoke
            XlabelFinalCtl = chk(XlabelFinalCtl)

        elif (XlabelFinalCtl == 2):
            logg('call XlabelFinal_2')
            XlabelFinal_2()
            logg('after call XlabelFinal_2')
            # test and adjust for new spoke
            XlabelFinalCtl = chk(XlabelFinalCtl)

        else:
            #final
            logg('final XlabelFinal')    
            XlabelFinalCtl = 0 # break
        #endif
    #wend
#end XlabelFinal

def xioi_1():
    global p
    logg('xioi_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xioi-1 processing text ')
    logg("""xpos=(""")
    if (r == p['OK']):
        logg('push text ' + """xpos=(""")
        datPush("xpos=(")
        logg('after ' + """xpos=(""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing text ')
    logg("""xfpos""")
    if (r == p['OK']):
        logg('push text ' + """xfpos""")
        datPush("xfpos")
        logg('after ' + """xfpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing text ')
    logg(""")""")
    if (r == p['OK']):
        logg('push text ' + """)""")
        datPush(")")
        logg('after ' + """)""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing text ')
    logg("""cxsdfn""")
    if (r == p['OK']):
        logg('push text ' + """cxsdfn""")
        datPush("cxsdfn")
        logg('after ' + """cxsdfn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing text ')
    logg("""xfpos""")
    if (r == p['OK']):
        logg('push text ' + """xfpos""")
        datPush("xfpos")
        logg('after ' + """xfpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( cut ) ')
    if (r == p['OK']):
        logg('call cut ')
        p['sy']['cut'](p)
        logg('after cut')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( swap ) ')
    if (r == p['OK']):
        logg('call swap ')
        p['sy']['swap'](p)
        logg('after swap')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( c1 ) ')
    if (r == p['OK']):
        logg('call c1 ')
        p['sy']['c1'](p)
        logg('after c1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing text ')
    logg("""xfpos""")
    if (r == p['OK']):
        logg('push text ' + """xfpos""")
        datPush("xfpos")
        logg('after ' + """xfpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( @++ ) ')
    if (r == p['OK']):
        logg('call @++ ')
        p['sy']['@++'](p)
        logg('after @++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( dup ) ')
    if (r == p['OK']):
        logg('call dup ')
        p['sy']['dup'](p)
        logg('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing text ')
    logg("""ans=(""")
    if (r == p['OK']):
        logg('push text ' + """ans=(""")
        datPush("ans=(")
        logg('after ' + """ans=(""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( swap ) ')
    if (r == p['OK']):
        logg('call swap ')
        p['sy']['swap'](p)
        logg('after swap')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing text ')
    logg(""")""")
    if (r == p['OK']):
        logg('push text ' + """)""")
        datPush(")")
        logg('after ' + """)""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioi-1 processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xioi_1')
#end xioi_1

def xioi (x):
    global p
    logg('begin xioi')
    ## point of umbrella
    xioiCtl = 1 # starting spoke
    while xioiCtl != 0:
        logg('loop xioiCtl = ' + xioiCtl.__str__())
        if (xioiCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xioiCtl == 1):
            logg('call xioi_1')
            xioi_1()
            logg('after call xioi_1')
            # test and adjust for new spoke
            xioiCtl = chk(xioiCtl)

        else:
            #final
            logg('final xioi')    
            xioiCtl = 0 # break
        #endif
    #wend
#end xioi

def garbageIn_1():
    global p
    logg('garbageIn_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing text ')
    logg("""GCLix""")
    if (r == p['OK']):
        logg('push text ' + """GCLix""")
        datPush("GCLix")
        logg('after ' + """GCLix""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing text ')
    logg("""GCL""")
    if (r == p['OK']):
        logg('push text ' + """GCL""")
        datPush("GCL")
        logg('after ' + """GCL""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing verb ( ar! ) ')
    if (r == p['OK']):
        logg('call ar! ')
        p['sy']['ar!'](p)
        logg('after ar!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing text ')
    logg("""GCL""")
    if (r == p['OK']):
        logg('push text ' + """GCL""")
        datPush("GCL")
        logg('after ' + """GCL""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing text ')
    logg("""GCLix""")
    if (r == p['OK']):
        logg('push text ' + """GCLix""")
        datPush("GCLix")
        logg('after ' + """GCLix""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing verb ( @++ ) ')
    if (r == p['OK']):
        logg('call @++ ')
        p['sy']['@++'](p)
        logg('after @++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for garbageIn-1 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final garbageIn_1')
#end garbageIn_1

def garbageIn (x):
    global p
    logg('begin garbageIn')
    ## point of umbrella
    garbageInCtl = 1 # starting spoke
    while garbageInCtl != 0:
        logg('loop garbageInCtl = ' + garbageInCtl.__str__())
        if (garbageInCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (garbageInCtl == 1):
            logg('call garbageIn_1')
            garbageIn_1()
            logg('after call garbageIn_1')
            # test and adjust for new spoke
            garbageInCtl = chk(garbageInCtl)

        else:
            #final
            logg('final garbageIn')    
            garbageInCtl = 0 # break
        #endif
    #wend
#end garbageIn

def xxioi_1():
    global p
    logg('xxioi_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xxioi-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xxioi-1 processing verb ( xioi ) ')
    if (r == p['OK']):
        logg('call xioi ')
        p['sy']['xioi'](p)
        logg('after xioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xxioi-1 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xxioi_1')
#end xxioi_1

def xxioi (x):
    global p
    logg('begin xxioi')
    ## point of umbrella
    xxioiCtl = 1 # starting spoke
    while xxioiCtl != 0:
        logg('loop xxioiCtl = ' + xxioiCtl.__str__())
        if (xxioiCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xxioiCtl == 1):
            logg('call xxioi_1')
            xxioi_1()
            logg('after call xxioi_1')
            # test and adjust for new spoke
            xxioiCtl = chk(xxioiCtl)

        else:
            #final
            logg('final xxioi')    
            xxioiCtl = 0 # break
        #endif
    #wend
#end xxioi

def xioo_1():
    global p
    logg('xioo_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xioo-1 processing text ')
    logg("""xfpos""")
    if (r == p['OK']):
        logg('push text ' + """xfpos""")
        datPush("xfpos")
        logg('after ' + """xfpos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioo-1 processing verb ( @-- ) ')
    if (r == p['OK']):
        logg('call @-- ')
        p['sy']['@--'](p)
        logg('after @--')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xioo-1 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xioo_1')
#end xioo_1

def xioo (x):
    global p
    logg('begin xioo')
    ## point of umbrella
    xiooCtl = 1 # starting spoke
    while xiooCtl != 0:
        logg('loop xiooCtl = ' + xiooCtl.__str__())
        if (xiooCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xiooCtl == 1):
            logg('call xioo_1')
            xioo_1()
            logg('after call xioo_1')
            # test and adjust for new spoke
            xiooCtl = chk(xiooCtl)

        else:
            #final
            logg('final xioo')    
            xiooCtl = 0 # break
        #endif
    #wend
#end xioo

def step_1():
    global p
    logg('step_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for step-1 processing text ')
    logg("""sta""")
    if (r == p['OK']):
        logg('push text ' + """sta""")
        datPush("sta")
        logg('after ' + """sta""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing text ')
    logg("""step """)
    if (r == p['OK']):
        logg('push text ' + """step """)
        datPush("step ")
        logg('after ' + """step """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing text ')
    logg("""sta""")
    if (r == p['OK']):
        logg('push text ' + """sta""")
        datPush("sta")
        logg('after ' + """sta""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing text ')
    logg("""- null""")
    if (r == p['OK']):
        logg('push text ' + """- null""")
        datPush("- null")
        logg('after ' + """- null""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing verb ( cat ) ')
    if (r == p['OK']):
        logg('call cat ')
        p['sy']['cat'](p)
        logg('after cat')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing verb ( ask ) ')
    if (r == p['OK']):
        logg('call ask ')
        p['sy']['ask'](p)
        logg('after ask')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing text ')
    logg("""stx""")
    if (r == p['OK']):
        logg('push text ' + """stx""")
        datPush("stx")
        logg('after ' + """stx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final step_1')
#end step_1

def step_2():
    global p
    logg('step_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for step-2 processing text ')
    logg("""stx""")
    if (r == p['OK']):
        logg('push text ' + """stx""")
        datPush("stx")
        logg('after ' + """stx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-2 processing verb ( len ) ')
    if (r == p['OK']):
        logg('call len ')
        p['sy']['len'](p)
        logg('after len')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-2 processing text ')
    logg("""0""")
    if (r == p['OK']):
        logg('push text ' + """0""")
        datPush("0")
        logg('after ' + """0""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-2 processing text ')
    logg("""sta""")
    if (r == p['OK']):
        logg('push text ' + """sta""")
        datPush("sta")
        logg('after ' + """sta""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for step-2 processing verb ( .X ) ')
    if (r == p['OK']):
        logg('call .X ')
        p['sy']['.X'](p)
        logg('after .X')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final step_2')
#end step_2

def step_3():
    global p
    logg('step_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for step-3 processing verb ( bmain ) ')
    if (r == p['OK']):
        logg('call bmain ')
        p['sy']['bmain'](p)
        logg('after bmain')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final step_3')
#end step_3

def step (x):
    global p
    logg('begin step')
    ## point of umbrella
    stepCtl = 1 # starting spoke
    while stepCtl != 0:
        logg('loop stepCtl = ' + stepCtl.__str__())
        if (stepCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (stepCtl == 1):
            logg('call step_1')
            step_1()
            logg('after call step_1')
            # test and adjust for new spoke
            stepCtl = chk(stepCtl)

        elif (stepCtl == 2):
            logg('call step_2')
            step_2()
            logg('after call step_2')
            # test and adjust for new spoke
            stepCtl = chk(stepCtl)

        elif (stepCtl == 3):
            logg('call step_3')
            step_3()
            logg('after call step_3')
            # test and adjust for new spoke
            stepCtl = chk(stepCtl)

        else:
            #final
            logg('final step')    
            stepCtl = 0 # break
        #endif
    #wend
#end step

def writeRecords_1():
    global p
    logg('writeRecords_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for writeRecords-1 processing text ')
    logg("""stump for now""")
    if (r == p['OK']):
        logg('push text ' + """stump for now""")
        datPush("stump for now")
        logg('after ' + """stump for now""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRecords-1 processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRecords-1 processing verb ( .s ) ')
    if (r == p['OK']):
        logg('call .s ')
        p['sy']['.s'](p)
        logg('after .s')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRecords-1 processing verb ( dumpNDS ) ')
    if (r == p['OK']):
        logg('call dumpNDS ')
        p['sy']['dumpNDS'](p)
        logg('after dumpNDS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRecords-1 processing text ')
    logg("""??""")
    if (r == p['OK']):
        logg('push text ' + """??""")
        datPush("??")
        logg('after ' + """??""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRecords-1 processing verb ( ask ) ')
    if (r == p['OK']):
        logg('call ask ')
        p['sy']['ask'](p)
        logg('after ask')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final writeRecords_1')
#end writeRecords_1

def writeRecords (x):
    global p
    logg('begin writeRecords')
    ## point of umbrella
    writeRecordsCtl = 1 # starting spoke
    while writeRecordsCtl != 0:
        logg('loop writeRecordsCtl = ' + writeRecordsCtl.__str__())
        if (writeRecordsCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (writeRecordsCtl == 1):
            logg('call writeRecords_1')
            writeRecords_1()
            logg('after call writeRecords_1')
            # test and adjust for new spoke
            writeRecordsCtl = chk(writeRecordsCtl)

        else:
            #final
            logg('final writeRecords')    
            writeRecordsCtl = 0 # break
        #endif
    #wend
#end writeRecords

def bmain_1():
    global p
    logg('bmain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for bmain-1 processing text ')
    logg(""">?""")
    if (r == p['OK']):
        logg('push text ' + """>?""")
        datPush(">?")
        logg('after ' + """>?""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing verb ( ask ) ')
    if (r == p['OK']):
        logg('call ask ')
        p['sy']['ask'](p)
        logg('after ask')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing verb ( dup ) ')
    if (r == p['OK']):
        logg('call dup ')
        p['sy']['dup'](p)
        logg('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing verb ( ! ) ')
    if (r == p['OK']):
        logg('call ! ')
        p['sy']['!'](p)
        logg('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing verb ( ==quit ) ')
    if (r == p['OK']):
        logg('call ==quit ')
        p['sy']['==quit'](p)
        logg('after ==quit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing text ')
    logg("""bbox done""")
    if (r == p['OK']):
        logg('push text ' + """bbox done""")
        datPush("bbox done")
        logg('after ' + """bbox done""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final bmain_1')
#end bmain_1

def bmain_2():
    global p
    logg('bmain_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for bmain-2 processing verb ( b2 ) ')
    if (r == p['OK']):
        logg('call b2 ')
        p['sy']['b2'](p)
        logg('after b2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-2 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final bmain_2')
#end bmain_2

def bmain (x):
    global p
    logg('begin bmain')
    ## point of umbrella
    bmainCtl = 1 # starting spoke
    while bmainCtl != 0:
        logg('loop bmainCtl = ' + bmainCtl.__str__())
        if (bmainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (bmainCtl == 1):
            logg('call bmain_1')
            bmain_1()
            logg('after call bmain_1')
            # test and adjust for new spoke
            bmainCtl = chk(bmainCtl)

        elif (bmainCtl == 2):
            logg('call bmain_2')
            bmain_2()
            logg('after call bmain_2')
            # test and adjust for new spoke
            bmainCtl = chk(bmainCtl)

        else:
            #final
            logg('final bmain')    
            bmainCtl = 0 # break
        #endif
    #wend
#end bmain

def Ver_1():
    global p
    logg('Ver_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Ver-1 processing text ')
    logg("""bbox version 3.29b.XX""")
    if (r == p['OK']):
        logg('push text ' + """bbox version 3.29b.XX""")
        datPush("bbox version 3.29b.XX")
        logg('after ' + """bbox version 3.29b.XX""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Ver-1 processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Ver_1')
#end Ver_1

def Ver (x):
    global p
    logg('begin Ver')
    ## point of umbrella
    VerCtl = 1 # starting spoke
    while VerCtl != 0:
        logg('loop VerCtl = ' + VerCtl.__str__())
        if (VerCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (VerCtl == 1):
            logg('call Ver_1')
            Ver_1()
            logg('after call Ver_1')
            # test and adjust for new spoke
            VerCtl = chk(VerCtl)

        else:
            #final
            logg('final Ver')    
            VerCtl = 0 # break
        #endif
    #wend
#end Ver

def b2_1():
    global p
    logg('b2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-1 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-1 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-1 processing verb ( len ) ')
    if (r == p['OK']):
        logg('call len ')
        p['sy']['len'](p)
        logg('after len')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-1 processing verb ( ==0 ) ')
    if (r == p['OK']):
        logg('call ==0 ')
        p['sy']['==0'](p)
        logg('after ==0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final b2_1')
#end b2_1

def b2_2():
    global p
    logg('b2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-2 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-2 processing verb ( c1 ) ')
    if (r == p['OK']):
        logg('call c1 ')
        p['sy']['c1'](p)
        logg('after c1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-2 processing verb ( Q? ) ')
    if (r == p['OK']):
        logg('call Q? ')
        p['sy']['Q?'](p)
        logg('after Q?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-2 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-2 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-2 processing verb ( woB ) ')
    if (r == p['OK']):
        logg('call woB ')
        p['sy']['woB'](p)
        logg('after woB')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final b2_2')
#end b2_2

def b2_3():
    global p
    logg('b2_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-3 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-3 processing verb ( c1 ) ')
    if (r == p['OK']):
        logg('call c1 ')
        p['sy']['c1'](p)
        logg('after c1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-3 processing verb ( T? ) ')
    if (r == p['OK']):
        logg('call T? ')
        p['sy']['T?'](p)
        logg('after T?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-3 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-3 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-3 processing verb ( woB ) ')
    if (r == p['OK']):
        logg('call woB ')
        p['sy']['woB'](p)
        logg('after woB')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final b2_3')
#end b2_3

def b2_4():
    global p
    logg('b2_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-4 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-4 processing verb ( isnum? ) ')
    if (r == p['OK']):
        logg('call isnum? ')
        p['sy']['isnum?'](p)
        logg('after isnum?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-4 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-4 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final b2_4')
#end b2_4

def b2_5():
    global p
    logg('b2_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-5 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-5 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-5 processing verb ( ==push ) ')
    if (r == p['OK']):
        logg('call ==push ')
        p['sy']['==push'](p)
        logg('after ==push')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-5 processing text ')
    logg("""-----txt""")
    if (r == p['OK']):
        logg('push text ' + """-----txt""")
        datPush("-----txt")
        logg('after ' + """-----txt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-5 processing verb ( ask ) ')
    if (r == p['OK']):
        logg('call ask ')
        p['sy']['ask'](p)
        logg('after ask')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final b2_5')
#end b2_5

def b2_6():
    global p
    logg('b2_6')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-6 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-6 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-6 processing verb ( ==pop ) ')
    if (r == p['OK']):
        logg('call ==pop ')
        p['sy']['==pop'](p)
        logg('after ==pop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-6 processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final b2_6')
#end b2_6

def b2_7():
    global p
    logg('b2_7')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-7 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-7 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-7 processing text ')
    logg("""{{""")
    if (r == p['OK']):
        logg('push text ' + """{{""")
        datPush("{{")
        logg('after ' + """{{""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-7 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-7 processing text ')
    logg(""" """)
    if (r == p['OK']):
        logg('push text ' + """ """)
        datPush(" ")
        logg('after ' + """ """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-7 processing verb ( bcollect ) ')
    if (r == p['OK']):
        logg('call bcollect ')
        p['sy']['bcollect'](p)
        logg('after bcollect')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final b2_7')
#end b2_7

def b2_8():
    global p
    logg('b2_8')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-8 processing text ')
    logg("""bb""")
    if (r == p['OK']):
        logg('push text ' + """bb""")
        datPush("bb")
        logg('after ' + """bb""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-8 processing verb ( @ ) ')
    if (r == p['OK']):
        logg('call @ ')
        p['sy']['@'](p)
        logg('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-8 processing verb ( .X ) ')
    if (r == p['OK']):
        logg('call .X ')
        p['sy']['.X'](p)
        logg('after .X')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final b2_8')
#end b2_8

def b2_9():
    global p
    logg('b2_9')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-9 processing text ')
    logg("""failed""")
    if (r == p['OK']):
        logg('push text ' + """failed""")
        datPush("failed")
        logg('after ' + """failed""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-9 processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final b2_9')
#end b2_9

def b2 (x):
    global p
    logg('begin b2')
    ## point of umbrella
    b2Ctl = 1 # starting spoke
    while b2Ctl != 0:
        logg('loop b2Ctl = ' + b2Ctl.__str__())
        if (b2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (b2Ctl == 1):
            logg('call b2_1')
            b2_1()
            logg('after call b2_1')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        elif (b2Ctl == 2):
            logg('call b2_2')
            b2_2()
            logg('after call b2_2')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        elif (b2Ctl == 3):
            logg('call b2_3')
            b2_3()
            logg('after call b2_3')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        elif (b2Ctl == 4):
            logg('call b2_4')
            b2_4()
            logg('after call b2_4')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        elif (b2Ctl == 5):
            logg('call b2_5')
            b2_5()
            logg('after call b2_5')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        elif (b2Ctl == 6):
            logg('call b2_6')
            b2_6()
            logg('after call b2_6')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        elif (b2Ctl == 7):
            logg('call b2_7')
            b2_7()
            logg('after call b2_7')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        elif (b2Ctl == 8):
            logg('call b2_8')
            b2_8()
            logg('after call b2_8')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        elif (b2Ctl == 9):
            logg('call b2_9')
            b2_9()
            logg('after call b2_9')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        else:
            #final
            logg('final b2')    
            b2Ctl = 0 # break
        #endif
    #wend
#end b2

def bcollect_1():
    global p
    logg('bcollect_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for bcollect-1 processing text ')
    logg("""&""")
    if (r == p['OK']):
        logg('push text ' + """&""")
        datPush("&")
        logg('after ' + """&""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bcollect-1 processing verb ( ask ) ')
    if (r == p['OK']):
        logg('call ask ')
        p['sy']['ask'](p)
        logg('after ask')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bcollect-1 processing verb ( ... ) ')
    if (r == p['OK']):
        logg('call ... ')
        p['sy']['...'](p)
        logg('after ...')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final bcollect_1')
#end bcollect_1

def bcollect_2():
    global p
    logg('bcollect_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for bcollect-2 processing verb ( dup ) ')
    if (r == p['OK']):
        logg('call dup ')
        p['sy']['dup'](p)
        logg('after dup')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bcollect-2 processing text ')
    logg("""}}""")
    if (r == p['OK']):
        logg('push text ' + """}}""")
        datPush("}}")
        logg('after ' + """}}""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bcollect-2 processing verb ( = ) ')
    if (r == p['OK']):
        logg('call = ')
        p['sy']['='](p)
        logg('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bcollect-2 processing verb ( drop ) ')
    if (r == p['OK']):
        logg('call drop ')
        p['sy']['drop'](p)
        logg('after drop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final bcollect_2')
#end bcollect_2

def bcollect_3():
    global p
    logg('bcollect_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for bcollect-3 processing verb ( cats ) ')
    if (r == p['OK']):
        logg('call cats ')
        p['sy']['cats'](p)
        logg('after cats')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bcollect-3 processing verb ( tail. ) ')
    if (r == p['OK']):
        logg('call tail. ')
        p['sy']['tail.'](p)
        logg('after tail.')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final bcollect_3')
#end bcollect_3

def bcollect (x):
    global p
    logg('begin bcollect')
    ## point of umbrella
    bcollectCtl = 1 # starting spoke
    while bcollectCtl != 0:
        logg('loop bcollectCtl = ' + bcollectCtl.__str__())
        if (bcollectCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (bcollectCtl == 1):
            logg('call bcollect_1')
            bcollect_1()
            logg('after call bcollect_1')
            # test and adjust for new spoke
            bcollectCtl = chk(bcollectCtl)

        elif (bcollectCtl == 2):
            logg('call bcollect_2')
            bcollect_2()
            logg('after call bcollect_2')
            # test and adjust for new spoke
            bcollectCtl = chk(bcollectCtl)

        elif (bcollectCtl == 3):
            logg('call bcollect_3')
            bcollect_3()
            logg('after call bcollect_3')
            # test and adjust for new spoke
            bcollectCtl = chk(bcollectCtl)

        else:
            #final
            logg('final bcollect')    
            bcollectCtl = 0 # break
        #endif
    #wend
#end bcollect

def xsdVersion_1():
    global p
    logg('xsdVersion_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdVersion-1 processing text ')
    logg("""xsd Version 2020-04-17-2010""")
    if (r == p['OK']):
        logg('push text ' + """xsd Version 2020-04-17-2010""")
        datPush("xsd Version 2020-04-17-2010")
        logg('after ' + """xsd Version 2020-04-17-2010""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdVersion-1 processing verb ( msg ) ')
    if (r == p['OK']):
        logg('call msg ')
        p['sy']['msg'](p)
        logg('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdVersion_1')
#end xsdVersion_1

def xsdVersion (x):
    global p
    logg('begin xsdVersion')
    ## point of umbrella
    xsdVersionCtl = 1 # starting spoke
    while xsdVersionCtl != 0:
        logg('loop xsdVersionCtl = ' + xsdVersionCtl.__str__())
        if (xsdVersionCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdVersionCtl == 1):
            logg('call xsdVersion_1')
            xsdVersion_1()
            logg('after call xsdVersion_1')
            # test and adjust for new spoke
            xsdVersionCtl = chk(xsdVersionCtl)

        else:
            #final
            logg('final xsdVersion')    
            xsdVersionCtl = 0 # break
        #endif
    #wend
#end xsdVersion

# stream routines 

def EQquit(p):
    logg ('==quit')
    needle = 'quit'
    needle = needle.upper()
    return(eqeq(needle))
#end EQquit

def EQ0(p):
    logg ('==0')
    needle = '0'
    needle = needle.upper()
    return(eqeq(needle))
#end EQ0

def EQpush(p):
    logg ('==push')
    needle = 'push'
    needle = needle.upper()
    return(eqeq(needle))
#end EQpush

def EQpop(p):
    logg ('==pop')
    needle = 'pop'
    needle = needle.upper()
    return(eqeq(needle))
#end EQpop

# END stream routines 

def main(startpoint,trace='off'):
    global p
    p = {}
    p['v'] = {} # nds
    p['v']['trace'] = trace
    if ( p['v']['trace'] != 'off'):
        print('begin main')
    #endif
    p['dat'] = [] # data stack
    p['r'] = [] # r stack
    p['l'] = {} # lib table
    p['sy'] = {} # symbol table
    p['sy']['exit'] = exitp
    p['sy']['pop'] = datPop
    p['sy']['push'] = datPush
    p['sy']['dump'] = dump
    p['sy']['.s'] = dots
    p['sy']['.sy'] = dotsy
    p['sy']['.si'] = doti  # uncallable debug/trace only
    p['sy']['logg'] = logg # uncallable debug/trace only
    prepSy()
    p['OK'] = 'pOK'
    p['NOK'] = 'pNOK'

    # paragraph xbegin
    p['sy']['xbegin'] = xbegin
    #

    # paragraph L1
    p['sy']['L1'] = L1
    #

    # paragraph p1
    p['sy']['p1'] = p1
    #

    # paragraph L1a1
    p['sy']['L1a1'] = L1a1
    #

    # paragraph fan1
    p['sy']['fan1'] = fan1
    #

    # paragraph schemaChk
    p['sy']['schemaChk'] = schemaChk
    #

    # paragraph parseAttributes
    p['sy']['parseAttributes'] = parseAttributes
    #

    # paragraph getAttributeValue
    p['sy']['getAttributeValue'] = getAttributeValue
    #

    # paragraph GAV2
    p['sy']['GAV2'] = GAV2
    #

    # paragraph GAVtillQ
    p['sy']['GAVtillQ'] = GAVtillQ
    #

    # paragraph GAVtillT
    p['sy']['GAVtillT'] = GAVtillT
    #

    # paragraph getattributeName
    p['sy']['getattributeName'] = getattributeName
    #

    # paragraph GAN2
    p['sy']['GAN2'] = GAN2
    #

    # paragraph fan30
    p['sy']['fan30'] = fan30
    #

    # paragraph fctillLT2XN3
    p['sy']['fctillLT2XN3'] = fctillLT2XN3
    #

    # paragraph fctillLT2XN3a
    p['sy']['fctillLT2XN3a'] = fctillLT2XN3a
    #

    # paragraph XN3Fan
    p['sy']['XN3Fan'] = XN3Fan
    #

    # paragraph procBang
    p['sy']['procBang'] = procBang
    #

    # paragraph fan2
    p['sy']['fan2'] = fan2
    #

    # paragraph fan2a
    p['sy']['fan2a'] = fan2a
    #

    # paragraph ParseNodeName
    p['sy']['ParseNodeName'] = ParseNodeName
    #

    # paragraph fan4
    p['sy']['fan4'] = fan4
    #

    # paragraph lastChk
    p['sy']['lastChk'] = lastChk
    #

    # paragraph xsdInit
    p['sy']['xsdInit'] = xsdInit
    #

    # paragraph parentPlus
    p['sy']['parentPlus'] = parentPlus
    #

    # paragraph abort
    p['sy']['abort'] = abort
    #

    # paragraph Xlabel
    p['sy']['Xlabel'] = Xlabel
    #

    # paragraph Xlabel2
    p['sy']['Xlabel2'] = Xlabel2
    #

    # paragraph XlabelFinal
    p['sy']['XlabelFinal'] = XlabelFinal
    #

    # paragraph xioi
    p['sy']['xioi'] = xioi
    #

    # paragraph garbageIn
    p['sy']['garbageIn'] = garbageIn
    #

    # paragraph xxioi
    p['sy']['xxioi'] = xxioi
    #

    # paragraph xioo
    p['sy']['xioo'] = xioo
    #

    # paragraph step
    p['sy']['step'] = step
    #

    # paragraph writeRecords
    p['sy']['writeRecords'] = writeRecords
    #

    # paragraph bmain
    p['sy']['bmain'] = bmain
    #

    # paragraph ==quit
    p['sy']['==quit'] = EQquit
    #

    # paragraph Ver
    p['sy']['Ver'] = Ver
    #

    # paragraph b2
    p['sy']['b2'] = b2
    #

    # paragraph ==0
    p['sy']['==0'] = EQ0
    #

    # paragraph ==push
    p['sy']['==push'] = EQpush
    #

    # paragraph ==pop
    p['sy']['==pop'] = EQpop
    #

    # paragraph bcollect
    p['sy']['bcollect'] = bcollect
    #

    # paragraph xsdVersion
    p['sy']['xsdVersion'] = xsdVersion
    #

    p['sy']['start'] = p['sy'][startpoint] 
#end main
def start(trace='off'):
    p['v']['trace'] = trace # save trace setting
    p['sy']['start'](trace) # process begins at start
#end start

# helper rtns 

def eqeq(needle):
    global p
    logg('begin eqeq - ' + needle )
    op1 = p['sy']['pop']()
    op1 = op1.upper()
    op2 = needle.upper()
    if (op1 == op2):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#end eqeq

def logg(strin):
    global p
    if (p['v']['trace'] == 'on'):
        nop = raw_input(strin)  
    #endif
#end logg

def chk(ctl):
    # tests ok/nok/tail/... of verb return to adjust ctl 
    global p
    okn = p['sy']['pop']()
    logg('chk-okn ' + okn.__str__())
    if (okn == 'tail.'):
        ans = 1
    elif (okn == p['NOK']):
        ans = ctl + 1
    elif (okn == '...'):
        ans = ctl + 1
    else:
        ans = 0 # clause passed 
        datPush(p['OK']) # leave ok on stack
    #endif
    logg('chk-ret=' + ans.__str__())
    return(ans)
#end chk

def datPush(val):
    global p
    p['dat'].append(val)
    logg('push('+val.__str__() + ")")
#end datPush

def dots(p):
    # callable reveal datastack
    print('dat:' + p['dat'].__str__()+'TOS')
    p['sy']['push'](p['OK'])
#end dots

def dotsy(p):
    # callable reveal symbol table
    m = p['sy'].keys()
    print('sy:(' + m.__str__() +')')
    p['sy']['push'](p['OK'])
#end dotsy

def doti(p):
    # not callable reveal datastack
    print('dat:' + p['dat'].__str__()+'TOS')
#end doti
def exitp(p):
    exit()
#end exitp

def datPop():
    global p
    v = p['dat'].pop()
    logg('................pop('+ v.__str__() + ")")
    return(v)
#end datPop

def prepSy():
    global p
    import doVerb
    p = doVerb.init(p) # load vectors
#end prepSy

def getp():
    # not callable routine to retrieve p 
    global p
    return(p)
#end getp

def dump(p):
    # callable routine to view and retrieve p 
    print('begin dump')
    print(p)
    print('after dump')
    p['sy']['push'](p['OK'])
    return(p)
#end dump

def help():
    print 'begin help'
    print "usage: "
    print "import NAME"
    print "z = NAME"
    print "z.main(startpoint,trace) prepares vectors "
    print "v =  NAME.getp() # grabs and allows passage of vectors "
    print "to execute: "
    print "-- z.start(trace) "
    print ''
    print "to add externial vectors: "
    print "v /*from dump */ = NAME.take(v,VectorFilename) - adds vectors into process via file "
    print "format of vectorFile: "
    print "-1 def main(v) sets and returns structure v "
    print "--- v['sy'][verbName] = procName "
    print "-2 def procName(v) "
    print ''
    print "can also call takeV verb in code "
    print '  datastack (vectorfilename,,) '
    print ' any other needed parameters may follow '
    print ''
    print 'end help'
#end help

def take(px,VectorFile):
    global p
    # given a P set file - add vectors to architecture 
    # do wild import
    j = __import__( VectorFile ) # no .py extension
    # run x.main(p)
    p = j.main(px)
    px = p
    return(p) #ret p
#end take

def do(cmd):
    global p
    p['sy'][cmd](p)
#end do

