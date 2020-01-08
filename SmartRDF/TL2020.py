
#file TL2020.py
#generated for TL2020.basii 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def TLMain_1():
    global p
    logg('TLMain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- script fileName?  -- ') 
    if (r == p['OK']):
        logg('push text script fileName?  ')
        datPush("script fileName? ")
        logg('after script fileName?  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ask ) ')
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
    logg('processing verb ( dup ) ')
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
    logg('processing text -- sfn -- ') 
    if (r == p['OK']):
        logg('push text sfn ')
        datPush("sfn")
        logg('after sfn ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ! ) ')
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
    logg('processing verb ( initTL ) ')
    if (r == p['OK']):
        logg('call initTL ')
        p['sy']['initTL'](p)
        logg('after initTL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( TL1 ) ')
    if (r == p['OK']):
        logg('call TL1 ')
        p['sy']['TL1'](p)
        logg('after TL1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final TLMain_1')
#end TLMain_1

def TLMain (x):
    global p
    logg('begin TLMain')
    ## point of umbrella
    TLMainCtl = 1 # starting spoke
    while TLMainCtl != 0:
        logg('loop TLMainCtl = ' + TLMainCtl.__str__())
        if (TLMainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (TLMainCtl == 1):
            logg('call TLMain_1')
            TLMain_1()
            logg('after call TLMain_1')
            # test and adjust for new spoke
            TLMainCtl = chk(TLMainCtl)

        else:
            #final
            logg('final TLMain')    
            TLMainCtl = 0 # break
        #endif
    #wend
#end TLMain

def initTL_1():
    global p
    logg('initTL_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- fioiP -- ') 
    if (r == p['OK']):
        logg('push text fioiP ')
        datPush("fioiP")
        logg('after fioiP ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( takeV ) ')
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
    logg('processing text -- bpx.db -- ') 
    if (r == p['OK']):
        logg('push text bpx.db ')
        datPush("bpx.db")
        logg('after bpx.db ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- SQV -- ') 
    if (r == p['OK']):
        logg('push text SQV ')
        datPush("SQV")
        logg('after SQV ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( takeV ) ')
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
    logg('processing verb ( read ) ')
    if (r == p['OK']):
        logg('call read ')
        p['sy']['read'](p)
        logg('after read')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final initTL_1')
#end initTL_1

def initTL (x):
    global p
    logg('begin initTL')
    ## point of umbrella
    initTLCtl = 1 # starting spoke
    while initTLCtl != 0:
        logg('loop initTLCtl = ' + initTLCtl.__str__())
        if (initTLCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (initTLCtl == 1):
            logg('call initTL_1')
            initTL_1()
            logg('after call initTL_1')
            # test and adjust for new spoke
            initTLCtl = chk(initTLCtl)

        else:
            #final
            logg('final initTL')    
            initTLCtl = 0 # break
        #endif
    #wend
#end initTL

def read_1():
    global p
    logg('read_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( .s ) ')
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
    logg('processing text -- >?  -- ') 
    if (r == p['OK']):
        logg('push text >?  ')
        datPush(">? ")
        logg('after >?  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ask ) ')
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
    logg('processing verb ( drop ) ')
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
    logg('final read_1')
#end read_1

def read (x):
    global p
    logg('begin read')
    ## point of umbrella
    readCtl = 1 # starting spoke
    while readCtl != 0:
        logg('loop readCtl = ' + readCtl.__str__())
        if (readCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (readCtl == 1):
            logg('call read_1')
            read_1()
            logg('after call read_1')
            # test and adjust for new spoke
            readCtl = chk(readCtl)

        else:
            #final
            logg('final read')    
            readCtl = 0 # break
        #endif
    #wend
#end read

def TL1_1():
    global p
    logg('TL1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==create ) ')
    if (r == p['OK']):
        logg('call ==create ')
        p['sy']['==create'](p)
        logg('after ==create')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ==tuple ) ')
    if (r == p['OK']):
        logg('call ==tuple ')
        p['sy']['==tuple'](p)
        logg('after ==tuple')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ==(( ) ')
    if (r == p['OK']):
        logg('call ==(( ')
        p['sy']['==(('](p)
        logg('after ==((')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( keyset ) ')
    if (r == p['OK']):
        logg('call keyset ')
        p['sy']['keyset'](p)
        logg('after keyset')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( actCreTL1 ) ')
    if (r == p['OK']):
        logg('call actCreTL1 ')
        p['sy']['actCreTL1'](p)
        logg('after actCreTL1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( read ) ')
    if (r == p['OK']):
        logg('call read ')
        p['sy']['read'](p)
        logg('after read')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( tail. ) ')
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
    logg('final TL1_1')
#end TL1_1

def TL1_2():
    global p
    logg('TL1_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==set ) ')
    if (r == p['OK']):
        logg('call ==set ')
        p['sy']['==set'](p)
        logg('after ==set')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( of ) ')
    if (r == p['OK']):
        logg('call of ')
        p['sy']['of'](p)
        logg('after of')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( [keysetValues] ) ')
    if (r == p['OK']):
        logg('call [keysetValues] ')
        p['sy']['[keysetValues]'](p)
        logg('after [keysetValues]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( === ) ')
    if (r == p['OK']):
        logg('call === ')
        p['sy']['==='](p)
        logg('after ===')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( read ) ')
    if (r == p['OK']):
        logg('call read ')
        p['sy']['read'](p)
        logg('after read')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final TL1_2')
#end TL1_2

def TL1_3():
    global p
    logg('TL1_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==get ) ')
    if (r == p['OK']):
        logg('call ==get ')
        p['sy']['==get'](p)
        logg('after ==get')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( of ) ')
    if (r == p['OK']):
        logg('call of ')
        p['sy']['of'](p)
        logg('after of')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( [keysetValues] ) ')
    if (r == p['OK']):
        logg('call [keysetValues] ')
        p['sy']['[keysetValues]'](p)
        logg('after [keysetValues]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( read ) ')
    if (r == p['OK']):
        logg('call read ')
        p['sy']['read'](p)
        logg('after read')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final TL1_3')
#end TL1_3

def TL1_4():
    global p
    logg('TL1_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==process ) ')
    if (r == p['OK']):
        logg('call ==process ')
        p['sy']['==process'](p)
        logg('after ==process')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( cnset ) ')
    if (r == p['OK']):
        logg('call cnset ')
        p['sy']['cnset'](p)
        logg('after cnset')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( read ) ')
    if (r == p['OK']):
        logg('call read ')
        p['sy']['read'](p)
        logg('after read')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final TL1_4')
#end TL1_4

def TL1 (x):
    global p
    logg('begin TL1')
    ## point of umbrella
    TL1Ctl = 1 # starting spoke
    while TL1Ctl != 0:
        logg('loop TL1Ctl = ' + TL1Ctl.__str__())
        if (TL1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (TL1Ctl == 1):
            logg('call TL1_1')
            TL1_1()
            logg('after call TL1_1')
            # test and adjust for new spoke
            TL1Ctl = chk(TL1Ctl)

        elif (TL1Ctl == 2):
            logg('call TL1_2')
            TL1_2()
            logg('after call TL1_2')
            # test and adjust for new spoke
            TL1Ctl = chk(TL1Ctl)

        elif (TL1Ctl == 3):
            logg('call TL1_3')
            TL1_3()
            logg('after call TL1_3')
            # test and adjust for new spoke
            TL1Ctl = chk(TL1Ctl)

        elif (TL1Ctl == 4):
            logg('call TL1_4')
            TL1_4()
            logg('after call TL1_4')
            # test and adjust for new spoke
            TL1Ctl = chk(TL1Ctl)

        else:
            #final
            logg('final TL1')    
            TL1Ctl = 0 # break
        #endif
    #wend
#end TL1

def keyset_1():
    global p
    logg('keyset_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( fpword ) ')
    if (r == p['OK']):
        logg('call fpword ')
        p['sy']['fpword'](p)
        logg('after fpword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing text -- keyset1 -- ') 
    if (r == p['OK']):
        logg('push text keyset1 ')
        datPush("keyset1")
        logg('after keyset1 ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( msg ) ')
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
    logg('processing verb ( read ) ')
    if (r == p['OK']):
        logg('call read ')
        p['sy']['read'](p)
        logg('after read')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ... ) ')
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
    logg('final keyset_1')
#end keyset_1

def keyset_2():
    global p
    logg('keyset_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( dup ) ')
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
    logg('processing verb ( ==) ) ')
    if (r == p['OK']):
        logg('call ==) ')
        p['sy']['==)'](p)
        logg('after ==)')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( drop ) ')
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
    logg('processing text -- keyset2 -- ') 
    if (r == p['OK']):
        logg('push text keyset2 ')
        datPush("keyset2")
        logg('after keyset2 ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( msg ) ')
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
    logg('processing verb ( read ) ')
    if (r == p['OK']):
        logg('call read ')
        p['sy']['read'](p)
        logg('after read')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final keyset_2')
#end keyset_2

def keyset_3():
    global p
    logg('keyset_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( dup ) ')
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
    logg('processing verb ( ==)) ) ')
    if (r == p['OK']):
        logg('call ==)) ')
        p['sy']['==))'](p)
        logg('after ==))')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( drop ) ')
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
    logg('processing verb ( ; ) ')
    if (r == p['OK']):
        logg('call ; ')
        p['sy'][';'](p)
        logg('after ;')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( def ) ')
    if (r == p['OK']):
        logg('call def ')
        p['sy']['def'](p)
        logg('after def')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( actCreTL1 ) ')
    if (r == p['OK']):
        logg('call actCreTL1 ')
        p['sy']['actCreTL1'](p)
        logg('after actCreTL1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( :- ) ')
    if (r == p['OK']):
        logg('call :- ')
        p['sy'][':-'](p)
        logg('after :-')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( [[ ) ')
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
    logg('processing verb ( 1 ) ')
    if (r == p['OK']):
        logg('call 1 ')
        p['sy']['1'](p)
        logg('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ]] ) ')
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
    logg('processing text -- actCreTL1 -- ') 
    if (r == p['OK']):
        logg('push text actCreTL1 ')
        datPush("actCreTL1")
        logg('after actCreTL1 ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( msg ) ')
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
    logg('processing verb ( read ) ')
    if (r == p['OK']):
        logg('call read ')
        p['sy']['read'](p)
        logg('after read')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final keyset_3')
#end keyset_3

def keyset (x):
    global p
    logg('begin keyset')
    ## point of umbrella
    keysetCtl = 1 # starting spoke
    while keysetCtl != 0:
        logg('loop keysetCtl = ' + keysetCtl.__str__())
        if (keysetCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (keysetCtl == 1):
            logg('call keyset_1')
            keyset_1()
            logg('after call keyset_1')
            # test and adjust for new spoke
            keysetCtl = chk(keysetCtl)

        elif (keysetCtl == 2):
            logg('call keyset_2')
            keyset_2()
            logg('after call keyset_2')
            # test and adjust for new spoke
            keysetCtl = chk(keysetCtl)

        elif (keysetCtl == 3):
            logg('call keyset_3')
            keyset_3()
            logg('after call keyset_3')
            # test and adjust for new spoke
            keysetCtl = chk(keysetCtl)

        else:
            #final
            logg('final keyset')    
            keysetCtl = 0 # break
        #endif
    #wend
#end keyset

def cnset_1():
    global p
    logg('cnset_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( fpword ) ')
    if (r == p['OK']):
        logg('call fpword ')
        p['sy']['fpword'](p)
        logg('after fpword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ... ) ')
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
    logg('final cnset_1')
#end cnset_1

def cnset_2():
    global p
    logg('cnset_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( dup ) ')
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
    logg('processing verb ( ==[[ ) ')
    if (r == p['OK']):
        logg('call ==[[ ')
        p['sy']['==[['](p)
        logg('after ==[[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( drop ) ')
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
    logg('processing verb ( ==]] ) ')
    if (r == p['OK']):
        logg('call ==]] ')
        p['sy']['==]]'](p)
        logg('after ==]]')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( 1 ) ')
    if (r == p['OK']):
        logg('call 1 ')
        p['sy']['1'](p)
        logg('after 1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( vn ) ')
    if (r == p['OK']):
        logg('call vn ')
        p['sy']['vn'](p)
        logg('after vn')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( ! ) ')
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
    logg('processing verb ( verbset ) ')
    if (r == p['OK']):
        logg('call verbset ')
        p['sy']['verbset'](p)
        logg('after verbset')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( tail. ) ')
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
    logg('final cnset_2')
#end cnset_2

def cnset_3():
    global p
    logg('cnset_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( dup ) ')
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
    logg('processing verb ( ==; ) ')
    if (r == p['OK']):
        logg('call ==; ')
        p['sy']['==;'](p)
        logg('after ==;')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( drop ) ')
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
    logg('final cnset_3')
#end cnset_3

def cnset_4():
    global p
    logg('cnset_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==@endend ) ')
    if (r == p['OK']):
        logg('call ==@endend ')
        p['sy']['==@endend'](p)
        logg('after ==@endend')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( closeDB ) ')
    if (r == p['OK']):
        logg('call closeDB ')
        p['sy']['closeDB'](p)
        logg('after closeDB')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final cnset_4')
#end cnset_4

def cnset (x):
    global p
    logg('begin cnset')
    ## point of umbrella
    cnsetCtl = 1 # starting spoke
    while cnsetCtl != 0:
        logg('loop cnsetCtl = ' + cnsetCtl.__str__())
        if (cnsetCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (cnsetCtl == 1):
            logg('call cnset_1')
            cnset_1()
            logg('after call cnset_1')
            # test and adjust for new spoke
            cnsetCtl = chk(cnsetCtl)

        elif (cnsetCtl == 2):
            logg('call cnset_2')
            cnset_2()
            logg('after call cnset_2')
            # test and adjust for new spoke
            cnsetCtl = chk(cnsetCtl)

        elif (cnsetCtl == 3):
            logg('call cnset_3')
            cnset_3()
            logg('after call cnset_3')
            # test and adjust for new spoke
            cnsetCtl = chk(cnsetCtl)

        elif (cnsetCtl == 4):
            logg('call cnset_4')
            cnset_4()
            logg('after call cnset_4')
            # test and adjust for new spoke
            cnsetCtl = chk(cnsetCtl)

        else:
            #final
            logg('final cnset')    
            cnsetCtl = 0 # break
        #endif
    #wend
#end cnset

def verbset_1():
    global p
    logg('verbset_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ... ) ')
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
    logg('final verbset_1')
#end verbset_1

def verbset_2():
    global p
    logg('verbset_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- verset2 -- ') 
    if (r == p['OK']):
        logg('push text verset2 ')
        datPush("verset2")
        logg('after verset2 ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( msg ) ')
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
    logg('processing verb ( read ) ')
    if (r == p['OK']):
        logg('call read ')
        p['sy']['read'](p)
        logg('after read')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final verbset_2')
#end verbset_2

def verbset_3():
    global p
    logg('verbset_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( .s ) ')
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

    #final
    logg('final verbset_3')
#end verbset_3

def verbset_4():
    global p
    logg('verbset_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( .s ) ')
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

    #final
    logg('final verbset_4')
#end verbset_4

def verbset (x):
    global p
    logg('begin verbset')
    ## point of umbrella
    verbsetCtl = 1 # starting spoke
    while verbsetCtl != 0:
        logg('loop verbsetCtl = ' + verbsetCtl.__str__())
        if (verbsetCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (verbsetCtl == 1):
            logg('call verbset_1')
            verbset_1()
            logg('after call verbset_1')
            # test and adjust for new spoke
            verbsetCtl = chk(verbsetCtl)

        elif (verbsetCtl == 2):
            logg('call verbset_2')
            verbset_2()
            logg('after call verbset_2')
            # test and adjust for new spoke
            verbsetCtl = chk(verbsetCtl)

        elif (verbsetCtl == 3):
            logg('call verbset_3')
            verbset_3()
            logg('after call verbset_3')
            # test and adjust for new spoke
            verbsetCtl = chk(verbsetCtl)

        elif (verbsetCtl == 4):
            logg('call verbset_4')
            verbset_4()
            logg('after call verbset_4')
            # test and adjust for new spoke
            verbsetCtl = chk(verbsetCtl)

        else:
            #final
            logg('final verbset')    
            verbsetCtl = 0 # break
        #endif
    #wend
#end verbset
