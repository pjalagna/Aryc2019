"""
sr232V vector file for pbox
registerChannel(ch)
sniff(ch) ==> cts,rts,dRdy,dRcvd
send(ch,msg) ==> 0001 means busy, 
                 111x means msg mailboxed
                 1000 means ready
rcvLoop(ch) ==> waits for msg, msg is 
      <que>
         <t> time </t>
         <from> sending channel </from>
         <msg> text </msg>
      </que>
"""
def main(p):
    import sr232
    p['package']['sr232'] = sr232
    p['help']['sr232']= """
    independent send/receive routines 
    registerChannel(channelName) to clear and ready
    rcvLoop(channel) to get info, 
    send(ch,msg) to send message
    """
    p['sy']['send'] = srSend
    p['help']["send"]='send (ch,msg,,status) send message to channel returns status 0001 busy, 1110 msg mailboxed, 1000 ready' 
    p['sy']['rcv'] = srRcv
    p['help']['rcv'] = 'rcv (channel,,message) waits for message to channel response is in <que> format'
    p['sy']['sniff'] = srSniff
    p['help']['sniff'] = 'sniff (channel,,) displays status of channel'
    p['sy']['registerChannel'] = srRegister
    p['help']['registerChannel'] = 'registerChannel (channelName,,) readys and clears channel for use'
    return(p)
#main
def srRegister(p):
    """
    registerChannel
    """
    ch = p['sy']['pop']()
    p['package']['sr232'].registerChannel(ch)
    p['sy']['push'](p['OK'])
#

def srSniff(p):
    """
    channel sniff
    """
    ch = p['sy']['pop']()
    p['package']['sr232'].sniff(ch)
    p['sy']['push'](p['OK'])
#
def srRcv(p):
    """
    
    """
    ch = p['sy']['pop']()
    ans = p['package']['sr232'].rcvLoop(ch)
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
def srSend(p):
    """
    send (ch,msg)
    """
    msg = p['sy']['pop']()
    ch = p['sy']['pop']()
    ans = p['package']['sr232'].send(ch,msg) #responds w/ status
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#

        
   
   
