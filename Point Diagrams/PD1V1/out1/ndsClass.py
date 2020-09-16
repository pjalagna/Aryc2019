class nds() :
    """ LUD=09/20/2012 \n
        Named Data Store : class=nds actions: \n
        bang att dots depth nMove\n
        attrec atick atickrec aticktick bangl
        dump
        """
    
	# NDS (class?)
	# =====================================================
	# 2/2/9	pja	original
	# 2/21/2009 pja bang is unique
	# 2/21/2009 pja added attrec - gives back set
	# 3/19/2009 pja depth added
	# 7/29/2009 pja added aticktick
	# 7/30/2009 pja added bangl
	# 9/20/2012 pja added dump
	# =====================================================
	# supporting imports
	
	# actions
    # __init__
    def __init__(self, na) :
        self.ndsar = []
        import StrnumClass
        # set up a num str conversion variable
        self.cv = StrnumClass.strnum()
        self.name = na
        self.type = 'nds'
        self.strace = 0 # off
        self.ndsarix = 0
	# end init
	
    def getix(self):
	return(self.ndsarix)
	   
    def setix(self,ix):
	self.ndsarix = ix
    def depth(self):
        return(self.getix())
    #end def depth
    
    # bangl write list element returns the index
    def bangl(self,columnName,columnValue):
        # does columnName.count exist
        qa = self.att(columnName + ".count")
        # print "test qa(" + qa + ")"
        if qa != 'nok' :
            # yes
            # print "qa[0]=(" + qa[0] + ")"
            # print "qa=(" + qa + ")"
            qn = self.cv.str2num(qa)
            qn = qn + 1
            # update count record
            self.bang(columnName + ".count",self.cv.num2str(qn))
        else:
            qn = 0
            # create .count record (qa)
            self.bang(columnName + ".count",'0')
        # endif
        # write rec at qn
        self.bang(columnName + "." + qn.__str__(),columnValue)
        # return qa
        return(qn)
    # end bangl
    
    def aticktick(self,ftarget,btarget,pos):
        """ returns record of k that begins with ftarget and ends with btarget; pos is jacobson device """
        t = []
        for k,v,m in self.ndsar :
            if k[0:len(ftarget)]== ftarget:
                if k[-len(btarget):]==btarget:
                    t.append([k,v,m])
        if len(t) < pos:
            ans = ['nok']
        else:
            ans = t[pos-1]
        return (ans)
    # end aticktick
    
    # bang - unique store on k
    def bang( self , k , v) :
        # is there a record of k?
        t = self.attrec(k)
        if t[0] == 'nok' :
	   m = self.getix() 
	   self.ndsar.append([ k,v,m ])
	   self.setix(m+1)
	else:
            # rewrite v of record
            self.ndsar[t[2]][1] = v
    # end bang
	
    def dots(self) :
	   print '===== ' + self.name + ' ==========='
	   print 'length is' , len(self.ndsar)
	   for k,v,m in self.ndsar:
               print 'k',k,'v',v,'m',m
	   print '======================================'
	   
    # dots
    def dump(self):
      """ returns XML string with contents of stack """
      import random
      id1 = random.randint(1,300)
      ans = "<Nds ID='" + id1.__str__() + "'> \n"
      ans += "    <NdsVals> \n"
      for k,v,m in self.ndsar:
         ans += "    <Val k='" + k.__str__() + "'> \n"
         ans +=  v.__str__() + "\n"
         ans += "    </Valk k='" + k.__str__() + "'> \n"
      # end for
      ans += "    </NdsVals> \n"
      ans += "    <NdsID ID='" + id1.__str__() + "'/> \n"
      ans += "</Nds>"
      return(ans)
    # end dump
    def att(self, keyIn) :
       ans = 'nok'
       if len(self.ndsar) == 0 :
          ans = 'nok'
       else:
           for k,v,m in self.ndsar:
               if k == keyIn:
                   ans = v
       return(ans)
    # end att

    # nMove (from,to)
    def nMove(self, FFrom, TTo):
        """ moves from one cell to another """
        x1 = self.att(FFrom)
        self.bang(TTo,x1)
    # end nMove
    
    # at-tick-rec  atickrec returns record that contains target, pos is counter as jacobson device
    def atickrec(self,target, pos) :
        t = []
        for k,v,m in self.ndsar:
            try:
                j = k.index(target)
            except:
                j = -1
            if j != -1:
                t.append([k,v,m])
            # print 't=',t
        if len(t) < pos:
            ans = ['nok']
        else:
            ans = t[pos-1]
        return (ans)
        
    # at-tick atick(target,pos) returns key/nok for target
    def atick(self,target,pos):
        t = self.atickrec(target,pos)
        if len(t) < 3:
            ans = 'nok'
        else:
            ans = t[0]
        return (ans)
    # end at-tick
    
    # attrec returns the set
    def attrec(self, keyIn) :
       ans = ['nok']
       if len(self.ndsar) == 0 :
          ans = ['nok']
       else:
           for k,v,m in self.ndsar:
               if k == keyIn:
                   ans = [k,v,m]
       return(ans)
    # end att
# end class nds
