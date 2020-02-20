
#file b2020.py
#generated for Berta2020.basii at Sat Feb 15 22:22:59 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def BertaStart_1():
    global p
    logg('BertaStart_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for BertaStart-1 processing verb ( BertaInit ) ')
    if (r == p['OK']):
        logg('call BertaInit ')
        p['sy']['BertaInit'](p)
        logg('after BertaInit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for BertaStart-1 processing verb ( setPage ) ')
    if (r == p['OK']):
        logg('call setPage ')
        p['sy']['setPage'](p)
        logg('after setPage')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for BertaStart-1 processing verb ( fini ) ')
    if (r == p['OK']):
        logg('call fini ')
        p['sy']['fini'](p)
        logg('after fini')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final BertaStart_1')
#end BertaStart_1

def BertaStart (x):
    global p
    logg('begin BertaStart')
    ## point of umbrella
    BertaStartCtl = 1 # starting spoke
    while BertaStartCtl != 0:
        logg('loop BertaStartCtl = ' + BertaStartCtl.__str__())
        if (BertaStartCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (BertaStartCtl == 1):
            logg('call BertaStart_1')
            BertaStart_1()
            logg('after call BertaStart_1')
            # test and adjust for new spoke
            BertaStartCtl = chk(BertaStartCtl)

        else:
            #final
            logg('final BertaStart')    
            BertaStartCtl = 0 # break
        #endif
    #wend
#end BertaStart

def BertaInit_1():
    global p
    logg('BertaInit_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for BertaInit-1 processing text ')
    logg("""ScreenV""")
    if (r == p['OK']):
        logg('push text ' + """ScreenV""")
        datPush("ScreenV")
        logg('after ' + """ScreenV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for BertaInit-1 processing verb ( takeV ) ')
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
    logg('for BertaInit-1 processing text ')
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
    logg('for BertaInit-1 processing verb ( takeV ) ')
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
    logg('final BertaInit_1')
#end BertaInit_1

def BertaInit (x):
    global p
    logg('begin BertaInit')
    ## point of umbrella
    BertaInitCtl = 1 # starting spoke
    while BertaInitCtl != 0:
        logg('loop BertaInitCtl = ' + BertaInitCtl.__str__())
        if (BertaInitCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (BertaInitCtl == 1):
            logg('call BertaInit_1')
            BertaInit_1()
            logg('after call BertaInit_1')
            # test and adjust for new spoke
            BertaInitCtl = chk(BertaInitCtl)

        else:
            #final
            logg('final BertaInit')    
            BertaInitCtl = 0 # break
        #endif
    #wend
#end BertaInit

def setPage_1():
    global p
    logg('setPage_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( sc0 ) ')
    if (r == p['OK']):
        logg('call sc0 ')
        p['sy']['sc0'](p)
        logg('after sc0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""red exit to exit""")
    if (r == p['OK']):
        logg('push text ' + """red exit to exit""")
        datPush("red exit to exit")
        logg('after ' + """red exit to exit""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""bundle""")
    if (r == p['OK']):
        logg('push text ' + """bundle""")
        datPush("bundle")
        logg('after ' + """bundle""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""bundle""")
    if (r == p['OK']):
        logg('push text ' + """bundle""")
        datPush("bundle")
        logg('after ' + """bundle""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scE ) ')
    if (r == p['OK']):
        logg('call scE ')
        p['sy']['scE'](p)
        logg('after scE')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Rule""")
    if (r == p['OK']):
        logg('push text ' + """Rule""")
        datPush("Rule")
        logg('after ' + """Rule""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Rule""")
    if (r == p['OK']):
        logg('push text ' + """Rule""")
        datPush("Rule")
        logg('after ' + """Rule""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scE ) ')
    if (r == p['OK']):
        logg('call scE ')
        p['sy']['scE'](p)
        logg('after scE')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Threshold""")
    if (r == p['OK']):
        logg('push text ' + """Threshold""")
        datPush("Threshold")
        logg('after ' + """Threshold""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Threshold""")
    if (r == p['OK']):
        logg('push text ' + """Threshold""")
        datPush("Threshold")
        logg('after ' + """Threshold""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scE ) ')
    if (r == p['OK']):
        logg('call scE ')
        p['sy']['scE'](p)
        logg('after scE')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Action""")
    if (r == p['OK']):
        logg('push text ' + """Action""")
        datPush("Action")
        logg('after ' + """Action""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Action""")
    if (r == p['OK']):
        logg('push text ' + """Action""")
        datPush("Action")
        logg('after ' + """Action""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scE ) ')
    if (r == p['OK']):
        logg('call scE ')
        p['sy']['scE'](p)
        logg('after scE')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""test""")
    if (r == p['OK']):
        logg('push text ' + """test""")
        datPush("test")
        logg('after ' + """test""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""test""")
    if (r == p['OK']):
        logg('push text ' + """test""")
        datPush("test")
        logg('after ' + """test""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scE ) ')
    if (r == p['OK']):
        logg('call scE ')
        p['sy']['scE'](p)
        logg('after scE')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Line1""")
    if (r == p['OK']):
        logg('push text ' + """Line1""")
        datPush("Line1")
        logg('after ' + """Line1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""line1""")
    if (r == p['OK']):
        logg('push text ' + """line1""")
        datPush("line1")
        logg('after ' + """line1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
    logg("""100""")
    if (r == p['OK']):
        logg('push text ' + """100""")
        datPush("100")
        logg('after ' + """100""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scEx ) ')
    if (r == p['OK']):
        logg('call scEx ')
        p['sy']['scEx'](p)
        logg('after scEx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Line2""")
    if (r == p['OK']):
        logg('push text ' + """Line2""")
        datPush("Line2")
        logg('after ' + """Line2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""line2""")
    if (r == p['OK']):
        logg('push text ' + """line2""")
        datPush("line2")
        logg('after ' + """line2""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
    logg("""100""")
    if (r == p['OK']):
        logg('push text ' + """100""")
        datPush("100")
        logg('after ' + """100""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scEx ) ')
    if (r == p['OK']):
        logg('call scEx ')
        p['sy']['scEx'](p)
        logg('after scEx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Line3""")
    if (r == p['OK']):
        logg('push text ' + """Line3""")
        datPush("Line3")
        logg('after ' + """Line3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""10""")
    if (r == p['OK']):
        logg('push text ' + """10""")
        datPush("10")
        logg('after ' + """10""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""line3""")
    if (r == p['OK']):
        logg('push text ' + """line3""")
        datPush("line3")
        logg('after ' + """line3""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""10""")
    if (r == p['OK']):
        logg('push text ' + """10""")
        datPush("10")
        logg('after ' + """10""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
    logg("""100""")
    if (r == p['OK']):
        logg('push text ' + """100""")
        datPush("100")
        logg('after ' + """100""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scEx ) ')
    if (r == p['OK']):
        logg('call scEx ')
        p['sy']['scEx'](p)
        logg('after scEx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Line4""")
    if (r == p['OK']):
        logg('push text ' + """Line4""")
        datPush("Line4")
        logg('after ' + """Line4""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""11""")
    if (r == p['OK']):
        logg('push text ' + """11""")
        datPush("11")
        logg('after ' + """11""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""line4""")
    if (r == p['OK']):
        logg('push text ' + """line4""")
        datPush("line4")
        logg('after ' + """line4""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""11""")
    if (r == p['OK']):
        logg('push text ' + """11""")
        datPush("11")
        logg('after ' + """11""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
    logg("""100""")
    if (r == p['OK']):
        logg('push text ' + """100""")
        datPush("100")
        logg('after ' + """100""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scEx ) ')
    if (r == p['OK']):
        logg('call scEx ')
        p['sy']['scEx'](p)
        logg('after scEx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Line5""")
    if (r == p['OK']):
        logg('push text ' + """Line5""")
        datPush("Line5")
        logg('after ' + """Line5""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""12""")
    if (r == p['OK']):
        logg('push text ' + """12""")
        datPush("12")
        logg('after ' + """12""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""line5""")
    if (r == p['OK']):
        logg('push text ' + """line5""")
        datPush("line5")
        logg('after ' + """line5""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""12""")
    if (r == p['OK']):
        logg('push text ' + """12""")
        datPush("12")
        logg('after ' + """12""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
    logg("""100""")
    if (r == p['OK']):
        logg('push text ' + """100""")
        datPush("100")
        logg('after ' + """100""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scEx ) ')
    if (r == p['OK']):
        logg('call scEx ')
        p['sy']['scEx'](p)
        logg('after scEx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Line6""")
    if (r == p['OK']):
        logg('push text ' + """Line6""")
        datPush("Line6")
        logg('after ' + """Line6""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""13""")
    if (r == p['OK']):
        logg('push text ' + """13""")
        datPush("13")
        logg('after ' + """13""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""line6""")
    if (r == p['OK']):
        logg('push text ' + """line6""")
        datPush("line6")
        logg('after ' + """line6""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""13""")
    if (r == p['OK']):
        logg('push text ' + """13""")
        datPush("13")
        logg('after ' + """13""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
    logg("""100""")
    if (r == p['OK']):
        logg('push text ' + """100""")
        datPush("100")
        logg('after ' + """100""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scEx ) ')
    if (r == p['OK']):
        logg('call scEx ')
        p['sy']['scEx'](p)
        logg('after scEx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Line7""")
    if (r == p['OK']):
        logg('push text ' + """Line7""")
        datPush("Line7")
        logg('after ' + """Line7""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""14""")
    if (r == p['OK']):
        logg('push text ' + """14""")
        datPush("14")
        logg('after ' + """14""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""line7""")
    if (r == p['OK']):
        logg('push text ' + """line7""")
        datPush("line7")
        logg('after ' + """line7""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""14""")
    if (r == p['OK']):
        logg('push text ' + """14""")
        datPush("14")
        logg('after ' + """14""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
    logg("""100""")
    if (r == p['OK']):
        logg('push text ' + """100""")
        datPush("100")
        logg('after ' + """100""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scEx ) ')
    if (r == p['OK']):
        logg('call scEx ')
        p['sy']['scEx'](p)
        logg('after scEx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Line8""")
    if (r == p['OK']):
        logg('push text ' + """Line8""")
        datPush("Line8")
        logg('after ' + """Line8""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""15""")
    if (r == p['OK']):
        logg('push text ' + """15""")
        datPush("15")
        logg('after ' + """15""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""line8""")
    if (r == p['OK']):
        logg('push text ' + """line8""")
        datPush("line8")
        logg('after ' + """line8""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""15""")
    if (r == p['OK']):
        logg('push text ' + """15""")
        datPush("15")
        logg('after ' + """15""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
    logg("""100""")
    if (r == p['OK']):
        logg('push text ' + """100""")
        datPush("100")
        logg('after ' + """100""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scEx ) ')
    if (r == p['OK']):
        logg('call scEx ')
        p['sy']['scEx'](p)
        logg('after scEx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""Line9""")
    if (r == p['OK']):
        logg('push text ' + """Line9""")
        datPush("Line9")
        logg('after ' + """Line9""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""16""")
    if (r == p['OK']):
        logg('push text ' + """16""")
        datPush("16")
        logg('after ' + """16""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing verb ( scL ) ')
    if (r == p['OK']):
        logg('call scL ')
        p['sy']['scL'](p)
        logg('after scL')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""line9""")
    if (r == p['OK']):
        logg('push text ' + """line9""")
        datPush("line9")
        logg('after ' + """line9""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
    logg("""16""")
    if (r == p['OK']):
        logg('push text ' + """16""")
        datPush("16")
        logg('after ' + """16""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing text ')
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
    logg('for setPage-1 processing text ')
    logg("""100""")
    if (r == p['OK']):
        logg('push text ' + """100""")
        datPush("100")
        logg('after ' + """100""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scEx ) ')
    if (r == p['OK']):
        logg('call scEx ')
        p['sy']['scEx'](p)
        logg('after scEx')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for setPage-1 processing verb ( scGo ) ')
    if (r == p['OK']):
        logg('call scGo ')
        p['sy']['scGo'](p)
        logg('after scGo')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final setPage_1')
#end setPage_1

def setPage (x):
    global p
    logg('begin setPage')
    ## point of umbrella
    setPageCtl = 1 # starting spoke
    while setPageCtl != 0:
        logg('loop setPageCtl = ' + setPageCtl.__str__())
        if (setPageCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (setPageCtl == 1):
            logg('call setPage_1')
            setPage_1()
            logg('after call setPage_1')
            # test and adjust for new spoke
            setPageCtl = chk(setPageCtl)

        else:
            #final
            logg('final setPage')    
            setPageCtl = 0 # break
        #endif
    #wend
#end setPage

def fini_1():
    global p
    logg('fini_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fini-1 processing verb ( t0 ) ')
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
    logg('for fini-1 processing verb ( fini2 ) ')
    if (r == p['OK']):
        logg('call fini2 ')
        p['sy']['fini2'](p)
        logg('after fini2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final fini_1')
#end fini_1

def fini (x):
    global p
    logg('begin fini')
    ## point of umbrella
    finiCtl = 1 # starting spoke
    while finiCtl != 0:
        logg('loop finiCtl = ' + finiCtl.__str__())
        if (finiCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (finiCtl == 1):
            logg('call fini_1')
            fini_1()
            logg('after call fini_1')
            # test and adjust for new spoke
            finiCtl = chk(finiCtl)

        else:
            #final
            logg('final fini')    
            finiCtl = 0 # break
        #endif
    #wend
#end fini

def fini2_1():
    global p
    logg('fini2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fini2-1 processing verb ( dup ) ')
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
    logg('for fini2-1 processing verb ( ch0 ) ')
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
    logg('for fini2-1 processing verb ( = ) ')
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
    logg('for fini2-1 processing verb ( drop ) ')
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
    logg('for fini2-1 processing verb ( .t ) ')
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
    logg('for fini2-1 processing text ')
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
    logg('for fini2-1 processing verb ( ask ) ')
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
    logg('final fini2_1')
#end fini2_1

def fini2_2():
    global p
    logg('fini2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for fini2-2 processing verb ( t! ) ')
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
    logg('for fini2-2 processing verb ( tail. ) ')
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
    logg('final fini2_2')
#end fini2_2

def fini2 (x):
    global p
    logg('begin fini2')
    ## point of umbrella
    fini2Ctl = 1 # starting spoke
    while fini2Ctl != 0:
        logg('loop fini2Ctl = ' + fini2Ctl.__str__())
        if (fini2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (fini2Ctl == 1):
            logg('call fini2_1')
            fini2_1()
            logg('after call fini2_1')
            # test and adjust for new spoke
            fini2Ctl = chk(fini2Ctl)

        elif (fini2Ctl == 2):
            logg('call fini2_2')
            fini2_2()
            logg('after call fini2_2')
            # test and adjust for new spoke
            fini2Ctl = chk(fini2Ctl)

        else:
            #final
            logg('final fini2')    
            fini2Ctl = 0 # break
        #endif
    #wend
#end fini2

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

    # paragraph BertaStart
    p['sy']['BertaStart'] = BertaStart
    #

    # paragraph BertaInit
    p['sy']['BertaInit'] = BertaInit
    #

    # paragraph setPage
    p['sy']['setPage'] = setPage
    #

    # paragraph fini
    p['sy']['fini'] = fini
    #

    # paragraph fini2
    p['sy']['fini2'] = fini2
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

