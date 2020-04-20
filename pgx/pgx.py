
#file pgx.py
#generated for pgxNotes.txt at Mon Apr 13 02:34:44 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def pgmain_1():
    global p
    logg('pgmain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgmain-1 processing verb ( pgf0 ) ')
    if (r == p['OK']):
        logg('call pgf0 ')
        p['sy']['pgf0'](p)
        logg('after pgf0')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgmain-1 processing verb ( loop1 ) ')
    if (r == p['OK']):
        logg('call loop1 ')
        p['sy']['loop1'](p)
        logg('after loop1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final pgmain_1')
#end pgmain_1

def pgmain (x):
    global p
    logg('begin pgmain')
    ## point of umbrella
    pgmainCtl = 1 # starting spoke
    while pgmainCtl != 0:
        logg('loop pgmainCtl = ' + pgmainCtl.__str__())
        if (pgmainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgmainCtl == 1):
            logg('call pgmain_1')
            pgmain_1()
            logg('after call pgmain_1')
            # test and adjust for new spoke
            pgmainCtl = chk(pgmainCtl)

        else:
            #final
            logg('final pgmain')    
            pgmainCtl = 0 # break
        #endif
    #wend
#end pgmain

def loop1_1():
    global p
    logg('loop1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for loop1-1 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loop1-1 processing verb ( @ ) ')
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
    logg('for loop1-1 processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loop1-1 processing verb ( = ) ')
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
    logg('for loop1-1 processing text ')
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
    logg('for loop1-1 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loop1-1 processing verb ( ! ) ')
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
    logg('for loop1-1 processing verb ( tail. ) ')
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
    logg('final loop1_1')
#end loop1_1

