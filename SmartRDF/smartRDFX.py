
#file smartRDFX.py
#generated for smartRDF.basii at Fri Jan 24 14:50:20 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def initIOI_1():
    global p
    logg('initIOI_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for initIOI-1 processing text ')
    logg("""fioiP""")
    if (r == p['OK']):
        logg('push text ' + """fioiP""")
        datPush("fioiP")
        logg('after ' + """fioiP""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initIOI-1 processing verb ( takeV ) ')
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
    logg('for initIOI-1 processing verb ( ... ) ')
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
    logg('final initIOI_1')
#end initIOI_1

def initIOI_2():
    global p
    logg('initIOI_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for initIOI-2 processing text ')
    logg("""RDF.db""")
    if (r == p['OK']):
        logg('push text ' + """RDF.db""")
        datPush("RDF.db")
        logg('after ' + """RDF.db""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initIOI-2 processing text ')
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
    logg('for initIOI-2 processing verb ( takeV ) ')
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
    logg('for initIOI-2 processing verb ( ... ) ')
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
    logg('final initIOI_2')
#end initIOI_2

def initIOI_3():
    global p
    logg('initIOI_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for initIOI-3 processing text ')
    logg("""create table if not exists RDFTuple ( subject , predicate, object, ssubject, spredicate, sobject, osubject, opredicate, oobject);""")
    if (r == p['OK']):
        logg('push text ' + """create table if not exists RDFTuple ( subject , predicate, object, ssubject, spredicate, sobject, osubject, opredicate, oobject);""")
        datPush("create table if not exists RDFTuple ( subject , predicate, object, ssubject, spredicate, sobject, osubject, opredicate, oobject);")
        logg('after ' + """create table if not exists RDFTuple ( subject , predicate, object, ssubject, spredicate, sobject, osubject, opredicate, oobject);""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initIOI-3 processing verb ( SQX ) ')
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
    logg('final initIOI_3')
#end initIOI_3

def initIOI (x):
    global p
    logg('begin initIOI')
    ## point of umbrella
    initIOICtl = 1 # starting spoke
    while initIOICtl != 0:
        logg('loop initIOICtl = ' + initIOICtl.__str__())
        if (initIOICtl == -1):
            nop = -1 # false test to set up elif chain

        elif (initIOICtl == 1):
            logg('call initIOI_1')
            initIOI_1()
            logg('after call initIOI_1')
            # test and adjust for new spoke
            initIOICtl = chk(initIOICtl)

        elif (initIOICtl == 2):
            logg('call initIOI_2')
            initIOI_2()
            logg('after call initIOI_2')
            # test and adjust for new spoke
            initIOICtl = chk(initIOICtl)

        elif (initIOICtl == 3):
            logg('call initIOI_3')
            initIOI_3()
            logg('after call initIOI_3')
            # test and adjust for new spoke
            initIOICtl = chk(initIOICtl)

        else:
            #final
            logg('final initIOI')    
            initIOICtl = 0 # break
        #endif
    #wend
#end initIOI

def RDFMain_1():
    global p
    logg('RDFMain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for RDFMain-1 processing text ')
    logg("""script file""")
    if (r == p['OK']):
        logg('push text ' + """script file""")
        datPush("script file")
        logg('after ' + """script file""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFMain-1 processing verb ( ask ) ')
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
    logg('for RDFMain-1 processing verb ( dup ) ')
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
    logg('for RDFMain-1 processing text ')
    logg("""scriptF""")
    if (r == p['OK']):
        logg('push text ' + """scriptF""")
        datPush("scriptF")
        logg('after ' + """scriptF""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFMain-1 processing verb ( ! ) ')
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
    logg('for RDFMain-1 processing verb ( initIOI ) ')
    if (r == p['OK']):
        logg('call initIOI ')
        p['sy']['initIOI'](p)
        logg('after initIOI')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFMain-1 processing verb ( RDFMain2 ) ')
    if (r == p['OK']):
        logg('call RDFMain2 ')
        p['sy']['RDFMain2'](p)
        logg('after RDFMain2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final RDFMain_1')
#end RDFMain_1

def RDFMain (x):
    global p
    logg('begin RDFMain')
    ## point of umbrella
    RDFMainCtl = 1 # starting spoke
    while RDFMainCtl != 0:
        logg('loop RDFMainCtl = ' + RDFMainCtl.__str__())
        if (RDFMainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (RDFMainCtl == 1):
            logg('call RDFMain_1')
            RDFMain_1()
            logg('after call RDFMain_1')
            # test and adjust for new spoke
            RDFMainCtl = chk(RDFMainCtl)

        else:
            #final
            logg('final RDFMain')    
            RDFMainCtl = 0 # break
        #endif
    #wend
#end RDFMain

def RDFMain2_1():
    global p
    logg('RDFMain2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for RDFMain2-1 processing verb ( fpword ) ')
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
    logg('for RDFMain2-1 processing verb ( ... ) ')
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
    logg('final RDFMain2_1')
#end RDFMain2_1

def RDFMain2_2():
    global p
    logg('RDFMain2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for RDFMain2-2 processing verb ( ==RDF ) ')
    if (r == p['OK']):
        logg('call ==RDF ')
        p['sy']['==RDF'](p)
        logg('after ==RDF')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFMain2-2 processing verb ( RDFMain3 ) ')
    if (r == p['OK']):
        logg('call RDFMain3 ')
        p['sy']['RDFMain3'](p)
        logg('after RDFMain3')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFMain2-2 processing verb ( fpword ) ')
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
    logg('for RDFMain2-2 processing verb ( ==/RDF ) ')
    if (r == p['OK']):
        logg('call ==/RDF ')
        p['sy']['==/RDF'](p)
        logg('after ==/RDF')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFMain2-2 processing verb ( actRDFMain2 ) ')
    if (r == p['OK']):
        logg('call actRDFMain2 ')
        p['sy']['actRDFMain2'](p)
        logg('after actRDFMain2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final RDFMain2_2')
#end RDFMain2_2

def RDFMain2_3():
    global p
    logg('RDFMain2_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for RDFMain2-3 processing text ')
    logg("""error at RDFMain2 """)
    if (r == p['OK']):
        logg('push text ' + """error at RDFMain2 """)
        datPush("error at RDFMain2 ")
        logg('after ' + """error at RDFMain2 """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFMain2-3 processing verb ( abort ) ')
    if (r == p['OK']):
        logg('call abort ')
        p['sy']['abort'](p)
        logg('after abort')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final RDFMain2_3')
#end RDFMain2_3

def RDFMain2 (x):
    global p
    logg('begin RDFMain2')
    ## point of umbrella
    RDFMain2Ctl = 1 # starting spoke
    while RDFMain2Ctl != 0:
        logg('loop RDFMain2Ctl = ' + RDFMain2Ctl.__str__())
        if (RDFMain2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (RDFMain2Ctl == 1):
            logg('call RDFMain2_1')
            RDFMain2_1()
            logg('after call RDFMain2_1')
            # test and adjust for new spoke
            RDFMain2Ctl = chk(RDFMain2Ctl)

        elif (RDFMain2Ctl == 2):
            logg('call RDFMain2_2')
            RDFMain2_2()
            logg('after call RDFMain2_2')
            # test and adjust for new spoke
            RDFMain2Ctl = chk(RDFMain2Ctl)

        elif (RDFMain2Ctl == 3):
            logg('call RDFMain2_3')
            RDFMain2_3()
            logg('after call RDFMain2_3')
            # test and adjust for new spoke
            RDFMain2Ctl = chk(RDFMain2Ctl)

        else:
            #final
            logg('final RDFMain2')    
            RDFMain2Ctl = 0 # break
        #endif
    #wend
#end RDFMain2

def :-_]]():
    global p
    logg(':-_]]')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--]] processing verb ( verify ) ')
    if (r == p['OK']):
        logg('call verify ')
        p['sy']['verify'](p)
        logg('after verify')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final :-_]]')
#end :-_]]

def :-_2():
    global p
    logg(':-_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--2 processing text ')
    logg("""error at RDFMain3""")
    if (r == p['OK']):
        logg('push text ' + """error at RDFMain3""")
        datPush("error at RDFMain3")
        logg('after ' + """error at RDFMain3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--2 processing verb ( abort ) ')
    if (r == p['OK']):
        logg('call abort ')
        p['sy']['abort'](p)
        logg('after abort')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final :-_2')
#end :-_2

def :- (x):
    global p
    logg('begin :-')
    ## point of umbrella
    :-Ctl = 1 # starting spoke
    while :-Ctl != 0:
        logg('loop :-Ctl = ' + :-Ctl.__str__())
        if (:-Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (:-Ctl == 1):
            logg('call :-_]]')
            :-_]]()
            logg('after call :-_]]')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 2):
            logg('call :-_2')
            :-_2()
            logg('after call :-_2')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        else:
            #final
            logg('final :-')    
            :-Ctl = 0 # break
        #endif
    #wend
#end :-

def :-_]]():
    global p
    logg(':-_]]')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--]] processing verb ( ... ) ')
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
    logg('final :-_]]')
