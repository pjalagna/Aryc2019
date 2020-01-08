"""
#file doVerb.py
pja 01-08-2020 added inp verb
-------------- added .X verb
pja 12-29-2019 edited att==@ to return '' on nos
pja 12-27-2019 redid this header block
               added ?space after msg inverb ask
               added takeV - imports vector files
# pja 3/9/2018 - added swap, drop, elipsis, dup roll depth
# -------- integer math:  mdas pwr root mod @++ @-- @0
# -------- str:  cat, cats, len find split 
# pja 2/10/2018 - added ask
# pja 2/8/2018
"""
def init(p):
    # load symbol table with all preset verbs
    #       symbol   verb
    p['sy']['dumpNDS'] = ndsOut
    p['sy']['takeV'] = takeV
    p['sy']['msg'] = msg
    p['sy']['='] = eq
    p['sy']['<>'] = neq
    p['sy']['!'] = bang
    p['sy']['@'] = att
    p['sy']['depth'] = depth
    p['sy']['ask'] = ask
    p['sy']['inp'] = inp
    p['sy']['tail.'] = tail
    p['sy']['drop'] = drop
    p['sy']['swap'] = swap
    p['sy']['dup'] = dup
    p['sy']['roll'] = roll
    p['sy']['...'] = elipsis
    p['sy']['cat'] = cat
    p['sy']['cats'] = cats
    p['sy']['len'] = length
    p['sy']['+'] = mplus
    p['sy']['-'] = mminus
    p['sy']['/'] = mdiv
    p['sy']['*'] = mmul
    p['sy']['**'] = mpwr
    p['sy']['-**'] = mroot
    p['sy']['mod'] = mmod
    p['sy']['++'] = mplusplus
    p['sy']['--'] = mminusminus
    p['sy']['@++'] = mattplusplus
    p['sy']['@--'] = mattminusminus
    p['sy']['@0'] = mattzero
    p['sy']['find'] = find
    p['sy']['split'] = split
    p['sy']['.X'] = dox
    return(p)
#end init
def ndsOut(p):
    if (p['v']['trace'] == 'on'):
        print('ndsOut')
    #endif
    print('begin nds dump \n')
    print(p['v'])
    print('\n end nds dump \n')
    p['sy']['push'](p['OK'])
# end ndsOut

def dox(p):
    """ executes verb on stack """
    if (p['v']['trace'] == 'on'):
        print('.X')
    #endif
    m = p['sy']['pop']()
    p['sy'][m](p) 
    # verb adds ok/nok
#end dox

def takeV(p):
    # (vectorFile,,) add vectors to architecture 
    # get vectorfile
    VectorFile = p['sy']['pop']()
    # do wild import
    j = __import__( VectorFile ) # no .py extension
    # run x.main(p)
    p = j.main(p)
    p['sy']['push'](p['OK'])
#end takeV

def depth(p):
    if (p['v']['trace'] == 'on'):
        print('depth')
    #endif
    d = len(p['dat'])
    s1 = d.__str__()
    p['sy']['push'](s1)
    p['sy']['push'](p['OK'])
#end depth

def roll(p):
    if (p['v']['trace'] == 'on'):
        print('roll')
    #endif
    #(a,b,c,,c,b,a)
    mc = p['sy']['pop']()
    mb = p['sy']['pop']()
    ma = p['sy']['pop']()
    p['sy']['push'](mc)
    p['sy']['push'](mb)
    p['sy']['push'](ma)
    p['sy']['push'](p['OK'])
#end roll
def find(p):
    if (p['v']['trace'] == 'on'):
        print('find')
    #endif
    # (haystack,needle,, "pos"/ "-1" )
    needle = p['sy']['pop']()
    haystack = p['sy']['pop']()
    pos = haystack.find(needle)
    sp = pos.__str__()
    p['sy']['push'](sp)
    p['sy']['push'](p['OK'])
#end find
def split(p):
    if (p['v']['trace'] == 'on'):
        print('split')
    #endif
    # (haystack,needle,,first,middle,last)
    needle = p['sy']['pop']()
    middle = needle
    haystack = p['sy']['pop']()
    posAR = haystack.split(needle) # [first,last]
    first = posAR[0].__str__()
    last = posAR[1].__str__()
    p['sy']['push'](first)
    p['sy']['push'](middle)
    p['sy']['push'](last)
    p['sy']['push'](p['OK'])
#end split

def mattzero(p):
    if (p['v']['trace'] == 'on'):
        print('@--')
    #endif
    # (add,) --> () v(addr) is v-1
    p['sy']['dup']
    p['sy']['@'] 
    s3 = "0"
    p['sy']['push'](s3) # (addr,val )
    p['sy']['swap']     # val,addr
    p['sy']['!']
    p['sy']['push'](p['OK'])
#end mattzero
def mattminusminus(p):
    if (p['v']['trace'] == 'on'):
        print('@--')
    #endif
    # (add,) --> () v(addr) is v-1
    p['sy']['dup']
    p['sy']['@'] 
    m2 = p['sy']['pop']() # get val
    n2 = int(m2)
    n1 = 1
    n3 = n1 - n2
    s3 = n3.__str__()
    p['sy']['push'](s3) # (addr,val )
    p['sy']['swap']     # val,addr
    p['sy']['!']
    p['sy']['push'](p['OK'])
#end mattminusminus
def mattplusplus(p):
    if (p['v']['trace'] == 'on'):
        print('@++')
    #endif
    # (add,) --> () v(addr) is ++
    p['sy']['dup']
    p['sy']['@'] 
    m2 = p['sy']['pop']() # get val
    n2 = int(m2)
    n1 = 1
    n3 = n1 + n2
    s3 = n3.__str__()
    p['sy']['push'](s3) # (addr,val )
    p['sy']['swap']     # val,addr
    p['sy']['!']
    p['sy']['push'](p['OK'])
