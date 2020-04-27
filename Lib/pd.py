
#file pd.py
#generated for pd.basii at Thu Apr 23 11:35:29 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def pdc_1():
    global p
    logg('pdc_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc-1 processing text ')
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
    logg('for pdc-1 processing text ')
    logg("""lisw""")
    if (r == p['OK']):
        logg('push text ' + """lisw""")
        datPush("lisw")
        logg('after ' + """lisw""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc-1 processing verb ( ! ) ')
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
    logg('for pdc-1 processing verb ( pdc2 ) ')
    if (r == p['OK']):
        logg('call pdc2 ')
        p['sy']['pdc2'](p)
        logg('after pdc2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final pdc_1')
#end pdc_1

def pdc (x):
    global p
    logg('begin pdc')
    ## point of umbrella
    pdcCtl = 1 # starting spoke
    while pdcCtl != 0:
        logg('loop pdcCtl = ' + pdcCtl.__str__())
        if (pdcCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pdcCtl == 1):
            logg('call pdc_1')
            pdc_1()
            logg('after call pdc_1')
            # test and adjust for new spoke
            pdcCtl = chk(pdcCtl)

        else:
            #final
            logg('final pdc')    
            pdcCtl = 0 # break
        #endif
    #wend
#end pdc

def pdc2_1():
    global p
    logg('pdc2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc2-1 processing text ')
    logg("""lisw""")
    if (r == p['OK']):
        logg('push text ' + """lisw""")
        datPush("lisw")
        logg('after ' + """lisw""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc2-1 processing verb ( @ ) ')
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
    logg('for pdc2-1 processing text ')
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
    logg('for pdc2-1 processing verb ( <> ) ')
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

    #final
    logg('final pdc2_1')
#end pdc2_1

def pdc2_2():
    global p
    logg('pdc2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc2-2 processing verb ( word ) ')
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
    logg('for pdc2-2 processing text ')
    logg("""cellNo""")
    if (r == p['OK']):
        logg('push text ' + """cellNo""")
        datPush("cellNo")
        logg('after ' + """cellNo""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc2-2 processing verb ( ! ) ')
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
    logg('for pdc2-2 processing verb ( ... ) ')
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
    logg('final pdc2_2')
#end pdc2_2

def pdc2_3():
    global p
    logg('pdc2_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc2-3 processing verb ( ckcn ) ')
    if (r == p['OK']):
        logg('call ckcn ')
        p['sy']['ckcn'](p)
        logg('after ckcn')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc2-3 processing verb ( ... ) ')
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
    logg('final pdc2_3')
#end pdc2_3

def pdc2_4():
    global p
    logg('pdc2_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc2-4 processing text ')
    logg("""cellNo""")
    if (r == p['OK']):
        logg('push text ' + """cellNo""")
        datPush("cellNo")
        logg('after ' + """cellNo""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc2-4 processing verb ( @ ) ')
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
    logg('for pdc2-4 processing text ')
    logg("""end""")
    if (r == p['OK']):
        logg('push text ' + """end""")
        datPush("end")
        logg('after ' + """end""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc2-4 processing verb ( = ) ')
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
    logg('final pdc2_4')
#end pdc2_4

def pdc2_5():
    global p
    logg('pdc2_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc2-5 processing verb ( pdc3 ) ')
    if (r == p['OK']):
        logg('call pdc3 ')
        p['sy']['pdc3'](p)
        logg('after pdc3')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc2-5 processing verb ( tail. ) ')
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
    logg('final pdc2_5')
#end pdc2_5

def pdc2 (x):
    global p
    logg('begin pdc2')
    ## point of umbrella
    pdc2Ctl = 1 # starting spoke
    while pdc2Ctl != 0:
        logg('loop pdc2Ctl = ' + pdc2Ctl.__str__())
        if (pdc2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (pdc2Ctl == 1):
            logg('call pdc2_1')
            pdc2_1()
            logg('after call pdc2_1')
            # test and adjust for new spoke
            pdc2Ctl = chk(pdc2Ctl)

        elif (pdc2Ctl == 2):
            logg('call pdc2_2')
            pdc2_2()
            logg('after call pdc2_2')
            # test and adjust for new spoke
            pdc2Ctl = chk(pdc2Ctl)

        elif (pdc2Ctl == 3):
            logg('call pdc2_3')
            pdc2_3()
            logg('after call pdc2_3')
            # test and adjust for new spoke
            pdc2Ctl = chk(pdc2Ctl)

        elif (pdc2Ctl == 4):
            logg('call pdc2_4')
            pdc2_4()
            logg('after call pdc2_4')
            # test and adjust for new spoke
            pdc2Ctl = chk(pdc2Ctl)

        elif (pdc2Ctl == 5):
            logg('call pdc2_5')
            pdc2_5()
            logg('after call pdc2_5')
            # test and adjust for new spoke
            pdc2Ctl = chk(pdc2Ctl)

        else:
            #final
            logg('final pdc2')    
            pdc2Ctl = 0 # break
        #endif
    #wend
#end pdc2

def ckcn_1():
    global p
    logg('ckcn_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ckcn-1 processing text ')
    logg("""cellNo""")
    if (r == p['OK']):
        logg('push text ' + """cellNo""")
        datPush("cellNo")
        logg('after ' + """cellNo""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing verb ( @ ) ')
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
    logg('for ckcn-1 processing verb ( dup ) ')
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
    logg('for ckcn-1 processing text ')
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
    logg('for ckcn-1 processing verb ( find ) ')
    if (r == p['OK']):
        logg('call find ')
        p['sy']['find'](p)
        logg('after find')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing text ')
    logg("""n2""")
    if (r == p['OK']):
        logg('push text ' + """n2""")
        datPush("n2")
        logg('after ' + """n2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing verb ( ! ) ')
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
    logg('for ckcn-1 processing verb ( drop ) ')
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
    logg('for ckcn-1 processing text ')
    logg("""n1""")
    if (r == p['OK']):
        logg('push text ' + """n1""")
        datPush("n1")
        logg('after ' + """n1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing verb ( ! ) ')
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
    logg('for ckcn-1 processing text ')
    logg("""n1""")
    if (r == p['OK']):
        logg('push text ' + """n1""")
        datPush("n1")
        logg('after ' + """n1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing verb ( @ ) ')
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
    logg('for ckcn-1 processing text ')
    logg("""nocell""")
    if (r == p['OK']):
        logg('push text ' + """nocell""")
        datPush("nocell")
        logg('after ' + """nocell""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing text ')
    logg("""n2""")
    if (r == p['OK']):
        logg('push text ' + """n2""")
        datPush("n2")
        logg('after ' + """n2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing verb ( @ ) ')
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
    logg('for ckcn-1 processing verb ( lib! ) ')
    if (r == p['OK']):
        logg('call lib! ')
        p['sy']['lib!'](p)
        logg('after lib!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing text ')
    logg("""n2""")
    if (r == p['OK']):
        logg('push text ' + """n2""")
        datPush("n2")
        logg('after ' + """n2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing verb ( @ ) ')
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
    logg('for ckcn-1 processing text ')
    logg("""cellNo""")
    if (r == p['OK']):
        logg('push text ' + """cellNo""")
        datPush("cellNo")
        logg('after ' + """cellNo""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ckcn-1 processing verb ( ! ) ')
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
    logg('final ckcn_1')
#end ckcn_1

def ckcn_2():
    global p
    logg('ckcn_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ckcn-2 processing verb ( drop ) ')
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
    logg('final ckcn_2')
#end ckcn_2

def ckcn (x):
    global p
    logg('begin ckcn')
    ## point of umbrella
    ckcnCtl = 1 # starting spoke
    while ckcnCtl != 0:
        logg('loop ckcnCtl = ' + ckcnCtl.__str__())
        if (ckcnCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (ckcnCtl == 1):
            logg('call ckcn_1')
            ckcn_1()
            logg('after call ckcn_1')
            # test and adjust for new spoke
            ckcnCtl = chk(ckcnCtl)

        elif (ckcnCtl == 2):
            logg('call ckcn_2')
            ckcn_2()
            logg('after call ckcn_2')
            # test and adjust for new spoke
            ckcnCtl = chk(ckcnCtl)

        else:
            #final
            logg('final ckcn')    
            ckcnCtl = 0 # break
        #endif
    #wend
#end ckcn

def pdc3_1():
    global p
    logg('pdc3_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc3-1 processing verb ( word ) ')
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
    logg('for pdc3-1 processing text ')
    logg("""op""")
    if (r == p['OK']):
        logg('push text ' + """op""")
        datPush("op")
        logg('after ' + """op""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-1 processing verb ( ! ) ')
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
    logg('for pdc3-1 processing verb ( ... ) ')
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
    logg('final pdc3_1')
#end pdc3_1

def pdc3_2():
    global p
    logg('pdc3_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc3-2 processing text ')
    logg("""op""")
    if (r == p['OK']):
        logg('push text ' + """op""")
        datPush("op")
        logg('after ' + """op""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-2 processing verb ( @ ) ')
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
    logg('for pdc3-2 processing text ')
    logg("""x""")
    if (r == p['OK']):
        logg('push text ' + """x""")
        datPush("x")
        logg('after ' + """x""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-2 processing verb ( = ) ')
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
    logg('final pdc3_2')
#end pdc3_2

def pdc3_3():
    global p
    logg('pdc3_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc3-3 processing text ')
    logg("""op""")
    if (r == p['OK']):
        logg('push text ' + """op""")
        datPush("op")
        logg('after ' + """op""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-3 processing verb ( @ ) ')
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
    logg('for pdc3-3 processing text ')
    logg("""end""")
    if (r == p['OK']):
        logg('push text ' + """end""")
        datPush("end")
        logg('after ' + """end""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-3 processing verb ( = ) ')
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
    logg('for pdc3-3 processing text ')
    logg("""-1""")
    if (r == p['OK']):
        logg('push text ' + """-1""")
        datPush("-1")
        logg('after ' + """-1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-3 processing text ')
    logg("""lisw""")
    if (r == p['OK']):
        logg('push text ' + """lisw""")
        datPush("lisw")
        logg('after ' + """lisw""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-3 processing verb ( ! ) ')
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
    logg('final pdc3_3')
#end pdc3_3

def pdc3_4():
    global p
    logg('pdc3_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pdc3-4 processing verb ( word ) ')
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
    logg('for pdc3-4 processing verb ( drop ) ')
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
    logg('for pdc3-4 processing verb ( word ) ')
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
    logg('for pdc3-4 processing text ')
    logg("""yescell""")
    if (r == p['OK']):
        logg('push text ' + """yescell""")
        datPush("yescell")
        logg('after ' + """yescell""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing verb ( ! ) ')
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
    logg('for pdc3-4 processing text ')
    logg("""cellNo""")
    if (r == p['OK']):
        logg('push text ' + """cellNo""")
        datPush("cellNo")
        logg('after ' + """cellNo""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing verb ( @ ) ')
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
    logg('for pdc3-4 processing text ')
    logg("""op""")
    if (r == p['OK']):
        logg('push text ' + """op""")
        datPush("op")
        logg('after ' + """op""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing verb ( dup ) ')
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
    logg('for pdc3-4 processing verb ( @ ) ')
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
    logg('for pdc3-4 processing verb ( lib! ) ')
    if (r == p['OK']):
        logg('call lib! ')
        p['sy']['lib!'](p)
        logg('after lib!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing text ')
    logg("""cellNo""")
    if (r == p['OK']):
        logg('push text ' + """cellNo""")
        datPush("cellNo")
        logg('after ' + """cellNo""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing verb ( @ ) ')
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
    logg('for pdc3-4 processing text ')
    logg("""yescell""")
    if (r == p['OK']):
        logg('push text ' + """yescell""")
        datPush("yescell")
        logg('after ' + """yescell""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing verb ( dup ) ')
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
    logg('for pdc3-4 processing verb ( @ ) ')
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
    logg('for pdc3-4 processing verb ( lib! ) ')
    if (r == p['OK']):
        logg('call lib! ')
        p['sy']['lib!'](p)
        logg('after lib!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing text ')
    logg("""cellNo""")
    if (r == p['OK']):
        logg('push text ' + """cellNo""")
        datPush("cellNo")
        logg('after ' + """cellNo""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing verb ( @ ) ')
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
    logg('for pdc3-4 processing text ')
    logg("""nocell""")
    if (r == p['OK']):
        logg('push text ' + """nocell""")
        datPush("nocell")
        logg('after ' + """nocell""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing text ')
    logg("""-99""")
    if (r == p['OK']):
        logg('push text ' + """-99""")
        datPush("-99")
        logg('after ' + """-99""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing verb ( lib! ) ')
    if (r == p['OK']):
        logg('call lib! ')
        p['sy']['lib!'](p)
        logg('after lib!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pdc3-4 processing verb ( tail. ) ')
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
    logg('final pdc3_4')
#end pdc3_4

def pdc3 (x):
    global p
    logg('begin pdc3')
    ## point of umbrella
    pdc3Ctl = 1 # starting spoke
    while pdc3Ctl != 0:
        logg('loop pdc3Ctl = ' + pdc3Ctl.__str__())
        if (pdc3Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (pdc3Ctl == 1):
            logg('call pdc3_1')
            pdc3_1()
            logg('after call pdc3_1')
            # test and adjust for new spoke
            pdc3Ctl = chk(pdc3Ctl)

        elif (pdc3Ctl == 2):
            logg('call pdc3_2')
            pdc3_2()
            logg('after call pdc3_2')
            # test and adjust for new spoke
            pdc3Ctl = chk(pdc3Ctl)

        elif (pdc3Ctl == 3):
            logg('call pdc3_3')
            pdc3_3()
            logg('after call pdc3_3')
            # test and adjust for new spoke
            pdc3Ctl = chk(pdc3Ctl)

        elif (pdc3Ctl == 4):
            logg('call pdc3_4')
            pdc3_4()
            logg('after call pdc3_4')
            # test and adjust for new spoke
            pdc3Ctl = chk(pdc3Ctl)

        else:
            #final
            logg('final pdc3')    
            pdc3Ctl = 0 # break
        #endif
    #wend
#end pdc3

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

    # paragraph pdc
    p['sy']['pdc'] = pdc
    #

    # paragraph pdc2
    p['sy']['pdc2'] = pdc2
    #

    # paragraph ckcn
    p['sy']['ckcn'] = ckcn
    #

    # paragraph pdc3
    p['sy']['pdc3'] = pdc3
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