#end :-_]]

def :-_2():
    global p
    logg(':-_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--2 processing verb ( dup ) ')
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
    logg('for :--2 processing verb ( ==event ) ')
    if (r == p['OK']):
        logg('call ==event ')
        p['sy']['==event'](p)
        logg('after ==event')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--2 processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--2 processing verb ( ! ) ')
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
    logg('final :-_2')
#end :-_2

def :-_3():
    global p
    logg(':-_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--3 processing verb ( dup ) ')
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
    logg('for :--3 processing verb ( ==action ) ')
    if (r == p['OK']):
        logg('call ==action ')
        p['sy']['==action'](p)
        logg('after ==action')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--3 processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--3 processing verb ( ! ) ')
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
    logg('final :-_3')
#end :-_3

def :-_4():
    global p
    logg(':-_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--4 processing verb ( dup ) ')
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
    logg('for :--4 processing verb ( ==predicate ) ')
    if (r == p['OK']):
        logg('call ==predicate ')
        p['sy']['==predicate'](p)
        logg('after ==predicate')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--4 processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--4 processing verb ( ! ) ')
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
    logg('final :-_4')
#end :-_4

def :-_5():
    global p
    logg(':-_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--5 processing verb ( dup ) ')
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
    logg('for :--5 processing verb ( ==watch ) ')
    if (r == p['OK']):
        logg('call ==watch ')
        p['sy']['==watch'](p)
        logg('after ==watch')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--5 processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--5 processing verb ( ! ) ')
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
    logg('final :-_5')
