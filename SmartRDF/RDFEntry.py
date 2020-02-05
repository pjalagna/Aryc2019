
#file RDFEntry.py
#generated for RDFEntry.basii at Tue Feb  4 21:54:43 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def RDFEntry_1():
    global p
    logg('RDFEntry_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for RDFEntry-1 processing verb ( initRDF ) ')
    if (r == p['OK']):
        logg('call initRDF ')
        p['sy']['initRDF'](p)
        logg('after initRDF')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFEntry-1 processing verb ( clearAll ) ')
    if (r == p['OK']):
        logg('call clearAll ')
        p['sy']['clearAll'](p)
        logg('after clearAll')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFEntry-1 processing text ')
    logg("""?>""")
    if (r == p['OK']):
        logg('push text ' + """?>""")
        datPush("?>")
        logg('after ' + """?>""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFEntry-1 processing verb ( ask ) ')
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
    logg('for RDFEntry-1 processing verb ( setSStr ) ')
    if (r == p['OK']):
        logg('call setSStr ')
        p['sy']['setSStr'](p)
        logg('after setSStr')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFEntry-1 processing verb ( getSubject ) ')
    if (r == p['OK']):
        logg('call getSubject ')
        p['sy']['getSubject'](p)
        logg('after getSubject')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFEntry-1 processing verb ( getPredicate ) ')
    if (r == p['OK']):
        logg('call getPredicate ')
        p['sy']['getPredicate'](p)
        logg('after getPredicate')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFEntry-1 processing verb ( getObject ) ')
    if (r == p['OK']):
        logg('call getObject ')
        p['sy']['getObject'](p)
        logg('after getObject')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFEntry-1 processing verb ( writeTuple ) ')
    if (r == p['OK']):
        logg('call writeTuple ')
        p['sy']['writeTuple'](p)
        logg('after writeTuple')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for RDFEntry-1 processing verb ( tail. ) ')
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
    logg('final RDFEntry_1')
#end RDFEntry_1

def RDFEntry (x):
    global p
    logg('begin RDFEntry')
    ## point of umbrella
    RDFEntryCtl = 1 # starting spoke
    while RDFEntryCtl != 0:
        logg('loop RDFEntryCtl = ' + RDFEntryCtl.__str__())
        if (RDFEntryCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (RDFEntryCtl == 1):
            logg('call RDFEntry_1')
            RDFEntry_1()
            logg('after call RDFEntry_1')
            # test and adjust for new spoke
            RDFEntryCtl = chk(RDFEntryCtl)

        else:
            #final
            logg('final RDFEntry')    
            RDFEntryCtl = 0 # break
        #endif
    #wend
#end RDFEntry

def getSubject_1():
    global p
    logg('getSubject_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getSubject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-1 processing verb ( ... ) ')
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
    logg('final getSubject_1')
#end getSubject_1

def getSubject_2():
    global p
    logg('getSubject_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getSubject-2 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-2 processing verb ( ==( ) ')
    if (r == p['OK']):
        logg('call ==( ')
        p['sy']['==('](p)
        logg('after ==(')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-2 processing verb ( complexSubject ) ')
    if (r == p['OK']):
        logg('call complexSubject ')
        p['sy']['complexSubject'](p)
        logg('after complexSubject')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final getSubject_2')
#end getSubject_2

def getSubject_3():
    global p
    logg('getSubject_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getSubject-3 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-3 processing text ')
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
    logg('for getSubject-3 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final getSubject_3')
#end getSubject_3

def getSubject (x):
    global p
    logg('begin getSubject')
    ## point of umbrella
    getSubjectCtl = 1 # starting spoke
    while getSubjectCtl != 0:
        logg('loop getSubjectCtl = ' + getSubjectCtl.__str__())
        if (getSubjectCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (getSubjectCtl == 1):
            logg('call getSubject_1')
            getSubject_1()
            logg('after call getSubject_1')
            # test and adjust for new spoke
            getSubjectCtl = chk(getSubjectCtl)

        elif (getSubjectCtl == 2):
            logg('call getSubject_2')
            getSubject_2()
            logg('after call getSubject_2')
            # test and adjust for new spoke
            getSubjectCtl = chk(getSubjectCtl)

        elif (getSubjectCtl == 3):
            logg('call getSubject_3')
            getSubject_3()
            logg('after call getSubject_3')
            # test and adjust for new spoke
            getSubjectCtl = chk(getSubjectCtl)

        else:
            #final
            logg('final getSubject')    
            getSubjectCtl = 0 # break
        #endif
    #wend
#end getSubject

def complexSubject_1():
    global p
    logg('complexSubject_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing text ')
    logg("""s-subject""")
    if (r == p['OK']):
        logg('push text ' + """s-subject""")
        datPush("s-subject")
        logg('after ' + """s-subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing text ')
    logg("""s-predicate""")
    if (r == p['OK']):
        logg('push text ' + """s-predicate""")
        datPush("s-predicate")
        logg('after ' + """s-predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing text ')
    logg("""s-object""")
    if (r == p['OK']):
        logg('push text ' + """s-object""")
        datPush("s-object")
        logg('after ' + """s-object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( drop ) ')
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
    logg('final complexSubject_1')
#end complexSubject_1

def complexSubject (x):
    global p
    logg('begin complexSubject')
    ## point of umbrella
    complexSubjectCtl = 1 # starting spoke
    while complexSubjectCtl != 0:
        logg('loop complexSubjectCtl = ' + complexSubjectCtl.__str__())
        if (complexSubjectCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (complexSubjectCtl == 1):
            logg('call complexSubject_1')
            complexSubject_1()
            logg('after call complexSubject_1')
            # test and adjust for new spoke
            complexSubjectCtl = chk(complexSubjectCtl)

        else:
            #final
            logg('final complexSubject')    
            complexSubjectCtl = 0 # break
        #endif
    #wend
#end complexSubject

def getPredicate_1():
    global p
    logg('getPredicate_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getPredicate-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-1 processing verb ( ... ) ')
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
    logg('final getPredicate_1')
#end getPredicate_1

def getPredicate_2():
    global p
    logg('getPredicate_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getPredicate-2 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-2 processing verb ( ==( ) ')
    if (r == p['OK']):
        logg('call ==( ')
        p['sy']['==('](p)
        logg('after ==(')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-2 processing verb ( complexPredicate ) ')
    if (r == p['OK']):
        logg('call complexPredicate ')
        p['sy']['complexPredicate'](p)
        logg('after complexPredicate')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final getPredicate_2')
#end getPredicate_2

def getPredicate_3():
    global p
    logg('getPredicate_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getPredicate-3 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-3 processing text ')
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
    logg('for getPredicate-3 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final getPredicate_3')
#end getPredicate_3

def getPredicate (x):
    global p
    logg('begin getPredicate')
    ## point of umbrella
    getPredicateCtl = 1 # starting spoke
    while getPredicateCtl != 0:
        logg('loop getPredicateCtl = ' + getPredicateCtl.__str__())
        if (getPredicateCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (getPredicateCtl == 1):
            logg('call getPredicate_1')
            getPredicate_1()
            logg('after call getPredicate_1')
            # test and adjust for new spoke
            getPredicateCtl = chk(getPredicateCtl)

        elif (getPredicateCtl == 2):
            logg('call getPredicate_2')
            getPredicate_2()
            logg('after call getPredicate_2')
            # test and adjust for new spoke
            getPredicateCtl = chk(getPredicateCtl)

        elif (getPredicateCtl == 3):
            logg('call getPredicate_3')
            getPredicate_3()
            logg('after call getPredicate_3')
            # test and adjust for new spoke
            getPredicateCtl = chk(getPredicateCtl)

        else:
            #final
            logg('final getPredicate')    
            getPredicateCtl = 0 # break
        #endif
    #wend
#end getPredicate

def complexPredicate_1():
    global p
    logg('complexPredicate_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing text ')
    logg("""p-subject""")
    if (r == p['OK']):
        logg('push text ' + """p-subject""")
        datPush("p-subject")
        logg('after ' + """p-subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing text ')
    logg("""p-predicate""")
    if (r == p['OK']):
        logg('push text ' + """p-predicate""")
        datPush("p-predicate")
        logg('after ' + """p-predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing text ')
    logg("""p-object""")
    if (r == p['OK']):
        logg('push text ' + """p-object""")
        datPush("p-object")
        logg('after ' + """p-object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( drop ) ')
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
    logg('final complexPredicate_1')
#end complexPredicate_1

def complexPredicate (x):
    global p
    logg('begin complexPredicate')
    ## point of umbrella
    complexPredicateCtl = 1 # starting spoke
    while complexPredicateCtl != 0:
        logg('loop complexPredicateCtl = ' + complexPredicateCtl.__str__())
        if (complexPredicateCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (complexPredicateCtl == 1):
            logg('call complexPredicate_1')
            complexPredicate_1()
            logg('after call complexPredicate_1')
            # test and adjust for new spoke
            complexPredicateCtl = chk(complexPredicateCtl)

        else:
            #final
            logg('final complexPredicate')    
            complexPredicateCtl = 0 # break
        #endif
    #wend
#end complexPredicate

def getObject_1():
    global p
    logg('getObject_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getObject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-1 processing verb ( ... ) ')
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
    logg('final getObject_1')
#end getObject_1

def getObject_2():
    global p
    logg('getObject_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getObject-2 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-2 processing verb ( ==( ) ')
    if (r == p['OK']):
        logg('call ==( ')
        p['sy']['==('](p)
        logg('after ==(')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-2 processing verb ( complexObject ) ')
    if (r == p['OK']):
        logg('call complexObject ')
        p['sy']['complexObject'](p)
        logg('after complexObject')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final getObject_2')
#end getObject_2

def getObject_3():
    global p
    logg('getObject_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getObject-3 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-3 processing text ')
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
    logg('for getObject-3 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final getObject_3')
#end getObject_3

def getObject (x):
    global p
    logg('begin getObject')
    ## point of umbrella
    getObjectCtl = 1 # starting spoke
    while getObjectCtl != 0:
        logg('loop getObjectCtl = ' + getObjectCtl.__str__())
        if (getObjectCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (getObjectCtl == 1):
            logg('call getObject_1')
            getObject_1()
            logg('after call getObject_1')
            # test and adjust for new spoke
            getObjectCtl = chk(getObjectCtl)

        elif (getObjectCtl == 2):
            logg('call getObject_2')
            getObject_2()
            logg('after call getObject_2')
            # test and adjust for new spoke
            getObjectCtl = chk(getObjectCtl)

        elif (getObjectCtl == 3):
            logg('call getObject_3')
            getObject_3()
            logg('after call getObject_3')
            # test and adjust for new spoke
            getObjectCtl = chk(getObjectCtl)

        else:
            #final
            logg('final getObject')    
            getObjectCtl = 0 # break
        #endif
    #wend
#end getObject

def complexObject_1():
    global p
    logg('complexObject_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing text ')
    logg("""o-subject""")
    if (r == p['OK']):
        logg('push text ' + """o-subject""")
        datPush("o-subject")
        logg('after ' + """o-subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing text ')
    logg("""o-predicate""")
    if (r == p['OK']):
        logg('push text ' + """o-predicate""")
        datPush("o-predicate")
        logg('after ' + """o-predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing text ')
    logg("""o-object""")
    if (r == p['OK']):
        logg('push text ' + """o-object""")
        datPush("o-object")
        logg('after ' + """o-object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( save ) ')
    if (r == p['OK']):
        logg('call save ')
        p['sy']['save'](p)
        logg('after save')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( getToken ) ')
    if (r == p['OK']):
        logg('call getToken ')
        p['sy']['getToken'](p)
        logg('after getToken')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( token ) ')
    if (r == p['OK']):
        logg('call token ')
        p['sy']['token'](p)
        logg('after token')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( drop ) ')
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
    logg('final complexObject_1')
#end complexObject_1

def complexObject (x):
    global p
    logg('begin complexObject')
    ## point of umbrella
    complexObjectCtl = 1 # starting spoke
    while complexObjectCtl != 0:
        logg('loop complexObjectCtl = ' + complexObjectCtl.__str__())
        if (complexObjectCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (complexObjectCtl == 1):
            logg('call complexObject_1')
            complexObject_1()
            logg('after call complexObject_1')
            # test and adjust for new spoke
            complexObjectCtl = chk(complexObjectCtl)

        else:
            #final
            logg('final complexObject')    
            complexObjectCtl = 0 # break
        #endif
    #wend
#end complexObject

def writeTuple_1():
    global p
    logg('writeTuple_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( gennx ) ')
    if (r == p['OK']):
        logg('call gennx ')
        p['sy']['gennx'](p)
        logg('after gennx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""ID""")
    if (r == p['OK']):
        logg('push text ' + """ID""")
        datPush("ID")
        logg('after ' + """ID""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( ! ) ')
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
    logg('for writeTuple-1 processing text ')
    logg("""Update stage ( ID = '""")
    if (r == p['OK']):
        logg('push text ' + """Update stage ( ID = '""")
        datPush("Update stage ( ID = '")
        logg('after ' + """Update stage ( ID = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""ID""")
    if (r == p['OK']):
        logg('push text ' + """ID""")
        datPush("ID")
        logg('after ' + """ID""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", subject = '""")
    if (r == p['OK']):
        logg('push text ' + """, subject = '""")
        datPush(", subject = '")
        logg('after ' + """, subject = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", s-subject = '""")
    if (r == p['OK']):
        logg('push text ' + """, s-subject = '""")
        datPush(", s-subject = '")
        logg('after ' + """, s-subject = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""s-subject""")
    if (r == p['OK']):
        logg('push text ' + """s-subject""")
        datPush("s-subject")
        logg('after ' + """s-subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", s-predicate = '""")
    if (r == p['OK']):
        logg('push text ' + """, s-predicate = '""")
        datPush(", s-predicate = '")
        logg('after ' + """, s-predicate = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""s-predicate""")
    if (r == p['OK']):
        logg('push text ' + """s-predicate""")
        datPush("s-predicate")
        logg('after ' + """s-predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", s-object = '""")
    if (r == p['OK']):
        logg('push text ' + """, s-object = '""")
        datPush(", s-object = '")
        logg('after ' + """, s-object = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""s-object""")
    if (r == p['OK']):
        logg('push text ' + """s-object""")
        datPush("s-object")
        logg('after ' + """s-object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", predicate = '""")
    if (r == p['OK']):
        logg('push text ' + """, predicate = '""")
        datPush(", predicate = '")
        logg('after ' + """, predicate = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", p-subject = '""")
    if (r == p['OK']):
        logg('push text ' + """, p-subject = '""")
        datPush(", p-subject = '")
        logg('after ' + """, p-subject = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""p-subject""")
    if (r == p['OK']):
        logg('push text ' + """p-subject""")
        datPush("p-subject")
        logg('after ' + """p-subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", p-predicate = '""")
    if (r == p['OK']):
        logg('push text ' + """, p-predicate = '""")
        datPush(", p-predicate = '")
        logg('after ' + """, p-predicate = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""p-predicate""")
    if (r == p['OK']):
        logg('push text ' + """p-predicate""")
        datPush("p-predicate")
        logg('after ' + """p-predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", p-object = '""")
    if (r == p['OK']):
        logg('push text ' + """, p-object = '""")
        datPush(", p-object = '")
        logg('after ' + """, p-object = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""p-object""")
    if (r == p['OK']):
        logg('push text ' + """p-object""")
        datPush("p-object")
        logg('after ' + """p-object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", object = '""")
    if (r == p['OK']):
        logg('push text ' + """, object = '""")
        datPush(", object = '")
        logg('after ' + """, object = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", o-subject = '""")
    if (r == p['OK']):
        logg('push text ' + """, o-subject = '""")
        datPush(", o-subject = '")
        logg('after ' + """, o-subject = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""o-subject""")
    if (r == p['OK']):
        logg('push text ' + """o-subject""")
        datPush("o-subject")
        logg('after ' + """o-subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", o-predicate = '""")
    if (r == p['OK']):
        logg('push text ' + """, o-predicate = '""")
        datPush(", o-predicate = '")
        logg('after ' + """, o-predicate = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""o-predicate""")
    if (r == p['OK']):
        logg('push text ' + """o-predicate""")
        datPush("o-predicate")
        logg('after ' + """o-predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""", o-object = '""")
    if (r == p['OK']):
        logg('push text ' + """, o-object = '""")
        datPush(", o-object = '")
        logg('after ' + """, o-object = '""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing text ')
    logg("""o-object""")
    if (r == p['OK']):
        logg('push text ' + """o-object""")
        datPush("o-object")
        logg('after ' + """o-object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( @ ) ')
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
    logg('for writeTuple-1 processing verb ( cat ) ')
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
    logg('for writeTuple-1 processing text ')
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
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing text ')
    logg(""") ; """)
    if (r == p['OK']):
        logg('push text ' + """) ; """)
        datPush(") ; ")
        logg('after ' + """) ; """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeTuple-1 processing verb ( cats ) ')
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
    logg('for writeTuple-1 processing verb ( .s ) ')
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
    logg('for writeTuple-1 processing verb ( clearAll ) ')
    if (r == p['OK']):
        logg('call clearAll ')
        p['sy']['clearAll'](p)
        logg('after clearAll')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final writeTuple_1')
#end writeTuple_1

def writeTuple (x):
    global p
    logg('begin writeTuple')
    ## point of umbrella
    writeTupleCtl = 1 # starting spoke
    while writeTupleCtl != 0:
        logg('loop writeTupleCtl = ' + writeTupleCtl.__str__())
        if (writeTupleCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (writeTupleCtl == 1):
            logg('call writeTuple_1')
            writeTuple_1()
            logg('after call writeTuple_1')
            # test and adjust for new spoke
            writeTupleCtl = chk(writeTupleCtl)

        else:
            #final
            logg('final writeTuple')    
            writeTupleCtl = 0 # break
        #endif
    #wend
#end writeTuple

def save_1():
    global p
    logg('save_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for save-1 processing verb ( ! ) ')
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
    logg('final save_1')
#end save_1

def save (x):
    global p
    logg('begin save')
    ## point of umbrella
    saveCtl = 1 # starting spoke
    while saveCtl != 0:
        logg('loop saveCtl = ' + saveCtl.__str__())
        if (saveCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (saveCtl == 1):
            logg('call save_1')
            save_1()
            logg('after call save_1')
            # test and adjust for new spoke
            saveCtl = chk(saveCtl)

        else:
            #final
            logg('final save')    
            saveCtl = 0 # break
        #endif
    #wend
#end save

def getToken_1():
    global p
    logg('getToken_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getToken-1 processing verb ( Sword ) ')
    if (r == p['OK']):
        logg('call Sword ')
        p['sy']['Sword'](p)
        logg('after Sword')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getToken-1 processing text ')
    logg("""token""")
    if (r == p['OK']):
        logg('push text ' + """token""")
        datPush("token")
        logg('after ' + """token""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getToken-1 processing verb ( ! ) ')
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
    logg('final getToken_1')
#end getToken_1

def getToken (x):
    global p
    logg('begin getToken')
    ## point of umbrella
    getTokenCtl = 1 # starting spoke
    while getTokenCtl != 0:
        logg('loop getTokenCtl = ' + getTokenCtl.__str__())
        if (getTokenCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (getTokenCtl == 1):
            logg('call getToken_1')
            getToken_1()
            logg('after call getToken_1')
            # test and adjust for new spoke
            getTokenCtl = chk(getTokenCtl)

        else:
            #final
            logg('final getToken')    
            getTokenCtl = 0 # break
        #endif
    #wend
#end getToken

def token_1():
    global p
    logg('token_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for token-1 processing text ')
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
    logg('for token-1 processing text ')
    logg("""token""")
    if (r == p['OK']):
        logg('push text ' + """token""")
        datPush("token")
        logg('after ' + """token""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for token-1 processing verb ( @ ) ')
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
    logg('for token-1 processing verb ( ar@ ) ')
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

    #final
    logg('final token_1')
#end token_1

def token (x):
    global p
    logg('begin token')
    ## point of umbrella
    tokenCtl = 1 # starting spoke
    while tokenCtl != 0:
        logg('loop tokenCtl = ' + tokenCtl.__str__())
        if (tokenCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (tokenCtl == 1):
            logg('call token_1')
            token_1()
            logg('after call token_1')
            # test and adjust for new spoke
            tokenCtl = chk(tokenCtl)

        else:
            #final
            logg('final token')    
            tokenCtl = 0 # break
        #endif
    #wend
#end token

def clearAll_1():
    global p
    logg('clearAll_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
    logg("""s-subject""")
    if (r == p['OK']):
        logg('push text ' + """s-subject""")
        datPush("s-subject")
        logg('after ' + """s-subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
    logg("""s-predicate""")
    if (r == p['OK']):
        logg('push text ' + """s-predicate""")
        datPush("s-predicate")
        logg('after ' + """s-predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
    logg("""s-object""")
    if (r == p['OK']):
        logg('push text ' + """s-object""")
        datPush("s-object")
        logg('after ' + """s-object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
    logg("""p-subject""")
    if (r == p['OK']):
        logg('push text ' + """p-subject""")
        datPush("p-subject")
        logg('after ' + """p-subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
    logg("""p-predicate""")
    if (r == p['OK']):
        logg('push text ' + """p-predicate""")
        datPush("p-predicate")
        logg('after ' + """p-predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
    logg("""p-object""")
    if (r == p['OK']):
        logg('push text ' + """p-object""")
        datPush("p-object")
        logg('after ' + """p-object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
    logg("""o-subject""")
    if (r == p['OK']):
        logg('push text ' + """o-subject""")
        datPush("o-subject")
        logg('after ' + """o-subject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
    logg("""o-predicate""")
    if (r == p['OK']):
        logg('push text ' + """o-predicate""")
        datPush("o-predicate")
        logg('after ' + """o-predicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('for clearAll-1 processing text ')
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
    logg('for clearAll-1 processing text ')
    logg("""o-object""")
    if (r == p['OK']):
        logg('push text ' + """o-object""")
        datPush("o-object")
        logg('after ' + """o-object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clearAll-1 processing verb ( ! ) ')
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
    logg('final clearAll_1')
#end clearAll_1

def clearAll (x):
    global p
    logg('begin clearAll')
    ## point of umbrella
    clearAllCtl = 1 # starting spoke
    while clearAllCtl != 0:
        logg('loop clearAllCtl = ' + clearAllCtl.__str__())
        if (clearAllCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (clearAllCtl == 1):
            logg('call clearAll_1')
            clearAll_1()
            logg('after call clearAll_1')
            # test and adjust for new spoke
            clearAllCtl = chk(clearAllCtl)

        else:
            #final
            logg('final clearAll')    
            clearAllCtl = 0 # break
        #endif
    #wend
#end clearAll

def initRDF_1():
    global p
    logg('initRDF_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
    logg("""RDF""")
    if (r == p['OK']):
        logg('push text ' + """RDF""")
        datPush("RDF")
        logg('after ' + """RDF""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing verb ( takeV ) ')
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
    logg('for initRDF-1 processing text ')
    logg("""SioV""")
    if (r == p['OK']):
        logg('push text ' + """SioV""")
        datPush("SioV")
        logg('after ' + """SioV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing verb ( takeV ) ')
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
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing verb ( takeV ) ')
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
    logg('final initRDF_1')
#end initRDF_1

def initRDF (x):
    global p
    logg('begin initRDF')
    ## point of umbrella
    initRDFCtl = 1 # starting spoke
    while initRDFCtl != 0:
        logg('loop initRDFCtl = ' + initRDFCtl.__str__())
        if (initRDFCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (initRDFCtl == 1):
            logg('call initRDF_1')
            initRDF_1()
            logg('after call initRDF_1')
            # test and adjust for new spoke
            initRDFCtl = chk(initRDFCtl)

        else:
            #final
            logg('final initRDF')    
            initRDFCtl = 0 # break
        #endif
    #wend
#end initRDF

# stream routines 

def EQzopz(p):
    logg ('==(')
    needle = '('
    needle = needle.upper()
    return(eqeq(needle))
#end EQzopz

def EQzopz(p):
    logg ('==(')
    needle = '('
    needle = needle.upper()
    return(eqeq(needle))
#end EQzopz

def EQzopz(p):
    logg ('==(')
    needle = '('
    needle = needle.upper()
    return(eqeq(needle))
#end EQzopz

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

    # paragraph RDFEntry
    p['sy']['RDFEntry'] = RDFEntry
    #

    # paragraph getSubject
    p['sy']['getSubject'] = getSubject
    #

    # paragraph ==(
    p['sy']['==('] = EQzopz
    #

    # paragraph complexSubject
    p['sy']['complexSubject'] = complexSubject
    #

    # paragraph getPredicate
    p['sy']['getPredicate'] = getPredicate
    #

    # paragraph ==(
    p['sy']['==('] = EQzopz
    #

    # paragraph complexPredicate
    p['sy']['complexPredicate'] = complexPredicate
    #

    # paragraph getObject
    p['sy']['getObject'] = getObject
    #

    # paragraph ==(
    p['sy']['==('] = EQzopz
    #

    # paragraph complexObject
    p['sy']['complexObject'] = complexObject
    #

    # paragraph writeTuple
    p['sy']['writeTuple'] = writeTuple
    #

    # paragraph save
    p['sy']['save'] = save
    #

    # paragraph getToken
    p['sy']['getToken'] = getToken
    #

    # paragraph token
    p['sy']['token'] = token
    #

    # paragraph clearAll
    p['sy']['clearAll'] = clearAll
    #

    # paragraph initRDF
    p['sy']['initRDF'] = initRDF
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

