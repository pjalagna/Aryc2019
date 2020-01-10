
#file goldfish01.py
#generated for goldfish01.basii at Thu Jan  9 22:12:07 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def initGF_1():
    global p
    logg('initGF_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for initGF-1 processing text ')
    logg("""GF.db""")
    if (r == p['OK']):
        logg('push text ' + """GF.db""")
        datPush("GF.db")
        logg('after ' + """GF.db""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initGF-1 processing text ')
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
    logg('for initGF-1 processing verb ( takeV ) ')
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

    #final
    logg('final initGF_1')
#end initGF_1

def initGF (x):
    global p
    logg('begin initGF')
    ## point of umbrella
    initGFCtl = 1 # starting spoke
    while initGFCtl != 0:
        logg('loop initGFCtl = ' + initGFCtl.__str__())
        if (initGFCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (initGFCtl == 1):
            logg('call initGF_1')
            initGF_1()
            logg('after call initGF_1')
            # test and adjust for new spoke
            initGFCtl = chk(initGFCtl)

        else:
            #final
            logg('final initGF')    
            initGFCtl = 0 # break
        #endif
    #wend
#end initGF

def admin_1():
    global p
    logg('admin_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for admin-1 processing verb ( initGF ) ')
    if (r == p['OK']):
        logg('call initGF ')
        p['sy']['initGF'](p)
        logg('after initGF')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-1 processing text ')
    logg(""" this action will destroy all data (continue) or (exit) """)
    if (r == p['OK']):
        logg('push text ' + """ this action will destroy all data (continue) or (exit) """)
        datPush(" this action will destroy all data (continue) or (exit) ")
        logg('after ' + """ this action will destroy all data (continue) or (exit) """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-1 processing verb ( ask ) ')
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
    logg('for admin-1 processing text ')
    logg("""adminans""")
    if (r == p['OK']):
        logg('push text ' + """adminans""")
        datPush("adminans")
        logg('after ' + """adminans""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-1 processing verb ( ! ) ')
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
    logg('for admin-1 processing verb ( ... ) ')
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
    logg('final admin_1')
#end admin_1

def admin_2():
    global p
    logg('admin_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for admin-2 processing text ')
    logg("""adminans""")
    if (r == p['OK']):
        logg('push text ' + """adminans""")
        datPush("adminans")
        logg('after ' + """adminans""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-2 processing verb ( @ ) ')
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
    logg('for admin-2 processing verb ( ==continue ) ')
    if (r == p['OK']):
        logg('call ==continue ')
        p['sy']['==continue'](p)
        logg('after ==continue')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-2 processing text ')
    logg("""drop table if exists 'GF' ;""")
    if (r == p['OK']):
        logg('push text ' + """drop table if exists 'GF' ;""")
        datPush("drop table if exists 'GF' ;")
        logg('after ' + """drop table if exists 'GF' ;""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-2 processing verb ( SQX ) ')
    if (r == p['OK']):
        logg('call SQX ')
        p['sy']['SQX'](p)
        logg('after SQX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-2 processing text ')
    logg("""create table GF ( ix , type, txt , primary key(ix) );""")
    if (r == p['OK']):
        logg('push text ' + """create table GF ( ix , type, txt , primary key(ix) );""")
        datPush("create table GF ( ix , type, txt , primary key(ix) );")
        logg('after ' + """create table GF ( ix , type, txt , primary key(ix) );""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-2 processing verb ( SQX ) ')
    if (r == p['OK']):
        logg('call SQX ')
        p['sy']['SQX'](p)
        logg('after SQX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-2 processing text ')
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
    logg('for admin-2 processing text ')
    logg("""conclusion""")
    if (r == p['OK']):
        logg('push text ' + """conclusion""")
        datPush("conclusion")
        logg('after ' + """conclusion""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-2 processing text ')
    logg("""is it a goldfish""")
    if (r == p['OK']):
        logg('push text ' + """is it a goldfish""")
        datPush("is it a goldfish")
        logg('after ' + """is it a goldfish""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-2 processing verb ( writeRec ) ')
    if (r == p['OK']):
        logg('call writeRec ')
        p['sy']['writeRec'](p)
        logg('after writeRec')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for admin-2 processing verb ( SQClose ) ')
    if (r == p['OK']):
        logg('call SQClose ')
        p['sy']['SQClose'](p)
        logg('after SQClose')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final admin_2')
#end admin_2

def admin_3():
    global p
    logg('admin_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for admin-3 processing verb ( exit ) ')
    if (r == p['OK']):
        logg('call exit ')
        p['sy']['exit'](p)
        logg('after exit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final admin_3')
#end admin_3

def admin (x):
    global p
    logg('begin admin')
    ## point of umbrella
    adminCtl = 1 # starting spoke
    while adminCtl != 0:
        logg('loop adminCtl = ' + adminCtl.__str__())
        if (adminCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (adminCtl == 1):
            logg('call admin_1')
            admin_1()
            logg('after call admin_1')
            # test and adjust for new spoke
            adminCtl = chk(adminCtl)

        elif (adminCtl == 2):
            logg('call admin_2')
            admin_2()
            logg('after call admin_2')
            # test and adjust for new spoke
            adminCtl = chk(adminCtl)

        elif (adminCtl == 3):
            logg('call admin_3')
            admin_3()
            logg('after call admin_3')
            # test and adjust for new spoke
            adminCtl = chk(adminCtl)

        else:
            #final
            logg('final admin')    
            adminCtl = 0 # break
        #endif
    #wend
#end admin

def GFcold_1():
    global p
    logg('GFcold_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GFcold-1 processing verb ( initGF ) ')
    if (r == p['OK']):
        logg('call initGF ')
        p['sy']['initGF'](p)
        logg('after initGF')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GFcold-1 processing text ')
    logg("""final statement""")
    if (r == p['OK']):
        logg('push text ' + """final statement""")
        datPush("final statement")
        logg('after ' + """final statement""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GFcold-1 processing verb ( ask ) ')
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
    logg('for GFcold-1 processing text ')
    logg("""finalS""")
    if (r == p['OK']):
        logg('push text ' + """finalS""")
        datPush("finalS")
        logg('after ' + """finalS""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GFcold-1 processing verb ( ! ) ')
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
    logg('for GFcold-1 processing text ')
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
    logg('for GFcold-1 processing text ')
    logg("""conclusion""")
    if (r == p['OK']):
        logg('push text ' + """conclusion""")
        datPush("conclusion")
        logg('after ' + """conclusion""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GFcold-1 processing text ')
    logg("""finalS""")
    if (r == p['OK']):
        logg('push text ' + """finalS""")
        datPush("finalS")
        logg('after ' + """finalS""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GFcold-1 processing verb ( @ ) ')
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
    logg('for GFcold-1 processing verb ( writeRec ) ')
    if (r == p['OK']):
        logg('call writeRec ')
        p['sy']['writeRec'](p)
        logg('after writeRec')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GFcold-1 processing verb ( SQClose ) ')
    if (r == p['OK']):
        logg('call SQClose ')
        p['sy']['SQClose'](p)
        logg('after SQClose')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GFcold_1')
#end GFcold_1

def GFcold (x):
    global p
    logg('begin GFcold')
    ## point of umbrella
    GFcoldCtl = 1 # starting spoke
    while GFcoldCtl != 0:
        logg('loop GFcoldCtl = ' + GFcoldCtl.__str__())
        if (GFcoldCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (GFcoldCtl == 1):
            logg('call GFcold_1')
            GFcold_1()
            logg('after call GFcold_1')
            # test and adjust for new spoke
            GFcoldCtl = chk(GFcoldCtl)

        else:
            #final
            logg('final GFcold')    
            GFcoldCtl = 0 # break
        #endif
    #wend
#end GFcold

def GFMain_1():
    global p
    logg('GFMain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GFMain-1 processing verb ( initGF ) ')
    if (r == p['OK']):
        logg('call initGF ')
        p['sy']['initGF'](p)
        logg('after initGF')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GFMain-1 processing text ')
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
    logg('for GFMain-1 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GFMain-1 processing verb ( ! ) ')
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
    logg('for GFMain-1 processing verb ( GF2 ) ')
    if (r == p['OK']):
        logg('call GF2 ')
        p['sy']['GF2'](p)
        logg('after GF2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GFMain-1 processing verb ( SQClose ) ')
    if (r == p['OK']):
        logg('call SQClose ')
        p['sy']['SQClose'](p)
        logg('after SQClose')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final GFMain_1')
#end GFMain_1

def GFMain (x):
    global p
    logg('begin GFMain')
    ## point of umbrella
    GFMainCtl = 1 # starting spoke
    while GFMainCtl != 0:
        logg('loop GFMainCtl = ' + GFMainCtl.__str__())
        if (GFMainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (GFMainCtl == 1):
            logg('call GFMain_1')
            GFMain_1()
            logg('after call GFMain_1')
            # test and adjust for new spoke
            GFMainCtl = chk(GFMainCtl)

        else:
            #final
            logg('final GFMain')    
            GFMainCtl = 0 # break
        #endif
    #wend
#end GFMain

def GF2_1():
    global p
    logg('GF2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GF2-1 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GF2-1 processing verb ( @ ) ')
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
    logg('for GF2-1 processing verb ( ==0 ) ')
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
    logg('final GF2_1')
#end GF2_1

def GF2_2():
    global p
    logg('GF2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for GF2-2 processing verb ( fanOnIType ) ')
    if (r == p['OK']):
        logg('call fanOnIType ')
        p['sy']['fanOnIType'](p)
        logg('after fanOnIType')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for GF2-2 processing verb ( tail. ) ')
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
    logg('final GF2_2')
#end GF2_2

def GF2 (x):
    global p
    logg('begin GF2')
    ## point of umbrella
    GF2Ctl = 1 # starting spoke
    while GF2Ctl != 0:
        logg('loop GF2Ctl = ' + GF2Ctl.__str__())
        if (GF2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (GF2Ctl == 1):
            logg('call GF2_1')
            GF2_1()
            logg('after call GF2_1')
            # test and adjust for new spoke
            GF2Ctl = chk(GF2Ctl)

        elif (GF2Ctl == 2):
            logg('call GF2_2')
            GF2_2()
            logg('after call GF2_2')
            # test and adjust for new spoke
            GF2Ctl = chk(GF2Ctl)

        else:
            #final
            logg('final GF2')    
            GF2Ctl = 0 # break
        #endif
    #wend
#end GF2

def fanOnIType_1():
    global p
    logg('fanOnIType_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fanOnIType-1 processing verb ( itype ) ')
    if (r == p['OK']):
        logg('call itype ')
        p['sy']['itype'](p)
        logg('after itype')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fanOnIType-1 processing verb ( ... ) ')
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
    logg('final fanOnIType_1')
#end fanOnIType_1

def fanOnIType_2():
    global p
    logg('fanOnIType_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fanOnIType-2 processing verb ( dup ) ')
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
    logg('for fanOnIType-2 processing verb ( ==question ) ')
    if (r == p['OK']):
        logg('call ==question ')
        p['sy']['==question'](p)
        logg('after ==question')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fanOnIType-2 processing verb ( drop ) ')
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
    logg('for fanOnIType-2 processing verb ( doQuestion ) ')
    if (r == p['OK']):
        logg('call doQuestion ')
        p['sy']['doQuestion'](p)
        logg('after doQuestion')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fanOnIType_2')
#end fanOnIType_2

def fanOnIType_3():
    global p
    logg('fanOnIType_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fanOnIType-3 processing verb ( dup ) ')
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
    logg('for fanOnIType-3 processing verb ( ==conclusion ) ')
    if (r == p['OK']):
        logg('call ==conclusion ')
        p['sy']['==conclusion'](p)
        logg('after ==conclusion')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fanOnIType-3 processing verb ( drop ) ')
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
    logg('for fanOnIType-3 processing verb ( doConclusion ) ')
    if (r == p['OK']):
        logg('call doConclusion ')
        p['sy']['doConclusion'](p)
        logg('after doConclusion')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fanOnIType_3')
#end fanOnIType_3

def fanOnIType_4():
    global p
    logg('fanOnIType_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fanOnIType-4 processing text ')
    logg(""" error on fanOnIType """)
    if (r == p['OK']):
        logg('push text ' + """ error on fanOnIType """)
        datPush(" error on fanOnIType ")
        logg('after ' + """ error on fanOnIType """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for fanOnIType-4 processing verb ( swap ) ')
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
    logg('for fanOnIType-4 processing verb ( cat ) ')
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
    logg('for fanOnIType-4 processing verb ( msg ) ')
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
    logg('for fanOnIType-4 processing verb ( exit ) ')
    if (r == p['OK']):
        logg('call exit ')
        p['sy']['exit'](p)
        logg('after exit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fanOnIType_4')
#end fanOnIType_4

def fanOnIType (x):
    global p
    logg('begin fanOnIType')
    ## point of umbrella
    fanOnITypeCtl = 1 # starting spoke
    while fanOnITypeCtl != 0:
        logg('loop fanOnITypeCtl = ' + fanOnITypeCtl.__str__())
        if (fanOnITypeCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (fanOnITypeCtl == 1):
            logg('call fanOnIType_1')
            fanOnIType_1()
            logg('after call fanOnIType_1')
            # test and adjust for new spoke
            fanOnITypeCtl = chk(fanOnITypeCtl)

        elif (fanOnITypeCtl == 2):
            logg('call fanOnIType_2')
            fanOnIType_2()
            logg('after call fanOnIType_2')
            # test and adjust for new spoke
            fanOnITypeCtl = chk(fanOnITypeCtl)

        elif (fanOnITypeCtl == 3):
            logg('call fanOnIType_3')
            fanOnIType_3()
            logg('after call fanOnIType_3')
            # test and adjust for new spoke
            fanOnITypeCtl = chk(fanOnITypeCtl)

        elif (fanOnITypeCtl == 4):
            logg('call fanOnIType_4')
            fanOnIType_4()
            logg('after call fanOnIType_4')
            # test and adjust for new spoke
            fanOnITypeCtl = chk(fanOnITypeCtl)

        else:
            #final
            logg('final fanOnIType')    
            fanOnITypeCtl = 0 # break
        #endif
    #wend
#end fanOnIType

def doQuestion_1():
    global p
    logg('doQuestion_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doQuestion-1 processing verb ( itxt ) ')
    if (r == p['OK']):
        logg('call itxt ')
        p['sy']['itxt'](p)
        logg('after itxt')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-1 processing verb ( msg ) ')
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
    logg('for doQuestion-1 processing text ')
    logg("""True (yes/no)""")
    if (r == p['OK']):
        logg('push text ' + """True (yes/no)""")
        datPush("True (yes/no)")
        logg('after ' + """True (yes/no)""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-1 processing verb ( ask ) ')
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
    logg('for doQuestion-1 processing verb ( ... ) ')
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
    logg('final doQuestion_1')
#end doQuestion_1

def doQuestion_2():
    global p
    logg('doQuestion_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doQuestion-2 processing verb ( dup ) ')
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
    logg('for doQuestion-2 processing verb ( ==yes ) ')
    if (r == p['OK']):
        logg('call ==yes ')
        p['sy']['==yes'](p)
        logg('after ==yes')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-2 processing verb ( drop ) ')
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
    logg('for doQuestion-2 processing text ')
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
    logg('for doQuestion-2 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-2 processing verb ( @ ) ')
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
    logg('for doQuestion-2 processing verb ( * ) ')
    if (r == p['OK']):
        logg('call * ')
        p['sy']['*'](p)
        logg('after *')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-2 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-2 processing verb ( ! ) ')
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
    logg('final doQuestion_2')
#end doQuestion_2

def doQuestion_3():
    global p
    logg('doQuestion_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doQuestion-3 processing verb ( dup ) ')
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
    logg('for doQuestion-3 processing verb ( ==no ) ')
    if (r == p['OK']):
        logg('call ==no ')
        p['sy']['==no'](p)
        logg('after ==no')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-3 processing verb ( drop ) ')
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
    logg('for doQuestion-3 processing text ')
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
    logg('for doQuestion-3 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-3 processing verb ( @ ) ')
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
    logg('for doQuestion-3 processing verb ( * ) ')
    if (r == p['OK']):
        logg('call * ')
        p['sy']['*'](p)
        logg('after *')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-3 processing text ')
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
    logg('for doQuestion-3 processing verb ( + ) ')
    if (r == p['OK']):
        logg('call + ')
        p['sy']['+'](p)
        logg('after +')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-3 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-3 processing verb ( ! ) ')
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
    logg('final doQuestion_3')
#end doQuestion_3

def doQuestion_4():
    global p
    logg('doQuestion_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doQuestion-4 processing text ')
    logg(""" error at doQuestion """)
    if (r == p['OK']):
        logg('push text ' + """ error at doQuestion """)
        datPush(" error at doQuestion ")
        logg('after ' + """ error at doQuestion """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doQuestion-4 processing verb ( swap ) ')
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
    logg('for doQuestion-4 processing verb ( cat ) ')
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
    logg('for doQuestion-4 processing verb ( msg ) ')
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
    logg('for doQuestion-4 processing verb ( exit ) ')
    if (r == p['OK']):
        logg('call exit ')
        p['sy']['exit'](p)
        logg('after exit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final doQuestion_4')
#end doQuestion_4

def doQuestion (x):
    global p
    logg('begin doQuestion')
    ## point of umbrella
    doQuestionCtl = 1 # starting spoke
    while doQuestionCtl != 0:
        logg('loop doQuestionCtl = ' + doQuestionCtl.__str__())
        if (doQuestionCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (doQuestionCtl == 1):
            logg('call doQuestion_1')
            doQuestion_1()
            logg('after call doQuestion_1')
            # test and adjust for new spoke
            doQuestionCtl = chk(doQuestionCtl)

        elif (doQuestionCtl == 2):
            logg('call doQuestion_2')
            doQuestion_2()
            logg('after call doQuestion_2')
            # test and adjust for new spoke
            doQuestionCtl = chk(doQuestionCtl)

        elif (doQuestionCtl == 3):
            logg('call doQuestion_3')
            doQuestion_3()
            logg('after call doQuestion_3')
            # test and adjust for new spoke
            doQuestionCtl = chk(doQuestionCtl)

        elif (doQuestionCtl == 4):
            logg('call doQuestion_4')
            doQuestion_4()
            logg('after call doQuestion_4')
            # test and adjust for new spoke
            doQuestionCtl = chk(doQuestionCtl)

        else:
            #final
            logg('final doQuestion')    
            doQuestionCtl = 0 # break
        #endif
    #wend
#end doQuestion

def doConclusion_1():
    global p
    logg('doConclusion_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doConclusion-1 processing verb ( itxt ) ')
    if (r == p['OK']):
        logg('call itxt ')
        p['sy']['itxt'](p)
        logg('after itxt')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-1 processing verb ( msg ) ')
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
    logg('for doConclusion-1 processing text ')
    logg("""was i right (yes/no)/ begin again (again) / (quit)""")
    if (r == p['OK']):
        logg('push text ' + """was i right (yes/no)/ begin again (again) / (quit)""")
        datPush("was i right (yes/no)/ begin again (again) / (quit)")
        logg('after ' + """was i right (yes/no)/ begin again (again) / (quit)""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-1 processing verb ( ask ) ')
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
    logg('for doConclusion-1 processing verb ( ... ) ')
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
    logg('final doConclusion_1')
#end doConclusion_1

def doConclusion_2():
    global p
    logg('doConclusion_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doConclusion-2 processing verb ( dup ) ')
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
    logg('for doConclusion-2 processing verb ( ==quit ) ')
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
    logg('for doConclusion-2 processing verb ( drop ) ')
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
    logg('for doConclusion-2 processing text ')
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
    logg('for doConclusion-2 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-2 processing verb ( ! ) ')
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
    logg('final doConclusion_2')
#end doConclusion_2

def doConclusion_3():
    global p
    logg('doConclusion_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doConclusion-3 processing verb ( dup ) ')
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
    logg('for doConclusion-3 processing verb ( ==yes ) ')
    if (r == p['OK']):
        logg('call ==yes ')
        p['sy']['==yes'](p)
        logg('after ==yes')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-3 processing verb ( drop ) ')
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
    logg('for doConclusion-3 processing text ')
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
    logg('for doConclusion-3 processing verb ( ask ) ')
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
    logg('for doConclusion-3 processing verb ( drop ) ')
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
    logg('for doConclusion-3 processing text ')
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
    logg('for doConclusion-3 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-3 processing verb ( ! ) ')
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
    logg('final doConclusion_3')
#end doConclusion_3

def doConclusion_4():
    global p
    logg('doConclusion_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doConclusion-4 processing verb ( dup ) ')
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
    logg('for doConclusion-4 processing verb ( ==again ) ')
    if (r == p['OK']):
        logg('call ==again ')
        p['sy']['==again'](p)
        logg('after ==again')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-4 processing verb ( drop ) ')
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
    logg('for doConclusion-4 processing text ')
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
    logg('for doConclusion-4 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-4 processing verb ( ! ) ')
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
    logg('final doConclusion_4')
#end doConclusion_4

def doConclusion_5():
    global p
    logg('doConclusion_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( dup ) ')
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
    logg('for doConclusion-5 processing verb ( ==no ) ')
    if (r == p['OK']):
        logg('call ==no ')
        p['sy']['==no'](p)
        logg('after ==no')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( drop ) ')
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
    logg('for doConclusion-5 processing text ')
    logg(""" what is the correct answer """)
    if (r == p['OK']):
        logg('push text ' + """ what is the correct answer """)
        datPush(" what is the correct answer ")
        logg('after ' + """ what is the correct answer """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( ask ) ')
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
    logg('for doConclusion-5 processing text ')
    logg("""correct""")
    if (r == p['OK']):
        logg('push text ' + """correct""")
        datPush("correct")
        logg('after ' + """correct""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( ! ) ')
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
    logg('for doConclusion-5 processing text ')
    logg("""what true/false question should i ask to tell the difference so that your answer is true""")
    if (r == p['OK']):
        logg('push text ' + """what true/false question should i ask to tell the difference so that your answer is true""")
        datPush("what true/false question should i ask to tell the difference so that your answer is true")
        logg('after ' + """what true/false question should i ask to tell the difference so that your answer is true""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( ask ) ')
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
    logg('for doConclusion-5 processing text ')
    logg("""TrueAns""")
    if (r == p['OK']):
        logg('push text ' + """TrueAns""")
        datPush("TrueAns")
        logg('after ' + """TrueAns""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( ! ) ')
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
    logg('for doConclusion-5 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( @ ) ')
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
    logg('for doConclusion-5 processing text ')
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
    logg('for doConclusion-5 processing verb ( * ) ')
    if (r == p['OK']):
        logg('call * ')
        p['sy']['*'](p)
        logg('after *')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing text ')
    logg("""truepos""")
    if (r == p['OK']):
        logg('push text ' + """truepos""")
        datPush("truepos")
        logg('after ' + """truepos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( ! ) ')
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
    logg('for doConclusion-5 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( @ ) ')
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
    logg('for doConclusion-5 processing text ')
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
    logg('for doConclusion-5 processing verb ( * ) ')
    if (r == p['OK']):
        logg('call * ')
        p['sy']['*'](p)
        logg('after *')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing text ')
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
    logg('for doConclusion-5 processing verb ( + ) ')
    if (r == p['OK']):
        logg('call + ')
        p['sy']['+'](p)
        logg('after +')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing text ')
    logg("""falsepos""")
    if (r == p['OK']):
        logg('push text ' + """falsepos""")
        datPush("falsepos")
        logg('after ' + """falsepos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( ! ) ')
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
    logg('for doConclusion-5 processing text ')
    logg("""truepos""")
    if (r == p['OK']):
        logg('push text ' + """truepos""")
        datPush("truepos")
        logg('after ' + """truepos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( @ ) ')
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
    logg('for doConclusion-5 processing text ')
    logg("""Conclusion""")
    if (r == p['OK']):
        logg('push text ' + """Conclusion""")
        datPush("Conclusion")
        logg('after ' + """Conclusion""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing text ')
    logg("""correct""")
    if (r == p['OK']):
        logg('push text ' + """correct""")
        datPush("correct")
        logg('after ' + """correct""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( @ ) ')
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
    logg('for doConclusion-5 processing verb ( writeRec ) ')
    if (r == p['OK']):
        logg('call writeRec ')
        p['sy']['writeRec'](p)
        logg('after writeRec')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing text ')
    logg("""falsepos""")
    if (r == p['OK']):
        logg('push text ' + """falsepos""")
        datPush("falsepos")
        logg('after ' + """falsepos""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( @ ) ')
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
    logg('for doConclusion-5 processing text ')
    logg("""conclusioin""")
    if (r == p['OK']):
        logg('push text ' + """conclusioin""")
        datPush("conclusioin")
        logg('after ' + """conclusioin""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( itxt ) ')
    if (r == p['OK']):
        logg('call itxt ')
        p['sy']['itxt'](p)
        logg('after itxt')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( writeRec ) ')
    if (r == p['OK']):
        logg('call writeRec ')
        p['sy']['writeRec'](p)
        logg('after writeRec')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( @ ) ')
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
    logg('for doConclusion-5 processing text ')
    logg("""Question""")
    if (r == p['OK']):
        logg('push text ' + """Question""")
        datPush("Question")
        logg('after ' + """Question""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing text ')
    logg("""TrueAns""")
    if (r == p['OK']):
        logg('push text ' + """TrueAns""")
        datPush("TrueAns")
        logg('after ' + """TrueAns""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( @ ) ')
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
    logg('for doConclusion-5 processing verb ( writeRec ) ')
    if (r == p['OK']):
        logg('call writeRec ')
        p['sy']['writeRec'](p)
        logg('after writeRec')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing text ')
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
    logg('for doConclusion-5 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-5 processing verb ( ! ) ')
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
    logg('final doConclusion_5')
#end doConclusion_5

def doConclusion_6():
    global p
    logg('doConclusion_6')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for doConclusion-6 processing text ')
    logg(""" error at doConclusion """)
    if (r == p['OK']):
        logg('push text ' + """ error at doConclusion """)
        datPush(" error at doConclusion ")
        logg('after ' + """ error at doConclusion """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for doConclusion-6 processing verb ( swap ) ')
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
    logg('for doConclusion-6 processing verb ( cat ) ')
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
    logg('for doConclusion-6 processing verb ( msg ) ')
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
    logg('for doConclusion-6 processing verb ( exit ) ')
    if (r == p['OK']):
        logg('call exit ')
        p['sy']['exit'](p)
        logg('after exit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final doConclusion_6')
#end doConclusion_6

def doConclusion (x):
    global p
    logg('begin doConclusion')
    ## point of umbrella
    doConclusionCtl = 1 # starting spoke
    while doConclusionCtl != 0:
        logg('loop doConclusionCtl = ' + doConclusionCtl.__str__())
        if (doConclusionCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (doConclusionCtl == 1):
            logg('call doConclusion_1')
            doConclusion_1()
            logg('after call doConclusion_1')
            # test and adjust for new spoke
            doConclusionCtl = chk(doConclusionCtl)

        elif (doConclusionCtl == 2):
            logg('call doConclusion_2')
            doConclusion_2()
            logg('after call doConclusion_2')
            # test and adjust for new spoke
            doConclusionCtl = chk(doConclusionCtl)

        elif (doConclusionCtl == 3):
            logg('call doConclusion_3')
            doConclusion_3()
            logg('after call doConclusion_3')
            # test and adjust for new spoke
            doConclusionCtl = chk(doConclusionCtl)

        elif (doConclusionCtl == 4):
            logg('call doConclusion_4')
            doConclusion_4()
            logg('after call doConclusion_4')
            # test and adjust for new spoke
            doConclusionCtl = chk(doConclusionCtl)

        elif (doConclusionCtl == 5):
            logg('call doConclusion_5')
            doConclusion_5()
            logg('after call doConclusion_5')
            # test and adjust for new spoke
            doConclusionCtl = chk(doConclusionCtl)

        elif (doConclusionCtl == 6):
            logg('call doConclusion_6')
            doConclusion_6()
            logg('after call doConclusion_6')
            # test and adjust for new spoke
            doConclusionCtl = chk(doConclusionCtl)

        else:
            #final
            logg('final doConclusion')    
            doConclusionCtl = 0 # break
        #endif
    #wend
#end doConclusion

def itxt_1():
    global p
    logg('itxt_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for itxt-1 processing text ')
    logg("""select txt from GF where ix='""")
    if (r == p['OK']):
        logg('push text ' + """select txt from GF where ix='""")
        datPush("select txt from GF where ix='")
        logg('after ' + """select txt from GF where ix='""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for itxt-1 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for itxt-1 processing verb ( @ ) ')
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
    logg('for itxt-1 processing verb ( cat ) ')
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
    logg('for itxt-1 processing text ')
    logg("""';""")
    if (r == p['OK']):
        logg('push text ' + """';""")
        datPush("';")
        logg('after ' + """';""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for itxt-1 processing verb ( cat ) ')
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
    logg('for itxt-1 processing verb ( SQRead ) ')
    if (r == p['OK']):
        logg('call SQRead ')
        p['sy']['SQRead'](p)
        logg('after SQRead')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final itxt_1')
#end itxt_1

def itxt (x):
    global p
    logg('begin itxt')
    ## point of umbrella
    itxtCtl = 1 # starting spoke
    while itxtCtl != 0:
        logg('loop itxtCtl = ' + itxtCtl.__str__())
        if (itxtCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (itxtCtl == 1):
            logg('call itxt_1')
            itxt_1()
            logg('after call itxt_1')
            # test and adjust for new spoke
            itxtCtl = chk(itxtCtl)

        else:
            #final
            logg('final itxt')    
            itxtCtl = 0 # break
        #endif
    #wend
#end itxt

def itype_1():
    global p
    logg('itype_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for itype-1 processing text ')
    logg("""select type from GF where ix='""")
    if (r == p['OK']):
        logg('push text ' + """select type from GF where ix='""")
        datPush("select type from GF where ix='")
        logg('after ' + """select type from GF where ix='""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for itype-1 processing text ')
    logg("""i""")
    if (r == p['OK']):
        logg('push text ' + """i""")
        datPush("i")
        logg('after ' + """i""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for itype-1 processing verb ( @ ) ')
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
    logg('for itype-1 processing verb ( cat ) ')
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
    logg('for itype-1 processing text ')
    logg("""';""")
    if (r == p['OK']):
        logg('push text ' + """';""")
        datPush("';")
        logg('after ' + """';""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for itype-1 processing verb ( cat ) ')
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
    logg('for itype-1 processing verb ( SQRead ) ')
    if (r == p['OK']):
        logg('call SQRead ')
        p['sy']['SQRead'](p)
        logg('after SQRead')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final itype_1')
#end itype_1

def itype (x):
    global p
    logg('begin itype')
    ## point of umbrella
    itypeCtl = 1 # starting spoke
    while itypeCtl != 0:
        logg('loop itypeCtl = ' + itypeCtl.__str__())
        if (itypeCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (itypeCtl == 1):
            logg('call itype_1')
            itype_1()
            logg('after call itype_1')
            # test and adjust for new spoke
            itypeCtl = chk(itypeCtl)

        else:
            #final
            logg('final itype')    
            itypeCtl = 0 # break
        #endif
    #wend
#end itype

def writeRec_1():
    global p
    logg('writeRec_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for writeRec-1 processing text ')
    logg("""tmp-txt""")
    if (r == p['OK']):
        logg('push text ' + """tmp-txt""")
        datPush("tmp-txt")
        logg('after ' + """tmp-txt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( ! ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""tmp-type""")
    if (r == p['OK']):
        logg('push text ' + """tmp-type""")
        datPush("tmp-type")
        logg('after ' + """tmp-type""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( ! ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""tmp-ix""")
    if (r == p['OK']):
        logg('push text ' + """tmp-ix""")
        datPush("tmp-ix")
        logg('after ' + """tmp-ix""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( ! ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""INSERT OR REPLACE INTO table(ix,type,txt) VALUES(""")
    if (r == p['OK']):
        logg('push text ' + """INSERT OR REPLACE INTO table(ix,type,txt) VALUES(""")
        datPush("INSERT OR REPLACE INTO table(ix,type,txt) VALUES(")
        logg('after ' + """INSERT OR REPLACE INTO table(ix,type,txt) VALUES(""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing text ')
    logg("""'""")
    if (r == p['OK']):
        logg('push text ' + """'""")
        datPush("'")
        logg('after ' + """'""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( cat ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""tmp-ix""")
    if (r == p['OK']):
        logg('push text ' + """tmp-ix""")
        datPush("tmp-ix")
        logg('after ' + """tmp-ix""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( @ ) ')
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
    logg('for writeRec-1 processing verb ( cat ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""'""")
    if (r == p['OK']):
        logg('push text ' + """'""")
        datPush("'")
        logg('after ' + """'""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( cat ) ')
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
    logg('for writeRec-1 processing text ')
    logg(""",""")
    if (r == p['OK']):
        logg('push text ' + """,""")
        datPush(",")
        logg('after ' + """,""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( cats ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""'""")
    if (r == p['OK']):
        logg('push text ' + """'""")
        datPush("'")
        logg('after ' + """'""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( cat ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""tmp-type""")
    if (r == p['OK']):
        logg('push text ' + """tmp-type""")
        datPush("tmp-type")
        logg('after ' + """tmp-type""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( @ ) ')
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
    logg('for writeRec-1 processing verb ( cat ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""'""")
    if (r == p['OK']):
        logg('push text ' + """'""")
        datPush("'")
        logg('after ' + """'""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( cat ) ')
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
    logg('for writeRec-1 processing text ')
    logg(""",""")
    if (r == p['OK']):
        logg('push text ' + """,""")
        datPush(",")
        logg('after ' + """,""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( cats ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""'""")
    if (r == p['OK']):
        logg('push text ' + """'""")
        datPush("'")
        logg('after ' + """'""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( cat ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""tmp-txt""")
    if (r == p['OK']):
        logg('push text ' + """tmp-txt""")
        datPush("tmp-txt")
        logg('after ' + """tmp-txt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( @ ) ')
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
    logg('for writeRec-1 processing verb ( cat ) ')
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
    logg('for writeRec-1 processing text ')
    logg("""'""")
    if (r == p['OK']):
        logg('push text ' + """'""")
        datPush("'")
        logg('after ' + """'""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( cat ) ')
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
    logg('for writeRec-1 processing text ')
    logg(""");""")
    if (r == p['OK']):
        logg('push text ' + """);""")
        datPush(");")
        logg('after ' + """);""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeRec-1 processing verb ( cats ) ')
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
    logg('for writeRec-1 processing verb ( dup ) ')
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
    logg('for writeRec-1 processing verb ( msg ) ')
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
    logg('for writeRec-1 processing text ')
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
    logg('for writeRec-1 processing verb ( ask ) ')
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
    logg('for writeRec-1 processing verb ( SQX ) ')
    if (r == p['OK']):
        logg('call SQX ')
        p['sy']['SQX'](p)
        logg('after SQX')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final writeRec_1')
#end writeRec_1

def writeRec (x):
    global p
    logg('begin writeRec')
    ## point of umbrella
    writeRecCtl = 1 # starting spoke
    while writeRecCtl != 0:
        logg('loop writeRecCtl = ' + writeRecCtl.__str__())
        if (writeRecCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (writeRecCtl == 1):
            logg('call writeRec_1')
            writeRec_1()
            logg('after call writeRec_1')
            # test and adjust for new spoke
            writeRecCtl = chk(writeRecCtl)

        else:
            #final
            logg('final writeRec')    
            writeRecCtl = 0 # break
        #endif
    #wend
#end writeRec

# stream routines 

def EQcontinue(p):
    logg ('==continue')
    needle = 'continue'
    needle = needle.upper()
    return(eqeq(needle))
#end EQcontinue

def EQ0(p):
    logg ('==0')
    needle = '0'
    needle = needle.upper()
    return(eqeq(needle))
#end EQ0

def EQquestion(p):
    logg ('==question')
    needle = 'question'
    needle = needle.upper()
    return(eqeq(needle))
#end EQquestion

def EQconclusion(p):
    logg ('==conclusion')
    needle = 'conclusion'
    needle = needle.upper()
    return(eqeq(needle))
#end EQconclusion

def EQyes(p):
    logg ('==yes')
    needle = 'yes'
    needle = needle.upper()
    return(eqeq(needle))
#end EQyes

def EQno(p):
    logg ('==no')
    needle = 'no'
    needle = needle.upper()
    return(eqeq(needle))
#end EQno

def EQquit(p):
    logg ('==quit')
    needle = 'quit'
    needle = needle.upper()
    return(eqeq(needle))
#end EQquit

def EQyes(p):
    logg ('==yes')
    needle = 'yes'
    needle = needle.upper()
    return(eqeq(needle))
#end EQyes

def EQagain(p):
    logg ('==again')
    needle = 'again'
    needle = needle.upper()
    return(eqeq(needle))
#end EQagain

def EQno(p):
    logg ('==no')
    needle = 'no'
    needle = needle.upper()
    return(eqeq(needle))
#end EQno

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

    # paragraph initGF
    p['sy']['initGF'] = initGF
    #

    # paragraph admin
    p['sy']['admin'] = admin
    #

    # paragraph ==continue
    p['sy']['==continue'] = EQcontinue
    #

    # paragraph GFcold
    p['sy']['GFcold'] = GFcold
    #

    # paragraph GFMain
    p['sy']['GFMain'] = GFMain
    #

    # paragraph GF2
    p['sy']['GF2'] = GF2
    #

    # paragraph ==0
    p['sy']['==0'] = EQ0
    #

    # paragraph fanOnIType
    p['sy']['fanOnIType'] = fanOnIType
    #

    # paragraph ==question
    p['sy']['==question'] = EQquestion
    #

    # paragraph ==conclusion
    p['sy']['==conclusion'] = EQconclusion
    #

    # paragraph doQuestion
    p['sy']['doQuestion'] = doQuestion
    #

    # paragraph ==yes
    p['sy']['==yes'] = EQyes
    #

    # paragraph ==no
    p['sy']['==no'] = EQno
    #

    # paragraph doConclusion
    p['sy']['doConclusion'] = doConclusion
    #

    # paragraph ==quit
    p['sy']['==quit'] = EQquit
    #

    # paragraph ==yes
    p['sy']['==yes'] = EQyes
    #

    # paragraph ==again
    p['sy']['==again'] = EQagain
    #

    # paragraph ==no
    p['sy']['==no'] = EQno
    #

    # paragraph itxt
    p['sy']['itxt'] = itxt
    #

    # paragraph itype
    p['sy']['itype'] = itype
    #

    # paragraph writeRec
    p['sy']['writeRec'] = writeRec
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

