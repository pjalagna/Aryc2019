
#file mbsi.py
#generated for t.hlp 

 
def st():
    global p
    
    if (p['v']['trace'] == 'on'):
        print('st')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call a')
        #endif
        p['sy']['a'](p)
        if (p['v']['trace'] == 'on'):
            print('after a')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        print('final st')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end st

def start (x):
    global p
    if (p['v']['trace'] == 'on'):
        print('start')
        #print('dat',p['dat'])
    #endif
    datPush(p['NOK'])

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            print('call st')
        #endif
        st()
        if (p['v']['trace'] == 'on'):
            print('after call st')
        #endif
    #endif
    #

    #final
    if (p['v']['trace'] == 'on'):
        print('final start')    
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end start

def aa():
    global p
    
    if (p['v']['trace'] == 'on'):
        print('aa')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "hello "')
        #endif
        datPush("hello ")
        if (p['v']['trace'] == 'on'):
            print('after "hello "')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call g')
        #endif
        p['sy']['g'](p)
        if (p['v']['trace'] == 'on'):
            print('after g')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call msg')
        #endif
        p['sy']['msg'](p)
        if (p['v']['trace'] == 'on'):
            print('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "1"')
        #endif
        datPush("1")
        if (p['v']['trace'] == 'on'):
            print('after "1"')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "E"')
        #endif
        datPush("E")
        if (p['v']['trace'] == 'on'):
            print('after "E"')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call !')
        #endif
        p['sy']['!'](p)
        if (p['v']['trace'] == 'on'):
            print('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call b')
        #endif
        p['sy']['b'](p)
        if (p['v']['trace'] == 'on'):
            print('after b')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "2"')
        #endif
        datPush("2")
        if (p['v']['trace'] == 'on'):
            print('after "2"')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "E"')
        #endif
        datPush("E")
        if (p['v']['trace'] == 'on'):
            print('after "E"')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call !')
        #endif
        p['sy']['!'](p)
        if (p['v']['trace'] == 'on'):
            print('after !')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call b')
        #endif
        p['sy']['b'](p)
        if (p['v']['trace'] == 'on'):
            print('after b')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "done "')
        #endif
        datPush("done ")
        if (p['v']['trace'] == 'on'):
            print('after "done "')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call msg')
        #endif
        p['sy']['msg'](p)
        if (p['v']['trace'] == 'on'):
            print('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        print('final aa')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end aa

def a (x):
    global p
    if (p['v']['trace'] == 'on'):
        print('a')
        #print('dat',p['dat'])
    #endif
    datPush(p['NOK'])

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            print('call aa')
        #endif
        aa()
        if (p['v']['trace'] == 'on'):
            print('after call aa')
        #endif
    #endif
    #

    #final
    if (p['v']['trace'] == 'on'):
        print('final a')    
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end a

def bb():
    global p
    
    if (p['v']['trace'] == 'on'):
        print('bb')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "E"')
        #endif
        datPush("E")
        if (p['v']['trace'] == 'on'):
            print('after "E"')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call @')
        #endif
        p['sy']['@'](p)
        if (p['v']['trace'] == 'on'):
            print('after @')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "1"')
        #endif
        datPush("1")
        if (p['v']['trace'] == 'on'):
            print('after "1"')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call =')
        #endif
        p['sy']['='](p)
        if (p['v']['trace'] == 'on'):
            print('after =')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "one"')
        #endif
        datPush("one")
        if (p['v']['trace'] == 'on'):
            print('after "one"')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call msg')
        #endif
        p['sy']['msg'](p)
        if (p['v']['trace'] == 'on'):
            print('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        print('final bb')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end bb

def bbb():
    global p
    
    if (p['v']['trace'] == 'on'):
        print('bbb')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "two"')
        #endif
        datPush("two")
        if (p['v']['trace'] == 'on'):
            print('after "two"')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call msg')
        #endif
        p['sy']['msg'](p)
        if (p['v']['trace'] == 'on'):
            print('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        print('final bbb')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end bbb

def b (x):
    global p
    if (p['v']['trace'] == 'on'):
        print('b')
        #print('dat',p['dat'])
    #endif
    datPush(p['NOK'])

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            print('call bb')
        #endif
        bb()
        if (p['v']['trace'] == 'on'):
            print('after call bb')
        #endif
    #endif
    #

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            print('call bbb')
        #endif
        bbb()
        if (p['v']['trace'] == 'on'):
            print('after call bbb')
        #endif
    #endif
    #

    #final
    if (p['v']['trace'] == 'on'):
        print('final b')    
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end b

def g1():
    global p
    
    if (p['v']['trace'] == 'on'):
        print('g1')
        #print('dat',p['dat'])
    #endif
    datPush(p['OK'])

    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call "here at g1"')
        #endif
        datPush("here at g1")
        if (p['v']['trace'] == 'on'):
            print('after "here at g1"')
        #endif
        datPush(p['OK'])
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    r = p['sy']['pop']()
    if (r == p['OK']):
        if (p['v']['trace'] == 'on'):
            print('call msg')
        #endif
        p['sy']['msg'](p)
        if (p['v']['trace'] == 'on'):
            print('after msg')
        #endif
        # datPush(p['OK']) # verb supplies ok/nok
    else:
        p['sy']['push'](r) # pass nok to next
    #endif
    
    #final
    if (p['v']['trace'] == 'on'):
        print('final g1')
    #endif
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end g1

def g (x):
    global p
    if (p['v']['trace'] == 'on'):
        print('g')
        #print('dat',p['dat'])
    #endif
    datPush(p['NOK'])

    # 
    r = p['sy']['pop']()
    if(r == p['NOK']):
        if (p['v']['trace'] == 'on'):
            print('call g1')
        #endif
        g1()
        if (p['v']['trace'] == 'on'):
            print('after call g1')
        #endif
    #endif
    #

    #final
    if (p['v']['trace'] == 'on'):
        print('final g')    
    r =  p['sy']['pop']()
    if (r == p['NOK']):
        datPush(p['NOK'])
    else:
        datPush(p['OK'])
    #endif
#end g

def main(trace='off'):
    global p
    p = {}
    p['dat'] = [] # data stack
    p['r'] = [] # r stack
    p['v'] = {} # nds
    p['l'] = {} # lib table
    p['sy'] = {} # symbol table
    p['sy']['pop'] = datPop
    p['sy']['push'] = datPush
    p['v']['trace'] = trace
    prepSy()
    p['OK'] = 'pOK'
    p['NOK'] = 'pNOK'

    # 
    p['sy']['start'] = start
    #

    # 
    p['sy']['a'] = a
    #

    # 
    p['sy']['b'] = b
    #

    # 
    p['sy']['g'] = g
    #

    p['sy']['start'](0) # process begins at start
#end main

# helper rtns 
def datPush(val):
    global p
    p['dat'].append(val)
    if (p['v']['trace'] == 'on'):
        print('push',val)
    #endif
#end datPush

def datPop():
    global p
    v = p['dat'].pop()
    if (p['v']['trace'] == 'on'):
        print('................pop', v)
    #endif
    return(v)
#end datPop

def prepSy():
    global p
    import doVerb
    p = doVerb.init(p) # load vectors
#end prepSy

def dump():
    global p
    return(p)
#end dump

