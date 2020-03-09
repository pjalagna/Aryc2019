
#file BPX.py
#generated for BPX.basii at Sun Mar  8 00:57:31 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def BPXMain_1():
    global p
    logg('BPXMain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for BPXMain-1 processing verb ( BPXInit ) ')
    if (r == p['OK']):
        logg('call BPXInit ')
        p['sy']['BPXInit'](p)
        logg('after BPXInit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for BPXMain-1 processing verb ( doParagraph ) ')
    if (r == p['OK']):
        logg('call doParagraph ')
        p['sy']['doParagraph'](p)
        logg('after doParagraph')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final BPXMain_1')
#end BPXMain_1

def BPXMain (x):
    global p
    logg('begin BPXMain')
    ## point of umbrella
    BPXMainCtl = 1 # starting spoke
    while BPXMainCtl != 0:
        logg('loop BPXMainCtl = ' + BPXMainCtl.__str__())
        if (BPXMainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (BPXMainCtl == 1):
            logg('call BPXMain_1')
            BPXMain_1()
            logg('after call BPXMain_1')
            # test and adjust for new spoke
            BPXMainCtl = chk(BPXMainCtl)

        else:
            #final
            logg('final BPXMain')    
            BPXMainCtl = 0 # break
        #endif
    #wend
#end BPXMain

def BPXInit_1():
    global p
    logg('BPXInit_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for BPXInit-1 processing text ')
    logg("""init none """)
    if (r == p['OK']):
        logg('push text ' + """init none """)
        datPush("init none ")
        logg('after ' + """init none """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for BPXInit-1 processing verb ( msg ) ')
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
    logg('final BPXInit_1')
#end BPXInit_1

def BPXInit (x):
    global p
    logg('begin BPXInit')
    ## point of umbrella
    BPXInitCtl = 1 # starting spoke
    while BPXInitCtl != 0:
        logg('loop BPXInitCtl = ' + BPXInitCtl.__str__())
        if (BPXInitCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (BPXInitCtl == 1):
            logg('call BPXInit_1')
            BPXInit_1()
            logg('after call BPXInit_1')
            # test and adjust for new spoke
            BPXInitCtl = chk(BPXInitCtl)

        else:
            #final
            logg('final BPXInit')    
            BPXInitCtl = 0 # break
        #endif
    #wend
#end BPXInit

def doParagraph_1():
    global p
    logg('doParagraph_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doParagraph-1 processing verb ( word ) ')
    if (r == p['OK']):
        logg('call word ')
        p['sy']['word'](p)
        logg('after word')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-1 processing text ')
    logg("""px""")
    if (r == p['OK']):
        logg('push text ' + """px""")
        datPush("px")
        logg('after ' + """px""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-1 processing verb ( ! ) ')
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
    logg('for doParagraph-1 processing verb ( ... ) ')
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
    logg('final doParagraph_1')
#end doParagraph_1

def doParagraph_2():
    global p
    logg('doParagraph_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doParagraph-2 processing text ')
    logg("""px""")
    if (r == p['OK']):
        logg('push text ' + """px""")
        datPush("px")
        logg('after ' + """px""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-2 processing verb ( @ ) ')
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
    logg('for doParagraph-2 processing text ')
    logg(""";;""")
    if (r == p['OK']):
        logg('push text ' + """;;""")
        datPush(";;")
        logg('after ' + """;;""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-2 processing verb ( = ) ')
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
    logg('for doParagraph-2 processing verb ( BPXFinal ) ')
    if (r == p['OK']):
        logg('call BPXFinal ')
        p['sy']['BPXFinal'](p)
        logg('after BPXFinal')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final doParagraph_2')
#end doParagraph_2

def doParagraph_3():
    global p
    logg('doParagraph_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing text ')
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
    logg('for doParagraph-3 processing text ')
    logg("""e""")
    if (r == p['OK']):
        logg('push text ' + """e""")
        datPush("e")
        logg('after ' + """e""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing verb ( ! ) ')
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
    logg('for doParagraph-3 processing text ')
    logg("""px""")
    if (r == p['OK']):
        logg('push text ' + """px""")
        datPush("px")
        logg('after ' + """px""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing verb ( @ ) ')
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
    logg('for doParagraph-3 processing text ')
    logg("""def""")
    if (r == p['OK']):
        logg('push text ' + """def""")
        datPush("def")
        logg('after ' + """def""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing verb ( = ) ')
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
    logg('for doParagraph-3 processing verb ( word ) ')
    if (r == p['OK']):
        logg('call word ')
        p['sy']['word'](p)
        logg('after word')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing text ')
    logg("""BPXpn""")
    if (r == p['OK']):
        logg('push text ' + """BPXpn""")
        datPush("BPXpn")
        logg('after ' + """BPXpn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing verb ( ! ) ')
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
    logg('for doParagraph-3 processing verb ( writePAR ) ')
    if (r == p['OK']):
        logg('call writePAR ')
        p['sy']['writePAR'](p)
        logg('after writePAR')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing text ')
    logg("""1""")
    if (r == p['OK']):
        logg('push text ' + """1""")
        datPush("1")
        logg('after ' + """1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing text ')
    logg("""e""")
    if (r == p['OK']):
        logg('push text ' + """e""")
        datPush("e")
        logg('after ' + """e""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing verb ( ! ) ')
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
    logg('for doParagraph-3 processing verb ( word ) ')
    if (r == p['OK']):
        logg('call word ')
        p['sy']['word'](p)
        logg('after word')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing text ')
    logg(""":-""")
    if (r == p['OK']):
        logg('push text ' + """:-""")
        datPush(":-")
        logg('after ' + """:-""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing verb ( = ) ')
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
    logg('for doParagraph-3 processing text ')
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
    logg('for doParagraph-3 processing text ')
    logg("""BPXcn""")
    if (r == p['OK']):
        logg('push text ' + """BPXcn""")
        datPush("BPXcn")
        logg('after ' + """BPXcn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing verb ( ! ) ')
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
    logg('for doParagraph-3 processing verb ( doClauses ) ')
    if (r == p['OK']):
        logg('call doClauses ')
        p['sy']['doClauses'](p)
        logg('after doClauses')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-3 processing verb ( tail. ) ')
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
    logg('final doParagraph_3')
#end doParagraph_3

def doParagraph_4():
    global p
    logg('doParagraph_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doParagraph-4 processing text ')
    logg("""e""")
    if (r == p['OK']):
        logg('push text ' + """e""")
        datPush("e")
        logg('after ' + """e""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-4 processing verb ( @ ) ')
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
    logg('for doParagraph-4 processing text ')
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
    logg('for doParagraph-4 processing verb ( = ) ')
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
    logg('for doParagraph-4 processing text ')
    logg("""expected def""")
    if (r == p['OK']):
        logg('push text ' + """expected def""")
        datPush("expected def")
        logg('after ' + """expected def""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-4 processing verb ( msg ) ')
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
    logg('final doParagraph_4')
#end doParagraph_4

def doParagraph_5():
    global p
    logg('doParagraph_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doParagraph-5 processing text ')
    logg("""e""")
    if (r == p['OK']):
        logg('push text ' + """e""")
        datPush("e")
        logg('after ' + """e""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-5 processing verb ( @ ) ')
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
    logg('for doParagraph-5 processing text ')
    logg("""1""")
    if (r == p['OK']):
        logg('push text ' + """1""")
        datPush("1")
        logg('after ' + """1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-5 processing verb ( = ) ')
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
    logg('for doParagraph-5 processing text ')
    logg("""expected :- """)
    if (r == p['OK']):
        logg('push text ' + """expected :- """)
        datPush("expected :- ")
        logg('after ' + """expected :- """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doParagraph-5 processing verb ( msg ) ')
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
    logg('final doParagraph_5')
#end doParagraph_5

def doParagraph (x):
    global p
    logg('begin doParagraph')
    ## point of umbrella
    doParagraphCtl = 1 # starting spoke
    while doParagraphCtl != 0:
        logg('loop doParagraphCtl = ' + doParagraphCtl.__str__())
        if (doParagraphCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (doParagraphCtl == 1):
            logg('call doParagraph_1')
            doParagraph_1()
            logg('after call doParagraph_1')
            # test and adjust for new spoke
            doParagraphCtl = chk(doParagraphCtl)

        elif (doParagraphCtl == 2):
            logg('call doParagraph_2')
            doParagraph_2()
            logg('after call doParagraph_2')
            # test and adjust for new spoke
            doParagraphCtl = chk(doParagraphCtl)

        elif (doParagraphCtl == 3):
            logg('call doParagraph_3')
            doParagraph_3()
            logg('after call doParagraph_3')
            # test and adjust for new spoke
            doParagraphCtl = chk(doParagraphCtl)

        elif (doParagraphCtl == 4):
            logg('call doParagraph_4')
            doParagraph_4()
            logg('after call doParagraph_4')
            # test and adjust for new spoke
            doParagraphCtl = chk(doParagraphCtl)

        elif (doParagraphCtl == 5):
            logg('call doParagraph_5')
            doParagraph_5()
            logg('after call doParagraph_5')
            # test and adjust for new spoke
            doParagraphCtl = chk(doParagraphCtl)

        else:
            #final
            logg('final doParagraph')    
            doParagraphCtl = 0 # break
        #endif
    #wend
#end doParagraph

def doClauses_1():
    global p
    logg('doClauses_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doClauses-1 processing verb ( word ) ')
    if (r == p['OK']):
        logg('call word ')
        p['sy']['word'](p)
        logg('after word')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-1 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-1 processing verb ( ! ) ')
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
    logg('for doClauses-1 processing verb ( ... ) ')
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
    logg('final doClauses_1')
#end doClauses_1

def doClauses_2():
    global p
    logg('doClauses_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doClauses-2 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-2 processing verb ( @ ) ')
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
    logg('for doClauses-2 processing text ')
    logg(""";""")
    if (r == p['OK']):
        logg('push text ' + """;""")
        datPush(";")
        logg('after ' + """;""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-2 processing verb ( = ) ')
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
    logg('for doClauses-2 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-2 processing verb ( @ ) ')
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
    logg('for doClauses-2 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-2 processing verb ( ! ) ')
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
    logg('for doClauses-2 processing text ')
    logg("""BPXcn""")
    if (r == p['OK']):
        logg('push text ' + """BPXcn""")
        datPush("BPXcn")
        logg('after ' + """BPXcn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-2 processing verb ( @ ) ')
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
    logg('for doClauses-2 processing verb ( ++ ) ')
    if (r == p['OK']):
        logg('call ++ ')
        p['sy']['++'](p)
        logg('after ++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-2 processing text ')
    logg("""BPXcn""")
    if (r == p['OK']):
        logg('push text ' + """BPXcn""")
        datPush("BPXcn")
        logg('after ' + """BPXcn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-2 processing verb ( ! ) ')
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
    logg('for doClauses-2 processing text ')
    logg("""1""")
    if (r == p['OK']):
        logg('push text ' + """1""")
        datPush("1")
        logg('after ' + """1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-2 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-2 processing verb ( ! ) ')
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
    logg('for doClauses-2 processing verb ( writeBPX ) ')
    if (r == p['OK']):
        logg('call writeBPX ')
        p['sy']['writeBPX'](p)
        logg('after writeBPX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final doClauses_2')
#end doClauses_2

def doClauses_3():
    global p
    logg('doClauses_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doClauses-3 processing text ')
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
    logg('for doClauses-3 processing text ')
    logg("""e""")
    if (r == p['OK']):
        logg('push text ' + """e""")
        datPush("e")
        logg('after ' + """e""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing verb ( ! ) ')
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
    logg('for doClauses-3 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing verb ( @ ) ')
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
    logg('for doClauses-3 processing text ')
    logg("""[[""")
    if (r == p['OK']):
        logg('push text ' + """[[""")
        datPush("[[")
        logg('after ' + """[[""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing verb ( = ) ')
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
    logg('for doClauses-3 processing verb ( word ) ')
    if (r == p['OK']):
        logg('call word ')
        p['sy']['word'](p)
        logg('after word')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing text ')
    logg("""BPXcn""")
    if (r == p['OK']):
        logg('push text ' + """BPXcn""")
        datPush("BPXcn")
        logg('after ' + """BPXcn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing verb ( ! ) ')
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
    logg('for doClauses-3 processing text ')
    logg("""1""")
    if (r == p['OK']):
        logg('push text ' + """1""")
        datPush("1")
        logg('after ' + """1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing text ')
    logg("""e""")
    if (r == p['OK']):
        logg('push text ' + """e""")
        datPush("e")
        logg('after ' + """e""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing verb ( ! ) ')
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
    logg('for doClauses-3 processing verb ( word ) ')
    if (r == p['OK']):
        logg('call word ')
        p['sy']['word'](p)
        logg('after word')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing text ')
    logg("""]]""")
    if (r == p['OK']):
        logg('push text ' + """]]""")
        datPush("]]")
        logg('after ' + """]]""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing verb ( = ) ')
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
    logg('for doClauses-3 processing text ')
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
    logg('for doClauses-3 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing verb ( ! ) ')
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
    logg('for doClauses-3 processing verb ( doBPXvt ) ')
    if (r == p['OK']):
        logg('call doBPXvt ')
        p['sy']['doBPXvt'](p)
        logg('after doBPXvt')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-3 processing verb ( tail. ) ')
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
    logg('final doClauses_3')
#end doClauses_3

def doClauses_4():
    global p
    logg('doClauses_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doClauses-4 processing text ')
    logg("""e""")
    if (r == p['OK']):
        logg('push text ' + """e""")
        datPush("e")
        logg('after ' + """e""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-4 processing verb ( @ ) ')
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
    logg('for doClauses-4 processing text ')
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
    logg('for doClauses-4 processing verb ( = ) ')
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
    logg('for doClauses-4 processing text ')
    logg(""" expected [[ """)
    if (r == p['OK']):
        logg('push text ' + """ expected [[ """)
        datPush(" expected [[ ")
        logg('after ' + """ expected [[ """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-4 processing verb ( msg ) ')
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
    logg('final doClauses_4')
#end doClauses_4

def doClauses_5():
    global p
    logg('doClauses_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doClauses-5 processing text ')
    logg("""e""")
    if (r == p['OK']):
        logg('push text ' + """e""")
        datPush("e")
        logg('after ' + """e""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-5 processing verb ( @ ) ')
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
    logg('for doClauses-5 processing text ')
    logg("""1""")
    if (r == p['OK']):
        logg('push text ' + """1""")
        datPush("1")
        logg('after ' + """1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-5 processing verb ( = ) ')
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
    logg('for doClauses-5 processing text ')
    logg(""" expected ]] """)
    if (r == p['OK']):
        logg('push text ' + """ expected ]] """)
        datPush(" expected ]] ")
        logg('after ' + """ expected ]] """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doClauses-5 processing verb ( msg ) ')
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
    logg('final doClauses_5')
#end doClauses_5

def doClauses (x):
    global p
    logg('begin doClauses')
    ## point of umbrella
    doClausesCtl = 1 # starting spoke
    while doClausesCtl != 0:
        logg('loop doClausesCtl = ' + doClausesCtl.__str__())
        if (doClausesCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (doClausesCtl == 1):
            logg('call doClauses_1')
            doClauses_1()
            logg('after call doClauses_1')
            # test and adjust for new spoke
            doClausesCtl = chk(doClausesCtl)

        elif (doClausesCtl == 2):
            logg('call doClauses_2')
            doClauses_2()
            logg('after call doClauses_2')
            # test and adjust for new spoke
            doClausesCtl = chk(doClausesCtl)

        elif (doClausesCtl == 3):
            logg('call doClauses_3')
            doClauses_3()
            logg('after call doClauses_3')
            # test and adjust for new spoke
            doClausesCtl = chk(doClausesCtl)

        elif (doClausesCtl == 4):
            logg('call doClauses_4')
            doClauses_4()
            logg('after call doClauses_4')
            # test and adjust for new spoke
            doClausesCtl = chk(doClausesCtl)

        elif (doClausesCtl == 5):
            logg('call doClauses_5')
            doClauses_5()
            logg('after call doClauses_5')
            # test and adjust for new spoke
            doClausesCtl = chk(doClausesCtl)

        else:
            #final
            logg('final doClauses')    
            doClausesCtl = 0 # break
        #endif
    #wend
#end doClauses

def doBPXvt_1():
    global p
    logg('doBPXvt_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doBPXvt-1 processing verb ( word ) ')
    if (r == p['OK']):
        logg('call word ')
        p['sy']['word'](p)
        logg('after word')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-1 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-1 processing verb ( ! ) ')
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
    logg('for doBPXvt-1 processing verb ( ... ) ')
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
    logg('final doBPXvt_1')
#end doBPXvt_1

def doBPXvt_2():
    global p
    logg('doBPXvt_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doBPXvt-2 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-2 processing verb ( @ ) ')
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
    logg('for doBPXvt-2 processing text ')
    logg("""..""")
    if (r == p['OK']):
        logg('push text ' + """..""")
        datPush("..")
        logg('after ' + """..""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-2 processing verb ( c1 ) ')
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
    logg('for doBPXvt-2 processing verb ( = ) ')
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
    logg('for doBPXvt-2 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-2 processing verb ( @ ) ')
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
    logg('for doBPXvt-2 processing verb ( ++ ) ')
    if (r == p['OK']):
        logg('call ++ ')
        p['sy']['++'](p)
        logg('after ++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-2 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-2 processing verb ( ! ) ')
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
    logg('for doBPXvt-2 processing verb ( writeBPX ) ')
    if (r == p['OK']):
        logg('call writeBPX ')
        p['sy']['writeBPX'](p)
        logg('after writeBPX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final doBPXvt_2')
#end doBPXvt_2

def doBPXvt_3():
    global p
    logg('doBPXvt_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing verb ( @ ) ')
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
    logg('for doBPXvt-3 processing verb ( c1 ) ')
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
    logg('for doBPXvt-3 processing verb ( Q? ) ')
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
    logg('for doBPXvt-3 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing verb ( @ ) ')
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
    logg('for doBPXvt-3 processing verb ( woB ) ')
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

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing text ')
    logg("""BPXpara1""")
    if (r == p['OK']):
        logg('push text ' + """BPXpara1""")
        datPush("BPXpara1")
        logg('after ' + """BPXpara1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing verb ( ! ) ')
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
    logg('for doBPXvt-3 processing text ')
    logg("""lit""")
    if (r == p['OK']):
        logg('push text ' + """lit""")
        datPush("lit")
        logg('after ' + """lit""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing verb ( ! ) ')
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
    logg('for doBPXvt-3 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing verb ( @ ) ')
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
    logg('for doBPXvt-3 processing verb ( ++ ) ')
    if (r == p['OK']):
        logg('call ++ ')
        p['sy']['++'](p)
        logg('after ++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing verb ( ! ) ')
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
    logg('for doBPXvt-3 processing verb ( writeBPX ) ')
    if (r == p['OK']):
        logg('call writeBPX ')
        p['sy']['writeBPX'](p)
        logg('after writeBPX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-3 processing verb ( tail. ) ')
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
    logg('final doBPXvt_3')
#end doBPXvt_3

def doBPXvt_4():
    global p
    logg('doBPXvt_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing verb ( @ ) ')
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
    logg('for doBPXvt-4 processing verb ( c1 ) ')
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
    logg('for doBPXvt-4 processing verb ( T? ) ')
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
    logg('for doBPXvt-4 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing verb ( @ ) ')
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
    logg('for doBPXvt-4 processing verb ( woB ) ')
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

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing text ')
    logg("""BPXpara1""")
    if (r == p['OK']):
        logg('push text ' + """BPXpara1""")
        datPush("BPXpara1")
        logg('after ' + """BPXpara1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing verb ( ! ) ')
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
    logg('for doBPXvt-4 processing text ')
    logg("""lit""")
    if (r == p['OK']):
        logg('push text ' + """lit""")
        datPush("lit")
        logg('after ' + """lit""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing verb ( ! ) ')
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
    logg('for doBPXvt-4 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing verb ( @ ) ')
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
    logg('for doBPXvt-4 processing verb ( ++ ) ')
    if (r == p['OK']):
        logg('call ++ ')
        p['sy']['++'](p)
        logg('after ++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing verb ( ! ) ')
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
    logg('for doBPXvt-4 processing verb ( writeBPX ) ')
    if (r == p['OK']):
        logg('call writeBPX ')
        p['sy']['writeBPX'](p)
        logg('after writeBPX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-4 processing verb ( tail. ) ')
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
    logg('final doBPXvt_4')
#end doBPXvt_4

def doBPXvt_5():
    global p
    logg('doBPXvt_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing verb ( @ ) ')
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
    logg('for doBPXvt-5 processing verb ( isnum? ) ')
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
    logg('for doBPXvt-5 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing verb ( @ ) ')
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
    logg('for doBPXvt-5 processing text ')
    logg("""BPXpara1""")
    if (r == p['OK']):
        logg('push text ' + """BPXpara1""")
        datPush("BPXpara1")
        logg('after ' + """BPXpara1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing verb ( ! ) ')
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
    logg('for doBPXvt-5 processing text ')
    logg("""num""")
    if (r == p['OK']):
        logg('push text ' + """num""")
        datPush("num")
        logg('after ' + """num""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing verb ( ! ) ')
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
    logg('for doBPXvt-5 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing verb ( @ ) ')
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
    logg('for doBPXvt-5 processing verb ( ++ ) ')
    if (r == p['OK']):
        logg('call ++ ')
        p['sy']['++'](p)
        logg('after ++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing verb ( ! ) ')
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
    logg('for doBPXvt-5 processing verb ( writeBPX ) ')
    if (r == p['OK']):
        logg('call writeBPX ')
        p['sy']['writeBPX'](p)
        logg('after writeBPX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-5 processing verb ( tail. ) ')
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
    logg('final doBPXvt_5')
#end doBPXvt_5

def doBPXvt_6():
    global p
    logg('doBPXvt_6')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doBPXvt-6 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-6 processing verb ( @ ) ')
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
    logg('for doBPXvt-6 processing text ')
    logg("""//""")
    if (r == p['OK']):
        logg('push text ' + """//""")
        datPush("//")
        logg('after ' + """//""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-6 processing verb ( = ) ')
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
    logg('for doBPXvt-6 processing verb ( word ) ')
    if (r == p['OK']):
        logg('call word ')
        p['sy']['word'](p)
        logg('after word')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-6 processing text ')
    logg("""BPXpara1""")
    if (r == p['OK']):
        logg('push text ' + """BPXpara1""")
        datPush("BPXpara1")
        logg('after ' + """BPXpara1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-6 processing verb ( ! ) ')
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
    logg('for doBPXvt-6 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-6 processing verb ( @ ) ')
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
    logg('for doBPXvt-6 processing verb ( ++ ) ')
    if (r == p['OK']):
        logg('call ++ ')
        p['sy']['++'](p)
        logg('after ++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-6 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-6 processing verb ( ! ) ')
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
    logg('for doBPXvt-6 processing verb ( writeBPX ) ')
    if (r == p['OK']):
        logg('call writeBPX ')
        p['sy']['writeBPX'](p)
        logg('after writeBPX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-6 processing verb ( tail. ) ')
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
    logg('final doBPXvt_6')
#end doBPXvt_6

def doBPXvt_7():
    global p
    logg('doBPXvt_7')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doBPXvt-7 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-7 processing verb ( @ ) ')
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
    logg('for doBPXvt-7 processing verb ( ++ ) ')
    if (r == p['OK']):
        logg('call ++ ')
        p['sy']['++'](p)
        logg('after ++')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-7 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-7 processing verb ( ! ) ')
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
    logg('for doBPXvt-7 processing verb ( writeBPX ) ')
    if (r == p['OK']):
        logg('call writeBPX ')
        p['sy']['writeBPX'](p)
        logg('after writeBPX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doBPXvt-7 processing verb ( tail. ) ')
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
    logg('final doBPXvt_7')
#end doBPXvt_7

def doBPXvt (x):
    global p
    logg('begin doBPXvt')
    ## point of umbrella
    doBPXvtCtl = 1 # starting spoke
    while doBPXvtCtl != 0:
        logg('loop doBPXvtCtl = ' + doBPXvtCtl.__str__())
        if (doBPXvtCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (doBPXvtCtl == 1):
            logg('call doBPXvt_1')
            doBPXvt_1()
            logg('after call doBPXvt_1')
            # test and adjust for new spoke
            doBPXvtCtl = chk(doBPXvtCtl)

        elif (doBPXvtCtl == 2):
            logg('call doBPXvt_2')
            doBPXvt_2()
            logg('after call doBPXvt_2')
            # test and adjust for new spoke
            doBPXvtCtl = chk(doBPXvtCtl)

        elif (doBPXvtCtl == 3):
            logg('call doBPXvt_3')
            doBPXvt_3()
            logg('after call doBPXvt_3')
            # test and adjust for new spoke
            doBPXvtCtl = chk(doBPXvtCtl)

        elif (doBPXvtCtl == 4):
            logg('call doBPXvt_4')
            doBPXvt_4()
            logg('after call doBPXvt_4')
            # test and adjust for new spoke
            doBPXvtCtl = chk(doBPXvtCtl)

        elif (doBPXvtCtl == 5):
            logg('call doBPXvt_5')
            doBPXvt_5()
            logg('after call doBPXvt_5')
            # test and adjust for new spoke
            doBPXvtCtl = chk(doBPXvtCtl)

        elif (doBPXvtCtl == 6):
            logg('call doBPXvt_6')
            doBPXvt_6()
            logg('after call doBPXvt_6')
            # test and adjust for new spoke
            doBPXvtCtl = chk(doBPXvtCtl)

        elif (doBPXvtCtl == 7):
            logg('call doBPXvt_7')
            doBPXvt_7()
            logg('after call doBPXvt_7')
            # test and adjust for new spoke
            doBPXvtCtl = chk(doBPXvtCtl)

        else:
            #final
            logg('final doBPXvt')    
            doBPXvtCtl = 0 # break
        #endif
    #wend
#end doBPXvt

def writeBPX_1():
    global p
    logg('writeBPX_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for writeBPX-1 processing text ')
    logg("""BPX:""")
    if (r == p['OK']):
        logg('push text ' + """BPX:""")
        datPush("BPX:")
        logg('after ' + """BPX:""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeBPX-1 processing text ')
    logg("""BPXpn""")
    if (r == p['OK']):
        logg('push text ' + """BPXpn""")
        datPush("BPXpn")
        logg('after ' + """BPXpn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeBPX-1 processing verb ( @ ) ')
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
    logg('for writeBPX-1 processing verb ( cats ) ')
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
    logg('for writeBPX-1 processing text ')
    logg("""BPXcn""")
    if (r == p['OK']):
        logg('push text ' + """BPXcn""")
        datPush("BPXcn")
        logg('after ' + """BPXcn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeBPX-1 processing verb ( @ ) ')
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
    logg('for writeBPX-1 processing verb ( cats ) ')
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
    logg('for writeBPX-1 processing text ')
    logg("""BPXvn""")
    if (r == p['OK']):
        logg('push text ' + """BPXvn""")
        datPush("BPXvn")
        logg('after ' + """BPXvn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeBPX-1 processing verb ( @ ) ')
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
    logg('for writeBPX-1 processing verb ( cats ) ')
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
    logg('for writeBPX-1 processing text ')
    logg("""BPXvt""")
    if (r == p['OK']):
        logg('push text ' + """BPXvt""")
        datPush("BPXvt")
        logg('after ' + """BPXvt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeBPX-1 processing verb ( @ ) ')
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
    logg('for writeBPX-1 processing verb ( cats ) ')
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
    logg('for writeBPX-1 processing text ')
    logg("""BPXpara1""")
    if (r == p['OK']):
        logg('push text ' + """BPXpara1""")
        datPush("BPXpara1")
        logg('after ' + """BPXpara1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeBPX-1 processing verb ( @ ) ')
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
    logg('for writeBPX-1 processing verb ( cats ) ')
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
    logg('for writeBPX-1 processing text ')
    logg("""::""")
    if (r == p['OK']):
        logg('push text ' + """::""")
        datPush("::")
        logg('after ' + """::""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeBPX-1 processing verb ( cats ) ')
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
    logg('for writeBPX-1 processing verb ( msg ) ')
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
    logg('for writeBPX-1 processing text ')
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
    logg('for writeBPX-1 processing text ')
    logg("""BPXpara1""")
    if (r == p['OK']):
        logg('push text ' + """BPXpara1""")
        datPush("BPXpara1")
        logg('after ' + """BPXpara1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeBPX-1 processing verb ( ! ) ')
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
    logg('final writeBPX_1')
#end writeBPX_1

def writeBPX (x):
    global p
    logg('begin writeBPX')
    ## point of umbrella
    writeBPXCtl = 1 # starting spoke
    while writeBPXCtl != 0:
        logg('loop writeBPXCtl = ' + writeBPXCtl.__str__())
        if (writeBPXCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (writeBPXCtl == 1):
            logg('call writeBPX_1')
            writeBPX_1()
            logg('after call writeBPX_1')
            # test and adjust for new spoke
            writeBPXCtl = chk(writeBPXCtl)

        else:
            #final
            logg('final writeBPX')    
            writeBPXCtl = 0 # break
        #endif
    #wend
#end writeBPX

def writePAR_1():
    global p
    logg('writePAR_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for writePAR-1 processing text ')
    logg("""PAR:""")
    if (r == p['OK']):
        logg('push text ' + """PAR:""")
        datPush("PAR:")
        logg('after ' + """PAR:""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writePAR-1 processing text ')
    logg("""BPXpn""")
    if (r == p['OK']):
        logg('push text ' + """BPXpn""")
        datPush("BPXpn")
        logg('after ' + """BPXpn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writePAR-1 processing verb ( @ ) ')
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
    logg('for writePAR-1 processing verb ( cats ) ')
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
    logg('for writePAR-1 processing text ')
    logg("""::""")
    if (r == p['OK']):
        logg('push text ' + """::""")
        datPush("::")
        logg('after ' + """::""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writePAR-1 processing verb ( cats ) ')
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
    logg('for writePAR-1 processing verb ( msg ) ')
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
    logg('final writePAR_1')
#end writePAR_1

def writePAR (x):
    global p
    logg('begin writePAR')
    ## point of umbrella
    writePARCtl = 1 # starting spoke
    while writePARCtl != 0:
        logg('loop writePARCtl = ' + writePARCtl.__str__())
        if (writePARCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (writePARCtl == 1):
            logg('call writePAR_1')
            writePAR_1()
            logg('after call writePAR_1')
            # test and adjust for new spoke
            writePARCtl = chk(writePARCtl)

        else:
            #final
            logg('final writePAR')    
            writePARCtl = 0 # break
        #endif
    #wend
#end writePAR

# stream routines 

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

    # paragraph BPXMain
    p['sy']['BPXMain'] = BPXMain
    #

    # paragraph BPXInit
    p['sy']['BPXInit'] = BPXInit
    #

    # paragraph doParagraph
    p['sy']['doParagraph'] = doParagraph
    #

    # paragraph doClauses
    p['sy']['doClauses'] = doClauses
    #

    # paragraph doBPXvt
    p['sy']['doBPXvt'] = doBPXvt
    #

    # paragraph writeBPX
    p['sy']['writeBPX'] = writeBPX
    #

    # paragraph writePAR
    p['sy']['writePAR'] = writePAR
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

