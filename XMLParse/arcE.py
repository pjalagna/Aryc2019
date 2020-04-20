
#file arcE.py
#generated for arcElt.basii at Tue Apr 14 12:19:37 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def aVersion_1():
    global p
    logg('aVersion_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for aVersion-1 processing text ')
    logg("""version0413-2012""")
    if (r == p['OK']):
        logg('push text ' + """version0413-2012""")
        datPush("version0413-2012")
        logg('after ' + """version0413-2012""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for aVersion-1 processing verb ( msg ) ')
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
    logg('final aVersion_1')
#end aVersion_1

def aVersion (x):
    global p
    logg('begin aVersion')
    ## point of umbrella
    aVersionCtl = 1 # starting spoke
    while aVersionCtl != 0:
        logg('loop aVersionCtl = ' + aVersionCtl.__str__())
        if (aVersionCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (aVersionCtl == 1):
            logg('call aVersion_1')
            aVersion_1()
            logg('after call aVersion_1')
            # test and adjust for new spoke
            aVersionCtl = chk(aVersionCtl)

        else:
            #final
            logg('final aVersion')    
            aVersionCtl = 0 # break
        #endif
    #wend
#end aVersion

def arcElt_1():
    global p
    logg('arcElt_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for arcElt-1 processing text ')
    logg("""def arcElt :-""")
    if (r == p['OK']):
        logg('push text ' + """def arcElt :-""")
        datPush("def arcElt :-")
        logg('after ' + """def arcElt :-""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcElt-1 processing verb ( msg ) ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( ! ) ')
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
    logg('for arcElt-1 processing verb ( xioi ) ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( = ) ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( ! ) ')
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
    logg('for arcElt-1 processing verb ( arcName ) ')
    if (r == p['OK']):
        logg('call arcName ')
        p['sy']['arcName'](p)
        logg('after arcName')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( ! ) ')
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
    logg('for arcElt-1 processing verb ( OpAttrS ) ')
    if (r == p['OK']):
        logg('call OpAttrS ')
        p['sy']['OpAttrS'](p)
        logg('after OpAttrS')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( ! ) ')
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
    logg('for arcElt-1 processing verb ( xioi ) ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( = ) ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( ! ) ')
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
    logg('for arcElt-1 processing verb ( content ) ')
    if (r == p['OK']):
        logg('call content ')
        p['sy']['content'](p)
        logg('after content')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( ! ) ')
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
    logg('for arcElt-1 processing verb ( xxioi ) ')
    if (r == p['OK']):
        logg('call xxioi ')
        p['sy']['xxioi'](p)
        logg('after xxioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcElt-1 processing text ')
    logg("""</""")
    if (r == p['OK']):
        logg('push text ' + """</""")
        datPush("</")
        logg('after ' + """</""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcElt-1 processing verb ( = ) ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( ! ) ')
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
    logg('for arcElt-1 processing verb ( EQarcName ) ')
    if (r == p['OK']):
        logg('call EQarcName ')
        p['sy']['EQarcName'](p)
        logg('after EQarcName')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcElt-1 processing text ')
    logg("""7""")
    if (r == p['OK']):
        logg('push text ' + """7""")
        datPush("7")
        logg('after ' + """7""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( ! ) ')
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
    logg('for arcElt-1 processing verb ( xioi ) ')
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
    logg('for arcElt-1 processing text ')
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
    logg('for arcElt-1 processing verb ( = ) ')
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
    logg('final arcElt_1')
#end arcElt_1

def arcElt_2():
    global p
    logg('arcElt_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for arcElt-2 processing text ')
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
    logg('for arcElt-2 processing verb ( @ ) ')
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
    logg('for arcElt-2 processing text ')
    logg("""format failure""")
    if (r == p['OK']):
        logg('push text ' + """format failure""")
        datPush("format failure")
        logg('after ' + """format failure""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcElt-2 processing verb ( cats ) ')
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
    logg('for arcElt-2 processing verb ( msg ) ')
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
    logg('final arcElt_2')
#end arcElt_2

def arcElt (x):
    global p
    logg('begin arcElt')
    ## point of umbrella
    arcEltCtl = 1 # starting spoke
    while arcEltCtl != 0:
        logg('loop arcEltCtl = ' + arcEltCtl.__str__())
        if (arcEltCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (arcEltCtl == 1):
            logg('call arcElt_1')
            arcElt_1()
            logg('after call arcElt_1')
            # test and adjust for new spoke
            arcEltCtl = chk(arcEltCtl)

        elif (arcEltCtl == 2):
            logg('call arcElt_2')
            arcElt_2()
            logg('after call arcElt_2')
            # test and adjust for new spoke
            arcEltCtl = chk(arcEltCtl)

        else:
            #final
            logg('final arcElt')    
            arcEltCtl = 0 # break
        #endif
    #wend
#end arcElt

def EQarcName_1():
    global p
    logg('EQarcName_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for EQarcName-1 processing text ')
    logg("""def EQarcName :-""")
    if (r == p['OK']):
        logg('push text ' + """def EQarcName :-""")
        datPush("def EQarcName :-")
        logg('after ' + """def EQarcName :-""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for EQarcName-1 processing verb ( msg ) ')
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
    logg('for EQarcName-1 processing text ')
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
    logg('for EQarcName-1 processing text ')
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
    logg('for EQarcName-1 processing verb ( ! ) ')
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
    logg('for EQarcName-1 processing verb ( Xlabel ) ')
    if (r == p['OK']):
        logg('call Xlabel ')
        p['sy']['Xlabel'](p)
        logg('after Xlabel')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for EQarcName-1 processing text ')
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
    logg('for EQarcName-1 processing text ')
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
    logg('for EQarcName-1 processing verb ( ! ) ')
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
    logg('for EQarcName-1 processing text ')
    logg("""name""")
    if (r == p['OK']):
        logg('push text ' + """name""")
        datPush("name")
        logg('after ' + """name""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for EQarcName-1 processing verb ( @ ) ')
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
    logg('for EQarcName-1 processing verb ( = ) ')
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
    logg('final EQarcName_1')
#end EQarcName_1

def EQarcName_2():
    global p
    logg('EQarcName_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for EQarcName-2 processing text ')
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
    logg('for EQarcName-2 processing verb ( @ ) ')
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
    logg('for EQarcName-2 processing text ')
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
    logg('for EQarcName-2 processing verb ( = ) ')
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
    logg('for EQarcName-2 processing text ')
    logg("""EQarcName expected Xlabel""")
    if (r == p['OK']):
        logg('push text ' + """EQarcName expected Xlabel""")
        datPush("EQarcName expected Xlabel")
        logg('after ' + """EQarcName expected Xlabel""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for EQarcName-2 processing verb ( abort ) ')
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
    logg('final EQarcName_2')
#end EQarcName_2

def EQarcName_3():
    global p
    logg('EQarcName_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for EQarcName-3 processing text ')
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
    logg('for EQarcName-3 processing verb ( @ ) ')
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
    logg('for EQarcName-3 processing text ')
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
    logg('for EQarcName-3 processing verb ( = ) ')
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
    logg('for EQarcName-3 processing text ')
    logg("""EQarcName expected same Qname""")
    if (r == p['OK']):
        logg('push text ' + """EQarcName expected same Qname""")
        datPush("EQarcName expected same Qname")
        logg('after ' + """EQarcName expected same Qname""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for EQarcName-3 processing verb ( abort ) ')
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
    logg('final EQarcName_3')
#end EQarcName_3

def EQarcName (x):
    global p
    logg('begin EQarcName')
    ## point of umbrella
    EQarcNameCtl = 1 # starting spoke
    while EQarcNameCtl != 0:
        logg('loop EQarcNameCtl = ' + EQarcNameCtl.__str__())
        if (EQarcNameCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (EQarcNameCtl == 1):
            logg('call EQarcName_1')
            EQarcName_1()
            logg('after call EQarcName_1')
            # test and adjust for new spoke
            EQarcNameCtl = chk(EQarcNameCtl)

        elif (EQarcNameCtl == 2):
            logg('call EQarcName_2')
            EQarcName_2()
            logg('after call EQarcName_2')
            # test and adjust for new spoke
            EQarcNameCtl = chk(EQarcNameCtl)

        elif (EQarcNameCtl == 3):
            logg('call EQarcName_3')
            EQarcName_3()
            logg('after call EQarcName_3')
            # test and adjust for new spoke
            EQarcNameCtl = chk(EQarcNameCtl)

        else:
            #final
            logg('final EQarcName')    
            EQarcNameCtl = 0 # break
        #endif
    #wend
#end EQarcName

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
    logg("""cxfn""")
    if (r == p['OK']):
        logg('push text ' + """cxfn""")
        datPush("cxfn")
        logg('after ' + """cxfn""" )
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

def arcName_1():
    global p
    logg('arcName_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for arcName-1 processing text ')
    logg("""def arcName :- """)
    if (r == p['OK']):
        logg('push text ' + """def arcName :- """)
        datPush("def arcName :- ")
        logg('after ' + """def arcName :- """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for arcName-1 processing verb ( msg ) ')
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
    logg('for arcName-1 processing verb ( Qname ) ')
    if (r == p['OK']):
        logg('call Qname ')
        p['sy']['Qname'](p)
        logg('after Qname')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final arcName_1')
#end arcName_1

def arcName (x):
    global p
    logg('begin arcName')
    ## point of umbrella
    arcNameCtl = 1 # starting spoke
    while arcNameCtl != 0:
        logg('loop arcNameCtl = ' + arcNameCtl.__str__())
        if (arcNameCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (arcNameCtl == 1):
            logg('call arcName_1')
            arcName_1()
            logg('after call arcName_1')
            # test and adjust for new spoke
            arcNameCtl = chk(arcNameCtl)

        else:
            #final
            logg('final arcName')    
            arcNameCtl = 0 # break
        #endif
    #wend
#end arcName

def Qname_1():
    global p
    logg('Qname_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Qname-1 processing text ')
    logg("""def Qname :- """)
    if (r == p['OK']):
        logg('push text ' + """def Qname :- """)
        datPush("def Qname :- ")
        logg('after ' + """def Qname :- """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-1 processing verb ( msg ) ')
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
    logg('for Qname-1 processing verb ( OpNSprefix ) ')
    if (r == p['OK']):
        logg('call OpNSprefix ')
        p['sy']['OpNSprefix'](p)
        logg('after OpNSprefix')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-1 processing verb ( xioi ) ')
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
    logg('for Qname-1 processing text ')
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
    logg('for Qname-1 processing verb ( = ) ')
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
    logg('for Qname-1 processing verb ( name ) ')
    if (r == p['OK']):
        logg('call name ')
        p['sy']['name'](p)
        logg('after name')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final Qname_1')
#end Qname_1

def Qname_2():
    global p
    logg('Qname_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Qname-2 processing text ')
    logg("""NSprefix""")
    if (r == p['OK']):
        logg('push text ' + """NSprefix""")
        datPush("NSprefix")
        logg('after ' + """NSprefix""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-2 processing verb ( @ ) ')
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
    logg('for Qname-2 processing text ')
    logg("""name""")
    if (r == p['OK']):
        logg('push text ' + """name""")
        datPush("name")
        logg('after ' + """name""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-2 processing verb ( ! ) ')
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
    logg('final Qname_2')
#end Qname_2

def Qname_3():
    global p
    logg('Qname_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Qname-3 processing text ')
    logg("""Qname expected Xlabel""")
    if (r == p['OK']):
        logg('push text ' + """Qname expected Xlabel""")
        datPush("Qname expected Xlabel")
        logg('after ' + """Qname expected Xlabel""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-3 processing verb ( abort ) ')
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

    r = p['sy']['pop']()
    logg('for Qname-3 processing verb ( ; ) ')
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
    logg('for Qname-3 processing verb ( def ) ')
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
    logg('for Qname-3 processing verb ( name ) ')
    if (r == p['OK']):
        logg('call name ')
        p['sy']['name'](p)
        logg('after name')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-3 processing verb ( :- ) ')
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
    logg('for Qname-3 processing verb ( [[ ) ')
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
    logg('for Qname-3 processing verb ( 1 ) ')
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
    logg('for Qname-3 processing verb ( ]] ) ')
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
    logg('for Qname-3 processing text ')
    logg("""def name :-""")
    if (r == p['OK']):
        logg('push text ' + """def name :-""")
        datPush("def name :-")
        logg('after ' + """def name :-""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-3 processing verb ( msg ) ')
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
    logg('for Qname-3 processing verb ( Xlabel ) ')
    if (r == p['OK']):
        logg('call Xlabel ')
        p['sy']['Xlabel'](p)
        logg('after Xlabel')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-3 processing text ')
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
    logg('for Qname-3 processing verb ( @ ) ')
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
    logg('for Qname-3 processing text ')
    logg("""name""")
    if (r == p['OK']):
        logg('push text ' + """name""")
        datPush("name")
        logg('after ' + """name""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-3 processing verb ( ! ) ')
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
    logg('final Qname_3')
#end Qname_3

def Qname_2():
    global p
    logg('Qname_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for Qname-2 processing text ')
    logg("""name expected Xlabel""")
    if (r == p['OK']):
        logg('push text ' + """name expected Xlabel""")
        datPush("name expected Xlabel")
        logg('after ' + """name expected Xlabel""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for Qname-2 processing verb ( abort ) ')
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
    logg('final Qname_2')
#end Qname_2

def Qname (x):
    global p
    logg('begin Qname')
    ## point of umbrella
    QnameCtl = 1 # starting spoke
    while QnameCtl != 0:
        logg('loop QnameCtl = ' + QnameCtl.__str__())
        if (QnameCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (QnameCtl == 1):
            logg('call Qname_1')
            Qname_1()
            logg('after call Qname_1')
            # test and adjust for new spoke
            QnameCtl = chk(QnameCtl)

        elif (QnameCtl == 2):
            logg('call Qname_2')
            Qname_2()
            logg('after call Qname_2')
            # test and adjust for new spoke
            QnameCtl = chk(QnameCtl)

        elif (QnameCtl == 3):
            logg('call Qname_3')
            Qname_3()
            logg('after call Qname_3')
            # test and adjust for new spoke
            QnameCtl = chk(QnameCtl)

        elif (QnameCtl == 4):
            logg('call Qname_2')
            Qname_2()
            logg('after call Qname_2')
            # test and adjust for new spoke
            QnameCtl = chk(QnameCtl)

        else:
            #final
            logg('final Qname')    
            QnameCtl = 0 # break
        #endif
    #wend
#end Qname

def OpNSprefix_1():
    global p
    logg('OpNSprefix_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for OpNSprefix-1 processing text ')
    logg("""def OpNSprefix :- """)
    if (r == p['OK']):
        logg('push text ' + """def OpNSprefix :- """)
        datPush("def OpNSprefix :- ")
        logg('after ' + """def OpNSprefix :- """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpNSprefix-1 processing verb ( msg ) ')
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
    logg('for OpNSprefix-1 processing verb ( Xlabel ) ')
    if (r == p['OK']):
        logg('call Xlabel ')
        p['sy']['Xlabel'](p)
        logg('after Xlabel')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpNSprefix-1 processing text ')
    logg("""NSprefix""")
    if (r == p['OK']):
        logg('push text ' + """NSprefix""")
        datPush("NSprefix")
        logg('after ' + """NSprefix""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpNSprefix-1 processing verb ( ! ) ')
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
    logg('final OpNSprefix_1')
#end OpNSprefix_1

def OpNSprefix_2():
    global p
    logg('OpNSprefix_2')
    datPush(p['OK'])

    #final
    logg('final OpNSprefix_2')
#end OpNSprefix_2

def OpNSprefix (x):
    global p
    logg('begin OpNSprefix')
    ## point of umbrella
    OpNSprefixCtl = 1 # starting spoke
    while OpNSprefixCtl != 0:
        logg('loop OpNSprefixCtl = ' + OpNSprefixCtl.__str__())
        if (OpNSprefixCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (OpNSprefixCtl == 1):
            logg('call OpNSprefix_1')
            OpNSprefix_1()
            logg('after call OpNSprefix_1')
            # test and adjust for new spoke
            OpNSprefixCtl = chk(OpNSprefixCtl)

        elif (OpNSprefixCtl == 2):
            logg('call OpNSprefix_2')
            OpNSprefix_2()
            logg('after call OpNSprefix_2')
            # test and adjust for new spoke
            OpNSprefixCtl = chk(OpNSprefixCtl)

        else:
            #final
            logg('final OpNSprefix')    
            OpNSprefixCtl = 0 # break
        #endif
    #wend
#end OpNSprefix

def content_1():
    global p
    logg('content_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for content-1 processing text ')
    logg("""def content :-""")
    if (r == p['OK']):
        logg('push text ' + """def content :-""")
        datPush("def content :-")
        logg('after ' + """def content :-""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for content-1 processing verb ( msg ) ')
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
    logg('for content-1 processing text ')
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
    logg('for content-1 processing text ')
    logg("""cst""")
    if (r == p['OK']):
        logg('push text ' + """cst""")
        datPush("cst")
        logg('after ' + """cst""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for content-1 processing verb ( ! ) ')
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
    logg('for content-1 processing verb ( collectTillLT ) ')
    if (r == p['OK']):
        logg('call collectTillLT ')
        p['sy']['collectTillLT'](p)
        logg('after collectTillLT')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for content-1 processing text ')
    logg("""collect""")
    if (r == p['OK']):
        logg('push text ' + """collect""")
        datPush("collect")
        logg('after ' + """collect""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for content-1 processing verb ( ! ) ')
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
    logg('final content_1')
#end content_1

def content (x):
    global p
    logg('begin content')
    ## point of umbrella
    contentCtl = 1 # starting spoke
    while contentCtl != 0:
        logg('loop contentCtl = ' + contentCtl.__str__())
        if (contentCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (contentCtl == 1):
            logg('call content_1')
            content_1()
            logg('after call content_1')
            # test and adjust for new spoke
            contentCtl = chk(contentCtl)

        else:
            #final
            logg('final content')    
            contentCtl = 0 # break
        #endif
    #wend
#end content

def collectTillLT_1():
    global p
    logg('collectTillLT_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for collectTillLT-1 processing text ')
    logg("""def collectTillLT :-""")
    if (r == p['OK']):
        logg('push text ' + """def collectTillLT :-""")
        datPush("def collectTillLT :-")
        logg('after ' + """def collectTillLT :-""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for collectTillLT-1 processing verb ( msg ) ')
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
    logg('for collectTillLT-1 processing verb ( xioi ) ')
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
    logg('for collectTillLT-1 processing text ')
    logg("""cstx""")
    if (r == p['OK']):
        logg('push text ' + """cstx""")
        datPush("cstx")
        logg('after ' + """cstx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for collectTillLT-1 processing verb ( ! ) ')
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
    logg('for collectTillLT-1 processing verb ( ... ) ')
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
    logg('final collectTillLT_1')
#end collectTillLT_1

def collectTillLT_2():
    global p
    logg('collectTillLT_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for collectTillLT-2 processing text ')
    logg("""cstx""")
    if (r == p['OK']):
        logg('push text ' + """cstx""")
        datPush("cstx")
        logg('after ' + """cstx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for collectTillLT-2 processing verb ( @ ) ')
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
    logg('for collectTillLT-2 processing text ')
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
    logg('for collectTillLT-2 processing verb ( = ) ')
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
    logg('for collectTillLT-2 processing verb ( contentFinal ) ')
    if (r == p['OK']):
        logg('call contentFinal ')
        p['sy']['contentFinal'](p)
        logg('after contentFinal')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final collectTillLT_2')
#end collectTillLT_2

def collectTillLT_3():
    global p
    logg('collectTillLT_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for collectTillLT-3 processing text ')
    logg("""cst""")
    if (r == p['OK']):
        logg('push text ' + """cst""")
        datPush("cst")
        logg('after ' + """cst""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for collectTillLT-3 processing verb ( @ ) ')
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
    logg('for collectTillLT-3 processing text ')
    logg("""cstx""")
    if (r == p['OK']):
        logg('push text ' + """cstx""")
        datPush("cstx")
        logg('after ' + """cstx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for collectTillLT-3 processing verb ( @ ) ')
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
    logg('for collectTillLT-3 processing verb ( cat ) ')
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
    logg('for collectTillLT-3 processing text ')
    logg("""cst""")
    if (r == p['OK']):
        logg('push text ' + """cst""")
        datPush("cst")
        logg('after ' + """cst""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for collectTillLT-3 processing verb ( ! ) ')
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
    logg('for collectTillLT-3 processing verb ( tail. ) ')
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
    logg('final collectTillLT_3')
#end collectTillLT_3

def collectTillLT (x):
    global p
    logg('begin collectTillLT')
    ## point of umbrella
    collectTillLTCtl = 1 # starting spoke
    while collectTillLTCtl != 0:
        logg('loop collectTillLTCtl = ' + collectTillLTCtl.__str__())
        if (collectTillLTCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (collectTillLTCtl == 1):
            logg('call collectTillLT_1')
            collectTillLT_1()
            logg('after call collectTillLT_1')
            # test and adjust for new spoke
            collectTillLTCtl = chk(collectTillLTCtl)

        elif (collectTillLTCtl == 2):
            logg('call collectTillLT_2')
            collectTillLT_2()
            logg('after call collectTillLT_2')
            # test and adjust for new spoke
            collectTillLTCtl = chk(collectTillLTCtl)

        elif (collectTillLTCtl == 3):
            logg('call collectTillLT_3')
            collectTillLT_3()
            logg('after call collectTillLT_3')
            # test and adjust for new spoke
            collectTillLTCtl = chk(collectTillLTCtl)

        else:
            #final
            logg('final collectTillLT')    
            collectTillLTCtl = 0 # break
        #endif
    #wend
#end collectTillLT

def OpAttrS_1():
    global p
    logg('OpAttrS_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for OpAttrS-1 processing text ')
    logg("""def OpAttrS :- """)
    if (r == p['OK']):
        logg('push text ' + """def OpAttrS :- """)
        datPush("def OpAttrS :- ")
        logg('after ' + """def OpAttrS :- """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpAttrS-1 processing verb ( msg ) ')
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
    logg('for OpAttrS-1 processing text ')
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
    logg('for OpAttrS-1 processing text ')
    logg("""attctr""")
    if (r == p['OK']):
        logg('push text ' + """attctr""")
        datPush("attctr")
        logg('after ' + """attctr""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpAttrS-1 processing verb ( ! ) ')
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
    logg('for OpAttrS-1 processing verb ( OpAttrS1 ) ')
    if (r == p['OK']):
        logg('call OpAttrS1 ')
        p['sy']['OpAttrS1'](p)
        logg('after OpAttrS1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final OpAttrS_1')
#end OpAttrS_1

def OpAttrS (x):
    global p
    logg('begin OpAttrS')
    ## point of umbrella
    OpAttrSCtl = 1 # starting spoke
    while OpAttrSCtl != 0:
        logg('loop OpAttrSCtl = ' + OpAttrSCtl.__str__())
        if (OpAttrSCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (OpAttrSCtl == 1):
            logg('call OpAttrS_1')
            OpAttrS_1()
            logg('after call OpAttrS_1')
            # test and adjust for new spoke
            OpAttrSCtl = chk(OpAttrSCtl)

        else:
            #final
            logg('final OpAttrS')    
            OpAttrSCtl = 0 # break
        #endif
    #wend
#end OpAttrS

def OpAttrS1_1():
    global p
    logg('OpAttrS1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for OpAttrS1-1 processing text ')
    logg("""def OpAttrS1 :-""")
    if (r == p['OK']):
        logg('push text ' + """def OpAttrS1 :-""")
        datPush("def OpAttrS1 :-")
        logg('after ' + """def OpAttrS1 :-""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpAttrS1-1 processing verb ( msg ) ')
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
    logg('for OpAttrS1-1 processing verb ( xioi ) ')
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
    logg('for OpAttrS1-1 processing text ')
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
    logg('for OpAttrS1-1 processing verb ( = ) ')
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
    logg('for OpAttrS1-1 processing verb ( Xlabel ) ')
    if (r == p['OK']):
        logg('call Xlabel ')
        p['sy']['Xlabel'](p)
        logg('after Xlabel')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpAttrS1-1 processing text ')
    logg("""attname""")
    if (r == p['OK']):
        logg('push text ' + """attname""")
        datPush("attname")
        logg('after ' + """attname""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpAttrS1-1 processing verb ( ! ) ')
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
    logg('for OpAttrS1-1 processing verb ( xioi ) ')
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
    logg('for OpAttrS1-1 processing text ')
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
    logg('for OpAttrS1-1 processing verb ( qstring ) ')
    if (r == p['OK']):
        logg('call qstring ')
        p['sy']['qstring'](p)
        logg('after qstring')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpAttrS1-1 processing verb ( storeAtt ) ')
    if (r == p['OK']):
        logg('call storeAtt ')
        p['sy']['storeAtt'](p)
        logg('after storeAtt')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for OpAttrS1-1 processing verb ( tail. ) ')
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
    logg('final OpAttrS1_1')
#end OpAttrS1_1

def OpAttrS1_2():
    global p
    logg('OpAttrS1_2')
    datPush(p['OK'])

    #final
    logg('final OpAttrS1_2')
#end OpAttrS1_2

def OpAttrS1 (x):
    global p
    logg('begin OpAttrS1')
    ## point of umbrella
    OpAttrS1Ctl = 1 # starting spoke
    while OpAttrS1Ctl != 0:
        logg('loop OpAttrS1Ctl = ' + OpAttrS1Ctl.__str__())
        if (OpAttrS1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (OpAttrS1Ctl == 1):
            logg('call OpAttrS1_1')
            OpAttrS1_1()
            logg('after call OpAttrS1_1')
            # test and adjust for new spoke
            OpAttrS1Ctl = chk(OpAttrS1Ctl)

        elif (OpAttrS1Ctl == 2):
            logg('call OpAttrS1_2')
            OpAttrS1_2()
            logg('after call OpAttrS1_2')
            # test and adjust for new spoke
            OpAttrS1Ctl = chk(OpAttrS1Ctl)

        else:
            #final
            logg('final OpAttrS1')    
            OpAttrS1Ctl = 0 # break
        #endif
    #wend
#end OpAttrS1

def qstring_1():
    global p
    logg('qstring_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for qstring-1 processing verb ( xioi ) ')
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
    logg('for qstring-1 processing verb ( Q? ) ')
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
    logg('for qstring-1 processing verb ( woB ) ')
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
    logg('final qstring_1')
#end qstring_1

def qstring_2():
    global p
    logg('qstring_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for qstring-2 processing verb ( xioi ) ')
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
    logg('for qstring-2 processing verb ( T? ) ')
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
    logg('for qstring-2 processing verb ( woB ) ')
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
    logg('final qstring_2')
#end qstring_2

def qstring_3():
    global p
    logg('qstring_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for qstring-3 processing text ')
    logg("""expected quoted string""")
    if (r == p['OK']):
        logg('push text ' + """expected quoted string""")
        datPush("expected quoted string")
        logg('after ' + """expected quoted string""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for qstring-3 processing verb ( abort ) ')
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
    logg('final qstring_3')
#end qstring_3

def qstring (x):
    global p
    logg('begin qstring')
    ## point of umbrella
    qstringCtl = 1 # starting spoke
    while qstringCtl != 0:
        logg('loop qstringCtl = ' + qstringCtl.__str__())
        if (qstringCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (qstringCtl == 1):
            logg('call qstring_1')
            qstring_1()
            logg('after call qstring_1')
            # test and adjust for new spoke
            qstringCtl = chk(qstringCtl)

        elif (qstringCtl == 2):
            logg('call qstring_2')
            qstring_2()
            logg('after call qstring_2')
            # test and adjust for new spoke
            qstringCtl = chk(qstringCtl)

        elif (qstringCtl == 3):
            logg('call qstring_3')
            qstring_3()
            logg('after call qstring_3')
            # test and adjust for new spoke
            qstringCtl = chk(qstringCtl)

        else:
            #final
            logg('final qstring')    
            qstringCtl = 0 # break
        #endif
    #wend
#end qstring

def storeAtt_1():
    global p
    logg('storeAtt_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for storeAtt-1 processing text ')
    logg("""attname""")
    if (r == p['OK']):
        logg('push text ' + """attname""")
        datPush("attname")
        logg('after ' + """attname""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for storeAtt-1 processing verb ( @ ) ')
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
    logg('for storeAtt-1 processing text ')
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
    logg('for storeAtt-1 processing verb ( cat ) ')
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
    logg('for storeAtt-1 processing text ')
    logg("""attctr""")
    if (r == p['OK']):
        logg('push text ' + """attctr""")
        datPush("attctr")
        logg('after ' + """attctr""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for storeAtt-1 processing verb ( @ ) ')
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
    logg('for storeAtt-1 processing verb ( cat ) ')
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
    logg('for storeAtt-1 processing verb ( ! ) ')
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
    logg('final storeAtt_1')
#end storeAtt_1

def storeAtt (x):
    global p
    logg('begin storeAtt')
    ## point of umbrella
    storeAttCtl = 1 # starting spoke
    while storeAttCtl != 0:
        logg('loop storeAttCtl = ' + storeAttCtl.__str__())
        if (storeAttCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (storeAttCtl == 1):
            logg('call storeAtt_1')
            storeAtt_1()
            logg('after call storeAtt_1')
            # test and adjust for new spoke
            storeAttCtl = chk(storeAttCtl)

        else:
            #final
            logg('final storeAtt')    
            storeAttCtl = 0 # break
        #endif
    #wend
#end storeAtt

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
    logg('for Xlabel-1 processing verb ( Xlabel2 ) ')
    if (r == p['OK']):
        logg('call Xlabel2 ')
        p['sy']['Xlabel2'](p)
        logg('after Xlabel2')
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
    logg('for Xlabel2-2 processing verb ( XlabelFinal ) ')
    if (r == p['OK']):
        logg('call XlabelFinal ')
        p['sy']['XlabelFinal'](p)
        logg('after XlabelFinal')
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
    logg('for Xlabel2-3 processing verb ( XlabelFinal ) ')
    if (r == p['OK']):
        logg('call XlabelFinal ')
        p['sy']['XlabelFinal'](p)
        logg('after XlabelFinal')
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
    logg('for Xlabel2-4 processing verb ( XlabelFinal ) ')
    if (r == p['OK']):
        logg('call XlabelFinal ')
        p['sy']['XlabelFinal'](p)
        logg('after XlabelFinal')
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
    logg('for Xlabel2-5 processing verb ( XlabelFinal ) ')
    if (r == p['OK']):
        logg('call XlabelFinal ')
        p['sy']['XlabelFinal'](p)
        logg('after XlabelFinal')
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
    logg('for Xlabel2-6 processing verb ( XlabelFinal ) ')
    if (r == p['OK']):
        logg('call XlabelFinal ')
        p['sy']['XlabelFinal'](p)
        logg('after XlabelFinal')
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

def xbegin_1():
    global p
    logg('xbegin_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xbegin-1 processing verb ( aVersion ) ')
    if (r == p['OK']):
        logg('call aVersion ')
        p['sy']['aVersion'](p)
        logg('after aVersion')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xbegin-1 processing text ')
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
    logg('for xbegin-1 processing verb ( takeV ) ')
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
    logg('for xbegin-1 processing text ')
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
    logg('for xbegin-1 processing verb ( ask ) ')
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
    logg('for xbegin-1 processing verb ( dup ) ')
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
    logg('for xbegin-1 processing text ')
    logg("""xfn""")
    if (r == p['OK']):
        logg('push text ' + """xfn""")
        datPush("xfn")
        logg('after ' + """xfn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xbegin-1 processing verb ( ! ) ')
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
    logg('for xbegin-1 processing verb ( f@ ) ')
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
    logg('for xbegin-1 processing verb ( dup ) ')
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
    logg('for xbegin-1 processing text ')
    logg("""cxfn""")
    if (r == p['OK']):
        logg('push text ' + """cxfn""")
        datPush("cxfn")
        logg('after ' + """cxfn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xbegin-1 processing verb ( ! ) ')
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
    logg('for xbegin-1 processing text ')
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
    logg('for xbegin-1 processing verb ( find ) ')
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
    logg('for xbegin-1 processing text ')
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
    logg('for xbegin-1 processing verb ( ! ) ')
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
    logg('for xbegin-1 processing verb ( arcElt ) ')
    if (r == p['OK']):
        logg('call arcElt ')
        p['sy']['arcElt'](p)
        logg('after arcElt')
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

def abort_1():
    global p
    logg('abort_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for abort-1 processing text ')
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
    logg('for abort-1 processing verb ( ask ) ')
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
    logg('for abort-1 processing verb ( exit ) ')
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

    # paragraph aVersion
    p['sy']['aVersion'] = aVersion
    #

    # paragraph arcElt
    p['sy']['arcElt'] = arcElt
    #

    # paragraph EQarcName
    p['sy']['EQarcName'] = EQarcName
    #

    # paragraph xioi
    p['sy']['xioi'] = xioi
    #

    # paragraph xxioi
    p['sy']['xxioi'] = xxioi
    #

    # paragraph xioo
    p['sy']['xioo'] = xioo
    #

    # paragraph arcName
    p['sy']['arcName'] = arcName
    #

    # paragraph Qname
    p['sy']['Qname'] = Qname
    #

    # paragraph OpNSprefix
    p['sy']['OpNSprefix'] = OpNSprefix
    #

    # paragraph content
    p['sy']['content'] = content
    #

    # paragraph collectTillLT
    p['sy']['collectTillLT'] = collectTillLT
    #

    # paragraph OpAttrS
    p['sy']['OpAttrS'] = OpAttrS
    #

    # paragraph OpAttrS1
    p['sy']['OpAttrS1'] = OpAttrS1
    #

    # paragraph qstring
    p['sy']['qstring'] = qstring
    #

    # paragraph storeAtt
    p['sy']['storeAtt'] = storeAtt
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

    # paragraph xbegin
    p['sy']['xbegin'] = xbegin
    #

    # paragraph abort
    p['sy']['abort'] = abort
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

