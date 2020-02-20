
#file s2020.py
#generated for smartRDF.basii at Sun Feb 16 06:29:52 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def Rmain_1():
    global p
    logg('Rmain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Rmain-1 processing verb ( initRDF ) ')
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
    logg('for Rmain-1 processing verb ( Rmain2 ) ')
    if (r == p['OK']):
        logg('call Rmain2 ')
        p['sy']['Rmain2'](p)
        logg('after Rmain2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Rmain_1')
#end Rmain_1

def Rmain (x):
    global p
    logg('begin Rmain')
    ## point of umbrella
    RmainCtl = 1 # starting spoke
    while RmainCtl != 0:
        logg('loop RmainCtl = ' + RmainCtl.__str__())
        if (RmainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (RmainCtl == 1):
            logg('call Rmain_1')
            Rmain_1()
            logg('after call Rmain_1')
            # test and adjust for new spoke
            RmainCtl = chk(RmainCtl)

        else:
            #final
            logg('final Rmain')    
            RmainCtl = 0 # break
        #endif
    #wend
#end Rmain

def Rmain2_1():
    global p
    logg('Rmain2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Rmain2-1 processing verb ( t0 ) ')
    if (r == p['OK']):
        logg('call t0 ')
        p['sy']['t0'](p)
        logg('after t0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Rmain2-1 processing verb ( getSubject ) ')
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
    logg('for Rmain2-1 processing text ')
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
    logg('for Rmain2-1 processing verb ( @ ) ')
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
    logg('for Rmain2-1 processing text ')
    logg("""done""")
    if (r == p['OK']):
        logg('push text ' + """done""")
        datPush("done")
        logg('after ' + """done""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Rmain2-1 processing verb ( = ) ')
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
    logg('for Rmain2-1 processing verb ( wait ) ')
    if (r == p['OK']):
        logg('call wait ')
        p['sy']['wait'](p)
        logg('after wait')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Rmain2_1')
#end Rmain2_1

def Rmain2_2():
    global p
    logg('Rmain2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Rmain2-2 processing verb ( getPredicate ) ')
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
    logg('for Rmain2-2 processing verb ( getObject ) ')
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
    logg('for Rmain2-2 processing verb ( tail. ) ')
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
    logg('final Rmain2_2')
#end Rmain2_2

def Rmain2 (x):
    global p
    logg('begin Rmain2')
    ## point of umbrella
    Rmain2Ctl = 1 # starting spoke
    while Rmain2Ctl != 0:
        logg('loop Rmain2Ctl = ' + Rmain2Ctl.__str__())
        if (Rmain2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (Rmain2Ctl == 1):
            logg('call Rmain2_1')
            Rmain2_1()
            logg('after call Rmain2_1')
            # test and adjust for new spoke
            Rmain2Ctl = chk(Rmain2Ctl)

        elif (Rmain2Ctl == 2):
            logg('call Rmain2_2')
            Rmain2_2()
            logg('after call Rmain2_2')
            # test and adjust for new spoke
            Rmain2Ctl = chk(Rmain2Ctl)

        else:
            #final
            logg('final Rmain2')    
            Rmain2Ctl = 0 # break
        #endif
    #wend
#end Rmain2

def initRDF_1():
    global p
    logg('initRDF_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
    logg("""tempNDSV""")
    if (r == p['OK']):
        logg('push text ' + """tempNDSV""")
        datPush("tempNDSV")
        logg('after ' + """tempNDSV""" )
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

    r = p['sy']['pop']()
    logg('for initRDF-1 processing verb ( dr0 ) ')
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
    logg('for initRDF-1 processing verb ( ! ) ')
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
    logg('for initRDF-1 processing verb ( ch0 ) ')
    if (r == p['OK']):
        logg('call ch0 ')
        p['sy']['ch0'](p)
        logg('after ch0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing text ')
    logg("""thing""")
    if (r == p['OK']):
        logg('push text ' + """thing""")
        datPush("thing")
        logg('after ' + """thing""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
    logg("""thing""")
    if (r == p['OK']):
        logg('push text ' + """thing""")
        datPush("thing")
        logg('after ' + """thing""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

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
    logg('for initRDF-1 processing verb ( @ ) ')
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
    logg('for initRDF-1 processing verb ( drvx ) ')
    if (r == p['OK']):
        logg('call drvx ')
        p['sy']['drvx'](p)
        logg('after drvx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

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
    logg('for initRDF-1 processing verb ( ! ) ')
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
    logg('for initRDF-1 processing verb ( ch0 ) ')
    if (r == p['OK']):
        logg('call ch0 ')
        p['sy']['ch0'](p)
        logg('after ch0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing text ')
    logg("""has""")
    if (r == p['OK']):
        logg('push text ' + """has""")
        datPush("has")
        logg('after ' + """has""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing verb ( @ ) ')
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
    logg('for initRDF-1 processing verb ( drvx ) ')
    if (r == p['OK']):
        logg('call drvx ')
        p['sy']['drvx'](p)
        logg('after drvx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

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
    logg('for initRDF-1 processing verb ( ! ) ')
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
    logg('for initRDF-1 processing verb ( ch0 ) ')
    if (r == p['OK']):
        logg('call ch0 ')
        p['sy']['ch0'](p)
        logg('after ch0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing text ')
    logg("""gets""")
    if (r == p['OK']):
        logg('push text ' + """gets""")
        datPush("gets")
        logg('after ' + """gets""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing verb ( @ ) ')
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
    logg('for initRDF-1 processing verb ( drvx ) ')
    if (r == p['OK']):
        logg('call drvx ')
        p['sy']['drvx'](p)
        logg('after drvx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

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
    logg('for initRDF-1 processing verb ( ! ) ')
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
    logg('for initRDF-1 processing verb ( ch0 ) ')
    if (r == p['OK']):
        logg('call ch0 ')
        p['sy']['ch0'](p)
        logg('after ch0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing text ')
    logg("""collision""")
    if (r == p['OK']):
        logg('push text ' + """collision""")
        datPush("collision")
        logg('after ' + """collision""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

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
    logg('for initRDF-1 processing verb ( @ ) ')
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
    logg('for initRDF-1 processing verb ( drvx ) ')
    if (r == p['OK']):
        logg('call drvx ')
        p['sy']['drvx'](p)
        logg('after drvx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

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
    logg('for initRDF-1 processing verb ( ! ) ')
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
    logg('for initRDF-1 processing verb ( ch0 ) ')
    if (r == p['OK']):
        logg('call ch0 ')
        p['sy']['ch0'](p)
        logg('after ch0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing text ')
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
    logg('for initRDF-1 processing text ')
    logg("""statement""")
    if (r == p['OK']):
        logg('push text ' + """statement""")
        datPush("statement")
        logg('after ' + """statement""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

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
    logg('for initRDF-1 processing verb ( @ ) ')
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
    logg('for initRDF-1 processing verb ( drvx ) ')
    if (r == p['OK']):
        logg('call drvx ')
        p['sy']['drvx'](p)
        logg('after drvx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

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
    logg('for initRDF-1 processing verb ( ! ) ')
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

def getSubject_1():
    global p
    logg('getSubject_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getSubject-1 processing text ')
    logg("""subject """)
    if (r == p['OK']):
        logg('push text ' + """subject """)
        datPush("subject ")
        logg('after ' + """subject """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-1 processing verb ( ask ) ')
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
    logg('for getSubject-1 processing text ')
    logg("""tsubject""")
    if (r == p['OK']):
        logg('push text ' + """tsubject""")
        datPush("tsubject")
        logg('after ' + """tsubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
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
    logg('for getSubject-2 processing text ')
    logg("""tsubject""")
    if (r == p['OK']):
        logg('push text ' + """tsubject""")
        datPush("tsubject")
        logg('after ' + """tsubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-2 processing verb ( t@ ) ')
    if (r == p['OK']):
        logg('call t@ ')
        p['sy']['t@'](p)
        logg('after t@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-2 processing verb ( word ) ')
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
    logg('for getSubject-2 processing text ')
    logg("""(""")
    if (r == p['OK']):
        logg('push text ' + """(""")
        datPush("(")
        logg('after ' + """(""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-2 processing verb ( = ) ')
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
    logg('for getSubject-3 processing text ')
    logg("""tsubject""")
    if (r == p['OK']):
        logg('push text ' + """tsubject""")
        datPush("tsubject")
        logg('after ' + """tsubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getSubject-3 processing verb ( t@ ) ')
    if (r == p['OK']):
        logg('call t@ ')
        p['sy']['t@'](p)
        logg('after t@')
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
    logg('for getSubject-3 processing verb ( ! ) ')
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
    logg('for complexSubject-1 processing verb ( word ) ')
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
    logg('for complexSubject-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( word ) ')
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
    logg('for complexSubject-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( word ) ')
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
    logg('for complexSubject-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
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

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( ch0 ) ')
    if (r == p['OK']):
        logg('call ch0 ')
        p['sy']['ch0'](p)
        logg('after ch0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing text ')
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
    logg('for complexSubject-1 processing text ')
    logg("""tsubject""")
    if (r == p['OK']):
        logg('push text ' + """tsubject""")
        datPush("tsubject")
        logg('after ' + """tsubject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing verb ( t@ ) ')
    if (r == p['OK']):
        logg('call t@ ')
        p['sy']['t@'](p)
        logg('after t@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing text ')
    logg("""thing""")
    if (r == p['OK']):
        logg('push text ' + """thing""")
        datPush("thing")
        logg('after ' + """thing""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing text ')
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
    logg('for complexSubject-1 processing verb ( @ ) ')
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
    logg('for complexSubject-1 processing verb ( drvx ) ')
    if (r == p['OK']):
        logg('call drvx ')
        p['sy']['drvx'](p)
        logg('after drvx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexSubject-1 processing text ')
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
    logg('for complexSubject-1 processing verb ( ! ) ')
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
    logg('for getPredicate-1 processing text ')
    logg("""predicate """)
    if (r == p['OK']):
        logg('push text ' + """predicate """)
        datPush("predicate ")
        logg('after ' + """predicate """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-1 processing verb ( ask ) ')
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
    logg('for getPredicate-1 processing text ')
    logg("""tpredicate""")
    if (r == p['OK']):
        logg('push text ' + """tpredicate""")
        datPush("tpredicate")
        logg('after ' + """tpredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
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
    logg('for getPredicate-2 processing text ')
    logg("""tpredicate""")
    if (r == p['OK']):
        logg('push text ' + """tpredicate""")
        datPush("tpredicate")
        logg('after ' + """tpredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-2 processing verb ( t@ ) ')
    if (r == p['OK']):
        logg('call t@ ')
        p['sy']['t@'](p)
        logg('after t@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-2 processing verb ( word ) ')
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
    logg('for getPredicate-2 processing text ')
    logg("""(""")
    if (r == p['OK']):
        logg('push text ' + """(""")
        datPush("(")
        logg('after ' + """(""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-2 processing verb ( = ) ')
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
    logg('for getPredicate-3 processing text ')
    logg("""tpredicate""")
    if (r == p['OK']):
        logg('push text ' + """tpredicate""")
        datPush("tpredicate")
        logg('after ' + """tpredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getPredicate-3 processing verb ( t@ ) ')
    if (r == p['OK']):
        logg('call t@ ')
        p['sy']['t@'](p)
        logg('after t@')
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
    logg('for getPredicate-3 processing verb ( ! ) ')
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
    logg('for complexPredicate-1 processing verb ( word ) ')
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
    logg('for complexPredicate-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( word ) ')
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
    logg('for complexPredicate-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( word ) ')
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
    logg('for complexPredicate-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
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

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( ch0 ) ')
    if (r == p['OK']):
        logg('call ch0 ')
        p['sy']['ch0'](p)
        logg('after ch0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing text ')
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
    logg('for complexPredicate-1 processing text ')
    logg("""tpredicate""")
    if (r == p['OK']):
        logg('push text ' + """tpredicate""")
        datPush("tpredicate")
        logg('after ' + """tpredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing verb ( t@ ) ')
    if (r == p['OK']):
        logg('call t@ ')
        p['sy']['t@'](p)
        logg('after t@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing text ')
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
    logg('for complexPredicate-1 processing text ')
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
    logg('for complexPredicate-1 processing verb ( @ ) ')
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
    logg('for complexPredicate-1 processing verb ( drvx ) ')
    if (r == p['OK']):
        logg('call drvx ')
        p['sy']['drvx'](p)
        logg('after drvx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexPredicate-1 processing text ')
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
    logg('for complexPredicate-1 processing verb ( ! ) ')
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
    logg('for getObject-1 processing text ')
    logg("""Object """)
    if (r == p['OK']):
        logg('push text ' + """Object """)
        datPush("Object ")
        logg('after ' + """Object """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-1 processing verb ( ask ) ')
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
    logg('for getObject-1 processing text ')
    logg("""tObject""")
    if (r == p['OK']):
        logg('push text ' + """tObject""")
        datPush("tObject")
        logg('after ' + """tObject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
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
    logg('for getObject-2 processing text ')
    logg("""tObject""")
    if (r == p['OK']):
        logg('push text ' + """tObject""")
        datPush("tObject")
        logg('after ' + """tObject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-2 processing verb ( t@ ) ')
    if (r == p['OK']):
        logg('call t@ ')
        p['sy']['t@'](p)
        logg('after t@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-2 processing verb ( word ) ')
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
    logg('for getObject-2 processing text ')
    logg("""(""")
    if (r == p['OK']):
        logg('push text ' + """(""")
        datPush("(")
        logg('after ' + """(""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-2 processing verb ( = ) ')
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
    logg('for getObject-3 processing text ')
    logg("""tObject""")
    if (r == p['OK']):
        logg('push text ' + """tObject""")
        datPush("tObject")
        logg('after ' + """tObject""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-3 processing verb ( t@ ) ')
    if (r == p['OK']):
        logg('call t@ ')
        p['sy']['t@'](p)
        logg('after t@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-3 processing text ')
    logg("""Object""")
    if (r == p['OK']):
        logg('push text ' + """Object""")
        datPush("Object")
        logg('after ' + """Object""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getObject-3 processing verb ( ! ) ')
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
    logg('for getObject-3 processing verb ( wait ) ')
    if (r == p['OK']):
        logg('call wait ')
        p['sy']['wait'](p)
        logg('after wait')
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
    logg('for complexObject-1 processing verb ( word ) ')
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
    logg('for complexObject-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( word ) ')
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
    logg('for complexObject-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( word ) ')
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
    logg('for complexObject-1 processing verb ( t! ) ')
    if (r == p['OK']):
        logg('call t! ')
        p['sy']['t!'](p)
        logg('after t!')
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

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( ch0 ) ')
    if (r == p['OK']):
        logg('call ch0 ')
        p['sy']['ch0'](p)
        logg('after ch0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing text ')
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
    logg('for complexObject-1 processing text ')
    logg("""tpredicate""")
    if (r == p['OK']):
        logg('push text ' + """tpredicate""")
        datPush("tpredicate")
        logg('after ' + """tpredicate""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing verb ( t@ ) ')
    if (r == p['OK']):
        logg('call t@ ')
        p['sy']['t@'](p)
        logg('after t@')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing text ')
    logg("""thing""")
    if (r == p['OK']):
        logg('push text ' + """thing""")
        datPush("thing")
        logg('after ' + """thing""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing text ')
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
    logg('for complexObject-1 processing verb ( @ ) ')
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
    logg('for complexObject-1 processing verb ( drvx ) ')
    if (r == p['OK']):
        logg('call drvx ')
        p['sy']['drvx'](p)
        logg('after drvx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for complexObject-1 processing text ')
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
    logg('for complexObject-1 processing verb ( ! ) ')
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
    logg('for complexObject-1 processing verb ( wait ) ')
    if (r == p['OK']):
        logg('call wait ')
        p['sy']['wait'](p)
        logg('after wait')
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

def wait_1():
    global p
    logg('wait_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for wait-1 processing verb ( .t ) ')
    if (r == p['OK']):
        logg('call .t ')
        p['sy']['.t'](p)
        logg('after .t')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for wait-1 processing verb ( dumpNDS ) ')
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
    logg('for wait-1 processing verb ( .s ) ')
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
    logg('for wait-1 processing text ')
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
    logg('for wait-1 processing verb ( ask ) ')
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
    logg('final wait_1')
#end wait_1

def wait (x):
    global p
    logg('begin wait')
    ## point of umbrella
    waitCtl = 1 # starting spoke
    while waitCtl != 0:
        logg('loop waitCtl = ' + waitCtl.__str__())
        if (waitCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (waitCtl == 1):
            logg('call wait_1')
            wait_1()
            logg('after call wait_1')
            # test and adjust for new spoke
            waitCtl = chk(waitCtl)

        else:
            #final
            logg('final wait')    
            waitCtl = 0 # break
        #endif
    #wend
#end wait

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

    # paragraph Rmain
    p['sy']['Rmain'] = Rmain
    #

    # paragraph Rmain2
    p['sy']['Rmain2'] = Rmain2
    #

    # paragraph initRDF
    p['sy']['initRDF'] = initRDF
    #

    # paragraph getSubject
    p['sy']['getSubject'] = getSubject
    #

    # paragraph complexSubject
    p['sy']['complexSubject'] = complexSubject
    #

    # paragraph getPredicate
    p['sy']['getPredicate'] = getPredicate
    #

    # paragraph complexPredicate
    p['sy']['complexPredicate'] = complexPredicate
    #

    # paragraph getObject
    p['sy']['getObject'] = getObject
    #

    # paragraph complexObject
    p['sy']['complexObject'] = complexObject
    #

    # paragraph wait
    p['sy']['wait'] = wait
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

