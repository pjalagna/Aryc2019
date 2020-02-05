class Sio: 
    """
file SioiClass.py
pja 02-04-2020

Sioi(self):
Sioo(self):
setiox(self,ioxin):
getiox(self):
setSStr(self,strin):
getSStr(self):
Still(self,targetCH):
Stillor(self,targetCHS):
Swhite(self):
Sctill(self,targetCH):
Sctillor(self,targetCHS):
Sword(self):
Spback(self,struct):


test as
import SioiClass
s = SioiClass.Sio()
s.setSStr('mary had "little lamb" once')
s.Sioi()
s.Sioo()
s.Sioi()
s.Sioo()
s.Swhite()
m = s.Sword() # mary
m
m = s.Sword() # had
m
m = s.Sword() # 'little lamb'
m
m = s.Spback(m)
m
m = s.Spback(m)
m
m = s.Sword() # mary
m

    """
    def __init__(self):
        self.SStr = ''
        self.iox = 0
    #
    def Sioi(self):
        m = self.SStr[self.iox]
        self.iox = self.iox + 1
        return(m)
    #
    def Sioo(self):
        self.iox = self.iox - 1
    #
    def setiox(self,ioxin):
        self.iox = ioxin
    #
    def getiox(self):
        return(self.iox)
    #
    def setSStr(self,strin):
        self.SStr = strin
    #
    def getSStr(self):
        return(self.SStr)
    #
    def Still(self,targetCH):
        """ skip till target """
        c = 1
        while (c==1):
            j = self.Sioi()
            if (j.__str__() == targetCH[0]):
                self.Sioo() # put last back
                c = 0
            elif (j.__str__() == '@eofeof'):
                c = -1
            #endif
        #wend
        return(c) # 0 = ok -1 = eof
    #end Still
    def Stillor(self,targetCHS):
        """ skip till any in target """
        c = 1
        while (c==1):
            j = self.Sioi()
            if (j.__str__() == '@eofeof'):
                c = -1 # eof
            else:  
                for m in targetCHS :
                    if (j.__str__() == m ):
                        c = 0
                        self.Sioo() # put last back
                    #endif
                #end for
            #endif
        #wend
        
    #end Stillor
    def Swhite(self):
        c = 0
        while (c==0):
            m = self.Sioi()
            m = m.__str__()
            if (m == ' '):
                c = 0 # stay in loop
            elif (m == chr(8)):
                c = 0 # stay in loop
            elif (m == '\n'):
                c = 0 # stay in loop
            elif (m=='/'): # comment check t1
                mm = self.Sioi()
                print('t1 mm=('+mm+')')
                if (mm == '*'): # yes comment t2
                    c2 = 0 
                    while (c2==0):
                        mmx = self.Sioi()
                        print('t2 mmx=('+mmx+')')
                        while (mmx != '*'): # w3
                            mmx = self.Sioi()
                            print('w3 mmx=('+mmx+')')
                        #wend w3
                        mv = self.Sioi()
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
        self.Sioo() # back up one
    # end Swhite
    """Sctill"""
    def Sctill(self,targetCH):
        """ collect till target """
        ans = ''
        c = 1
        while (c==1):
            j = self.Sioi()
            if (j.__str__() == '@eofeof'):
                ans = '@eofeof'
                c = -1
            elif (j.__str__() == targetCH[0] ):
                c = 0
            else:
                ans = ans + j.__str__()
            #endif
        #wend
        self.Sioo() # put last back
        return(ans)
    #end Sctill
    """Sctillor"""
    def Sctillor(self,targetCHS):
        """ collect till any in target """
        ans = ''
        c = 1
        while (c==1):
            j = self.Sioi()
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
        self.Sioo() # put last back
        return(ans)
    #end fctillor
    def Sword(self):
        """ g: [na,na,iox-current] \n
            returns [iox-old,word,iox-new,type] type="Q" for quoted strings , "S" for simple string
        """
        ioxOld = self.iox
        self.Swhite()
        j = self.Sioi()
        self.Sioo()
        # if quote grab till next quote
        if (j == '"'):
            ty = "Q"
            w1 = self.Sioi() # burn the \q
            wd = self.Sctill('"')
            x = self.Sioi() # burn the end \q
        elif (j == "'"):
            ty = "Q"
            w1 = self.Sioi() # burn the \tick
            wd = self.Sctill("'")
            x = self.Sioi() # burn the end \tick
        else:
            ty = "S"
            wd = self.Sctillor([' ','\n'])
        #endif
        ioxNew = self.iox
        return([ioxOld,wd,ioxNew,ty])
    #end fpword
    """Spback"""
    def Spback(self,struct):
        """ g: [ioxOld,na,na]
            resets iox to old
        """
        self.iox = struct[0]
        # adjust struct for return
        return([0, ' ',struct[0]])
    #end def
    """ Slookup  """
#end class