
#file smartRDFX.py
#generated for smartRDF.basii 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def RDFMain_1():
    global p
    logg('RDFMain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- script file -- ') 
    if (r == p['OK']):
        logg('push text script file ')
        datPush("script file")
        logg('after script file ')
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
    logg('processing text -- scriptF -- ') 
    if (r == p['OK']):
        logg('push text scriptF ')
        datPush("scriptF")
        logg('after scriptF ')
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
    logg('processing verb ( initIOI ) ')
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
    logg('final RDFMain_1')
#end RDFMain_1

def RDFMain_2():
    global p
    logg('RDFMain_2')
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
    logg('final RDFMain_2')
#end RDFMain_2

def RDFMain_3():
    global p
    logg('RDFMain_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing verb ( ==RDF ) ')
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
    logg('processing verb ( getSubject ) ')
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
    logg('processing text -- predicate -- ') 
    if (r == p['OK']):
        logg('push text predicate ')
        datPush("predicate")
        logg('after predicate ')
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
    logg('processing verb ( getObject ) ')
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
    logg('processing verb ( act1 ) ')
    if (r == p['OK']):
        logg('call act1 ')
        p['sy']['act1'](p)
        logg('after act1')
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
    logg('final RDFMain_3')
#end RDFMain_3

def RDFMain_4():
    global p
    logg('RDFMain_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- error at main  -- ') 
    if (r == p['OK']):
        logg('push text error at main  ')
        datPush("error at main ")
        logg('after error at main  ')
        datPush(p['OK'])
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('processing verb ( abort ) ')
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
    logg('final RDFMain_4')
#end RDFMain_4

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

        elif (RDFMainCtl == 2):
            logg('call RDFMain_2')
            RDFMain_2()
            logg('after call RDFMain_2')
            # test and adjust for new spoke
            RDFMainCtl = chk(RDFMainCtl)

        elif (RDFMainCtl == 3):
            logg('call RDFMain_3')
            RDFMain_3()
            logg('after call RDFMain_3')
            # test and adjust for new spoke
            RDFMainCtl = chk(RDFMainCtl)

        elif (RDFMainCtl == 4):
            logg('call RDFMain_4')
            RDFMain_4()
            logg('after call RDFMain_4')
            # test and adjust for new spoke
            RDFMainCtl = chk(RDFMainCtl)

        else:
            #final
            logg('final RDFMain')    
            RDFMainCtl = 0 # break
        #endif
    #wend
#end RDFMain

def getSubject_1():
    global p
    logg('getSubject_1')
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
    logg('final getSubject_1')
#end getSubject_1

def getSubject_2():
    global p
    logg('getSubject_2')
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
    logg('processing verb ( ==( ) ')
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
    logg('processing verb ( complexSubject ) ')
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

    #final
    logg('final getSubject_2')
#end getSubject_2

def getSubject_3():
    global p
    logg('getSubject_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- subject -- ') 
    if (r == p['OK']):
        logg('push text subject ')
        datPush("subject")
        logg('after subject ')
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
    logg('processing text -- subject1 -- ') 
    if (r == p['OK']):
        logg('push text subject1 ')
        datPush("subject1")
        logg('after subject1 ')
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
    logg('final complexSubject_1')
#end complexSubject_1

def complexSubject_2():
    global p
    logg('complexSubject_2')
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
    logg('processing text -- predicate1 -- ') 
    if (r == p['OK']):
        logg('push text predicate1 ')
        datPush("predicate1")
        logg('after predicate1 ')
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
    logg('final complexSubject_2')
#end complexSubject_2

def complexSubject_3():
    global p
    logg('complexSubject_3')
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
    logg('processing text -- object1 -- ') 
    if (r == p['OK']):
        logg('push text object1 ')
        datPush("object1")
        logg('after object1 ')
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

    #final
    logg('final complexSubject_3')
#end complexSubject_3

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

        elif (complexSubjectCtl == 2):
            logg('call complexSubject_2')
            complexSubject_2()
            logg('after call complexSubject_2')
            # test and adjust for new spoke
            complexSubjectCtl = chk(complexSubjectCtl)

        elif (complexSubjectCtl == 3):
            logg('call complexSubject_3')
            complexSubject_3()
            logg('after call complexSubject_3')
            # test and adjust for new spoke
            complexSubjectCtl = chk(complexSubjectCtl)

        else:
            #final
            logg('final complexSubject')    
            complexSubjectCtl = 0 # break
        #endif
    #wend
