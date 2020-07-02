"""
agent.py
allows pbox agents to
communicate 
usage:
import agent
agent.init() - sets up 5 channels 
agent.send(sendChannel,ReceiveChannel,command,{parameter})
channel0 is always command line
"""
"""
test as
import agent
agent.init()
agent.send(0,1,'push','hello')
agent.send(0,1,'depth')

"""
ch = [0,1,2,3,4,5,6,7,8]
pc = [0,1,2,3,4,5,6,7,8]
def init():
    import useLib
    import usePgx
    import pbox1
    pbox1.main('bmain')
    ch[1] = pbox1
    pc[1] = pbox1.p
    pc[1]['sy']['push'](1)
    pc[1]['sy']['push']('mych')
    pc[1]['sy']['!'](pc[1])
    no = pc[1]['sy']['pop']()
    import pbox2
    pbox2.main('bmain')
    ch[2] = pbox2
    pc[2] = pbox2.p
    pc[2]['sy']['push'](2)
    pc[2]['sy']['push']('mych')
    pc[2]['sy']['!'](pc[2])
    no = pc[2]['sy']['pop']()
    import pbox3
    pbox3.main('bmain')
    ch[3] = pbox3
    pc[3] = pbox3.p
    pc[3]['sy']['push'](3)
    pc[3]['sy']['push']('mych')
    pc[3]['sy']['!'](pc[3])
    no = pc[3]['sy']['pop']()
    import pbox4
    pbox4.main('bmain')
    ch[4] = pbox4
    pc[4] = pbox4.p
    pc[4]['sy']['push'](4)
    pc[4]['sy']['push']('mych')
    pc[4]['sy']['!'](pc[4])
    no = pc[4]['sy']['pop']()
    import pbox6
    pbox6.main('bmain')
    ch[6] = pbox6
    pc[6] = pbox6.p
    pc[6]['sy']['push'](6)
    pc[6]['sy']['push']('mych')
    pc[6]['sy']['!'](pc[6])
    no = pc[6]['sy']['pop']()
    import pbox7
    pbox7.main('bmain')
    ch[7] = pbox7
    pc[7] = pbox7.p
    pc[7]['sy']['push'](7)
    pc[7]['sy']['push']('mych')
    pc[7]['sy']['!'](pc[7])
    no = pc[7]['sy']['pop']()
    import pbox8
    pbox8.main('bmain')
    ch[8] = pbox8
    pc[8] = pbox8.p
    pc[8]['sy']['push'](8)
    pc[8]['sy']['push']('mych')
    pc[8]['sy']['!'](pc[8])
    no = pc[8]['sy']['pop']()
#
    
def send(sendChannel,ReceiveChannel,command,parameter=''):
    #command fan do,push,pop
    if (command == 'do'):
        ans = ch[ReceiveChannel].p['sy'][parameter](pc[ReceiveChannel])
        ans = ch[ReceiveChannel].p['sy']['pop']() #ok
    elif (command == 'push'):
        ch[ReceiveChannel].p['sy']['push'](parameter)
        ans = ''
    elif (command == 'pop'):
        ans = ch[ReceiveChannel].p['sy']['pop']()
    #endif
    return(ans) 
#
def main(p):
    import useLib
    import usePgx
    import useAgent
    import useOnto
    import agent
    agent.init()
    p['package']['agent'] = agent
    p['help']['agent'] = agent.__doc__
    p['sy']['agentPush']= agPush #(mych,recvCh,parameter)
    p['help']['agentPush']= "agPush (recvCh,parameter)"
    p['sy']['agentPop']= agPop
    p['help']['agentPop']= "agPop (recvCh,,txt)"
    p['sy']['agentDo']= agDo
    p['help']['agentDo']= "agDo (recvCh,command,,)"
    return(p)
#
def agPush(p):
    """
    (rcvCh,txt,,)
    """
    mych = 0
    para = p['sy']['pop']()
    rch = int(p['sy']['pop']())
    p['package']['agent'].send(mych,rch,'push',para)
    p['sy']['push'](p['OK'])
#
def agPop(p):
    """
    (rcvCh,,txt)
    """
    mych = 0
    rch = int(p['sy']['pop']())
    #rint("agPop rch=("+str(rch)+")")
    ans = p['package']['agent'].send(mych,rch,'pop')
    #rint("agPop ans=("+str(ans)+")")
    p['sy']['push'](str(ans))
    p['sy']['push'](p['OK'])
#
def agDo(p):
    """
    (rcv,command,,)
    """
    cmd = p['sy']['pop']()
    rch = int(p['sy']['pop']())
    mych = 0
    ans = p['package']['agent'].send(mych,rch,'do',cmd)
    p['sy']['push'](p['OK'])
#
    
    
    
    
    
    
    
        

