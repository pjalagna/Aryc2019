""" file fioiClass.py
pja 5/17/2020 f2tkn fixed runaway
pja 04-07-2020 edits to fwhite added \r
-------------- added f2tkn
pja 01-09-2020 added ' pickup in fpword
pja 12-27-2019 added code to fwhite
pja 12-26-2019 redid this header block
# pja 3-04-2017 tested fpword
# pja 9-24-12 edits to stop till, tillor, ctill on eof
# ------------ edits to clip targetCH to targetCH[0]
# pja 10-17-2012 changed print to #rint
# pja 1-4-13 added getAlpha getNums getAnum
# pja 2-27-13 added type to fpword to transmit "Q" for quoted string "S" for simple string
# fioi , fioo , get/set iox, flookup , fwhite, ftill,  fctill, ftillor
# fpword, fpback

comment code so far
        elif (m=='/'): # comment check
                mm = self.fioi()
                if (mm == '*'): # yes comment
                    mmx = self.fioi()
                    while (mmx != '*'):
                        mmx = self.fioi()
                    #end while
                #endif
"""
"""
test as
import fioiClass
s = fioiClass.fio('test3.txt')
s.fioxGet() #etc

"""
class fio():
    def __init__(self,fNa):
        self.fh = open(fNa,'r')
    # end init
    def fioi(self):
        p0 = self.fioxGet()
        ans = self.fh.read(1)
        # test for eof
        p1 = self.fioxGet() # iox after read
        if ( p0 == p1 ):
            ans = '@eofeof'
        #endif
        #rint ('ioi=(',ans,")")
        return(ans)
    # end fioi
    
    def fgetSize(self):
        return(self.fsz)
    #end fgetSize
    
    def fioo(self):
        #rint('ioo')
        j = self.fh.tell()
        j = j -1
        self.fh.seek(j) # resets file pointer
    # end fioo
    
    def fioxGet(self):
        return( self.fh.tell() )
    # end fioxGet
    
    def fioxSet(self,pos):
        self.fh.seek(pos)
    # end fioxSet
    
    def flookup(self,target):
        p1 = self.fioxGet()
        #rint ('p1=',p1)
        c = 0
        for d in range(0,target.__len__()):
            t = self.fioi()
            t = t.__str__()
            #rint ('t=(',t,")")
            #rint ('tar[d]=(',target[d],")")
            if (t != target[d].__str__()):
                c = -1
            #endif
        # end for
        if (c != 0):
            self.fioxSet(p1) # drop back to where you were
        # end if
        return(c) # 0 = ok , -1 = nok
    # end flookup
    def fwhite(self):
        c = 0
        while (c==0):
            m = self.fioi()
            m = m.__str__()
            if (m == ' '):
                c = 0 # stay in loop
            elif (m == chr(8)):
                c = 0 # stay in loop
            elif (m == '\n'):
                c = 0 # stay in loop
            elif (m == '\r'):
                c = 0 # stay in loop
            elif (m=='/'): # comment check t1
                mm = self.fioi()
                print('t1 mm=('+mm+')')
                if (mm == '*'): # yes comment t2
                    c2 = 0 
                    while (c2==0):
                        mmx = self.fioi()
                        print('t2 mmx=('+mmx+')')
                        while (mmx != '*'): # w3
                            mmx = self.fioi()
                            print('w3 mmx=('+mmx+')')
                        #wend w3
                        mv = self.fioi()
                        if (mv=='/'): # t3
                            print('t3 mv=('+mv+')')
                            # not sure self.fioi() # move one 
                            c2=-1 # break wc2
                            c=0 # keep looping after comment
                        else:
                            print('t3 else')
                            c2=0
                            c=0
                        #endif t3
                    #wend c2
                else: # t2
                    print('t2 else')
                    c=1 # break
                #endif t2
            else:
                c = -1
            # endif
        #wend
        self.fioo() # back up one
    # end fwhite
    def ftill(self,targetCH):
        """ skip till target """
        c = 1
        while (c==1):
            j = self.fioi()
            #rint('ftill j=(' + j.__str__() +')')
            if (j.__str__() == targetCH[0]):
                self.fioo() # put last back
                c = 0
            elif (j.__str__() == '@eofeof'):
                c = -1
            #endif
        #wend
        return(c) # 0 = ok -1 = eof
    #end ftill
    def ftillor(self,targetCHS):
        """ skip till any in target """
        c = 1
        while (c==1):
            j = self.fioi()
            if (j.__str__() == '@eofeof'):
                c = -1 # eof
            else:  
                for m in targetCHS :
                    if (j.__str__() == m ):
                        c = 0
                        self.fioo() # put last back
                    #endif
                #end for
            #endif
        #wend
        
    #end ftillor
    
    def fctill(self,targetCH):
        """ collect till target """
        ans = ''
        c = 1
        while (c==1):
            j = self.fioi()
            if (j.__str__() == '@eofeof'):
                ans = '@eofeof'
                c = -1
            elif (j.__str__() == targetCH[0] ):
                c = 0
            else:
                ans = ans + j.__str__()
            #endif
        #wend
        self.fioo() # put last back
        return(ans)
    #end fctill
    def fctillor(self,targetCHS):
        """ collect till any in target """
        ans = ''
        c = 1
        while (c==1):
            j = self.fioi()
            if (j.__str__() == '@eofeof'):
                c = -1
                ans = '@eofeof'
            else:
                for m in targetCHS:
                    if (j.__str__() == m ):
                        c = 0
                    #endif
                #end for
                if (c != 0):
                    ans = ans + j.__str__()
                #endif
            #endif
        #wend
        self.fioo() # put last back
        return(ans)
    #end fctill
    def fpword(self):
        """ g: [na,na,iox-current] \n
            returns [iox-old,word,iox-new,type] type="Q" for quoted strings , "S" for simple string
        """
        ioxOld = self.fioxGet()
        self.fwhite()
        j = self.fioi()
        self.fioo()
        # if quote grab till next quote
        if (j == '"'):
            ty = "Q"
            w1 = self.fioi() # burn the \q
            wd = self.fctill('"')
            x = self.fioi() # burn the end \q
        elif (j == "'"):
            ty = "Q"
            w1 = self.fioi() # burn the \tick
            wd = self.fctill("'")
            x = self.fioi() # burn the end \tick
        else:
            ty = "S"
            wd = self.fctillor([' ','\n'])
        #endif
        ioxNew = self.fioxGet()
        return([ioxOld,wd,ioxNew,ty])
    #end fpword
    def fpback(self,struct):
        """ g: [ioxOld,na,na]
            resets iox to old
        """
        self.fioxSet(struct[0])
        # adjust struct for return
        return([0, ' ',struct[0]])
    #end def
    def fgetAlpha(self):
        """ a-zA-Z """
        ioxOld = self.fioxGet()
        ans = ''
        # the first token must be Alpha
        aZ = 'qwertyuiopajklzxcvbnmdsfgh_QWERTYUIOPAJKLZXCVBNMDSFGH'
        t = self.fioi()
        try:
            m = aZ.index(t)
            ans = t
            a1 = 1
        except:
            a1 = -1
        finally:
            nop = 1
        if (a1 == 1):
            # collect till fail
            c = 0
            while (c==0):
                t1 = self.fioi()
                try:
                    m = aZ.index(t1)
                    ans += t1
                except:
                    c = -1 #break
                    self.fioo() # put the last one back
                finally:
                    nop = 1
                #end try
        else:
            self.fioxSet(ioxOld)
            ans = ''
        #endif
    
        return(ans)
    #end Alpha
    def fgetNum(self):
        """ a-zA-Z """
        ioxOld = self.fioxGet()
        ans = ''
        # the first token must be Alpha
        aZ = '0123456789.'
        t = self.fioi()
        try:
            m = aZ.index(t)
            ans = t
            a1 = 1
        except:
            a1 = -1
        finally:
            nop = 1
        if (a1 == 1):
            # collect till fail
            c = 0
            while (c==0):
                t1 = self.fioi()
                try:
                    m = aZ.index(t1)
                    ans += t1
                except:
                    c = -1 #break
                    self.fioo() # put the last one back
                finally:
                    nop = 1
                #end try
        else:
            self.fioxSet(ioxOld)
            ans = ''
        #endif
    
        return(ans)
    #end fgetNum
    def fgetANum(self):
        """ a-zA-Z """
        ioxOld = self.fioxGet()
        ans = ''
        # the first token must be Alpha
        aZ = '0123456789.qwertyuiopajklzxcvbnmdsfgh_QWERTYUIOPAJKLZXCVBNMDSFGH'
        t = self.fioi()
        try:
            m = aZ.index(t)
            ans = t
            a1 = 1
        except:
            a1 = -1
        finally:
            nop = 1
        if (a1 == 1):
            # collect till fail
            c = 0
            while (c==0):
                t1 = self.fioi()
                try:
                    m = aZ.index(t1)
                    ans += t1
                except:
                    c = -1 #break
                    self.fioo() # put the last one back
                finally:
                    nop = 1
                #end try
        else:
            self.fioxSet(ioxOld)
            ans = ''
        #endif
    
        return(ans)
    #end fgetANum
    def f2tkn(self,tkn,sw=0):
        # slide to token/eof if sw<>0 return collection
        cmax = len(tkn)
        col = '' # collector for sw<>0
        ct1 = 0
        fo = self.fioxGet()
        while (ct1==0):
            if (sw == 0):
                p = self.ftill(tkn[0])
                #rint('f2tkn p=('+ p.__str__() + ')')
                if (p == -1):
                    ct1 = -1
                #endif
            else:
                col = col + self.fctill(tkn[0])
                p = 0
            #endif
            if (p==0):
                cxx = -1
                ct2 = 0
                #match all
                while (ct2==0):
                    cxx = cxx + 1
                    if (cxx == cmax):
                        ct2 = -1 # everybody matched
                    else:
                        j = self.fioi()
                        if (sw <> 0):
                            col = col + j
                        #
                        if (j == '@eofeof'):
                            ct1 = -2 #break 1st loop
                        #
                        if (j <> tkn[cxx]):
                            ct2 = -2 #non match
                        #
                    #
                #wend
                if (ct2 == -1):
                    ct1 = 1 # good break
                    ansd = 'ok'
                    if (sw <> 0):
                       ans = col
                    else:
                        ans = ''
                    #
                #endif
            #endif p==0
        #wend
        if (ct1 == 1): #good ending
            if (sw <> 0):
                ans = col
            else:
                ans = ''
            #
            anss = 'ok'
        #endif
        else: 
            self.fioxSet(fo)
            ans = ''
            anss = "nok"
        #
        return(ans,anss)
    #end f2tkn
            
            
            
                 
       
# end class
