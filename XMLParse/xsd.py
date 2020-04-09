
#file xsd.py
#generated for xsdP.basii at Tue Mar 31 14:26:38 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def xsdVersion_1():
    global p
    logg('xsdVersion_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdVersion-1 processing text ')
    logg("""version 3.31.xx,c""")
    if (r == p['OK']):
        logg('push text ' + """version 3.31.xx,c""")
        datPush("version 3.31.xx,c")
        logg('after ' + """version 3.31.xx,c""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdVersion-1 processing verb ( msg ) ')
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
    logg('final xsdVersion_1')
#end xsdVersion_1

def xsdVersion (x):
    global p
    logg('begin xsdVersion')
    ## point of umbrella
    xsdVersionCtl = 1 # starting spoke
    while xsdVersionCtl != 0:
        logg('loop xsdVersionCtl = ' + xsdVersionCtl.__str__())
        if (xsdVersionCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdVersionCtl == 1):
            logg('call xsdVersion_1')
            xsdVersion_1()
            logg('after call xsdVersion_1')
            # test and adjust for new spoke
            xsdVersionCtl = chk(xsdVersionCtl)

        else:
            #final
            logg('final xsdVersion')    
            xsdVersionCtl = 0 # break
        #endif
    #wend
#end xsdVersion

def xsdmain_1():
    global p
    logg('xsdmain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdmain-1 processing verb ( xsdInit ) ')
    if (r == p['OK']):
        logg('call xsdInit ')
        p['sy']['xsdInit'](p)
        logg('after xsdInit')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdmain-1 processing verb ( xsda ) ')
    if (r == p['OK']):
        logg('call xsda ')
        p['sy']['xsda'](p)
        logg('after xsda')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdmain-1 processing verb ( xsdFinal ) ')
    if (r == p['OK']):
        logg('call xsdFinal ')
        p['sy']['xsdFinal'](p)
        logg('after xsdFinal')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdmain_1')
#end xsdmain_1

def xsdmain (x):
    global p
    logg('begin xsdmain')
    ## point of umbrella
    xsdmainCtl = 1 # starting spoke
    while xsdmainCtl != 0:
        logg('loop xsdmainCtl = ' + xsdmainCtl.__str__())
        if (xsdmainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdmainCtl == 1):
            logg('call xsdmain_1')
            xsdmain_1()
            logg('after call xsdmain_1')
            # test and adjust for new spoke
            xsdmainCtl = chk(xsdmainCtl)

        else:
            #final
            logg('final xsdmain')    
            xsdmainCtl = 0 # break
        #endif
    #wend
#end xsdmain

def xsdInit_1():
    global p
    logg('xsdInit_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
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
    logg('for xsdInit-1 processing verb ( ask ) ')
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
    logg('for xsdInit-1 processing verb ( dup ) ')
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
    logg('for xsdInit-1 processing text ')
    logg("""xsdfn""")
    if (r == p['OK']):
        logg('push text ' + """xsdfn""")
        datPush("xsdfn")
        logg('after ' + """xsdfn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""fioiV""")
    if (r == p['OK']):
        logg('push text ' + """fioiV""")
        datPush("fioiV")
        logg('after ' + """fioiV""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( takeV ) ')
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
    logg('for xsdInit-1 processing text ')
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
    logg('for xsdInit-1 processing verb ( takeV ) ')
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
    logg('for xsdInit-1 processing verb ( ar0 ) ')
    if (r == p['OK']):
        logg('call ar0 ')
        p['sy']['ar0'](p)
        logg('after ar0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing text ')
    logg("""parents""")
    if (r == p['OK']):
        logg('push text ' + """parents""")
        datPush("parents")
        logg('after ' + """parents""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdInit-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdInit_1')
#end xsdInit_1

def xsdInit (x):
    global p
    logg('begin xsdInit')
    ## point of umbrella
    xsdInitCtl = 1 # starting spoke
    while xsdInitCtl != 0:
        logg('loop xsdInitCtl = ' + xsdInitCtl.__str__())
        if (xsdInitCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdInitCtl == 1):
            logg('call xsdInit_1')
            xsdInit_1()
            logg('after call xsdInit_1')
            # test and adjust for new spoke
            xsdInitCtl = chk(xsdInitCtl)

        else:
            #final
            logg('final xsdInit')    
            xsdInitCtl = 0 # break
        #endif
    #wend
#end xsdInit

def xsdbang_1():
    global p
    logg('xsdbang_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdbang-1 processing verb ( swap ) ')
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
    logg('for xsdbang-1 processing verb ( dup ) ')
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
    logg('for xsdbang-1 processing verb ( msg ) ')
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
    logg('for xsdbang-1 processing verb ( dup ) ')
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
    logg('for xsdbang-1 processing text ')
    logg("""@eofeof""")
    if (r == p['OK']):
        logg('push text ' + """@eofeof""")
        datPush("@eofeof")
        logg('after ' + """@eofeof""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdbang-1 processing verb ( <> ) ')
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
    logg('for xsdbang-1 processing text ')
    logg(""" into """)
    if (r == p['OK']):
        logg('push text ' + """ into """)
        datPush(" into ")
        logg('after ' + """ into """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdbang-1 processing verb ( msg ) ')
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
    logg('for xsdbang-1 processing verb ( swap ) ')
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
    logg('for xsdbang-1 processing verb ( dup ) ')
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
    logg('for xsdbang-1 processing verb ( msg ) ')
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
    logg('for xsdbang-1 processing verb ( ! ) ')
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
    logg('final xsdbang_1')
#end xsdbang_1

def xsdbang_2():
    global p
    logg('xsdbang_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdbang-2 processing text ')
    logg("""detected end of file""")
    if (r == p['OK']):
        logg('push text ' + """detected end of file""")
        datPush("detected end of file")
        logg('after ' + """detected end of file""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdbang-2 processing verb ( msg ) ')
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
    logg('for xsdbang-2 processing verb ( dumpNDS ) ')
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
    logg('for xsdbang-2 processing verb ( .s ) ')
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
    logg('for xsdbang-2 processing text ')
    logg("""wait""")
    if (r == p['OK']):
        logg('push text ' + """wait""")
        datPush("wait")
        logg('after ' + """wait""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdbang-2 processing verb ( ask ) ')
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
    logg('for xsdbang-2 processing verb ( exit ) ')
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
    logg('final xsdbang_2')
#end xsdbang_2

def xsdbang (x):
    global p
    logg('begin xsdbang')
    ## point of umbrella
    xsdbangCtl = 1 # starting spoke
    while xsdbangCtl != 0:
        logg('loop xsdbangCtl = ' + xsdbangCtl.__str__())
        if (xsdbangCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdbangCtl == 1):
            logg('call xsdbang_1')
            xsdbang_1()
            logg('after call xsdbang_1')
            # test and adjust for new spoke
            xsdbangCtl = chk(xsdbangCtl)

        elif (xsdbangCtl == 2):
            logg('call xsdbang_2')
            xsdbang_2()
            logg('after call xsdbang_2')
            # test and adjust for new spoke
            xsdbangCtl = chk(xsdbangCtl)

        else:
            #final
            logg('final xsdbang')    
            xsdbangCtl = 0 # break
        #endif
    #wend
#end xsdbang

def xsda_1():
    global p
    logg('xsda_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsda-1 processing verb ( fwhite ) ')
    if (r == p['OK']):
        logg('call fwhite ')
        p['sy']['fwhite'](p)
        logg('after fwhite')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsda-1 processing verb ( fioi ) ')
    if (r == p['OK']):
        logg('call fioi ')
        p['sy']['fioi'](p)
        logg('after fioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsda-1 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsda-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsda-1 processing verb ( xsda2 ) ')
    if (r == p['OK']):
        logg('call xsda2 ')
        p['sy']['xsda2'](p)
        logg('after xsda2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsda-1 processing verb ( tail. ) ')
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
    logg('final xsda_1')
#end xsda_1

def xsda (x):
    global p
    logg('begin xsda')
    ## point of umbrella
    xsdaCtl = 1 # starting spoke
    while xsdaCtl != 0:
        logg('loop xsdaCtl = ' + xsdaCtl.__str__())
        if (xsdaCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdaCtl == 1):
            logg('call xsda_1')
            xsda_1()
            logg('after call xsda_1')
            # test and adjust for new spoke
            xsdaCtl = chk(xsdaCtl)

        else:
            #final
            logg('final xsda')    
            xsdaCtl = 0 # break
        #endif
    #wend
#end xsda

def xsda2_1():
    global p
    logg('xsda2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsda2-1 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsda2-1 processing verb ( @ ) ')
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
    logg('for xsda2-1 processing text ')
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
    logg('for xsda2-1 processing verb ( = ) ')
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
    logg('for xsda2-1 processing verb ( xsdb ) ')
    if (r == p['OK']):
        logg('call xsdb ')
        p['sy']['xsdb'](p)
        logg('after xsdb')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsda2_1')
#end xsda2_1

def xsda2_2():
    global p
    logg('xsda2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsda2-2 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsda2-2 processing verb ( @ ) ')
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
    logg('for xsda2-2 processing text ')
    logg("""@eofeof""")
    if (r == p['OK']):
        logg('push text ' + """@eofeof""")
        datPush("@eofeof")
        logg('after ' + """@eofeof""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsda2-2 processing verb ( = ) ')
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
    logg('for xsda2-2 processing verb ( xsdFinal ) ')
    if (r == p['OK']):
        logg('call xsdFinal ')
        p['sy']['xsdFinal'](p)
        logg('after xsdFinal')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsda2-2 processing verb ( exit ) ')
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
    logg('final xsda2_2')
#end xsda2_2

def xsda2_3():
    global p
    logg('xsda2_3')
    datPush(p['OK'])

    #final
    logg('final xsda2_3')
#end xsda2_3

def xsda2 (x):
    global p
    logg('begin xsda2')
    ## point of umbrella
    xsda2Ctl = 1 # starting spoke
    while xsda2Ctl != 0:
        logg('loop xsda2Ctl = ' + xsda2Ctl.__str__())
        if (xsda2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsda2Ctl == 1):
            logg('call xsda2_1')
            xsda2_1()
            logg('after call xsda2_1')
            # test and adjust for new spoke
            xsda2Ctl = chk(xsda2Ctl)

        elif (xsda2Ctl == 2):
            logg('call xsda2_2')
            xsda2_2()
            logg('after call xsda2_2')
            # test and adjust for new spoke
            xsda2Ctl = chk(xsda2Ctl)

        elif (xsda2Ctl == 3):
            logg('call xsda2_3')
            xsda2_3()
            logg('after call xsda2_3')
            # test and adjust for new spoke
            xsda2Ctl = chk(xsda2Ctl)

        else:
            #final
            logg('final xsda2')    
            xsda2Ctl = 0 # break
        #endif
    #wend
#end xsda2

def xsdb_1():
    global p
    logg('xsdb_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdb-1 processing verb ( fwhite ) ')
    if (r == p['OK']):
        logg('call fwhite ')
        p['sy']['fwhite'](p)
        logg('after fwhite')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdb-1 processing verb ( fioi ) ')
    if (r == p['OK']):
        logg('call fioi ')
        p['sy']['fioi'](p)
        logg('after fioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdb-1 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdb-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdb-1 processing verb ( ... ) ')
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
    logg('final xsdb_1')
#end xsdb_1

def xsdb_2():
    global p
    logg('xsdb_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdb-2 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdb-2 processing verb ( @ ) ')
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
    logg('for xsdb-2 processing text ')
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
    logg('for xsdb-2 processing verb ( = ) ')
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
    logg('for xsdb-2 processing verb ( tillComment ) ')
    if (r == p['OK']):
        logg('call tillComment ')
        p['sy']['tillComment'](p)
        logg('after tillComment')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdb_2')
#end xsdb_2

def xsdb_3():
    global p
    logg('xsdb_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdb-3 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdb-3 processing verb ( @ ) ')
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
    logg('for xsdb-3 processing text ')
    logg("""!""")
    if (r == p['OK']):
        logg('push text ' + """!""")
        datPush("!")
        logg('after ' + """!""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdb-3 processing verb ( = ) ')
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
    logg('for xsdb-3 processing verb ( tillComment ) ')
    if (r == p['OK']):
        logg('call tillComment ')
        p['sy']['tillComment'](p)
        logg('after tillComment')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdb_3')
#end xsdb_3

def xsdb_4():
    global p
    logg('xsdb_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdb-4 processing text ')
    logg(""" />""")
    if (r == p['OK']):
        logg('push text ' + """ />""")
        datPush(" />")
        logg('after ' + """ />""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdb-4 processing verb ( fctillor ) ')
    if (r == p['OK']):
        logg('call fctillor ')
        p['sy']['fctillor'](p)
        logg('after fctillor')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdb-4 processing verb ( xsdd ) ')
    if (r == p['OK']):
        logg('call xsdd ')
        p['sy']['xsdd'](p)
        logg('after xsdd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdb_4')
#end xsdb_4

def xsdb (x):
    global p
    logg('begin xsdb')
    ## point of umbrella
    xsdbCtl = 1 # starting spoke
    while xsdbCtl != 0:
        logg('loop xsdbCtl = ' + xsdbCtl.__str__())
        if (xsdbCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdbCtl == 1):
            logg('call xsdb_1')
            xsdb_1()
            logg('after call xsdb_1')
            # test and adjust for new spoke
            xsdbCtl = chk(xsdbCtl)

        elif (xsdbCtl == 2):
            logg('call xsdb_2')
            xsdb_2()
            logg('after call xsdb_2')
            # test and adjust for new spoke
            xsdbCtl = chk(xsdbCtl)

        elif (xsdbCtl == 3):
            logg('call xsdb_3')
            xsdb_3()
            logg('after call xsdb_3')
            # test and adjust for new spoke
            xsdbCtl = chk(xsdbCtl)

        elif (xsdbCtl == 4):
            logg('call xsdb_4')
            xsdb_4()
            logg('after call xsdb_4')
            # test and adjust for new spoke
            xsdbCtl = chk(xsdbCtl)

        else:
            #final
            logg('final xsdb')    
            xsdbCtl = 0 # break
        #endif
    #wend
#end xsdb

def xsdd_1():
    global p
    logg('xsdd_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdd-1 processing verb ( ioi ) ')
    if (r == p['OK']):
        logg('call ioi ')
        p['sy']['ioi'](p)
        logg('after ioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd-1 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd-1 processing verb ( ... ) ')
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
    logg('final xsdd_1')
#end xsdd_1

def xsdd_2():
    global p
    logg('xsdd_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdd-2 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd-2 processing verb ( @ ) ')
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
    logg('for xsdd-2 processing text ')
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
    logg('for xsdd-2 processing verb ( = ) ')
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
    logg('for xsdd-2 processing verb ( xsdd3 ) ')
    if (r == p['OK']):
        logg('call xsdd3 ')
        p['sy']['xsdd3'](p)
        logg('after xsdd3')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdd_2')
#end xsdd_2

def xsdd_3():
    global p
    logg('xsdd_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdd-3 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd-3 processing verb ( ! ) ')
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
    logg('for xsdd-3 processing verb ( xsdd2 ) ')
    if (r == p['OK']):
        logg('call xsdd2 ')
        p['sy']['xsdd2'](p)
        logg('after xsdd2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdd_3')
#end xsdd_3

def xsdd (x):
    global p
    logg('begin xsdd')
    ## point of umbrella
    xsddCtl = 1 # starting spoke
    while xsddCtl != 0:
        logg('loop xsddCtl = ' + xsddCtl.__str__())
        if (xsddCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsddCtl == 1):
            logg('call xsdd_1')
            xsdd_1()
            logg('after call xsdd_1')
            # test and adjust for new spoke
            xsddCtl = chk(xsddCtl)

        elif (xsddCtl == 2):
            logg('call xsdd_2')
            xsdd_2()
            logg('after call xsdd_2')
            # test and adjust for new spoke
            xsddCtl = chk(xsddCtl)

        elif (xsddCtl == 3):
            logg('call xsdd_3')
            xsdd_3()
            logg('after call xsdd_3')
            # test and adjust for new spoke
            xsddCtl = chk(xsddCtl)

        else:
            #final
            logg('final xsdd')    
            xsddCtl = 0 # break
        #endif
    #wend
#end xsdd

def xsdd3_1():
    global p
    logg('xsdd3_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdd3-1 processing verb ( checkName ) ')
    if (r == p['OK']):
        logg('call checkName ')
        p['sy']['checkName'](p)
        logg('after checkName')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd3-1 processing verb ( unstackParent ) ')
    if (r == p['OK']):
        logg('call unstackParent ')
        p['sy']['unstackParent'](p)
        logg('after unstackParent')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdd3_1')
#end xsdd3_1

def xsdd3_2():
    global p
    logg('xsdd3_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdd3-2 processing verb ( xsdStop ) ')
    if (r == p['OK']):
        logg('call xsdStop ')
        p['sy']['xsdStop'](p)
        logg('after xsdStop')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdd3_2')
#end xsdd3_2

def xsdd3 (x):
    global p
    logg('begin xsdd3')
    ## point of umbrella
    xsdd3Ctl = 1 # starting spoke
    while xsdd3Ctl != 0:
        logg('loop xsdd3Ctl = ' + xsdd3Ctl.__str__())
        if (xsdd3Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdd3Ctl == 1):
            logg('call xsdd3_1')
            xsdd3_1()
            logg('after call xsdd3_1')
            # test and adjust for new spoke
            xsdd3Ctl = chk(xsdd3Ctl)

        elif (xsdd3Ctl == 2):
            logg('call xsdd3_2')
            xsdd3_2()
            logg('after call xsdd3_2')
            # test and adjust for new spoke
            xsdd3Ctl = chk(xsdd3Ctl)

        else:
            #final
            logg('final xsdd3')    
            xsdd3Ctl = 0 # break
        #endif
    #wend
#end xsdd3

def xsdStop_1():
    global p
    logg('xsdStop_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdStop-1 processing verb ( dumpNDS ) ')
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
    logg('for xsdStop-1 processing verb ( .s ) ')
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
    logg('for xsdStop-1 processing text ')
    logg("""wait""")
    if (r == p['OK']):
        logg('push text ' + """wait""")
        datPush("wait")
        logg('after ' + """wait""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdStop-1 processing verb ( ask ) ')
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
    logg('for xsdStop-1 processing verb ( exit ) ')
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
    logg('final xsdStop_1')
#end xsdStop_1

def xsdStop (x):
    global p
    logg('begin xsdStop')
    ## point of umbrella
    xsdStopCtl = 1 # starting spoke
    while xsdStopCtl != 0:
        logg('loop xsdStopCtl = ' + xsdStopCtl.__str__())
        if (xsdStopCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdStopCtl == 1):
            logg('call xsdStop_1')
            xsdStop_1()
            logg('after call xsdStop_1')
            # test and adjust for new spoke
            xsdStopCtl = chk(xsdStopCtl)

        else:
            #final
            logg('final xsdStop')    
            xsdStopCtl = 0 # break
        #endif
    #wend
#end xsdStop

def xsdd2_1():
    global p
    logg('xsdd2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdd2-1 processing verb ( fioi ) ')
    if (r == p['OK']):
        logg('call fioi ')
        p['sy']['fioi'](p)
        logg('after fioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-1 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-1 processing verb ( ... ) ')
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
    logg('final xsdd2_1')
#end xsdd2_1

def xsdd2_2():
    global p
    logg('xsdd2_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdd2-2 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-2 processing verb ( @ ) ')
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
    logg('for xsdd2-2 processing text ')
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
    logg('for xsdd2-2 processing verb ( = ) ')
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
    logg('for xsdd2-2 processing text ')
    logg(""" />""")
    if (r == p['OK']):
        logg('push text ' + """ />""")
        datPush(" />")
        logg('after ' + """ />""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-2 processing verb ( fctillor ) ')
    if (r == p['OK']):
        logg('call fctillor ')
        p['sy']['fctillor'](p)
        logg('after fctillor')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-2 processing verb ( dup ) ')
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
    logg('for xsdd2-2 processing text ')
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
    logg('for xsdd2-2 processing verb ( find ) ')
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
    logg('for xsdd2-2 processing verb ( cut ) ')
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
    logg('for xsdd2-2 processing verb ( writeAtt ) ')
    if (r == p['OK']):
        logg('call writeAtt ')
        p['sy']['writeAtt'](p)
        logg('after writeAtt')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-2 processing verb ( tail. ) ')
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
    logg('final xsdd2_2')
#end xsdd2_2

def xsdd2_3():
    global p
    logg('xsdd2_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdd2-3 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-3 processing verb ( @ ) ')
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
    logg('for xsdd2-3 processing text ')
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
    logg('for xsdd2-3 processing verb ( = ) ')
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
    logg('for xsdd2-3 processing verb ( fioi ) ')
    if (r == p['OK']):
        logg('call fioi ')
        p['sy']['fioi'](p)
        logg('after fioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-3 processing verb ( detectID ) ')
    if (r == p['OK']):
        logg('call detectID ')
        p['sy']['detectID'](p)
        logg('after detectID')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdd2_3')
#end xsdd2_3

def xsdd2_4():
    global p
    logg('xsdd2_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for xsdd2-4 processing text ')
    logg("""cx""")
    if (r == p['OK']):
        logg('push text ' + """cx""")
        datPush("cx")
        logg('after ' + """cx""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-4 processing verb ( @ ) ')
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
    logg('for xsdd2-4 processing text ')
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
    logg('for xsdd2-4 processing verb ( = ) ')
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
    logg('for xsdd2-4 processing verb ( stackParents ) ')
    if (r == p['OK']):
        logg('call stackParents ')
        p['sy']['stackParents'](p)
        logg('after stackParents')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for xsdd2-4 processing verb ( detectID ) ')
    if (r == p['OK']):
        logg('call detectID ')
        p['sy']['detectID'](p)
        logg('after detectID')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final xsdd2_4')
#end xsdd2_4

def xsdd2 (x):
    global p
    logg('begin xsdd2')
    ## point of umbrella
    xsdd2Ctl = 1 # starting spoke
    while xsdd2Ctl != 0:
        logg('loop xsdd2Ctl = ' + xsdd2Ctl.__str__())
        if (xsdd2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (xsdd2Ctl == 1):
            logg('call xsdd2_1')
            xsdd2_1()
            logg('after call xsdd2_1')
            # test and adjust for new spoke
            xsdd2Ctl = chk(xsdd2Ctl)

        elif (xsdd2Ctl == 2):
            logg('call xsdd2_2')
            xsdd2_2()
            logg('after call xsdd2_2')
            # test and adjust for new spoke
            xsdd2Ctl = chk(xsdd2Ctl)

        elif (xsdd2Ctl == 3):
            logg('call xsdd2_3')
            xsdd2_3()
            logg('after call xsdd2_3')
            # test and adjust for new spoke
            xsdd2Ctl = chk(xsdd2Ctl)

        elif (xsdd2Ctl == 4):
            logg('call xsdd2_4')
            xsdd2_4()
            logg('after call xsdd2_4')
            # test and adjust for new spoke
            xsdd2Ctl = chk(xsdd2Ctl)

        else:
            #final
            logg('final xsdd2')    
            xsdd2Ctl = 0 # break
        #endif
    #wend
#end xsdd2

def writeAtt_1():
    global p
    logg('writeAtt_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for writeAtt-1 processing text ')
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
    logg('for writeAtt-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeAtt-1 processing verb ( drop ) ')
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
    logg('for writeAtt-1 processing text ')
    logg("""ax""")
    if (r == p['OK']):
        logg('push text ' + """ax""")
        datPush("ax")
        logg('after ' + """ax""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeAtt-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeAtt-1 processing text ')
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
    logg('for writeAtt-1 processing verb ( @ ) ')
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
    logg('for writeAtt-1 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeAtt-1 processing verb ( @ ) ')
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
    logg('for writeAtt-1 processing text ')
    logg("""$""")
    if (r == p['OK']):
        logg('push text ' + """$""")
        datPush("$")
        logg('after ' + """$""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeAtt-1 processing verb ( cat ) ')
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
    logg('for writeAtt-1 processing text ')
    logg("""ax""")
    if (r == p['OK']):
        logg('push text ' + """ax""")
        datPush("ax")
        logg('after ' + """ax""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for writeAtt-1 processing verb ( @ ) ')
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
    logg('for writeAtt-1 processing verb ( cat ) ')
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
    logg('for writeAtt-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final writeAtt_1')
#end writeAtt_1

def writeAtt (x):
    global p
    logg('begin writeAtt')
    ## point of umbrella
    writeAttCtl = 1 # starting spoke
    while writeAttCtl != 0:
        logg('loop writeAttCtl = ' + writeAttCtl.__str__())
        if (writeAttCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (writeAttCtl == 1):
            logg('call writeAtt_1')
            writeAtt_1()
            logg('after call writeAtt_1')
            # test and adjust for new spoke
            writeAttCtl = chk(writeAttCtl)

        else:
            #final
            logg('final writeAtt')    
            writeAttCtl = 0 # break
        #endif
    #wend
#end writeAtt

def stackParents_1():
    global p
    logg('stackParents_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for stackParents-1 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for stackParents-1 processing verb ( @ ) ')
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
    logg('for stackParents-1 processing text ')
    logg("""parents""")
    if (r == p['OK']):
        logg('push text ' + """parents""")
        datPush("parents")
        logg('after ' + """parents""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for stackParents-1 processing verb ( @ ) ')
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
    logg('for stackParents-1 processing verb ( dup ) ')
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
    logg('for stackParents-1 processing verb ( ar# ) ')
    if (r == p['OK']):
        logg('call ar# ')
        p['sy']['ar#'](p)
        logg('after ar#')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for stackParents-1 processing verb ( swap ) ')
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
    logg('for stackParents-1 processing verb ( ar! ) ')
    if (r == p['OK']):
        logg('call ar! ')
        p['sy']['ar!'](p)
        logg('after ar!')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for stackParents-1 processing text ')
    logg("""parents""")
    if (r == p['OK']):
        logg('push text ' + """parents""")
        datPush("parents")
        logg('after ' + """parents""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for stackParents-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for stackParents-1 processing verb ( xsdc2 ) ')
    if (r == p['OK']):
        logg('call xsdc2 ')
        p['sy']['xsdc2'](p)
        logg('after xsdc2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final stackParents_1')
#end stackParents_1

def stackParents (x):
    global p
    logg('begin stackParents')
    ## point of umbrella
    stackParentsCtl = 1 # starting spoke
    while stackParentsCtl != 0:
        logg('loop stackParentsCtl = ' + stackParentsCtl.__str__())
        if (stackParentsCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (stackParentsCtl == 1):
            logg('call stackParents_1')
            stackParents_1()
            logg('after call stackParents_1')
            # test and adjust for new spoke
            stackParentsCtl = chk(stackParentsCtl)

        else:
            #final
            logg('final stackParents')    
            stackParentsCtl = 0 # break
        #endif
    #wend
#end stackParents

def tillComment_1():
    global p
    logg('tillComment_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for tillComment-1 processing text ')
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
    logg('for tillComment-1 processing verb ( ftlc ) ')
    if (r == p['OK']):
        logg('call ftlc ')
        p['sy']['ftlc'](p)
        logg('after ftlc')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for tillComment-1 processing verb ( fioi ) ')
    if (r == p['OK']):
        logg('call fioi ')
        p['sy']['fioi'](p)
        logg('after fioi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for tillComment-1 processing verb ( drops ) ')
    if (r == p['OK']):
        logg('call drops ')
        p['sy']['drops'](p)
        logg('after drops')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final tillComment_1')
#end tillComment_1

def tillComment (x):
    global p
    logg('begin tillComment')
    ## point of umbrella
    tillCommentCtl = 1 # starting spoke
    while tillCommentCtl != 0:
        logg('loop tillCommentCtl = ' + tillCommentCtl.__str__())
        if (tillCommentCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (tillCommentCtl == 1):
            logg('call tillComment_1')
            tillComment_1()
            logg('after call tillComment_1')
            # test and adjust for new spoke
            tillCommentCtl = chk(tillCommentCtl)

        else:
            #final
            logg('final tillComment')    
            tillCommentCtl = 0 # break
        #endif
    #wend
#end tillComment

def detectID_1():
    global p
    logg('detectID_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for detectID-1 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-1 processing verb ( @ ) ')
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
    logg('for detectID-1 processing text ')
    logg("""$""")
    if (r == p['OK']):
        logg('push text ' + """$""")
        datPush("$")
        logg('after ' + """$""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-1 processing verb ( cat ) ')
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
    logg('for detectID-1 processing text ')
    logg("""id""")
    if (r == p['OK']):
        logg('push text ' + """id""")
        datPush("id")
        logg('after ' + """id""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-1 processing verb ( cat ) ')
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
    logg('for detectID-1 processing verb ( @ ) ')
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
    logg('for detectID-1 processing text ')
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
    logg('for detectID-1 processing verb ( <> ) ')
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
    logg('for detectID-1 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-1 processing verb ( @ ) ')
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
    logg('for detectID-1 processing text ')
    logg("""$""")
    if (r == p['OK']):
        logg('push text ' + """$""")
        datPush("$")
        logg('after ' + """$""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-1 processing verb ( cat ) ')
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
    logg('for detectID-1 processing text ')
    logg("""id""")
    if (r == p['OK']):
        logg('push text ' + """id""")
        datPush("id")
        logg('after ' + """id""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-1 processing verb ( cat ) ')
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
    logg('for detectID-1 processing verb ( @ ) ')
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
    logg('for detectID-1 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-1 processing verb ( @ ) ')
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
    logg('for detectID-1 processing text ')
    logg("""$$id""")
    if (r == p['OK']):
        logg('push text ' + """$$id""")
        datPush("$$id")
        logg('after ' + """$$id""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-1 processing verb ( cat ) ')
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
    logg('for detectID-1 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final detectID_1')
#end detectID_1

def detectID_2():
    global p
    logg('detectID_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for detectID-2 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-2 processing verb ( @ ) ')
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
    logg('for detectID-2 processing text ')
    logg("""$""")
    if (r == p['OK']):
        logg('push text ' + """$""")
        datPush("$")
        logg('after ' + """$""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-2 processing verb ( cat ) ')
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
    logg('for detectID-2 processing text ')
    logg("""Id""")
    if (r == p['OK']):
        logg('push text ' + """Id""")
        datPush("Id")
        logg('after ' + """Id""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-2 processing verb ( cat ) ')
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
    logg('for detectID-2 processing verb ( @ ) ')
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
    logg('for detectID-2 processing text ')
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
    logg('for detectID-2 processing verb ( <> ) ')
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
    logg('for detectID-2 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-2 processing verb ( @ ) ')
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
    logg('for detectID-2 processing text ')
    logg("""$""")
    if (r == p['OK']):
        logg('push text ' + """$""")
        datPush("$")
        logg('after ' + """$""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-2 processing verb ( cat ) ')
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
    logg('for detectID-2 processing text ')
    logg("""Id""")
    if (r == p['OK']):
        logg('push text ' + """Id""")
        datPush("Id")
        logg('after ' + """Id""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-2 processing verb ( cat ) ')
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
    logg('for detectID-2 processing verb ( @ ) ')
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
    logg('for detectID-2 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-2 processing verb ( @ ) ')
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
    logg('for detectID-2 processing text ')
    logg("""$$id""")
    if (r == p['OK']):
        logg('push text ' + """$$id""")
        datPush("$$id")
        logg('after ' + """$$id""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-2 processing verb ( cat ) ')
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
    logg('for detectID-2 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final detectID_2')
#end detectID_2

def detectID_3():
    global p
    logg('detectID_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for detectID-3 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-3 processing verb ( @ ) ')
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
    logg('for detectID-3 processing text ')
    logg("""$""")
    if (r == p['OK']):
        logg('push text ' + """$""")
        datPush("$")
        logg('after ' + """$""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-3 processing verb ( cat ) ')
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
    logg('for detectID-3 processing text ')
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
    logg('for detectID-3 processing verb ( cat ) ')
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
    logg('for detectID-3 processing verb ( @ ) ')
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
    logg('for detectID-3 processing text ')
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
    logg('for detectID-3 processing verb ( <> ) ')
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
    logg('for detectID-3 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-3 processing verb ( @ ) ')
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
    logg('for detectID-3 processing text ')
    logg("""$""")
    if (r == p['OK']):
        logg('push text ' + """$""")
        datPush("$")
        logg('after ' + """$""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-3 processing verb ( cat ) ')
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
    logg('for detectID-3 processing text ')
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
    logg('for detectID-3 processing verb ( cat ) ')
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
    logg('for detectID-3 processing verb ( @ ) ')
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
    logg('for detectID-3 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-3 processing verb ( @ ) ')
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
    logg('for detectID-3 processing text ')
    logg("""$$id""")
    if (r == p['OK']):
        logg('push text ' + """$$id""")
        datPush("$$id")
        logg('after ' + """$$id""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-3 processing verb ( cat ) ')
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
    logg('for detectID-3 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final detectID_3')
#end detectID_3

def detectID_4():
    global p
    logg('detectID_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for detectID-4 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-4 processing verb ( @ ) ')
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
    logg('for detectID-4 processing text ')
    logg("""$""")
    if (r == p['OK']):
        logg('push text ' + """$""")
        datPush("$")
        logg('after ' + """$""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-4 processing verb ( cat ) ')
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
    logg('for detectID-4 processing text ')
    logg("""Name""")
    if (r == p['OK']):
        logg('push text ' + """Name""")
        datPush("Name")
        logg('after ' + """Name""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-4 processing verb ( cat ) ')
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
    logg('for detectID-4 processing verb ( @ ) ')
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
    logg('for detectID-4 processing text ')
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
    logg('for detectID-4 processing verb ( <> ) ')
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
    logg('for detectID-4 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-4 processing verb ( @ ) ')
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
    logg('for detectID-4 processing text ')
    logg("""$""")
    if (r == p['OK']):
        logg('push text ' + """$""")
        datPush("$")
        logg('after ' + """$""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-4 processing verb ( cat ) ')
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
    logg('for detectID-4 processing text ')
    logg("""Name""")
    if (r == p['OK']):
        logg('push text ' + """Name""")
        datPush("Name")
        logg('after ' + """Name""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-4 processing verb ( cat ) ')
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
    logg('for detectID-4 processing verb ( @ ) ')
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
    logg('for detectID-4 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-4 processing verb ( @ ) ')
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
    logg('for detectID-4 processing text ')
    logg("""$$id""")
    if (r == p['OK']):
        logg('push text ' + """$$id""")
        datPush("$$id")
        logg('after ' + """$$id""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-4 processing verb ( cat ) ')
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
    logg('for detectID-4 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final detectID_4')
#end detectID_4

def detectID_5():
    global p
    logg('detectID_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for detectID-5 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-5 processing verb ( @ ) ')
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
    logg('for detectID-5 processing text ')
    logg("""en""")
    if (r == p['OK']):
        logg('push text ' + """en""")
        datPush("en")
        logg('after ' + """en""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-5 processing verb ( @ ) ')
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
    logg('for detectID-5 processing text ')
    logg("""$$id""")
    if (r == p['OK']):
        logg('push text ' + """$$id""")
        datPush("$$id")
        logg('after ' + """$$id""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for detectID-5 processing verb ( cat ) ')
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
    logg('for detectID-5 processing verb ( xsdbang ) ')
    if (r == p['OK']):
        logg('call xsdbang ')
        p['sy']['xsdbang'](p)
        logg('after xsdbang')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final detectID_5')
#end detectID_5

def detectID (x):
    global p
    logg('begin detectID')
    ## point of umbrella
    detectIDCtl = 1 # starting spoke
    while detectIDCtl != 0:
        logg('loop detectIDCtl = ' + detectIDCtl.__str__())
        if (detectIDCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (detectIDCtl == 1):
            logg('call detectID_1')
            detectID_1()
            logg('after call detectID_1')
            # test and adjust for new spoke
            detectIDCtl = chk(detectIDCtl)

        elif (detectIDCtl == 2):
            logg('call detectID_2')
            detectID_2()
            logg('after call detectID_2')
            # test and adjust for new spoke
            detectIDCtl = chk(detectIDCtl)

        elif (detectIDCtl == 3):
            logg('call detectID_3')
            detectID_3()
            logg('after call detectID_3')
            # test and adjust for new spoke
            detectIDCtl = chk(detectIDCtl)

        elif (detectIDCtl == 4):
            logg('call detectID_4')
            detectID_4()
            logg('after call detectID_4')
            # test and adjust for new spoke
            detectIDCtl = chk(detectIDCtl)

        elif (detectIDCtl == 5):
            logg('call detectID_5')
            detectID_5()
            logg('after call detectID_5')
            # test and adjust for new spoke
            detectIDCtl = chk(detectIDCtl)

        else:
            #final
            logg('final detectID')    
            detectIDCtl = 0 # break
        #endif
    #wend
#end detectID

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

    # paragraph xsdVersion
    p['sy']['xsdVersion'] = xsdVersion
    #

    # paragraph xsdmain
    p['sy']['xsdmain'] = xsdmain
    #

    # paragraph xsdInit
    p['sy']['xsdInit'] = xsdInit
    #

    # paragraph xsdbang
    p['sy']['xsdbang'] = xsdbang
    #

    # paragraph xsda
    p['sy']['xsda'] = xsda
    #

    # paragraph xsda2
    p['sy']['xsda2'] = xsda2
    #

    # paragraph xsdb
    p['sy']['xsdb'] = xsdb
    #

    # paragraph xsdd
    p['sy']['xsdd'] = xsdd
    #

    # paragraph xsdd3
    p['sy']['xsdd3'] = xsdd3
    #

    # paragraph xsdStop
    p['sy']['xsdStop'] = xsdStop
    #

    # paragraph xsdd2
    p['sy']['xsdd2'] = xsdd2
    #

    # paragraph writeAtt
    p['sy']['writeAtt'] = writeAtt
    #

    # paragraph stackParents
    p['sy']['stackParents'] = stackParents
    #

    # paragraph tillComment
    p['sy']['tillComment'] = tillComment
    #

    # paragraph detectID
    p['sy']['detectID'] = detectID
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

