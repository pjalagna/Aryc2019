# deviceSawClass.py
class deviceSaw:
    def __init__(self):
        self.mode = 's'
        self.n = 1
        self.z = 3 # zeros between saws
        self.zc = 3 # count down comparitor
        self.sleepTime = 2 # test 2 real 5
        import random
        self.rn = random
        import math
        self.ma = math
        import time
        self.sl = time.sleep
    # end ini
    def main(self):
        fm = open('hubaddr.txt','r')
        hubaddr =fm.readline()
        hubaddr = hubaddr[:-1] # drop crlf
        fm.close()
        import sr232
        c = 1
        while(c==1): # forever till ^ c
            n = self.getval()
            print(n) # send(n)
            sr232.send(hubaddr,n.__str__())
            self.sl(self.sleepTime)
        #wend
    #end main

    def getval(self):
        # get mode # test mode
        if (self.mode == 's'):
            ## == s (saw) ### get n ### n++ mod 11
            self.n = self.ma.fmod(self.n + 1, 11)
            ### if n=0
            if (self.n == 0):
                #### mode = z zero count down
                self.mode = 'z'
                ans = self.n
            else: ### else n=0
                ans = self.n #### send n
            ### endif n=0
        else: ## else mode
            if (self.zc != 0): ### test zc = 0
                self.zc = self.zc - 1 #### yes zc--
                ans = 0 #### print 0
            else: ### else zc=0
                ans = 0
                self.mode = 's' #### mode = 's'
                self.z = self.rn.randint(3,7)#### z = rand 3-7
                self.zc = self.z #### zc = z
            ### endif zc
        ### endif mode
        return(ans)
    #end getval
   
