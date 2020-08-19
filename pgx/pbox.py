
#file pbox.py
#generated for pgx.basii at Tue Aug 18 17:06:09 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def pgfinit_1():
    global p
    logg('pgfinit_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgfinit-1 processing text ')
    logg("""heapV""")
    if (r == p['OK']):
        logg('push text ' + """heapV""")
        datPush("heapV")
        logg('after ' + """heapV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgfinit-1 processing verb ( takeV ) ')
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
    logg('for pgfinit-1 processing verb ( heapInit ) ')
    if (r == p['OK']):
        logg('call heapInit ')
        p['sy']['heapInit'](p)
        logg('after heapInit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgfinit-1 processing text ')
    logg("""lrV""")
    if (r == p['OK']):
        logg('push text ' + """lrV""")
        datPush("lrV")
        logg('after ' + """lrV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgfinit-1 processing verb ( takeV ) ')
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
    logg('for pgfinit-1 processing text ')
    logg("""ok""")
    if (r == p['OK']):
        logg('push text ' + """ok""")
        datPush("ok")
        logg('after ' + """ok""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgfinit-1 processing text ')
    logg("""pgfid""")
    if (r == p['OK']):
        logg('push text ' + """pgfid""")
        datPush("pgfid")
        logg('after ' + """pgfid""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgfinit-1 processing verb ( ! ) ')
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
    logg('final pgfinit_1')
#end pgfinit_1

def pgfinit (x):
    global p
    logg('begin pgfinit')
    ## point of umbrella
    pgfinitCtl = 1 # starting spoke
    while pgfinitCtl != 0:
        logg('loop pgfinitCtl = ' + pgfinitCtl.__str__())
        if (pgfinitCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgfinitCtl == 1):
            logg('call pgfinit_1')
            pgfinit_1()
            logg('after call pgfinit_1')
            # test and adjust for new spoke
            pgfinitCtl = chk(pgfinitCtl)

        else:
            #final
            logg('final pgfinit')    
            pgfinitCtl = 0 # break
        #endif
    #wend
#end pgfinit

def pgf_1():
    global p
    logg('pgf_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgf-1 processing text ')
    logg("""pgfid""")
    if (r == p['OK']):
        logg('push text ' + """pgfid""")
        datPush("pgfid")
        logg('after ' + """pgfid""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-1 processing verb ( @ ) ')
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
    logg('for pgf-1 processing text ')
    logg("""ok""")
    if (r == p['OK']):
        logg('push text ' + """ok""")
        datPush("ok")
        logg('after ' + """ok""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-1 processing verb ( <> ) ')
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
    logg('for pgf-1 processing verb ( pgfinit ) ')
    if (r == p['OK']):
        logg('call pgfinit ')
        p['sy']['pgfinit'](p)
        logg('after pgfinit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-1 processing verb ( lnz ) ')
    if (r == p['OK']):
        logg('call lnz ')
        p['sy']['lnz'](p)
        logg('after lnz')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-1 processing verb ( lrz ) ')
    if (r == p['OK']):
        logg('call lrz ')
        p['sy']['lrz'](p)
        logg('after lrz')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-1 processing verb ( ... ) ')
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
    logg('final pgf_1')
#end pgf_1

def pgf_2():
    global p
    logg('pgf_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgf-2 processing text ')
    logg("""pgf""")
    if (r == p['OK']):
        logg('push text ' + """pgf""")
        datPush("pgf")
        logg('after ' + """pgf""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-2 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-2 processing verb ( dup ) ')
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
    logg('for pgf-2 processing verb ( ln! ) ')
    if (r == p['OK']):
        logg('call ln! ')
        p['sy']['ln!'](p)
        logg('after ln!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-2 processing verb ( l@ ) ')
    if (r == p['OK']):
        logg('call l@ ')
        p['sy']['l@'](p)
        logg('after l@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-2 processing verb ( lr! ) ')
    if (r == p['OK']):
        logg('call lr! ')
        p['sy']['lr!'](p)
        logg('after lr!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-2 processing text ')
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
    logg('for pgf-2 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf-2 processing verb ( ! ) ')
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
    logg('for pgf-2 processing verb ( pgc ) ')
    if (r == p['OK']):
        logg('call pgc ')
        p['sy']['pgc'](p)
        logg('after pgc')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final pgf_2')
#end pgf_2

def pgf (x):
    global p
    logg('begin pgf')
    ## point of umbrella
    pgfCtl = 1 # starting spoke
    while pgfCtl != 0:
        logg('loop pgfCtl = ' + pgfCtl.__str__())
        if (pgfCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgfCtl == 1):
            logg('call pgf_1')
            pgf_1()
            logg('after call pgf_1')
            # test and adjust for new spoke
            pgfCtl = chk(pgfCtl)

        elif (pgfCtl == 2):
            logg('call pgf_2')
            pgf_2()
            logg('after call pgf_2')
            # test and adjust for new spoke
            pgfCtl = chk(pgfCtl)

        else:
            #final
            logg('final pgf')    
            pgfCtl = 0 # break
        #endif
    #wend
#end pgf

def pgc_1():
    global p
    logg('pgc_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgc-1 processing text ')
    logg("""pgc ctl=""")
    if (r == p['OK']):
        logg('push text ' + """pgc ctl=""")
        datPush("pgc ctl=")
        logg('after ' + """pgc ctl=""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-1 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-1 processing verb ( @ ) ')
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
    logg('for pgc-1 processing verb ( cat ) ')
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
    logg('for pgc-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-1 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-1 processing verb ( @ ) ')
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
    logg('for pgc-1 processing text ')
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
    logg('for pgc-1 processing verb ( = ) ')
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
    logg('for pgc-1 processing verb ( ppgc ) ')
    if (r == p['OK']):
        logg('call ppgc ')
        p['sy']['ppgc'](p)
        logg('after ppgc')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-1 processing verb ( tail. ) ')
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
    logg('final pgc_1')
#end pgc_1

def pgc_2():
    global p
    logg('pgc_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgc-2 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-2 processing verb ( @ ) ')
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
    logg('for pgc-2 processing text ')
    logg("""2""")
    if (r == p['OK']):
        logg('push text ' + """2""")
        datPush("2")
        logg('after ' + """2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-2 processing verb ( = ) ')
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
    logg('for pgc-2 processing verb ( cpgc ) ')
    if (r == p['OK']):
        logg('call cpgc ')
        p['sy']['cpgc'](p)
        logg('after cpgc')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-2 processing verb ( tail. ) ')
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
    logg('final pgc_2')
#end pgc_2

def pgc_3():
    global p
    logg('pgc_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgc-3 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-3 processing verb ( @ ) ')
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
    logg('for pgc-3 processing text ')
    logg("""3""")
    if (r == p['OK']):
        logg('push text ' + """3""")
        datPush("3")
        logg('after ' + """3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-3 processing verb ( = ) ')
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
    logg('for pgc-3 processing verb ( pvpgc ) ')
    if (r == p['OK']):
        logg('call pvpgc ')
        p['sy']['pvpgc'](p)
        logg('after pvpgc')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-3 processing verb ( tail. ) ')
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
    logg('final pgc_3')
#end pgc_3

def pgc_4():
    global p
    logg('pgc_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgc-4 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-4 processing verb ( @ ) ')
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
    logg('for pgc-4 processing text ')
    logg("""4""")
    if (r == p['OK']):
        logg('push text ' + """4""")
        datPush("4")
        logg('after ' + """4""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-4 processing verb ( = ) ')
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
    logg('for pgc-4 processing verb ( cspgc ) ')
    if (r == p['OK']):
        logg('call cspgc ')
        p['sy']['cspgc'](p)
        logg('after cspgc')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-4 processing verb ( tail. ) ')
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
    logg('final pgc_4')
#end pgc_4

def pgc_5():
    global p
    logg('pgc_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgc-5 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-5 processing verb ( @ ) ')
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
    logg('for pgc-5 processing text ')
    logg("""5""")
    if (r == p['OK']):
        logg('push text ' + """5""")
        datPush("5")
        logg('after ' + """5""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-5 processing verb ( = ) ')
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
    logg('for pgc-5 processing verb ( pgf ) ')
    if (r == p['OK']):
        logg('call pgf ')
        p['sy']['pgf'](p)
        logg('after pgf')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-5 processing verb ( tail. ) ')
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
    logg('final pgc_5')
#end pgc_5

def pgc_6():
    global p
    logg('pgc_6')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgc-6 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-6 processing verb ( @ ) ')
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
    logg('for pgc-6 processing text ')
    logg("""6""")
    if (r == p['OK']):
        logg('push text ' + """6""")
        datPush("6")
        logg('after ' + """6""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-6 processing verb ( = ) ')
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
    logg('for pgc-6 processing verb ( pgcv2 ) ')
    if (r == p['OK']):
        logg('call pgcv2 ')
        p['sy']['pgcv2'](p)
        logg('after pgcv2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-6 processing verb ( tail. ) ')
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
    logg('final pgc_6')
#end pgc_6

def pgc_7():
    global p
    logg('pgc_7')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgc-7 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-7 processing verb ( @ ) ')
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
    logg('for pgc-7 processing text ')
    logg("""8""")
    if (r == p['OK']):
        logg('push text ' + """8""")
        datPush("8")
        logg('after ' + """8""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-7 processing verb ( = ) ')
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
    logg('for pgc-7 processing verb ( lr8 ) ')
    if (r == p['OK']):
        logg('call lr8 ')
        p['sy']['lr8'](p)
        logg('after lr8')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-7 processing verb ( tail. ) ')
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
    logg('final pgc_7')
#end pgc_7

def pgc_8():
    global p
    logg('pgc_8')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgc-8 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-8 processing verb ( @ ) ')
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
    logg('for pgc-8 processing text ')
    logg("""9""")
    if (r == p['OK']):
        logg('push text ' + """9""")
        datPush("9")
        logg('after ' + """9""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-8 processing verb ( = ) ')
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
    logg('for pgc-8 processing verb ( lr4 ) ')
    if (r == p['OK']):
        logg('call lr4 ')
        p['sy']['lr4'](p)
        logg('after lr4')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgc-8 processing verb ( tail. ) ')
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
    logg('final pgc_8')
#end pgc_8

def pgc_9():
    global p
    logg('pgc_9')
    datPush(p['OK'])

    #final
    logg('final pgc_9')
#end pgc_9

def pgc (x):
    global p
    logg('begin pgc')
    ## point of umbrella
    pgcCtl = 1 # starting spoke
    while pgcCtl != 0:
        logg('loop pgcCtl = ' + pgcCtl.__str__())
        if (pgcCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgcCtl == 1):
            logg('call pgc_1')
            pgc_1()
            logg('after call pgc_1')
            # test and adjust for new spoke
            pgcCtl = chk(pgcCtl)

        elif (pgcCtl == 2):
            logg('call pgc_2')
            pgc_2()
            logg('after call pgc_2')
            # test and adjust for new spoke
            pgcCtl = chk(pgcCtl)

        elif (pgcCtl == 3):
            logg('call pgc_3')
            pgc_3()
            logg('after call pgc_3')
            # test and adjust for new spoke
            pgcCtl = chk(pgcCtl)

        elif (pgcCtl == 4):
            logg('call pgc_4')
            pgc_4()
            logg('after call pgc_4')
            # test and adjust for new spoke
            pgcCtl = chk(pgcCtl)

        elif (pgcCtl == 5):
            logg('call pgc_5')
            pgc_5()
            logg('after call pgc_5')
            # test and adjust for new spoke
            pgcCtl = chk(pgcCtl)

        elif (pgcCtl == 6):
            logg('call pgc_6')
            pgc_6()
            logg('after call pgc_6')
            # test and adjust for new spoke
            pgcCtl = chk(pgcCtl)

        elif (pgcCtl == 7):
            logg('call pgc_7')
            pgc_7()
            logg('after call pgc_7')
            # test and adjust for new spoke
            pgcCtl = chk(pgcCtl)

        elif (pgcCtl == 8):
            logg('call pgc_8')
            pgc_8()
            logg('after call pgc_8')
            # test and adjust for new spoke
            pgcCtl = chk(pgcCtl)

        elif (pgcCtl == 9):
            logg('call pgc_9')
            pgc_9()
            logg('after call pgc_9')
            # test and adjust for new spoke
            pgcCtl = chk(pgcCtl)

        else:
            #final
            logg('final pgc')    
            pgcCtl = 0 # break
        #endif
    #wend
#end pgc

def ppgc_1():
    global p
    logg('ppgc_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ppgc-1 processing text ')
    logg("""ppgc""")
    if (r == p['OK']):
        logg('push text ' + """ppgc""")
        datPush("ppgc")
        logg('after ' + """ppgc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ppgc-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ppgc-1 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ppgc-1 processing text ')
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
    logg('for ppgc-1 processing verb ( ! ) ')
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
    logg('for ppgc-1 processing verb ( ... ) ')
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
    logg('final ppgc_1')
#end ppgc_1

def ppgc_2():
    global p
    logg('ppgc_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ppgc-2 processing text ')
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
    logg('for ppgc-2 processing text ')
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
    logg('for ppgc-2 processing verb ( ! ) ')
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
    logg('for ppgc-2 processing text ')
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
    logg('for ppgc-2 processing verb ( @ ) ')
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
    logg('for ppgc-2 processing text ')
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
    logg('for ppgc-2 processing verb ( = ) ')
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
    logg('for ppgc-2 processing verb ( pgdef ) ')
    if (r == p['OK']):
        logg('call pgdef ')
        p['sy']['pgdef'](p)
        logg('after pgdef')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ppgc-2 processing text ')
    logg("""2""")
    if (r == p['OK']):
        logg('push text ' + """2""")
        datPush("2")
        logg('after ' + """2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ppgc-2 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ppgc-2 processing verb ( ! ) ')
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
    logg('final ppgc_2')
#end ppgc_2

def ppgc_3():
    global p
    logg('ppgc_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ppgc-3 processing text ')
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
    logg('for ppgc-3 processing verb ( @ ) ')
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
    logg('for ppgc-3 processing text ')
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
    logg('for ppgc-3 processing verb ( = ) ')
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
    logg('for ppgc-3 processing text ')
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
    logg('for ppgc-3 processing text ')
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
    logg('for ppgc-3 processing verb ( ! ) ')
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
    logg('for ppgc-3 processing text ')
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
    logg('for ppgc-3 processing verb ( msg ) ')
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
    logg('for ppgc-3 processing text ')
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
    logg('for ppgc-3 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ppgc-3 processing verb ( ! ) ')
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
    logg('final ppgc_3')
#end ppgc_3

def ppgc_4():
    global p
    logg('ppgc_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for ppgc-4 processing text ')
    logg("""paragraph error""")
    if (r == p['OK']):
        logg('push text ' + """paragraph error""")
        datPush("paragraph error")
        logg('after ' + """paragraph error""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ppgc-4 processing verb ( msg ) ')
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
    logg('for ppgc-4 processing text ')
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
    logg('for ppgc-4 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for ppgc-4 processing verb ( ! ) ')
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
    logg('final ppgc_4')
#end ppgc_4

def ppgc (x):
    global p
    logg('begin ppgc')
    ## point of umbrella
    ppgcCtl = 1 # starting spoke
    while ppgcCtl != 0:
        logg('loop ppgcCtl = ' + ppgcCtl.__str__())
        if (ppgcCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (ppgcCtl == 1):
            logg('call ppgc_1')
            ppgc_1()
            logg('after call ppgc_1')
            # test and adjust for new spoke
            ppgcCtl = chk(ppgcCtl)

        elif (ppgcCtl == 2):
            logg('call ppgc_2')
            ppgc_2()
            logg('after call ppgc_2')
            # test and adjust for new spoke
            ppgcCtl = chk(ppgcCtl)

        elif (ppgcCtl == 3):
            logg('call ppgc_3')
            ppgc_3()
            logg('after call ppgc_3')
            # test and adjust for new spoke
            ppgcCtl = chk(ppgcCtl)

        elif (ppgcCtl == 4):
            logg('call ppgc_4')
            ppgc_4()
            logg('after call ppgc_4')
            # test and adjust for new spoke
            ppgcCtl = chk(ppgcCtl)

        else:
            #final
            logg('final ppgc')    
            ppgcCtl = 0 # break
        #endif
    #wend
#end ppgc

def pgdef_1():
    global p
    logg('pgdef_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgdef-1 processing text ')
    logg("""pgdef""")
    if (r == p['OK']):
        logg('push text ' + """pgdef""")
        datPush("pgdef")
        logg('after ' + """pgdef""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgdef-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgdef-1 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgdef-1 processing text ')
    logg("""pna""")
    if (r == p['OK']):
        logg('push text ' + """pna""")
        datPush("pna")
        logg('after ' + """pna""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgdef-1 processing verb ( ! ) ')
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
    logg('for pgdef-1 processing text ')
    logg("""pna is """)
    if (r == p['OK']):
        logg('push text ' + """pna is """)
        datPush("pna is ")
        logg('after ' + """pna is """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgdef-1 processing text ')
    logg("""pna""")
    if (r == p['OK']):
        logg('push text ' + """pna""")
        datPush("pna")
        logg('after ' + """pna""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgdef-1 processing verb ( @ ) ')
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
    logg('for pgdef-1 processing verb ( cats ) ')
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
    logg('for pgdef-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgdef-1 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgdef-1 processing verb ( drop ) ')
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
    logg('final pgdef_1')
#end pgdef_1

def pgdef (x):
    global p
    logg('begin pgdef')
    ## point of umbrella
    pgdefCtl = 1 # starting spoke
    while pgdefCtl != 0:
        logg('loop pgdefCtl = ' + pgdefCtl.__str__())
        if (pgdefCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgdefCtl == 1):
            logg('call pgdef_1')
            pgdef_1()
            logg('after call pgdef_1')
            # test and adjust for new spoke
            pgdefCtl = chk(pgdefCtl)

        else:
            #final
            logg('final pgdef')    
            pgdefCtl = 0 # break
        #endif
    #wend
#end pgdef

def cpgc_1():
    global p
    logg('cpgc_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cpgc-1 processing text ')
    logg("""cpgc""")
    if (r == p['OK']):
        logg('push text ' + """cpgc""")
        datPush("cpgc")
        logg('after ' + """cpgc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-1 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-1 processing text ')
    logg("""cnx""")
    if (r == p['OK']):
        logg('push text ' + """cnx""")
        datPush("cnx")
        logg('after ' + """cnx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-1 processing verb ( ! ) ')
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
    logg('for cpgc-1 processing text ')
    logg("""cnx=""")
    if (r == p['OK']):
        logg('push text ' + """cnx=""")
        datPush("cnx=")
        logg('after ' + """cnx=""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-1 processing text ')
    logg("""cnx""")
    if (r == p['OK']):
        logg('push text ' + """cnx""")
        datPush("cnx")
        logg('after ' + """cnx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-1 processing verb ( @ ) ')
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
    logg('for cpgc-1 processing verb ( cat ) ')
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
    logg('for cpgc-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-1 processing verb ( ... ) ')
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
    logg('final cpgc_1')
#end cpgc_1

def cpgc_2():
    global p
    logg('cpgc_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cpgc-2 processing text ')
    logg("""cnx""")
    if (r == p['OK']):
        logg('push text ' + """cnx""")
        datPush("cnx")
        logg('after ' + """cnx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-2 processing verb ( @ ) ')
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
    logg('for cpgc-2 processing verb ( SEMI? ) ')
    if (r == p['OK']):
        logg('call SEMI? ')
        p['sy']['SEMI?'](p)
        logg('after SEMI?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-2 processing text ')
    logg("""9""")
    if (r == p['OK']):
        logg('push text ' + """9""")
        datPush("9")
        logg('after ' + """9""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-2 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-2 processing verb ( ! ) ')
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
    logg('final cpgc_2')
#end cpgc_2

def cpgc_3():
    global p
    logg('cpgc_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cpgc-3 processing text ')
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
    logg('for cpgc-3 processing text ')
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
    logg('for cpgc-3 processing verb ( ! ) ')
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
    logg('for cpgc-3 processing text ')
    logg("""cnx""")
    if (r == p['OK']):
        logg('push text ' + """cnx""")
        datPush("cnx")
        logg('after ' + """cnx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing verb ( @ ) ')
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
    logg('for cpgc-3 processing text ')
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
    logg('for cpgc-3 processing verb ( = ) ')
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
    logg('for cpgc-3 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing text ')
    logg("""cnum""")
    if (r == p['OK']):
        logg('push text ' + """cnum""")
        datPush("cnum")
        logg('after ' + """cnum""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing verb ( ! ) ')
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
    logg('for cpgc-3 processing text ')
    logg("""cnum=""")
    if (r == p['OK']):
        logg('push text ' + """cnum=""")
        datPush("cnum=")
        logg('after ' + """cnum=""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing text ')
    logg("""cnum""")
    if (r == p['OK']):
        logg('push text ' + """cnum""")
        datPush("cnum")
        logg('after ' + """cnum""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing verb ( @ ) ')
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
    logg('for cpgc-3 processing verb ( cat ) ')
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
    logg('for cpgc-3 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing text ')
    logg("""2""")
    if (r == p['OK']):
        logg('push text ' + """2""")
        datPush("2")
        logg('after ' + """2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing text ')
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
    logg('for cpgc-3 processing verb ( ! ) ')
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
    logg('for cpgc-3 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing text ')
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
    logg('for cpgc-3 processing verb ( = ) ')
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
    logg('for cpgc-3 processing text ')
    logg("""3""")
    if (r == p['OK']):
        logg('push text ' + """3""")
        datPush("3")
        logg('after ' + """3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-3 processing verb ( ! ) ')
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
    logg('final cpgc_3')
#end cpgc_3

def cpgc_4():
    global p
    logg('cpgc_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cpgc-4 processing text ')
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
    logg('for cpgc-4 processing verb ( @ ) ')
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
    logg('for cpgc-4 processing text ')
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
    logg('for cpgc-4 processing verb ( = ) ')
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
    logg('for cpgc-4 processing text ')
    logg("""expected [[""")
    if (r == p['OK']):
        logg('push text ' + """expected [[""")
        datPush("expected [[")
        logg('after ' + """expected [[""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-4 processing text ')
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
    logg('for cpgc-4 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-4 processing verb ( ! ) ')
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
    logg('final cpgc_4')
#end cpgc_4

def cpgc_5():
    global p
    logg('cpgc_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cpgc-5 processing text ')
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
    logg('for cpgc-5 processing verb ( @ ) ')
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
    logg('for cpgc-5 processing text ')
    logg("""2""")
    if (r == p['OK']):
        logg('push text ' + """2""")
        datPush("2")
        logg('after ' + """2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-5 processing verb ( = ) ')
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
    logg('for cpgc-5 processing text ')
    logg("""expected ]]""")
    if (r == p['OK']):
        logg('push text ' + """expected ]]""")
        datPush("expected ]]")
        logg('after ' + """expected ]]""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-5 processing text ')
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
    logg('for cpgc-5 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-5 processing verb ( ! ) ')
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
    logg('final cpgc_5')
#end cpgc_5

def cpgc_6():
    global p
    logg('cpgc_6')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cpgc-6 processing text ')
    logg("""cpgc fall thru""")
    if (r == p['OK']):
        logg('push text ' + """cpgc fall thru""")
        datPush("cpgc fall thru")
        logg('after ' + """cpgc fall thru""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cpgc-6 processing verb ( msg ) ')
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
    logg('final cpgc_6')
#end cpgc_6

def cpgc (x):
    global p
    logg('begin cpgc')
    ## point of umbrella
    cpgcCtl = 1 # starting spoke
    while cpgcCtl != 0:
        logg('loop cpgcCtl = ' + cpgcCtl.__str__())
        if (cpgcCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (cpgcCtl == 1):
            logg('call cpgc_1')
            cpgc_1()
            logg('after call cpgc_1')
            # test and adjust for new spoke
            cpgcCtl = chk(cpgcCtl)

        elif (cpgcCtl == 2):
            logg('call cpgc_2')
            cpgc_2()
            logg('after call cpgc_2')
            # test and adjust for new spoke
            cpgcCtl = chk(cpgcCtl)

        elif (cpgcCtl == 3):
            logg('call cpgc_3')
            cpgc_3()
            logg('after call cpgc_3')
            # test and adjust for new spoke
            cpgcCtl = chk(cpgcCtl)

        elif (cpgcCtl == 4):
            logg('call cpgc_4')
            cpgc_4()
            logg('after call cpgc_4')
            # test and adjust for new spoke
            cpgcCtl = chk(cpgcCtl)

        elif (cpgcCtl == 5):
            logg('call cpgc_5')
            cpgc_5()
            logg('after call cpgc_5')
            # test and adjust for new spoke
            cpgcCtl = chk(cpgcCtl)

        elif (cpgcCtl == 6):
            logg('call cpgc_6')
            cpgc_6()
            logg('after call cpgc_6')
            # test and adjust for new spoke
            cpgcCtl = chk(cpgcCtl)

        else:
            #final
            logg('final cpgc')    
            cpgcCtl = 0 # break
        #endif
    #wend
#end cpgc

def pvpgc_1():
    global p
    logg('pvpgc_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pvpgc-1 processing text ')
    logg("""vpgc""")
    if (r == p['OK']):
        logg('push text ' + """vpgc""")
        datPush("vpgc")
        logg('after ' + """vpgc""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-1 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-1 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-1 processing verb ( ! ) ')
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
    logg('for pvpgc-1 processing text ')
    logg("""vx=""")
    if (r == p['OK']):
        logg('push text ' + """vx=""")
        datPush("vx=")
        logg('after ' + """vx=""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-1 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-1 processing verb ( @ ) ')
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
    logg('for pvpgc-1 processing verb ( cat ) ')
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
    logg('for pvpgc-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-1 processing verb ( ... ) ')
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
    logg('final pvpgc_1')
#end pvpgc_1

def pvpgc_2():
    global p
    logg('pvpgc_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pvpgc-2 processing text ')
    logg("""v-2""")
    if (r == p['OK']):
        logg('push text ' + """v-2""")
        datPush("v-2")
        logg('after ' + """v-2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-2 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-2 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-2 processing verb ( @ ) ')
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
    logg('for pvpgc-2 processing text ')
    logg("""...""")
    if (r == p['OK']):
        logg('push text ' + """...""")
        datPush("...")
        logg('after ' + """...""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-2 processing verb ( = ) ')
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
    logg('for pvpgc-2 processing verb ( pgcv2 ) ')
    if (r == p['OK']):
        logg('call pgcv2 ')
        p['sy']['pgcv2'](p)
        logg('after pgcv2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final pvpgc_2')
#end pvpgc_2

def pvpgc_3():
    global p
    logg('pvpgc_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pvpgc-3 processing text ')
    logg("""v-3""")
    if (r == p['OK']):
        logg('push text ' + """v-3""")
        datPush("v-3")
        logg('after ' + """v-3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-3 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-3 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-3 processing verb ( @ ) ')
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
    logg('for pvpgc-3 processing text ')
    logg("""tail.""")
    if (r == p['OK']):
        logg('push text ' + """tail.""")
        datPush("tail.")
        logg('after ' + """tail.""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-3 processing verb ( = ) ')
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
    logg('for pvpgc-3 processing verb ( pgcv3 ) ')
    if (r == p['OK']):
        logg('call pgcv3 ')
        p['sy']['pgcv3'](p)
        logg('after pgcv3')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final pvpgc_3')
#end pvpgc_3

def pvpgc_4():
    global p
    logg('pvpgc_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pvpgc-4 processing text ')
    logg("""v-4""")
    if (r == p['OK']):
        logg('push text ' + """v-4""")
        datPush("v-4")
        logg('after ' + """v-4""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-4 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-4 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-4 processing verb ( @ ) ')
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
    logg('for pvpgc-4 processing verb ( c1 ) ')
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
    logg('for pvpgc-4 processing verb ( Q? ) ')
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
    logg('for pvpgc-4 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-4 processing verb ( @ ) ')
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
    logg('for pvpgc-4 processing verb ( woB ) ')
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
    logg('for pvpgc-4 processing text ')
    logg("""3""")
    if (r == p['OK']):
        logg('push text ' + """3""")
        datPush("3")
        logg('after ' + """3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-4 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-4 processing verb ( ! ) ')
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
    logg('final pvpgc_4')
#end pvpgc_4

def pvpgc_5():
    global p
    logg('pvpgc_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pvpgc-5 processing text ')
    logg("""v-5""")
    if (r == p['OK']):
        logg('push text ' + """v-5""")
        datPush("v-5")
        logg('after ' + """v-5""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-5 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-5 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-5 processing verb ( @ ) ')
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
    logg('for pvpgc-5 processing verb ( c1 ) ')
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
    logg('for pvpgc-5 processing verb ( T? ) ')
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
    logg('for pvpgc-5 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-5 processing verb ( @ ) ')
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
    logg('for pvpgc-5 processing verb ( woB ) ')
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
    logg('for pvpgc-5 processing text ')
    logg("""3""")
    if (r == p['OK']):
        logg('push text ' + """3""")
        datPush("3")
        logg('after ' + """3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-5 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-5 processing verb ( ! ) ')
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
    logg('final pvpgc_5')
#end pvpgc_5

def pvpgc_6():
    global p
    logg('pvpgc_6')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pvpgc-6 processing text ')
    logg("""v-6""")
    if (r == p['OK']):
        logg('push text ' + """v-6""")
        datPush("v-6")
        logg('after ' + """v-6""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-6 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-6 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-6 processing verb ( @ ) ')
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
    logg('for pvpgc-6 processing text ')
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
    logg('for pvpgc-6 processing verb ( = ) ')
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
    logg('for pvpgc-6 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-6 processing verb ( l@ ) ')
    if (r == p['OK']):
        logg('call l@ ')
        p['sy']['l@'](p)
        logg('after l@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-6 processing verb ( lr! ) ')
    if (r == p['OK']):
        logg('call lr! ')
        p['sy']['lr!'](p)
        logg('after lr!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-6 processing text ')
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
    logg('for pvpgc-6 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-6 processing verb ( ! ) ')
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
    logg('final pvpgc_6')
#end pvpgc_6

def pvpgc_7():
    global p
    logg('pvpgc_7')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pvpgc-7 processing text ')
    logg("""v-7""")
    if (r == p['OK']):
        logg('push text ' + """v-7""")
        datPush("v-7")
        logg('after ' + """v-7""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-7 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-7 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-7 processing verb ( @ ) ')
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
    logg('for pvpgc-7 processing verb ( isnum? ) ')
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
    logg('for pvpgc-7 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-7 processing verb ( @ ) ')
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
    logg('for pvpgc-7 processing text ')
    logg("""3""")
    if (r == p['OK']):
        logg('push text ' + """3""")
        datPush("3")
        logg('after ' + """3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-7 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-7 processing verb ( ! ) ')
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
    logg('final pvpgc_7')
#end pvpgc_7

def pvpgc_8():
    global p
    logg('pvpgc_8')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pvpgc-8 processing text ')
    logg("""v-8""")
    if (r == p['OK']):
        logg('push text ' + """v-8""")
        datPush("v-8")
        logg('after ' + """v-8""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-8 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-8 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-8 processing verb ( @ ) ')
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
    logg('for pvpgc-8 processing verb ( P? ) ')
    if (r == p['OK']):
        logg('call P? ')
        p['sy']['P?'](p)
        logg('after P?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-8 processing text ')
    logg("""8""")
    if (r == p['OK']):
        logg('push text ' + """8""")
        datPush("8")
        logg('after ' + """8""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-8 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-8 processing verb ( ! ) ')
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
    logg('final pvpgc_8')
#end pvpgc_8

def pvpgc_9():
    global p
    logg('pvpgc_9')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pvpgc-9 processing text ')
    logg("""v-9""")
    if (r == p['OK']):
        logg('push text ' + """v-9""")
        datPush("v-9")
        logg('after ' + """v-9""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-9 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pvpgc-9 processing verb ( voknok ) ')
    if (r == p['OK']):
        logg('call voknok ')
        p['sy']['voknok'](p)
        logg('after voknok')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final pvpgc_9')
#end pvpgc_9

def pvpgc (x):
    global p
    logg('begin pvpgc')
    ## point of umbrella
    pvpgcCtl = 1 # starting spoke
    while pvpgcCtl != 0:
        logg('loop pvpgcCtl = ' + pvpgcCtl.__str__())
        if (pvpgcCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pvpgcCtl == 1):
            logg('call pvpgc_1')
            pvpgc_1()
            logg('after call pvpgc_1')
            # test and adjust for new spoke
            pvpgcCtl = chk(pvpgcCtl)

        elif (pvpgcCtl == 2):
            logg('call pvpgc_2')
            pvpgc_2()
            logg('after call pvpgc_2')
            # test and adjust for new spoke
            pvpgcCtl = chk(pvpgcCtl)

        elif (pvpgcCtl == 3):
            logg('call pvpgc_3')
            pvpgc_3()
            logg('after call pvpgc_3')
            # test and adjust for new spoke
            pvpgcCtl = chk(pvpgcCtl)

        elif (pvpgcCtl == 4):
            logg('call pvpgc_4')
            pvpgc_4()
            logg('after call pvpgc_4')
            # test and adjust for new spoke
            pvpgcCtl = chk(pvpgcCtl)

        elif (pvpgcCtl == 5):
            logg('call pvpgc_5')
            pvpgc_5()
            logg('after call pvpgc_5')
            # test and adjust for new spoke
            pvpgcCtl = chk(pvpgcCtl)

        elif (pvpgcCtl == 6):
            logg('call pvpgc_6')
            pvpgc_6()
            logg('after call pvpgc_6')
            # test and adjust for new spoke
            pvpgcCtl = chk(pvpgcCtl)

        elif (pvpgcCtl == 7):
            logg('call pvpgc_7')
            pvpgc_7()
            logg('after call pvpgc_7')
            # test and adjust for new spoke
            pvpgcCtl = chk(pvpgcCtl)

        elif (pvpgcCtl == 8):
            logg('call pvpgc_8')
            pvpgc_8()
            logg('after call pvpgc_8')
            # test and adjust for new spoke
            pvpgcCtl = chk(pvpgcCtl)

        elif (pvpgcCtl == 9):
            logg('call pvpgc_9')
            pvpgc_9()
            logg('after call pvpgc_9')
            # test and adjust for new spoke
            pvpgcCtl = chk(pvpgcCtl)

        else:
            #final
            logg('final pvpgc')    
            pvpgcCtl = 0 # break
        #endif
    #wend
#end pvpgc

def pgcv3_1():
    global p
    logg('pgcv3_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgcv3-1 processing text ')
    logg("""pgcv3""")
    if (r == p['OK']):
        logg('push text ' + """pgcv3""")
        datPush("pgcv3")
        logg('after ' + """pgcv3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv3-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv3-1 processing verb ( ln@ ) ')
    if (r == p['OK']):
        logg('call ln@ ')
        p['sy']['ln@'](p)
        logg('after ln@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv3-1 processing verb ( lr@ ) ')
    if (r == p['OK']):
        logg('call lr@ ')
        p['sy']['lr@'](p)
        logg('after lr@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv3-1 processing verb ( drop ) ')
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
    logg('for pgcv3-1 processing text ')
    logg("""5""")
    if (r == p['OK']):
        logg('push text ' + """5""")
        datPush("5")
        logg('after ' + """5""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv3-1 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv3-1 processing verb ( ! ) ')
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
    logg('final pgcv3_1')
#end pgcv3_1

def pgcv3 (x):
    global p
    logg('begin pgcv3')
    ## point of umbrella
    pgcv3Ctl = 1 # starting spoke
    while pgcv3Ctl != 0:
        logg('loop pgcv3Ctl = ' + pgcv3Ctl.__str__())
        if (pgcv3Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgcv3Ctl == 1):
            logg('call pgcv3_1')
            pgcv3_1()
            logg('after call pgcv3_1')
            # test and adjust for new spoke
            pgcv3Ctl = chk(pgcv3Ctl)

        else:
            #final
            logg('final pgcv3')    
            pgcv3Ctl = 0 # break
        #endif
    #wend
#end pgcv3

def voknok_1():
    global p
    logg('voknok_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for voknok-1 processing text ')
    logg("""voknok""")
    if (r == p['OK']):
        logg('push text ' + """voknok""")
        datPush("voknok")
        logg('after ' + """voknok""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for voknok-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for voknok-1 processing text ')
    logg("""vx""")
    if (r == p['OK']):
        logg('push text ' + """vx""")
        datPush("vx")
        logg('after ' + """vx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for voknok-1 processing verb ( @ ) ')
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
    logg('for voknok-1 processing verb ( protected ) ')
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
    logg('for voknok-1 processing text ')
    logg("""pOK""")
    if (r == p['OK']):
        logg('push text ' + """pOK""")
        datPush("pOK")
        logg('after ' + """pOK""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for voknok-1 processing verb ( = ) ')
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
    logg('for voknok-1 processing text ')
    logg("""3""")
    if (r == p['OK']):
        logg('push text ' + """3""")
        datPush("3")
        logg('after ' + """3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for voknok-1 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for voknok-1 processing verb ( ! ) ')
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
    logg('final voknok_1')
#end voknok_1

def voknok_2():
    global p
    logg('voknok_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for voknok-2 processing verb ( drop ) ')
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
    logg('for voknok-2 processing verb ( pgcv2 ) ')
    if (r == p['OK']):
        logg('call pgcv2 ')
        p['sy']['pgcv2'](p)
        logg('after pgcv2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final voknok_2')
#end voknok_2

def voknok (x):
    global p
    logg('begin voknok')
    ## point of umbrella
    voknokCtl = 1 # starting spoke
    while voknokCtl != 0:
        logg('loop voknokCtl = ' + voknokCtl.__str__())
        if (voknokCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (voknokCtl == 1):
            logg('call voknok_1')
            voknok_1()
            logg('after call voknok_1')
            # test and adjust for new spoke
            voknokCtl = chk(voknokCtl)

        elif (voknokCtl == 2):
            logg('call voknok_2')
            voknok_2()
            logg('after call voknok_2')
            # test and adjust for new spoke
            voknokCtl = chk(voknokCtl)

        else:
            #final
            logg('final voknok')    
            voknokCtl = 0 # break
        #endif
    #wend
#end voknok

def pgcv2_1():
    global p
    logg('pgcv2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgcv2-1 processing text ')
    logg("""pgcv2""")
    if (r == p['OK']):
        logg('push text ' + """pgcv2""")
        datPush("pgcv2")
        logg('after ' + """pgcv2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv2-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv2-1 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv2-1 processing verb ( P? ) ')
    if (r == p['OK']):
        logg('call P? ')
        p['sy']['P?'](p)
        logg('after P?')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv2-1 processing text ')
    logg("""2""")
    if (r == p['OK']):
        logg('push text ' + """2""")
        datPush("2")
        logg('after ' + """2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv2-1 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv2-1 processing verb ( ! ) ')
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
    logg('final pgcv2_1')
#end pgcv2_1

def pgcv2_2():
    global p
    logg('pgcv2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgcv2-2 processing text ')
    logg(""" - skipped """)
    if (r == p['OK']):
        logg('push text ' + """ - skipped """)
        datPush(" - skipped ")
        logg('after ' + """ - skipped """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv2-2 processing verb ( cat ) ')
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
    logg('for pgcv2-2 processing verb ( pplog ) ')
    if (r == p['OK']):
        logg('call pplog ')
        p['sy']['pplog'](p)
        logg('after pplog')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgcv2-2 processing verb ( drop ) ')
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
    logg('for pgcv2-2 processing verb ( tail. ) ')
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
    logg('final pgcv2_2')
#end pgcv2_2

def pgcv2 (x):
    global p
    logg('begin pgcv2')
    ## point of umbrella
    pgcv2Ctl = 1 # starting spoke
    while pgcv2Ctl != 0:
        logg('loop pgcv2Ctl = ' + pgcv2Ctl.__str__())
        if (pgcv2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgcv2Ctl == 1):
            logg('call pgcv2_1')
            pgcv2_1()
            logg('after call pgcv2_1')
            # test and adjust for new spoke
            pgcv2Ctl = chk(pgcv2Ctl)

        elif (pgcv2Ctl == 2):
            logg('call pgcv2_2')
            pgcv2_2()
            logg('after call pgcv2_2')
            # test and adjust for new spoke
            pgcv2Ctl = chk(pgcv2Ctl)

        else:
            #final
            logg('final pgcv2')    
            pgcv2Ctl = 0 # break
        #endif
    #wend
#end pgcv2

def lr8_1():
    global p
    logg('lr8_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for lr8-1 processing text ')
    logg("""lr8""")
    if (r == p['OK']):
        logg('push text ' + """lr8""")
        datPush("lr8")
        logg('after ' + """lr8""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-1 processing verb ( lr# ) ')
    if (r == p['OK']):
        logg('call lr# ')
        p['sy']['lr#'](p)
        logg('after lr#')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-1 processing text ')
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
    logg('for lr8-1 processing verb ( = ) ')
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
    logg('for lr8-1 processing verb ( lnz ) ')
    if (r == p['OK']):
        logg('call lnz ')
        p['sy']['lnz'](p)
        logg('after lnz')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-1 processing verb ( lrz ) ')
    if (r == p['OK']):
        logg('call lrz ')
        p['sy']['lrz'](p)
        logg('after lrz')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-1 processing text ')
    logg("""OK""")
    if (r == p['OK']):
        logg('push text ' + """OK""")
        datPush("OK")
        logg('after ' + """OK""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-1 processing text ')
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
    logg('for lr8-1 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-1 processing verb ( ! ) ')
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
    logg('final lr8_1')
#end lr8_1

def lr8_2():
    global p
    logg('lr8_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for lr8-2 processing verb ( lr@ ) ')
    if (r == p['OK']):
        logg('call lr@ ')
        p['sy']['lr@'](p)
        logg('after lr@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-2 processing verb ( ln@ ) ')
    if (r == p['OK']):
        logg('call ln@ ')
        p['sy']['ln@'](p)
        logg('after ln@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-2 processing verb ( drop ) ')
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
    logg('for lr8-2 processing text ')
    logg("""3""")
    if (r == p['OK']):
        logg('push text ' + """3""")
        datPush("3")
        logg('after ' + """3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-2 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr8-2 processing verb ( ! ) ')
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
    logg('final lr8_2')
#end lr8_2

def lr8 (x):
    global p
    logg('begin lr8')
    ## point of umbrella
    lr8Ctl = 1 # starting spoke
    while lr8Ctl != 0:
        logg('loop lr8Ctl = ' + lr8Ctl.__str__())
        if (lr8Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (lr8Ctl == 1):
            logg('call lr8_1')
            lr8_1()
            logg('after call lr8_1')
            # test and adjust for new spoke
            lr8Ctl = chk(lr8Ctl)

        elif (lr8Ctl == 2):
            logg('call lr8_2')
            lr8_2()
            logg('after call lr8_2')
            # test and adjust for new spoke
            lr8Ctl = chk(lr8Ctl)

        else:
            #final
            logg('final lr8')    
            lr8Ctl = 0 # break
        #endif
    #wend
#end lr8

def lr4_1():
    global p
    logg('lr4_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for lr4-1 processing text ')
    logg("""lr4""")
    if (r == p['OK']):
        logg('push text ' + """lr4""")
        datPush("lr4")
        logg('after ' + """lr4""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-1 processing verb ( lr# ) ')
    if (r == p['OK']):
        logg('call lr# ')
        p['sy']['lr#'](p)
        logg('after lr#')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-1 processing text ')
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
    logg('for lr4-1 processing verb ( = ) ')
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
    logg('for lr4-1 processing verb ( lnz ) ')
    if (r == p['OK']):
        logg('call lnz ')
        p['sy']['lnz'](p)
        logg('after lnz')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-1 processing verb ( lrz ) ')
    if (r == p['OK']):
        logg('call lrz ')
        p['sy']['lrz'](p)
        logg('after lrz')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-1 processing text ')
    logg("""NOK""")
    if (r == p['OK']):
        logg('push text ' + """NOK""")
        datPush("NOK")
        logg('after ' + """NOK""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-1 processing text ')
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
    logg('for lr4-1 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-1 processing verb ( ! ) ')
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
    logg('final lr4_1')
#end lr4_1

def lr4_2():
    global p
    logg('lr4_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for lr4-2 processing verb ( lr@ ) ')
    if (r == p['OK']):
        logg('call lr@ ')
        p['sy']['lr@'](p)
        logg('after lr@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-2 processing verb ( ln@ ) ')
    if (r == p['OK']):
        logg('call ln@ ')
        p['sy']['ln@'](p)
        logg('after ln@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-2 processing text ')
    logg("""6""")
    if (r == p['OK']):
        logg('push text ' + """6""")
        datPush("6")
        logg('after ' + """6""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-2 processing text ')
    logg("""pctl""")
    if (r == p['OK']):
        logg('push text ' + """pctl""")
        datPush("pctl")
        logg('after ' + """pctl""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for lr4-2 processing verb ( ! ) ')
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
    logg('final lr4_2')
#end lr4_2

def lr4 (x):
    global p
    logg('begin lr4')
    ## point of umbrella
    lr4Ctl = 1 # starting spoke
    while lr4Ctl != 0:
        logg('loop lr4Ctl = ' + lr4Ctl.__str__())
        if (lr4Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (lr4Ctl == 1):
            logg('call lr4_1')
            lr4_1()
            logg('after call lr4_1')
            # test and adjust for new spoke
            lr4Ctl = chk(lr4Ctl)

        elif (lr4Ctl == 2):
            logg('call lr4_2')
            lr4_2()
            logg('after call lr4_2')
            # test and adjust for new spoke
            lr4Ctl = chk(lr4Ctl)

        else:
            #final
            logg('final lr4')    
            lr4Ctl = 0 # break
        #endif
    #wend
#end lr4

def bmain_1():
    global p
    logg('bmain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for bmain-1 processing text ')
    logg("""off""")
    if (r == p['OK']):
        logg('push text ' + """off""")
        datPush("off")
        logg('after ' + """off""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing text ')
    logg("""zlogging""")
    if (r == p['OK']):
        logg('push text ' + """zlogging""")
        datPush("zlogging")
        logg('after ' + """zlogging""" )
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
    logg('for bmain-1 processing verb ( Ver ) ')
    if (r == p['OK']):
        logg('call Ver ')
        p['sy']['Ver'](p)
        logg('after Ver')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain-1 processing verb ( bmain2 ) ')
    if (r == p['OK']):
        logg('call bmain2 ')
        p['sy']['bmain2'](p)
        logg('after bmain2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final bmain_1')
#end bmain_1

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

        else:
            #final
            logg('final bmain')    
            bmainCtl = 0 # break
        #endif
    #wend
#end bmain

def bmain2_1():
    global p
    logg('bmain2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for bmain2-1 processing text ')
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
    logg('for bmain2-1 processing verb ( ask ) ')
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
    logg('for bmain2-1 processing verb ( dup ) ')
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
    logg('for bmain2-1 processing text ')
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
    logg('for bmain2-1 processing verb ( ! ) ')
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
    logg('for bmain2-1 processing verb ( loggingTest ) ')
    if (r == p['OK']):
        logg('call loggingTest ')
        p['sy']['loggingTest'](p)
        logg('after loggingTest')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain2-1 processing verb ( ==quit ) ')
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
    logg('for bmain2-1 processing text ')
    logg("""pbox done""")
    if (r == p['OK']):
        logg('push text ' + """pbox done""")
        datPush("pbox done")
        logg('after ' + """pbox done""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for bmain2-1 processing verb ( msg ) ')
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
    logg('final bmain2_1')
#end bmain2_1

def bmain2_2():
    global p
    logg('bmain2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for bmain2-2 processing verb ( b2 ) ')
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
    logg('for bmain2-2 processing verb ( tail. ) ')
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
    logg('final bmain2_2')
#end bmain2_2

def bmain2 (x):
    global p
    logg('begin bmain2')
    ## point of umbrella
    bmain2Ctl = 1 # starting spoke
    while bmain2Ctl != 0:
        logg('loop bmain2Ctl = ' + bmain2Ctl.__str__())
        if (bmain2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (bmain2Ctl == 1):
            logg('call bmain2_1')
            bmain2_1()
            logg('after call bmain2_1')
            # test and adjust for new spoke
            bmain2Ctl = chk(bmain2Ctl)

        elif (bmain2Ctl == 2):
            logg('call bmain2_2')
            bmain2_2()
            logg('after call bmain2_2')
            # test and adjust for new spoke
            bmain2Ctl = chk(bmain2Ctl)

        else:
            #final
            logg('final bmain2')    
            bmain2Ctl = 0 # break
        #endif
    #wend
#end bmain2

def Ver_1():
    global p
    logg('Ver_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Ver-1 processing text ')
    logg("""bbox version 8-18-2020 type help for more""")
    if (r == p['OK']):
        logg('push text ' + """bbox version 8-18-2020 type help for more""")
        datPush("bbox version 8-18-2020 type help for more")
        logg('after ' + """bbox version 8-18-2020 type help for more""" )
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

def loggingTest_1():
    global p
    logg('loggingTest_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for loggingTest-1 processing text ')
    logg("""zlogging""")
    if (r == p['OK']):
        logg('push text ' + """zlogging""")
        datPush("zlogging")
        logg('after ' + """zlogging""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loggingTest-1 processing verb ( @ ) ')
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
    logg('for loggingTest-1 processing text ')
    logg("""on""")
    if (r == p['OK']):
        logg('push text ' + """on""")
        datPush("on")
        logg('after ' + """on""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loggingTest-1 processing verb ( = ) ')
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
    logg('for loggingTest-1 processing text ')
    logg("""zlog""")
    if (r == p['OK']):
        logg('push text ' + """zlog""")
        datPush("zlog")
        logg('after ' + """zlog""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loggingTest-1 processing verb ( @ ) ')
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
    logg('for loggingTest-1 processing text ')
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
    logg('for loggingTest-1 processing verb ( @ ) ')
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
    logg('for loggingTest-1 processing verb ( cats ) ')
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
    logg('for loggingTest-1 processing text ')
    logg("""zlog""")
    if (r == p['OK']):
        logg('push text ' + """zlog""")
        datPush("zlog")
        logg('after ' + """zlog""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loggingTest-1 processing verb ( ! ) ')
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
    logg('final loggingTest_1')
#end loggingTest_1

def loggingTest_2():
    global p
    logg('loggingTest_2')
    datPush(p['OK'])

    #final
    logg('final loggingTest_2')
#end loggingTest_2

def loggingTest (x):
    global p
    logg('begin loggingTest')
    ## point of umbrella
    loggingTestCtl = 1 # starting spoke
    while loggingTestCtl != 0:
        logg('loop loggingTestCtl = ' + loggingTestCtl.__str__())
        if (loggingTestCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (loggingTestCtl == 1):
            logg('call loggingTest_1')
            loggingTest_1()
            logg('after call loggingTest_1')
            # test and adjust for new spoke
            loggingTestCtl = chk(loggingTestCtl)

        elif (loggingTestCtl == 2):
            logg('call loggingTest_2')
            loggingTest_2()
            logg('after call loggingTest_2')
            # test and adjust for new spoke
            loggingTestCtl = chk(loggingTestCtl)

        else:
            #final
            logg('final loggingTest')    
            loggingTestCtl = 0 # break
        #endif
    #wend
#end loggingTest

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
    logg('for b2-8 processing text ')
    logg("""help""")
    if (r == p['OK']):
        logg('push text ' + """help""")
        datPush("help")
        logg('after ' + """help""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for b2-8 processing verb ( = ) ')
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
    logg('for b2-8 processing verb ( dohelp ) ')
    if (r == p['OK']):
        logg('call dohelp ')
        p['sy']['dohelp'](p)
        logg('after dohelp')
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
    logg('for b2-9 processing verb ( @ ) ')
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
    logg('for b2-9 processing verb ( .X ) ')
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
    logg('final b2_9')
#end b2_9

def b2_10():
    global p
    logg('b2_10')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for b2-10 processing text ')
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
    logg('for b2-10 processing verb ( msg ) ')
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
    logg('final b2_10')
#end b2_10

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

        elif (b2Ctl == 10):
            logg('call b2_10')
            b2_10()
            logg('after call b2_10')
            # test and adjust for new spoke
            b2Ctl = chk(b2Ctl)

        else:
            #final
            logg('final b2')    
            b2Ctl = 0 # break
        #endif
    #wend
#end b2

def dohelp_1():
    global p
    logg('dohelp_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for dohelp-1 processing text ')
    logg("""help:""")
    if (r == p['OK']):
        logg('push text ' + """help:""")
        datPush("help:")
        logg('after ' + """help:""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""commands are:""")
    if (r == p['OK']):
        logg('push text ' + """commands are:""")
        datPush("commands are:")
        logg('after ' + """commands are:""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""push , pop , help(this message)""")
    if (r == p['OK']):
        logg('push text ' + """push , pop , help(this message)""")
        datPush("push , pop , help(this message)")
        logg('after ' + """push , pop , help(this message)""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""{{ multi-line any text till }} on its own line""")
    if (r == p['OK']):
        logg('push text ' + """{{ multi-line any text till }} on its own line""")
        datPush("{{ multi-line any text till }} on its own line")
        logg('after ' + """{{ multi-line any text till }} on its own line""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""any verb (use -verbs- command to see list)""")
    if (r == p['OK']):
        logg('push text ' + """any verb (use -verbs- command to see list)""")
        datPush("any verb (use -verbs- command to see list)")
        logg('after ' + """any verb (use -verbs- command to see list)""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""any number with or without quotes""")
    if (r == p['OK']):
        logg('push text ' + """any number with or without quotes""")
        datPush("any number with or without quotes")
        logg('after ' + """any number with or without quotes""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""a blank line""")
    if (r == p['OK']):
        logg('push text ' + """a blank line""")
        datPush("a blank line")
        logg('after ' + """a blank line""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
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
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""any quoted string that contains a verb name can be used with the -help?- command for more information""")
    if (r == p['OK']):
        logg('push text ' + """any quoted string that contains a verb name can be used with the -help?- command for more information""")
        datPush("any quoted string that contains a verb name can be used with the -help?- command for more information")
        logg('after ' + """any quoted string that contains a verb name can be used with the -help?- command for more information""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
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
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""programming:""")
    if (r == p['OK']):
        logg('push text ' + """programming:""")
        datPush("programming:")
        logg('after ' + """programming:""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""to load code (basiiCode,name,,) l!""")
    if (r == p['OK']):
        logg('push text ' + """to load code (basiiCode,name,,) l!""")
        datPush("to load code (basiiCode,name,,) l!")
        logg('after ' + """to load code (basiiCode,name,,) l!""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg(""" to execute (name,,) pgf""")
    if (r == p['OK']):
        logg('push text ' + """ to execute (name,,) pgf""")
        datPush(" to execute (name,,) pgf")
        logg('after ' + """ to execute (name,,) pgf""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
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
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('for dohelp-1 processing text ')
    logg("""end help""")
    if (r == p['OK']):
        logg('push text ' + """end help""")
        datPush("end help")
        logg('after ' + """end help""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dohelp-1 processing verb ( msg ) ')
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
    logg('final dohelp_1')
#end dohelp_1

def dohelp (x):
    global p
    logg('begin dohelp')
    ## point of umbrella
    dohelpCtl = 1 # starting spoke
    while dohelpCtl != 0:
        logg('loop dohelpCtl = ' + dohelpCtl.__str__())
        if (dohelpCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (dohelpCtl == 1):
            logg('call dohelp_1')
            dohelp_1()
            logg('after call dohelp_1')
            # test and adjust for new spoke
            dohelpCtl = chk(dohelpCtl)

        else:
            #final
            logg('final dohelp')    
            dohelpCtl = 0 # break
        #endif
    #wend
#end dohelp

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

def pgword_1():
    global p
    logg('pgword_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgword-1 processing text ')
    logg("""pgword""")
    if (r == p['OK']):
        logg('push text ' + """pgword""")
        datPush("pgword")
        logg('after ' + """pgword""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-1 processing verb ( pplogd ) ')
    if (r == p['OK']):
        logg('call pplogd ')
        p['sy']['pplogd'](p)
        logg('after pplogd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-1 processing text ')
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
    logg('for pgword-1 processing verb ( h^ ) ')
    if (r == p['OK']):
        logg('call h^ ')
        p['sy']['h^'](p)
        logg('after h^')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-1 processing verb ( lr@ ) ')
    if (r == p['OK']):
        logg('call lr@ ')
        p['sy']['lr@'](p)
        logg('after lr@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-1 processing verb ( trim ) ')
    if (r == p['OK']):
        logg('call trim ')
        p['sy']['trim'](p)
        logg('after trim')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-1 processing verb ( word ) ')
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
    logg('for pgword-1 processing verb ( trim ) ')
    if (r == p['OK']):
        logg('call trim ')
        p['sy']['trim'](p)
        logg('after trim')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-1 processing verb ( swap ) ')
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
    logg('for pgword-1 processing verb ( lr! ) ')
    if (r == p['OK']):
        logg('call lr! ')
        p['sy']['lr!'](p)
        logg('after lr!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-1 processing text ')
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
    logg('for pgword-1 processing verb ( h! ) ')
    if (r == p['OK']):
        logg('call h! ')
        p['sy']['h!'](p)
        logg('after h!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-1 processing verb ( ... ) ')
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
    logg('final pgword_1')
#end pgword_1

def pgword_2():
    global p
    logg('pgword_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgword-2 processing text ')
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
    logg('for pgword-2 processing verb ( h@ ) ')
    if (r == p['OK']):
        logg('call h@ ')
        p['sy']['h@'](p)
        logg('after h@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-2 processing text ')
    logg("""//-""")
    if (r == p['OK']):
        logg('push text ' + """//-""")
        datPush("//-")
        logg('after ' + """//-""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-2 processing verb ( = ) ')
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
    logg('for pgword-2 processing verb ( pgDoComment ) ')
    if (r == p['OK']):
        logg('call pgDoComment ')
        p['sy']['pgDoComment'](p)
        logg('after pgDoComment')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-2 processing verb ( hx ) ')
    if (r == p['OK']):
        logg('call hx ')
        p['sy']['hx'](p)
        logg('after hx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-2 processing verb ( tail. ) ')
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
    logg('final pgword_2')
#end pgword_2

def pgword_3():
    global p
    logg('pgword_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgword-3 processing text ')
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
    logg('for pgword-3 processing verb ( h@ ) ')
    if (r == p['OK']):
        logg('call h@ ')
        p['sy']['h@'](p)
        logg('after h@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-3 processing verb ( pplog ) ')
    if (r == p['OK']):
        logg('call pplog ')
        p['sy']['pplog'](p)
        logg('after pplog')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgword-3 processing verb ( hx ) ')
    if (r == p['OK']):
        logg('call hx ')
        p['sy']['hx'](p)
        logg('after hx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final pgword_3')
#end pgword_3

def pgword (x):
    global p
    logg('begin pgword')
    ## point of umbrella
    pgwordCtl = 1 # starting spoke
    while pgwordCtl != 0:
        logg('loop pgwordCtl = ' + pgwordCtl.__str__())
        if (pgwordCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgwordCtl == 1):
            logg('call pgword_1')
            pgword_1()
            logg('after call pgword_1')
            # test and adjust for new spoke
            pgwordCtl = chk(pgwordCtl)

        elif (pgwordCtl == 2):
            logg('call pgword_2')
            pgword_2()
            logg('after call pgword_2')
            # test and adjust for new spoke
            pgwordCtl = chk(pgwordCtl)

        elif (pgwordCtl == 3):
            logg('call pgword_3')
            pgword_3()
            logg('after call pgword_3')
            # test and adjust for new spoke
            pgwordCtl = chk(pgwordCtl)

        else:
            #final
            logg('final pgword')    
            pgwordCtl = 0 # break
        #endif
    #wend
#end pgword

def pgDoComment_1():
    global p
    logg('pgDoComment_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgDoComment-1 processing verb ( pgword ) ')
    if (r == p['OK']):
        logg('call pgword ')
        p['sy']['pgword'](p)
        logg('after pgword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgDoComment-1 processing verb ( dup ) ')
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
    logg('for pgDoComment-1 processing text ')
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
    logg('for pgDoComment-1 processing verb ( h! ) ')
    if (r == p['OK']):
        logg('call h! ')
        p['sy']['h!'](p)
        logg('after h!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgDoComment-1 processing text ')
    logg("""-//""")
    if (r == p['OK']):
        logg('push text ' + """-//""")
        datPush("-//")
        logg('after ' + """-//""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgDoComment-1 processing verb ( = ) ')
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
    logg('final pgDoComment_1')
#end pgDoComment_1

def pgDoComment_2():
    global p
    logg('pgDoComment_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgDoComment-2 processing verb ( tail. ) ')
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
    logg('final pgDoComment_2')
#end pgDoComment_2

def pgDoComment (x):
    global p
    logg('begin pgDoComment')
    ## point of umbrella
    pgDoCommentCtl = 1 # starting spoke
    while pgDoCommentCtl != 0:
        logg('loop pgDoCommentCtl = ' + pgDoCommentCtl.__str__())
        if (pgDoCommentCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgDoCommentCtl == 1):
            logg('call pgDoComment_1')
            pgDoComment_1()
            logg('after call pgDoComment_1')
            # test and adjust for new spoke
            pgDoCommentCtl = chk(pgDoCommentCtl)

        elif (pgDoCommentCtl == 2):
            logg('call pgDoComment_2')
            pgDoComment_2()
            logg('after call pgDoComment_2')
            # test and adjust for new spoke
            pgDoCommentCtl = chk(pgDoCommentCtl)

        else:
            #final
            logg('final pgDoComment')    
            pgDoCommentCtl = 0 # break
        #endif
    #wend
#end pgDoComment

def pplog_1():
    global p
    logg('pplog_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pplog-1 processing verb ( dup ) ')
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
    logg('for pplog-1 processing text ')
    logg("""ptrace""")
    if (r == p['OK']):
        logg('push text ' + """ptrace""")
        datPush("ptrace")
        logg('after ' + """ptrace""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pplog-1 processing verb ( @ ) ')
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
    logg('for pplog-1 processing text ')
    logg("""on""")
    if (r == p['OK']):
        logg('push text ' + """on""")
        datPush("on")
        logg('after ' + """on""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pplog-1 processing verb ( = ) ')
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
    logg('for pplog-1 processing text ')
    logg("""-log""")
    if (r == p['OK']):
        logg('push text ' + """-log""")
        datPush("-log")
        logg('after ' + """-log""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pplog-1 processing verb ( cat ) ')
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
    logg('for pplog-1 processing verb ( msg ) ')
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
    logg('final pplog_1')
#end pplog_1

def pplog_2():
    global p
    logg('pplog_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pplog-2 processing verb ( dup ) ')
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
    logg('for pplog-2 processing text ')
    logg("""ptrace""")
    if (r == p['OK']):
        logg('push text ' + """ptrace""")
        datPush("ptrace")
        logg('after ' + """ptrace""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pplog-2 processing verb ( @ ) ')
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
    logg('for pplog-2 processing text ')
    logg("""step""")
    if (r == p['OK']):
        logg('push text ' + """step""")
        datPush("step")
        logg('after ' + """step""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pplog-2 processing verb ( = ) ')
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
    logg('for pplog-2 processing text ')
    logg("""-log""")
    if (r == p['OK']):
        logg('push text ' + """-log""")
        datPush("-log")
        logg('after ' + """-log""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pplog-2 processing verb ( cat ) ')
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
    logg('for pplog-2 processing verb ( ask ) ')
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
    logg('for pplog-2 processing verb ( drop ) ')
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
    logg('final pplog_2')
#end pplog_2

def pplog_2():
    global p
    logg('pplog_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pplog-2 processing verb ( drop ) ')
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
    logg('final pplog_2')
#end pplog_2

def pplog (x):
    global p
    logg('begin pplog')
    ## point of umbrella
    pplogCtl = 1 # starting spoke
    while pplogCtl != 0:
        logg('loop pplogCtl = ' + pplogCtl.__str__())
        if (pplogCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pplogCtl == 1):
            logg('call pplog_1')
            pplog_1()
            logg('after call pplog_1')
            # test and adjust for new spoke
            pplogCtl = chk(pplogCtl)

        elif (pplogCtl == 2):
            logg('call pplog_2')
            pplog_2()
            logg('after call pplog_2')
            # test and adjust for new spoke
            pplogCtl = chk(pplogCtl)

        elif (pplogCtl == 3):
            logg('call pplog_2')
            pplog_2()
            logg('after call pplog_2')
            # test and adjust for new spoke
            pplogCtl = chk(pplogCtl)

        else:
            #final
            logg('final pplog')    
            pplogCtl = 0 # break
        #endif
    #wend
#end pplog

def pplogd_1():
    global p
    logg('pplogd_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pplogd-1 processing verb ( pplog ) ')
    if (r == p['OK']):
        logg('call pplog ')
        p['sy']['pplog'](p)
        logg('after pplog')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pplogd-1 processing verb ( drop ) ')
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
    logg('final pplogd_1')
#end pplogd_1

def pplogd (x):
    global p
    logg('begin pplogd')
    ## point of umbrella
    pplogdCtl = 1 # starting spoke
    while pplogdCtl != 0:
        logg('loop pplogdCtl = ' + pplogdCtl.__str__())
        if (pplogdCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pplogdCtl == 1):
            logg('call pplogd_1')
            pplogd_1()
            logg('after call pplogd_1')
            # test and adjust for new spoke
            pplogdCtl = chk(pplogdCtl)

        else:
            #final
            logg('final pplogd')    
            pplogdCtl = 0 # break
        #endif
    #wend
#end pplogd

# stream routines 

def EQzblzquit(p):
    logg ('==quit')
    needle = 'quit'
    needle = needle.upper()
    return(eqeq(needle))
#end EQzblzquit

def EQzblz0(p):
    logg ('==0')
    needle = '0'
    needle = needle.upper()
    return(eqeq(needle))
#end EQzblz0

def EQzblzpush(p):
    logg ('==push')
    needle = 'push'
    needle = needle.upper()
    return(eqeq(needle))
#end EQzblzpush

def EQzblzpop(p):
    logg ('==pop')
    needle = 'pop'
    needle = needle.upper()
    return(eqeq(needle))
#end EQzblzpop

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

    # paragraph pgfinit
    p['sy']['pgfinit'] = pgfinit
    #

    # paragraph pgf
    p['sy']['pgf'] = pgf
    #

    # paragraph pgc
    p['sy']['pgc'] = pgc
    #

    # paragraph ppgc
    p['sy']['ppgc'] = ppgc
    #

    # paragraph pgdef
    p['sy']['pgdef'] = pgdef
    #

    # paragraph cpgc
    p['sy']['cpgc'] = cpgc
    #

    # paragraph pvpgc
    p['sy']['pvpgc'] = pvpgc
    #

    # paragraph pgcv3
    p['sy']['pgcv3'] = pgcv3
    #

    # paragraph voknok
    p['sy']['voknok'] = voknok
    #

    # paragraph pgcv2
    p['sy']['pgcv2'] = pgcv2
    #

    # paragraph lr8
    p['sy']['lr8'] = lr8
    #

    # paragraph lr4
    p['sy']['lr4'] = lr4
    #

    # paragraph bmain
    p['sy']['bmain'] = bmain
    #

    # paragraph bmain2
    p['sy']['bmain2'] = bmain2
    #

    # paragraph ==quit
    p['sy']['==quit'] = EQzblzquit
    #

    # paragraph Ver
    p['sy']['Ver'] = Ver
    #

    # paragraph loggingTest
    p['sy']['loggingTest'] = loggingTest
    #

    # paragraph b2
    p['sy']['b2'] = b2
    #

    # paragraph ==0
    p['sy']['==0'] = EQzblz0
    #

    # paragraph ==push
    p['sy']['==push'] = EQzblzpush
    #

    # paragraph ==pop
    p['sy']['==pop'] = EQzblzpop
    #

    # paragraph dohelp
    p['sy']['dohelp'] = dohelp
    #

    # paragraph bcollect
    p['sy']['bcollect'] = bcollect
    #

    # paragraph pgword
    p['sy']['pgword'] = pgword
    #

    # paragraph pgDoComment
    p['sy']['pgDoComment'] = pgDoComment
    #

    # paragraph pplog
    p['sy']['pplog'] = pplog
    #

    # paragraph pplogd
    p['sy']['pplogd'] = pplogd
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
    if (p['v']['trace'] == 'step'):
        nop = raw_input(strin)  
    #endif
    if (p['v']['trace'] == 'on'):
        print("log-"+strin+"-log")  
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