#end :-_5

def :-_6():
    global p
    logg(':-_6')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--6 processing verb ( dup ) ')
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
    logg('for :--6 processing verb ( ==state ) ')
    if (r == p['OK']):
        logg('call ==state ')
        p['sy']['==state'](p)
        logg('after ==state')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--6 processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--6 processing verb ( ! ) ')
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
    logg('final :-_6')
#end :-_6

def :-_7():
    global p
    logg(':-_7')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--7 processing verb ( ==* ) ')
    if (r == p['OK']):
        logg('call ==* ')
        p['sy']['==*'](p)
        logg('after ==*')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--7 processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--7 processing verb ( ! ) ')
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
    logg('final :-_7')
#end :-_7

def :-_8():
    global p
    logg(':-_8')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--8 processing verb ( c1 ) ')
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
    logg('for :--8 processing verb ( ... ) ')
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
    logg('final :-_8')
#end :-_8

def :-_9():
    global p
    logg(':-_9')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--9 processing verb ( dup ) ')
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
    logg('for :--9 processing verb ( ==[ ) ')
    if (r == p['OK']):
        logg('call ==[ ')
        p['sy']['==['](p)
        logg('after ==[')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--9 processing verb ( getsubject9a ) ')
    if (r == p['OK']):
        logg('call getsubject9a ')
        p['sy']['getsubject9a'](p)
        logg('after getsubject9a')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final :-_9')
