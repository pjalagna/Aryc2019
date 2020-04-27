
#file test.py
#generated for test.basii at Thu Apr 23 10:41:13 2020 

# usage 
# import xx
# xx.main(startpoint)
# xx.start(trace)

 
def testMain_1():
    global p
    logg('testMain_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for testMain-1 processing text ')
    logg("""this is one""")
    if (r == p['OK']):
        logg('push text ' + """this is one""")
        datPush("this is one")
        logg('after ' + """this is one""" )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for testMain-1 processing verb ( msg ) ')
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
    logg('for testMain-1 processing verb ( ... ) ')
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
    logg('final testMain_1')
#end testMain_1

def testMain_2():
    global p
    logg('testMain_2')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for testMain-2 processing verb ( tm2 ) ')
    if (r == p['OK']):
        logg('call tm2 ')
        p['sy']['tm2'](p)
        logg('after tm2')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        logg('verb skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    #final
    logg('final testMain_2')
#end testMain_2

def testMain (x):
    global p
    logg('begin testMain')
    ## point of umbrella
    testMainCtl = 1 # starting spoke
    while testMainCtl != 0:
        logg('loop testMainCtl = ' + testMainCtl.__str__())
        if (testMainCtl == -1):
            nop = -1 # false test to set up elif chain

        elif (testMainCtl == 1):
            logg('call testMain_1')
            testMain_1()
            logg('after call testMain_1')
            # test and adjust for new spoke
            testMainCtl = chk(testMainCtl)

        elif (testMainCtl == 2):
            logg('call testMain_2')
            testMain_2()
            logg('after call testMain_2')
            # test and adjust for new spoke
            testMainCtl = chk(testMainCtl)

        else:
            #final
            logg('final testMain')    
            testMainCtl = 0 # break
        #endif
    #wend
#end testMain

def tm2_1():
    global p
    logg('tm2_1')
    datPush(p['OK'])

    r = p['sy']['pop']()
    logg('for tm2-1 processing text ')
    logg("""tm2 """)
    if (r == p['OK']):
        logg('push text ' + """tm2 """)
        datPush("tm2 ")
        logg('after ' + """tm2 """ )
        datPush(p['OK'])
    else:
        logg('text skipped')
        p['sy']['push'](r) # pass nok to next
    #endif

    r = p['sy']['pop']()
    logg('for tm2-1 processing verb ( msg ) ')
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
    logg('final tm2_1')
#end tm2_1

def tm2 (x):
    global p
    logg('begin tm2')
    ## point of umbrella
    tm2Ctl = 1 # starting spoke
    while tm2Ctl != 0:
        logg('loop tm2Ctl = ' + tm2Ctl.__str__())
        if (tm2Ctl == -1):
            nop = -1 # false test to set up elif chain

        elif (tm2Ctl == 1):
            logg('call tm2_1')
            tm2_1()
            logg('after call tm2_1')
            # test and adjust for new spoke
            tm2Ctl = chk(tm2Ctl)

        else:
            #final
            logg('final tm2')    
            tm2Ctl = 0 # break
        #endif
    #wend
#end tm2

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

    # paragraph testMain
    p['sy']['testMain'] = testMain
    #

    # paragraph tm2
    p['sy']['tm2'] = tm2
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