def loop1_2():
    global p
    logg('loop1_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for loop1-2 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loop1-2 processing verb ( @ ) ')
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
    logg('for loop1-2 processing text ')
    logg("""exit""")
    if (r == p['OK']):
        logg('push text ' + """exit""")
        datPush("exit")
        logg('after ' + """exit""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loop1-2 processing verb ( = ) ')
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
    logg('final loop1_2')
#end loop1_2

def loop1_3():
    global p
    logg('loop1_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for loop1-3 processing verb ( clausefail ) ')
    if (r == p['OK']):
        logg('call clausefail ')
        p['sy']['clausefail'](p)
        logg('after clausefail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loop1-3 processing verb ( pgf1 ) ')
    if (r == p['OK']):
        logg('call pgf1 ')
        p['sy']['pgf1'](p)
        logg('after pgf1')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loop1-3 processing verb ( cmdfan ) ')
    if (r == p['OK']):
        logg('call cmdfan ')
        p['sy']['cmdfan'](p)
        logg('after cmdfan')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for loop1-3 processing verb ( tail. ) ')
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
    logg('final loop1_3')
#end loop1_3

def loop1 (x):
    global p
    logg('begin loop1')
    ## point of umbrella
    loop1Ctl = 1 # starting spoke
    while loop1Ctl != 0:
        logg('loop loop1Ctl = ' + loop1Ctl.__str__())
        if (loop1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (loop1Ctl == 1):
            logg('call loop1_1')
            loop1_1()
            logg('after call loop1_1')
            # test and adjust for new spoke
            loop1Ctl = chk(loop1Ctl)

        elif (loop1Ctl == 2):
            logg('call loop1_2')
            loop1_2()
            logg('after call loop1_2')
            # test and adjust for new spoke
            loop1Ctl = chk(loop1Ctl)

        elif (loop1Ctl == 3):
            logg('call loop1_3')
            loop1_3()
            logg('after call loop1_3')
            # test and adjust for new spoke
            loop1Ctl = chk(loop1Ctl)

        else:
            #final
            logg('final loop1')    
            loop1Ctl = 0 # break
        #endif
    #wend
#end loop1

def pgf1_1():
    global p
    logg('pgf1_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgf1-1 processing verb ( rwd ) ')
    if (r == p['OK']):
        logg('call rwd ')
        p['sy']['rwd'](p)
        logg('after rwd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf1-1 processing text ')
    logg("""vt""")
    if (r == p['OK']):
        logg('push text ' + """vt""")
        datPush("vt")
        logg('after ' + """vt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for pgf1-1 processing verb ( ! ) ')
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
    logg('final pgf1_1')
#end pgf1_1

def pgf1 (x):
    global p
    logg('begin pgf1')
    ## point of umbrella
    pgf1Ctl = 1 # starting spoke
    while pgf1Ctl != 0:
        logg('loop pgf1Ctl = ' + pgf1Ctl.__str__())
        if (pgf1Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgf1Ctl == 1):
            logg('call pgf1_1')
            pgf1_1()
            logg('after call pgf1_1')
            # test and adjust for new spoke
            pgf1Ctl = chk(pgf1Ctl)

        else:
            #final
            logg('final pgf1')    
            pgf1Ctl = 0 # break
        #endif
    #wend
#end pgf1

def cmdfan_1():
    global p
    logg('cmdfan_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cmdfan-1 processing text ')
    logg("""vt""")
    if (r == p['OK']):
        logg('push text ' + """vt""")
        datPush("vt")
        logg('after ' + """vt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-1 processing verb ( @ ) ')
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
    logg('final cmdfan_1')
#end cmdfan_1

def cmdfan_vtdot():
    global p
    logg('cmdfan_vtdot')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cmdfan-vtdot processing verb ( [[ ) ')
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
    logg('for cmdfan-vtdot processing verb ( 2 ) ')
    if (r == p['OK']):
        logg('call 2 ')
        p['sy']['2'](p)
        logg('after 2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-vtdot processing verb ( ]] ) ')
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
    logg('for cmdfan-vtdot processing text ')
    logg("""vt""")
    if (r == p['OK']):
        logg('push text ' + """vt""")
        datPush("vt")
        logg('after ' + """vt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-vtdot processing verb ( @ ) ')
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
    logg('for cmdfan-vtdot processing text ')
    logg(""";""")
    if (r == p['OK']):
        logg('push text ' + """;""")
        datPush(";")
        logg('after ' + """;""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-vtdot processing verb ( = ) ')
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
    logg('for cmdfan-vtdot processing verb ( vtsemi ) ')
    if (r == p['OK']):
        logg('call vtsemi ')
        p['sy']['vtsemi'](p)
        logg('after vtsemi')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final cmdfan_vtdot')
#end cmdfan_vtdot

def cmdfan_3():
    global p
    logg('cmdfan_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cmdfan-3 processing text ')
    logg("""vt""")
    if (r == p['OK']):
        logg('push text ' + """vt""")
        datPush("vt")
        logg('after ' + """vt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-3 processing verb ( @ ) ')
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
    logg('for cmdfan-3 processing text ')
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
    logg('for cmdfan-3 processing verb ( = ) ')
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
    logg('for cmdfan-3 processing verb ( vttail ) ')
    if (r == p['OK']):
        logg('call vttail ')
        p['sy']['vttail'](p)
        logg('after vttail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final cmdfan_3')
#end cmdfan_3

def cmdfan_4():
    global p
    logg('cmdfan_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cmdfan-4 processing text ')
    logg("""vt""")
    if (r == p['OK']):
        logg('push text ' + """vt""")
        datPush("vt")
        logg('after ' + """vt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-4 processing verb ( @ ) ')
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
    logg('for cmdfan-4 processing text ')
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
    logg('for cmdfan-4 processing verb ( = ) ')
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
    logg('for cmdfan-4 processing verb ( vtcall ) ')
    if (r == p['OK']):
        logg('call vtcall ')
        p['sy']['vtcall'](p)
        logg('after vtcall')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final cmdfan_4')
#end cmdfan_4

def cmdfan_5():
    global p
    logg('cmdfan_5')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cmdfan-5 processing text ')
    logg("""vt""")
    if (r == p['OK']):
        logg('push text ' + """vt""")
        datPush("vt")
        logg('after ' + """vt""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-5 processing verb ( @ ) ')
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
    logg('for cmdfan-5 processing text ')
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
    logg('for cmdfan-5 processing verb ( = ) ')
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
    logg('for cmdfan-5 processing verb ( vtelips ) ')
    if (r == p['OK']):
        logg('call vtelips ')
        p['sy']['vtelips'](p)
        logg('after vtelips')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final cmdfan_5')
#end cmdfan_5

def cmdfan_20():
    global p
    logg('cmdfan_20')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cmdfan-20 processing verb ( dox ) ')
    if (r == p['OK']):
        logg('call dox ')
        p['sy']['dox'](p)
        logg('after dox')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final cmdfan_20')
#end cmdfan_20

def cmdfan_vtelips():
    global p
    logg('cmdfan_vtelips')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for cmdfan-vtelips processing verb ( [[ ) ')
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
    logg('for cmdfan-vtelips processing verb ( 1 ) ')
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
    logg('for cmdfan-vtelips processing verb ( ]] ) ')
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
    logg('for cmdfan-vtelips processing verb ( clausefail ) ')
    if (r == p['OK']):
        logg('call clausefail ')
        p['sy']['clausefail'](p)
        logg('after clausefail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-vtelips processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-vtelips processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for cmdfan-vtelips processing verb ( ! ) ')
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
    logg('final cmdfan_vtelips')
#end cmdfan_vtelips

def cmdfan (x):
    global p
    logg('begin cmdfan')
    ## point of umbrella
    cmdfanCtl = 1 # starting spoke
    while cmdfanCtl != 0:
        logg('loop cmdfanCtl = ' + cmdfanCtl.__str__())
        if (cmdfanCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (cmdfanCtl == 1):
            logg('call cmdfan_1')
            cmdfan_1()
            logg('after call cmdfan_1')
            # test and adjust for new spoke
            cmdfanCtl = chk(cmdfanCtl)

        elif (cmdfanCtl == 2):
            logg('call cmdfan_vtdot')
            cmdfan_vtdot()
            logg('after call cmdfan_vtdot')
            # test and adjust for new spoke
            cmdfanCtl = chk(cmdfanCtl)

        elif (cmdfanCtl == 3):
            logg('call cmdfan_3')
            cmdfan_3()
            logg('after call cmdfan_3')
            # test and adjust for new spoke
            cmdfanCtl = chk(cmdfanCtl)

        elif (cmdfanCtl == 4):
            logg('call cmdfan_4')
            cmdfan_4()
            logg('after call cmdfan_4')
            # test and adjust for new spoke
            cmdfanCtl = chk(cmdfanCtl)

        elif (cmdfanCtl == 5):
            logg('call cmdfan_5')
            cmdfan_5()
            logg('after call cmdfan_5')
            # test and adjust for new spoke
            cmdfanCtl = chk(cmdfanCtl)

        elif (cmdfanCtl == 6):
            logg('call cmdfan_20')
            cmdfan_20()
            logg('after call cmdfan_20')
            # test and adjust for new spoke
            cmdfanCtl = chk(cmdfanCtl)

        elif (cmdfanCtl == 7):
            logg('call cmdfan_vtelips')
            cmdfan_vtelips()
            logg('after call cmdfan_vtelips')
            # test and adjust for new spoke
            cmdfanCtl = chk(cmdfanCtl)

        else:
            #final
            logg('final cmdfan')    
            cmdfanCtl = 0 # break
        #endif
    #wend
#end cmdfan

def vtcall_1():
    global p
    logg('vtcall_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for vtcall-1 processing verb ( rwd ) ')
    if (r == p['OK']):
        logg('call rwd ')
        p['sy']['rwd'](p)
        logg('after rwd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtcall-1 processing verb ( dup ) ')
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
    logg('for vtcall-1 processing text ')
    logg("""pgna""")
    if (r == p['OK']):
        logg('push text ' + """pgna""")
        datPush("pgna")
        logg('after ' + """pgna""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtcall-1 processing verb ( @ ) ')
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
    logg('for vtcall-1 processing verb ( l@ ) ')
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
    logg('for vtcall-1 processing verb ( r< ) ')
    if (r == p['OK']):
        logg('call r< ')
        p['sy']['r<'](p)
        logg('after r<')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtcall-1 processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtcall-1 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtcall-1 processing verb ( ! ) ')
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
    logg('final vtcall_1')
#end vtcall_1

def vtcall (x):
    global p
    logg('begin vtcall')
    ## point of umbrella
    vtcallCtl = 1 # starting spoke
    while vtcallCtl != 0:
        logg('loop vtcallCtl = ' + vtcallCtl.__str__())
        if (vtcallCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (vtcallCtl == 1):
            logg('call vtcall_1')
            vtcall_1()
            logg('after call vtcall_1')
            # test and adjust for new spoke
            vtcallCtl = chk(vtcallCtl)

        else:
            #final
            logg('final vtcall')    
            vtcallCtl = 0 # break
        #endif
    #wend
#end vtcall

def vttail_1():
    global p
    logg('vttail_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for vttail-1 processing verb ( r> ) ')
    if (r == p['OK']):
        logg('call r> ')
        p['sy']['r>'](p)
        logg('after r>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vttail-1 processing verb ( dup ) ')
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
    logg('for vttail-1 processing text ')
    logg("""::""")
    if (r == p['OK']):
        logg('push text ' + """::""")
        datPush("::")
        logg('after ' + """::""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vttail-1 processing verb ( find ) ')
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
    logg('for vttail-1 processing verb ( cut ) ')
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
    logg('for vttail-1 processing verb ( swap ) ')
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
    logg('for vttail-1 processing verb ( drop ) ')
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
    logg('for vttail-1 processing verb ( swap ) ')
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
    logg('for vttail-1 processing verb ( drop ) ')
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
    logg('for vttail-1 processing verb ( l@ ) ')
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
    logg('for vttail-1 processing verb ( r< ) ')
    if (r == p['OK']):
        logg('call r< ')
        p['sy']['r<'](p)
        logg('after r<')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vttail-1 processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vttail-1 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vttail-1 processing verb ( ! ) ')
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
    logg('final vttail_1')
#end vttail_1

def vttail (x):
    global p
    logg('begin vttail')
    ## point of umbrella
    vttailCtl = 1 # starting spoke
    while vttailCtl != 0:
        logg('loop vttailCtl = ' + vttailCtl.__str__())
        if (vttailCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (vttailCtl == 1):
            logg('call vttail_1')
            vttail_1()
            logg('after call vttail_1')
            # test and adjust for new spoke
            vttailCtl = chk(vttailCtl)

        else:
            #final
            logg('final vttail')    
            vttailCtl = 0 # break
        #endif
    #wend
#end vttail

def vtdot_1():
    global p
    logg('vtdot_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for vtdot-1 processing verb ( protected ) ')
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
    logg('for vtdot-1 processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtdot-1 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtdot-1 processing verb ( ! ) ')
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
    logg('final vtdot_1')
#end vtdot_1

def vtdot_2():
    global p
    logg('vtdot_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for vtdot-2 processing verb ( OK ) ')
    if (r == p['OK']):
        logg('call OK ')
        p['sy']['OK'](p)
        logg('after OK')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtdot-2 processing text ')
    logg("""exit""")
    if (r == p['OK']):
        logg('push text ' + """exit""")
        datPush("exit")
        logg('after ' + """exit""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtdot-2 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtdot-2 processing verb ( ! ) ')
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
    logg('final vtdot_2')
#end vtdot_2

def vtdot (x):
    global p
    logg('begin vtdot')
    ## point of umbrella
    vtdotCtl = 1 # starting spoke
    while vtdotCtl != 0:
        logg('loop vtdotCtl = ' + vtdotCtl.__str__())
        if (vtdotCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (vtdotCtl == 1):
            logg('call vtdot_1')
            vtdot_1()
            logg('after call vtdot_1')
            # test and adjust for new spoke
            vtdotCtl = chk(vtdotCtl)

        elif (vtdotCtl == 2):
            logg('call vtdot_2')
            vtdot_2()
            logg('after call vtdot_2')
            # test and adjust for new spoke
            vtdotCtl = chk(vtdotCtl)

        else:
            #final
            logg('final vtdot')    
            vtdotCtl = 0 # break
        #endif
    #wend
#end vtdot

def vtsemi_1():
    global p
    logg('vtsemi_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for vtsemi-1 processing verb ( protected ) ')
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
    logg('for vtsemi-1 processing verb ( NOK ) ')
    if (r == p['OK']):
        logg('call NOK ')
        p['sy']['NOK'](p)
        logg('after NOK')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtsemi-1 processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtsemi-1 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtsemi-1 processing verb ( ! ) ')
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
    logg('final vtsemi_1')
#end vtsemi_1

def vtsemi_2():
    global p
    logg('vtsemi_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for vtsemi-2 processing verb ( NOK ) ')
    if (r == p['OK']):
        logg('call NOK ')
        p['sy']['NOK'](p)
        logg('after NOK')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtsemi-2 processing text ')
    logg("""exit""")
    if (r == p['OK']):
        logg('push text ' + """exit""")
        datPush("exit")
        logg('after ' + """exit""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtsemi-2 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for vtsemi-2 processing verb ( ! ) ')
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
    logg('final vtsemi_2')
#end vtsemi_2

def vtsemi (x):
    global p
    logg('begin vtsemi')
    ## point of umbrella
    vtsemiCtl = 1 # starting spoke
    while vtsemiCtl != 0:
        logg('loop vtsemiCtl = ' + vtsemiCtl.__str__())
        if (vtsemiCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (vtsemiCtl == 1):
            logg('call vtsemi_1')
            vtsemi_1()
            logg('after call vtsemi_1')
            # test and adjust for new spoke
            vtsemiCtl = chk(vtsemiCtl)

        elif (vtsemiCtl == 2):
            logg('call vtsemi_2')
            vtsemi_2()
            logg('after call vtsemi_2')
            # test and adjust for new spoke
            vtsemiCtl = chk(vtsemiCtl)

        else:
            #final
            logg('final vtsemi')    
            vtsemiCtl = 0 # break
        #endif
    #wend
#end vtsemi

def dox_1():
    global p
    logg('dox_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for dox-1 processing verb ( protected ) ')
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
    logg('for dox-1 processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dox-1 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dox-1 processing verb ( ! ) ')
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
    logg('final dox_1')
#end dox_1

def dox_2():
    global p
    logg('dox_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for dox-2 processing verb ( clausefail ) ')
    if (r == p['OK']):
        logg('call clausefail ')
        p['sy']['clausefail'](p)
        logg('after clausefail')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dox-2 processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dox-2 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for dox-2 processing verb ( ! ) ')
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
    logg('final dox_2')
#end dox_2

def dox (x):
    global p
    logg('begin dox')
    ## point of umbrella
    doxCtl = 1 # starting spoke
    while doxCtl != 0:
        logg('loop doxCtl = ' + doxCtl.__str__())
        if (doxCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (doxCtl == 1):
            logg('call dox_1')
            dox_1()
            logg('after call dox_1')
            # test and adjust for new spoke
            doxCtl = chk(doxCtl)

        elif (doxCtl == 2):
            logg('call dox_2')
            dox_2()
            logg('after call dox_2')
            # test and adjust for new spoke
            doxCtl = chk(doxCtl)

        else:
            #final
            logg('final dox')    
            doxCtl = 0 # break
        #endif
    #wend
#end dox

def clausefail_1():
    global p
    logg('clausefail_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for clausefail-1 processing verb ( rwd ) ')
    if (r == p['OK']):
        logg('call rwd ')
        p['sy']['rwd'](p)
        logg('after rwd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-1 processing text ')
    logg("""cf""")
    if (r == p['OK']):
        logg('push text ' + """cf""")
        datPush("cf")
        logg('after ' + """cf""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-1 processing verb ( ! ) ')
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
    logg('for clausefail-1 processing verb ( ... ) ')
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
    logg('final clausefail_1')
#end clausefail_1

def clausefail_2():
    global p
    logg('clausefail_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for clausefail-2 processing text ')
    logg("""cf""")
    if (r == p['OK']):
        logg('push text ' + """cf""")
        datPush("cf")
        logg('after ' + """cf""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-2 processing verb ( @ ) ')
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
    logg('for clausefail-2 processing text ')
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
    logg('for clausefail-2 processing verb ( = ) ')
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
    logg('for clausefail-2 processing verb ( getcfn ) ')
    if (r == p['OK']):
        logg('call getcfn ')
        p['sy']['getcfn'](p)
        logg('after getcfn')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-2 processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-2 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-2 processing verb ( ! ) ')
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
    logg('final clausefail_2')
#end clausefail_2

def clausefail_3():
    global p
    logg('clausefail_3')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for clausefail-3 processing text ')
    logg("""cf""")
    if (r == p['OK']):
        logg('push text ' + """cf""")
        datPush("cf")
        logg('after ' + """cf""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-3 processing verb ( @ ) ')
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
    logg('for clausefail-3 processing text ')
    logg(""";""")
    if (r == p['OK']):
        logg('push text ' + """;""")
        datPush(";")
        logg('after ' + """;""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-3 processing verb ( = ) ')
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
    logg('for clausefail-3 processing text ')
    logg(""";""")
    if (r == p['OK']):
        logg('push text ' + """;""")
        datPush(";")
        logg('after ' + """;""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-3 processing verb ( r> ) ')
    if (r == p['OK']):
        logg('call r> ')
        p['sy']['r>'](p)
        logg('after r>')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-3 processing verb ( cats ) ')
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
    logg('for clausefail-3 processing verb ( r< ) ')
    if (r == p['OK']):
        logg('call r< ')
        p['sy']['r<'](p)
        logg('after r<')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-3 processing text ')
    logg("""more""")
    if (r == p['OK']):
        logg('push text ' + """more""")
        datPush("more")
        logg('after ' + """more""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-3 processing text ')
    logg("""SWloop1""")
    if (r == p['OK']):
        logg('push text ' + """SWloop1""")
        datPush("SWloop1")
        logg('after ' + """SWloop1""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for clausefail-3 processing verb ( ! ) ')
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
    logg('final clausefail_3')
#end clausefail_3

def clausefail_4():
    global p
    logg('clausefail_4')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for clausefail-4 processing verb ( tail. ) ')
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
    logg('final clausefail_4')
#end clausefail_4

def clausefail (x):
    global p
    logg('begin clausefail')
    ## point of umbrella
    clausefailCtl = 1 # starting spoke
    while clausefailCtl != 0:
        logg('loop clausefailCtl = ' + clausefailCtl.__str__())
        if (clausefailCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (clausefailCtl == 1):
            logg('call clausefail_1')
            clausefail_1()
            logg('after call clausefail_1')
            # test and adjust for new spoke
            clausefailCtl = chk(clausefailCtl)

        elif (clausefailCtl == 2):
            logg('call clausefail_2')
            clausefail_2()
            logg('after call clausefail_2')
            # test and adjust for new spoke
            clausefailCtl = chk(clausefailCtl)

        elif (clausefailCtl == 3):
            logg('call clausefail_3')
            clausefail_3()
            logg('after call clausefail_3')
            # test and adjust for new spoke
            clausefailCtl = chk(clausefailCtl)

        elif (clausefailCtl == 4):
            logg('call clausefail_4')
            clausefail_4()
            logg('after call clausefail_4')
            # test and adjust for new spoke
            clausefailCtl = chk(clausefailCtl)

        else:
            #final
            logg('final clausefail')    
            clausefailCtl = 0 # break
        #endif
    #wend
#end clausefail

def getcfn_1():
    global p
    logg('getcfn_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for getcfn-1 processing verb ( rwd ) ')
    if (r == p['OK']):
        logg('call rwd ')
        p['sy']['rwd'](p)
        logg('after rwd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getcfn-1 processing text ')
    logg("""cfn""")
    if (r == p['OK']):
        logg('push text ' + """cfn""")
        datPush("cfn")
        logg('after ' + """cfn""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getcfn-1 processing verb ( ! ) ')
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
    logg('for getcfn-1 processing verb ( rwd ) ')
    if (r == p['OK']):
        logg('call rwd ')
        p['sy']['rwd'](p)
        logg('after rwd')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for getcfn-1 processing verb ( drop ) ')
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
    logg('final getcfn_1')
#end getcfn_1

def getcfn (x):
    global p
    logg('begin getcfn')
    ## point of umbrella
    getcfnCtl = 1 # starting spoke
    while getcfnCtl != 0:
        logg('loop getcfnCtl = ' + getcfnCtl.__str__())
        if (getcfnCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (getcfnCtl == 1):
            logg('call getcfn_1')
            getcfn_1()
            logg('after call getcfn_1')
            # test and adjust for new spoke
            getcfnCtl = chk(getcfnCtl)

        else:
            #final
            logg('final getcfn')    
            getcfnCtl = 0 # break
        #endif
    #wend
#end getcfn

def pgf0_1():
    global p
    logg('pgf0_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for pgf0-1 processing verb ( l@ ) ')
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
    logg('for pgf0-1 processing verb ( r< ) ')
    if (r == p['OK']):
        logg('call r< ')
        p['sy']['r<'](p)
        logg('after r<')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final pgf0_1')
#end pgf0_1

def pgf0 (x):
    global p
    logg('begin pgf0')
    ## point of umbrella
    pgf0Ctl = 1 # starting spoke
    while pgf0Ctl != 0:
        logg('loop pgf0Ctl = ' + pgf0Ctl.__str__())
        if (pgf0Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (pgf0Ctl == 1):
            logg('call pgf0_1')
            pgf0_1()
            logg('after call pgf0_1')
            # test and adjust for new spoke
            pgf0Ctl = chk(pgf0Ctl)

        else:
            #final
            logg('final pgf0')    
            pgf0Ctl = 0 # break
        #endif
    #wend
#end pgf0

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

    # paragraph pgmain
    p['sy']['pgmain'] = pgmain
    #

    # paragraph loop1
    p['sy']['loop1'] = loop1
    #

    # paragraph pgf1
    p['sy']['pgf1'] = pgf1
    #

    # paragraph cmdfan
    p['sy']['cmdfan'] = cmdfan
    #

    # paragraph vtcall
    p['sy']['vtcall'] = vtcall
    #

    # paragraph vttail
    p['sy']['vttail'] = vttail
    #

    # paragraph vtdot
    p['sy']['vtdot'] = vtdot
    #

    # paragraph vtsemi
    p['sy']['vtsemi'] = vtsemi
    #

    # paragraph dox
    p['sy']['dox'] = dox
    #

    # paragraph clausefail
    p['sy']['clausefail'] = clausefail
    #

    # paragraph getcfn
    p['sy']['getcfn'] = getcfn
    #

    # paragraph pgf0
    p['sy']['pgf0'] = pgf0
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