#end complexSubject

def getObject_1():
    global p
    logg('getObject_1')
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
    logg('final getObject_1')
#end getObject_1

def getObject_2():
    global p
    logg('getObject_2')
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
    logg('processing verb ( ==( ) ')
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
    logg('processing verb ( complexObject ) ')
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

    #final
    logg('final getObject_2')
#end getObject_2

def getObject_3():
    global p
    logg('getObject_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('processing text -- Object -- ') 
    if (r == p['OK']):
        logg('push text Object ')
        datPush("Object")
        logg('after Object ')
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
    logg('processing text -- subject2 -- ') 
    if (r == p['OK']):
        logg('push text subject2 ')
        datPush("subject2")
        logg('after subject2 ')
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
    logg('final complexObject_1')
#end complexObject_1

def complexObject_2():
    global p
    logg('complexObject_2')
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
    logg('processing text -- predicate2 -- ') 
    if (r == p['OK']):
        logg('push text predicate2 ')
        datPush("predicate2")
        logg('after predicate2 ')
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
    logg('final complexObject_2')
#end complexObject_2

def complexObject_3():
    global p
    logg('complexObject_3')
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
    logg('processing text -- object2 -- ') 
    if (r == p['OK']):
        logg('push text object2 ')
        datPush("object2")
        logg('after object2 ')
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

    #final
    logg('final complexObject_3')
#end complexObject_3

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

        elif (complexObjectCtl == 2):
            logg('call complexObject_2')
            complexObject_2()
            logg('after call complexObject_2')
            # test and adjust for new spoke
            complexObjectCtl = chk(complexObjectCtl)

        elif (complexObjectCtl == 3):
            logg('call complexObject_3')
            complexObject_3()
            logg('after call complexObject_3')
            # test and adjust for new spoke
            complexObjectCtl = chk(complexObjectCtl)

        else:
            #final
            logg('final complexObject')    
            complexObjectCtl = 0 # break
        #endif
    #wend
#end complexObject

def initIOI_1():
    global p
    logg('initIOI_1')
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

    #final
    logg('final initIOI_1')
#end initIOI_1

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

        else:
            #final
            logg('final initIOI')    
            initIOICtl = 0 # break
        #endif
    #wend
#end initIOI

def act1_1():
    global p
    logg('act1_1')
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

def EQzopz(p):
    logg ('==(')
    needle = '('
    needle = needle.upper()
    return(eqeq(needle))
#end EQzopz

def EQzcpz(p):
    logg ('==)')
    needle = ')'
    needle = needle.upper()
    return(eqeq(needle))
#end EQzcpz

def EQzopz(p):
    logg ('==(')
    needle = '('
    needle = needle.upper()
    return(eqeq(needle))
#end EQzopz

def EQzcpz(p):
    logg ('==)')
    needle = ')'
    needle = needle.upper()
    return(eqeq(needle))
#end EQzcpz

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
    p['sy']['pop'] = datPop
    p['sy']['push'] = datPush
    p['sy']['dump'] = dump
    p['sy']['.s'] = dots
    prepSy()
    p['OK'] = 'pOK'
    p['NOK'] = 'pNOK'

    # paragraph RDFMain
    p['sy']['RDFMain'] = RDFMain
    #

    # paragraph ==RDF
    p['sy']['==RDF'] = EQRDF
    #

    # paragraph getSubject
    p['sy']['getSubject'] = getSubject
    #

    # paragraph ==(
    p['sy']['==('] = EQzopz
    #

    # paragraph ==)
    p['sy']['==)'] = EQzcpz
    #

    # paragraph complexSubject
    p['sy']['complexSubject'] = complexSubject
    #

    # paragraph getObject
    p['sy']['getObject'] = getObject
    #

    # paragraph ==(
    p['sy']['==('] = EQzopz
    #

    # paragraph ==)
    p['sy']['==)'] = EQzcpz
    #

    # paragraph complexObject
    p['sy']['complexObject'] = complexObject
    #

    # paragraph initIOI
    p['sy']['initIOI'] = initIOI
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

def datPop():
    global p
    try:
        v = p['dat'].pop()
    except:
        v = ''
    finally:
    	nop = -1
    #end try
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

