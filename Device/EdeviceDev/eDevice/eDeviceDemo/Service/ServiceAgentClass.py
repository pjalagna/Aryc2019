# file ServiceAgentClass.py
class ServiceAgent:
    def __init__(self,channalIn,HubChannel):
        self.chIn = channalIn
        self.HubChannel = HubChannel
        import time
        self.sl = time.sleep
    #end init
    def main(self):
        import sr232
        c = 1
        while(c==1):
            # rcv
            a = sr232.listenStart('serv1',5)
            # unpack
            d = a[1] # the message
            fo = d.index('<msg>') + 5
            bo = d.index('</msg>')
            res = d[fo:bo]
            print(res)
            # do work
            ans = float(res) + 12
            # send resp
            s1 = sr232.send(self.HubChannel,ans.__str__())
            while (s1 != 1 ):
                s1 = sr232.send(self.HubChannel,ans.__str__())
            #wend
            s2 = sr232.send(self.HubChannel,ans.__str__())
            while (s2 != 0):
                s2 = sr232.send(self.HubChannel,ans.__str__())
            #wend
            # sleep
        #wend
    #end main