#end mattplusplus
    
def mminusminus(p):
    """ math plus """
    if (p['v']['trace'] == 'on'):
        print(' -- ')
    #endif
    m2 = p['sy']['pop']()
    n2 = int(m2)
    n1 = 1
    n3 = n1 - n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mminusminus
def mplusplus(p):
    """ math plus """
    if (p['v']['trace'] == 'on'):
        print(' ++ ')
    #endif
    m2 = p['sy']['pop']()
    n2 = int(m2)
    n1 = 1
    n3 = n1 + n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mplusplus
def mroot(p):
    """ math subtract """
    if (p['v']['trace'] == 'on'):
        print(' -** ')
    #endif
    # 16,2 -** -> 4
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 ** (n2 * -1)
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mroot
def mmod(p):
    """ math mod """
    if (p['v']['trace'] == 'on'):
        print('mod')
    #endif
    # 5,3 - --> 2 
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1.__mod__(n2)
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mmod
def mpwr(p):
    """ math subtract """
    if (p['v']['trace'] == 'on'):
        print(' ** ')
    #endif
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 ** n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mpwr
def mmul(p):
    """ math subtract """
    if (p['v']['trace'] == 'on'):
        print(' * ')
    #endif
    # 5,2 - --> 10
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 * n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mmul
def mdiv(p):
    """ math divide """
    if (p['v']['trace'] == 'on'):
        print(' int / ')
    #endif
    # 5,2 - --> 7
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 / n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mdiv
def mminus(p):
    """ math subtract """
    if (p['v']['trace'] == 'on'):
        print(' - ')
    #endif
    # 5,2 - --> 7
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 - n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mminus
def mplus(p):
    """ math plus """
    if (p['v']['trace'] == 'on'):
        print(' + ')
    #endif
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 + n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mplus
    
    
def length(p):
    if (p['v']['trace'] == 'on'):
        print('length')
    #endif
    m1 = p['sy']['pop']()
    m3 = len(m1)
    s3 = m3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end length

def cats(p):
    if (p['v']['trace'] == 'on'):
        print('cats')
    #endif
    m1 = p['sy']['pop']()
    m2 = p['sy']['pop']()
    m3 = m2 + " " + m1
    p['sy']['push'](m3)
    p['sy']['push'](p['OK'])
#end cats
def cat(p):
    if (p['v']['trace'] == 'on'):
        print('cat')
    #endif
    m1 = p['sy']['pop']()
    m2 = p['sy']['pop']()
    m3 = m2 + m1
    p['sy']['push'](m3)
    p['sy']['push'](p['OK'])
#end cat

def dup(p):
    if (p['v']['trace'] == 'on'):
        print('dup')
    #endif
    m1 = p['sy']['pop']()
    p['sy']['push'](m1)
    p['sy']['push'](m1)
    p['sy']['push'](p['OK'])
#end dup

def swap(p):
    if (p['v']['trace'] == 'on'):
        print('swap')
    #endif
    m1 = p['sy']['pop']()
    m2 = p['sy']['pop']()
    p['sy']['push'](m1)
    p['sy']['push'](m2)
    p['sy']['push'](p['OK'])
#end swap

def drop(p):
    if (p['v']['trace'] == 'on'):
        print('drop')
    #endif
    m = p['sy']['pop']()
    p['sy']['push'](p['OK'])
#end drop

def elipsis(p):
    """ AKA fail """
    if (p['v']['trace'] == 'on'):
        print('...')
    #endif
    p['sy']['push'](p['NOK'])
#end elipsis.
def tail(p):
    """ does tail recursion """
    p['sy']['push']('tail.')
#end tail.
def ask(p):
    if (p['v']['trace'] == 'on'):
        print('ask')
    #endif
    m = p['sy']['pop']()
    j = raw_input(':'+m+'? ')
    # push answer
    p['sy']['push'](j)
    # push ok
    p['sy']['push'](p['OK'])
#end ask
def inp(p):
    # get input w/o question
    if (p['v']['trace'] == 'on'):
        print('inp')
    #endif
    j = raw_input()
    # push answer
    p['sy']['push'](j)
    # push ok
    p['sy']['push'](p['OK'])
#end ask
def msg(p):
    if (p['v']['trace'] == 'on'):
        print('msg')
    #endif
    m = p['sy']['pop']()
    print(m)
    p['sy']['push'](p['OK'])
#end msg
def bang(p):
    if (p['v']['trace'] == 'on'):
        print('bang')
    #endif
    # (val,addr)
    ad = p['sy']['pop']()
    vval = p['sy']['pop']()
    p['v'][ad] = vval
    p['sy']['push'](p['OK'])
#endif
def att(p):
    if (p['v']['trace'] == 'on'):
        print('att')
    #endif
    ad = p['sy']['pop']()
    try:
    	p['sy']['push'](p['v'][ad])
    except:
    	p['sy']['push']('')
    finally:
    	p['sy']['push'](p['OK'])
    #end try
#end att
def eq(p):
    if (p['v']['trace'] == 'on'):
        print('eq')
    #endif
    op1 = p['sy']['pop']()
    op2 = p['sy']['pop']()
    if (op1 == op2):
       p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#end eq
def neq(p):
    if (p['v']['trace'] == 'on'):
        print('neq')
    #endif
    op1 = p['sy']['pop']()
    op2 = p['sy']['pop']()
    if (op1 != op2):
       p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#end eq  
    
