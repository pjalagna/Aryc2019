#file ASKp.py
""" interfaces with basii created processes """
def askP_init(p):
    p['sy']['ask'] = ask
    p['sy']['longAsk'] = longAsk
    return(p)
#end askP_init

def longAsk(p):
    """ takes in multiple lines till ".." """
    if (p['v']['trace'] == 'on'):
        print('longAsk')
    #endif
    out = ''
    m = p['sy']['pop']()
    ans = raw_input(m)
    while (m != '..'):
        out += ans
        m = "?..> "
    #wend
    p['sy']['push'](out)
    p['sy']['push'](p['OK'])
#end longAsk
    
    
def ask(p):
    if (p['v']['trace'] == 'on'):
        print('ask')
    #endif
    m = p['sy']['pop']()
    ans = raw_input(m)
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end msg