#end :-_9

def :-_10():
    global p
    logg(':-_10')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--10 processing verb ( dup ) ')
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
    logg('for :--10 processing verb ( ==[[ ) ')
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
    logg('for :--10 processing verb ( getsubject10a ) ')
    if (r == p['OK']):
        logg('call getsubject10a ')
        p['sy']['getsubject10a'](p)
        logg('after getsubject10a')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final :-_10')
#end :-_10

def :-_11():
    global p
    logg(':-_11')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--11 processing verb ( drop ) ')
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
    logg('final :-_11')
#end :-_11

def :-_getsubject11a():
    global p
    logg(':-_getsubject11a')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--getsubject11a processing verb ( [[ ) ')
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
    logg('for :--getsubject11a processing verb ( 12 ) ')
    if (r == p['OK']):
        logg('call 12 ')
        p['sy']['12'](p)
        logg('after 12')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--getsubject11a processing verb ( ]] ) ')
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
    logg('for :--getsubject11a processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--getsubject11a processing verb ( ! ) ')
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
    logg('final :-_getsubject11a')
#end :-_getsubject11a

def :-_13():
    global p
    logg(':-_13')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--13 processing text ')
    logg("""error at getsubject""")
    if (r == p['OK']):
        logg('push text ' + """error at getsubject""")
        datPush("error at getsubject")
        logg('after ' + """error at getsubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for :--13 processing verb ( abort ) ')
    if (r == p['OK']):
        logg('call abort ')
        p['sy']['abort'](p)
        logg('after abort')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final :-_13')
#end :-_13

def :- (x):
    global p
    logg('begin :-')
    ## point of umbrella
    :-Ctl = 1 # starting spoke
    while :-Ctl != 0:
        logg('loop :-Ctl = ' + :-Ctl.__str__())
        if (:-Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (:-Ctl == 1):
            logg('call :-_]]')
            :-_]]()
            logg('after call :-_]]')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 2):
            logg('call :-_2')
            :-_2()
            logg('after call :-_2')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 3):
            logg('call :-_3')
            :-_3()
            logg('after call :-_3')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 4):
            logg('call :-_4')
            :-_4()
            logg('after call :-_4')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 5):
            logg('call :-_5')
            :-_5()
            logg('after call :-_5')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 6):
            logg('call :-_6')
            :-_6()
            logg('after call :-_6')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 7):
            logg('call :-_7')
            :-_7()
            logg('after call :-_7')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 8):
            logg('call :-_8')
            :-_8()
            logg('after call :-_8')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 9):
            logg('call :-_9')
            :-_9()
            logg('after call :-_9')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 10):
            logg('call :-_10')
            :-_10()
            logg('after call :-_10')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 11):
            logg('call :-_11')
            :-_11()
            logg('after call :-_11')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 12):
            logg('call :-_getsubject11a')
            :-_getsubject11a()
            logg('after call :-_getsubject11a')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        elif (:-Ctl == 13):
            logg('call :-_13')
            :-_13()
            logg('after call :-_13')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        else:
            #final
            logg('final :-')    
            :-Ctl = 0 # break
        #endif
    #wend
#end :-

def :-_]]():
    global p
    logg(':-_]]')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--]] processing verb ( msg ) ')
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
    logg('for :--]] processing verb ( dump ) ')
    if (r == p['OK']):
        logg('call dump ')
        p['sy']['dump'](p)
        logg('after dump')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final :-_]]')
#end :-_]]

def :- (x):
    global p
    logg('begin :-')
    ## point of umbrella
    :-Ctl = 1 # starting spoke
    while :-Ctl != 0:
        logg('loop :-Ctl = ' + :-Ctl.__str__())
        if (:-Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (:-Ctl == 1):
            logg('call :-_]]')
            :-_]]()
            logg('after call :-_]]')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        else:
            #final
            logg('final :-')    
            :-Ctl = 0 # break
        #endif
    #wend
#end :-

def :-_]]():
    global p
    logg(':-_]]')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--]] processing verb ( msg ) ')
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
    logg('for :--]] processing verb ( dump ) ')
    if (r == p['OK']):
        logg('call dump ')
        p['sy']['dump'](p)
        logg('after dump')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final :-_]]')
#end :-_]]

def :- (x):
    global p
    logg('begin :-')
    ## point of umbrella
    :-Ctl = 1 # starting spoke
    while :-Ctl != 0:
        logg('loop :-Ctl = ' + :-Ctl.__str__())
        if (:-Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (:-Ctl == 1):
            logg('call :-_]]')
            :-_]]()
            logg('after call :-_]]')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        else:
            #final
            logg('final :-')    
            :-Ctl = 0 # break
        #endif
    #wend
#end :-

def [[_getsubjecy11a ():
    global p
    logg('[[_getsubjecy11a ')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for [[-getsubjecy11a  processing verb ( dump ) ')
    if (r == p['OK']):
        logg('call dump ')
        p['sy']['dump'](p)
        logg('after dump')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final [[_getsubjecy11a ')
#end [[_getsubjecy11a 

def [[ (x):
    global p
    logg('begin [[')
    ## point of umbrella
    [[Ctl = 1 # starting spoke
    while [[Ctl != 0:
        logg('loop [[Ctl = ' + [[Ctl.__str__())
        if ([[Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif ([[Ctl == 1):
            logg('call [[_getsubjecy11a ')
            [[_getsubjecy11a ()
            logg('after call [[_getsubjecy11a ')
            # test and adjust for new spoke
            [[Ctl = chk([[Ctl)

        else:
            #final
            logg('final [[')    
            [[Ctl = 0 # break
        #endif
    #wend
#end [[

def :-_]]():
    global p
    logg(':-_]]')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for :--]] processing verb ( msg ) ')
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
    logg('for :--]] processing verb ( dump ) ')
    if (r == p['OK']):
        logg('call dump ')
        p['sy']['dump'](p)
        logg('after dump')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final :-_]]')
#end :-_]]

def :- (x):
    global p
    logg('begin :-')
    ## point of umbrella
    :-Ctl = 1 # starting spoke
    while :-Ctl != 0:
        logg('loop :-Ctl = ' + :-Ctl.__str__())
        if (:-Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (:-Ctl == 1):
            logg('call :-_]]')
            :-_]]()
            logg('after call :-_]]')
            # test and adjust for new spoke
            :-Ctl = chk(:-Ctl)

        else:
            #final
            logg('final :-')    
            :-Ctl = 0 # break
        #endif
    #wend
#end :-

def act1_1():
    global p
    logg('act1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( @ ) ')
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
    logg('for act1-1 processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
    logg("""predicate""")
    if (r == p['OK']):
        logg('push text ' + """predicate""")
        datPush("predicate")
        logg('after ' + """predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( @ ) ')
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
    logg('for act1-1 processing text ')
    logg("""predicate""")
    if (r == p['OK']):
        logg('push text ' + """predicate""")
        datPush("predicate")
        logg('after ' + """predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
    logg("""object""")
    if (r == p['OK']):
        logg('push text ' + """object""")
        datPush("object")
        logg('after ' + """object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( @ ) ')
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
    logg('for act1-1 processing text ')
    logg("""object""")
    if (r == p['OK']):
        logg('push text ' + """object""")
        datPush("object")
        logg('after ' + """object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
    logg("""ssubject""")
    if (r == p['OK']):
        logg('push text ' + """ssubject""")
        datPush("ssubject")
        logg('after ' + """ssubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( @ ) ')
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
    logg('for act1-1 processing text ')
    logg("""ssubject""")
    if (r == p['OK']):
        logg('push text ' + """ssubject""")
        datPush("ssubject")
        logg('after ' + """ssubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
    logg("""spredicate""")
    if (r == p['OK']):
        logg('push text ' + """spredicate""")
        datPush("spredicate")
        logg('after ' + """spredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( @ ) ')
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
    logg('for act1-1 processing text ')
    logg("""spredicate""")
    if (r == p['OK']):
        logg('push text ' + """spredicate""")
        datPush("spredicate")
        logg('after ' + """spredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
    logg("""sobject""")
    if (r == p['OK']):
        logg('push text ' + """sobject""")
        datPush("sobject")
        logg('after ' + """sobject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( @ ) ')
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
    logg('for act1-1 processing text ')
    logg("""sobject""")
    if (r == p['OK']):
        logg('push text ' + """sobject""")
        datPush("sobject")
        logg('after ' + """sobject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
    logg("""osubject""")
    if (r == p['OK']):
        logg('push text ' + """osubject""")
        datPush("osubject")
        logg('after ' + """osubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( @ ) ')
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
    logg('for act1-1 processing text ')
    logg("""osubject""")
    if (r == p['OK']):
        logg('push text ' + """osubject""")
        datPush("osubject")
        logg('after ' + """osubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
    logg("""opredicate""")
    if (r == p['OK']):
        logg('push text ' + """opredicate""")
        datPush("opredicate")
        logg('after ' + """opredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( @ ) ')
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
    logg('for act1-1 processing text ')
    logg("""opredicate""")
    if (r == p['OK']):
        logg('push text ' + """opredicate""")
        datPush("opredicate")
        logg('after ' + """opredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
    logg("""oobject""")
    if (r == p['OK']):
        logg('push text ' + """oobject""")
        datPush("oobject")
        logg('after ' + """oobject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( @ ) ')
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
    logg('for act1-1 processing text ')
    logg("""oobject""")
    if (r == p['OK']):
        logg('push text ' + """oobject""")
        datPush("oobject")
        logg('after ' + """oobject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
    logg("""RDFTuple""")
    if (r == p['OK']):
        logg('push text ' + """RDFTuple""")
        datPush("RDFTuple")
        logg('after ' + """RDFTuple""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( SQWrite ) ')
    if (r == p['OK']):
        logg('call SQWrite ')
        p['sy']['SQWrite'](p)
        logg('after SQWrite')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""subject""")
    if (r == p['OK']):
        logg('push text ' + """subject""")
        datPush("subject")
        logg('after ' + """subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( ! ) ')
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
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""predicate""")
    if (r == p['OK']):
        logg('push text ' + """predicate""")
        datPush("predicate")
        logg('after ' + """predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( ! ) ')
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
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""object""")
    if (r == p['OK']):
        logg('push text ' + """object""")
        datPush("object")
        logg('after ' + """object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( ! ) ')
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
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""ssubject""")
    if (r == p['OK']):
        logg('push text ' + """ssubject""")
        datPush("ssubject")
        logg('after ' + """ssubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( ! ) ')
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
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""spredicate""")
    if (r == p['OK']):
        logg('push text ' + """spredicate""")
        datPush("spredicate")
        logg('after ' + """spredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( ! ) ')
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
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""sobject""")
    if (r == p['OK']):
        logg('push text ' + """sobject""")
        datPush("sobject")
        logg('after ' + """sobject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( ! ) ')
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
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""osubject""")
    if (r == p['OK']):
        logg('push text ' + """osubject""")
        datPush("osubject")
        logg('after ' + """osubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( ! ) ')
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
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""opredicate""")
    if (r == p['OK']):
        logg('push text ' + """opredicate""")
        datPush("opredicate")
        logg('after ' + """opredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( ! ) ')
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
    logg('for act1-1 processing text ')
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
    logg('for act1-1 processing text ')
    logg("""oobject""")
    if (r == p['OK']):
        logg('push text ' + """oobject""")
        datPush("oobject")
        logg('after ' + """oobject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for act1-1 processing verb ( ! ) ')
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
    logg('final act1_1')
#end act1_1

def act1 (x):
    global p
    logg('begin act1')
    ## point of umbrella
    act1Ctl = 1 # starting spoke
    while act1Ctl != 0:
        logg('loop act1Ctl = ' + act1Ctl.__str__())
        if (act1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (act1Ctl == 1):
            logg('call act1_1')
            act1_1()
            logg('after call act1_1')
            # test and adjust for new spoke
            act1Ctl = chk(act1Ctl)

        else:
            #final
            logg('final act1')    
            act1Ctl = 0 # break
        #endif
    #wend
#end act1

# stream routines 

def EQRDF(p):
    logg ('==RDF')
    needle = 'RDF'
    needle = needle.upper()
    return(eqeq(needle))
#end EQRDF

def EQzslzRDF(p):
    logg ('==/RDF')
    needle = '/RDF'
    needle = needle.upper()
    return(eqeq(needle))
#end EQzslzRDF

def EQevent(p):
    logg ('==event')
    needle = 'event'
    needle = needle.upper()
    return(eqeq(needle))
#end EQevent

def EQaction(p):
    logg ('==action')
    needle = 'action'
    needle = needle.upper()
    return(eqeq(needle))
#end EQaction

def EQpredicate(p):
    logg ('==predicate')
    needle = 'predicate'
    needle = needle.upper()
    return(eqeq(needle))
#end EQpredicate

def EQwatch(p):
    logg ('==watch')
    needle = 'watch'
    needle = needle.upper()
    return(eqeq(needle))
#end EQwatch

def EQstate(p):
    logg ('==state')
    needle = 'state'
    needle = needle.upper()
    return(eqeq(needle))
#end EQstate

def EQzsz(p):
    logg ('==*')
    needle = '*'
    needle = needle.upper()
    return(eqeq(needle))
#end EQzsz

def EQzobz(p):
    logg ('==[')
    needle = '['
    needle = needle.upper()
    return(eqeq(needle))
#end EQzobz

def EQzobzzobz(p):
    logg ('==[[')
    needle = '[['
    needle = needle.upper()
    return(eqeq(needle))
#end EQzobzzobz

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

    # paragraph initIOI
    p['sy']['initIOI'] = initIOI
    #

    # paragraph RDFMain
    p['sy']['RDFMain'] = RDFMain
    #

    # paragraph RDFMain2
    p['sy']['RDFMain2'] = RDFMain2
    #

    # paragraph ==RDF
    p['sy']['==RDF'] = EQRDF
    #

    # paragraph ==/RDF
    p['sy']['==/RDF'] = EQzslzRDF
    #

    # paragraph :-
    p['sy'][':-'] = :-
    #

    # paragraph :-
    p['sy'][':-'] = :-
    #

    # paragraph ==event
    p['sy']['==event'] = EQevent
    #

    # paragraph ==action
    p['sy']['==action'] = EQaction
    #

    # paragraph ==predicate
    p['sy']['==predicate'] = EQpredicate
    #

    # paragraph ==watch
    p['sy']['==watch'] = EQwatch
    #

    # paragraph ==state
    p['sy']['==state'] = EQstate
    #

    # paragraph ==*
    p['sy']['==*'] = EQzsz
    #

    # paragraph ==[
    p['sy']['==['] = EQzobz
    #

    # paragraph ==[[
    p['sy']['==[['] = EQzobzzobz
    #

    # paragraph :-
    p['sy'][':-'] = :-
    #

    # paragraph :-
    p['sy'][':-'] = :-
    #

    # paragraph [[
    p['sy']['[['] = [[
    #

    # paragraph :-
    p['sy'][':-'] = :-
    #

    # paragraph act1
    p['sy']['act1'] = act1
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

