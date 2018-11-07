
class pd3tstClass ():
  """ all the code below was generated by The Turing-Church point Builder program (V2.05.01 of AlagnaRythms Inc (Aryc) 2011 
      on Fri Nov 13 23:32:59 2015 

      From the point diagram file pd2Test.txt
  """

  def main(self,objj,trace):
    retbox = [0,objj,trace]
    objj['trace'] = self.trace
    if trace == 1:
        xx = objj['trace']( 'Begin pd3tst' , objj) 
    ctl = 1 # always begins at 1
    while 0 < ctl:
      if trace == 1:
        xx = objj['trace']  ( 'in loop -pd3tst.' + ctl.__str__() ,objj )
      if ctl == 1:
        xx = self.pd3tst_init(objj,trace)
        ctl = 2 # init always leads to 2
      elif ctl == 10000: # dump fixed as cell 10000
        retbox = self.dump(objj,trace)
        ctl = retbox[0]
      
      elif ctl == 60:
        retbox = self.pd3tst_proc60(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 61:
        retbox = self.pd3tst_proc61(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 62:
        retbox = self.pd3tst_proc62(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 24:
        retbox = self.pd3tst_proc24(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 20:
        retbox = self.pd3tst_proc20(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 21:
        retbox = self.pd3tst_proc21(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 22:
        retbox = self.pd3tst_proc22(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 23:
        retbox = self.pd3tst_proc23(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 3:
        retbox = self.pd3tst_proc3(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 2:
        retbox = self.pd3tst_proc2(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 5:
        retbox = self.pd3tst_proc5(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 7:
        retbox = self.pd3tst_proc7(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 6:
        retbox = self.pd3tst_proc6(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 9:
        retbox = self.pd3tst_proc9(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 8:
        retbox = self.pd3tst_proc8(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 11:
        retbox = self.pd3tst_proc11(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 10:
        retbox = self.pd3tst_proc10(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 13:
        retbox = self.pd3tst_proc13(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 12:
        retbox = self.pd3tst_proc12(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == 30:
        retbox = self.pd3tst_proc30(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      
      elif ctl == -100: #-100 is ok return
        ctl = -100 # nop
      else:
        print 'unknown range for ctl. ctl=',ctl,' ending'
        ctl = -3 # fail on unknown range
    #wend
      if trace == 1:
        xx = raw_input  ( 'loop ending. ctl=' + ctl.__str__() )
    return (retbox,objj)
  # end main

  def pd3tst_init(self,objj,trace):
    retbox = [0,objj,trace]
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_init ')
    # endif
    objj['c'] = {} # class store
    objj['v'] = {} # vector array
    import simpleVectorStk # push pop rtns 
    objj = simpleVectorStk.main(objj) # assume objj={} on entry 
    # add nds 
    import ndsClass 
    objj['nds'] = ndsClass.nds('var') 
    import simpleStk
    objj['es'] = simpleStk.Stk()
    # Imports and Vector setting
    

    import v_DLunk
    objj['v']["$unk"] = v_DLunk.main # objj,trace
    
    import v_DLdone
    objj['v']["$done"] = v_DLdone.main # objj,trace
    
    import v_UBUBBG
    objj['v']["__!"] = v_UBUBBG.main # objj,trace
    
    import v_clearNds
    objj['v']["clearNds"] = v_clearNds.main # objj,trace
    
    import v_UBUBwrite
    objj['v']["__write"] = v_UBUBwrite.main # objj,trace
    
    import v_UBUBatt
    objj['v']["__att"] = v_UBUBatt.main # objj,trace
    
    import v_pd3tst_SLSL7SLSL61SLSL
    objj['v']["//7//61//"] = v_pd3tst_SLSL7SLSL61SLSL.main # objj,trace
    
    import v_DLhello
    objj['v']["$hello"] = v_DLhello.main # objj,trace
    
    import v_DLbox
    objj['v']["$box"] = v_DLbox.main # objj,trace
    
    import v_UBUBmsg
    objj['v']["__msg"] = v_UBUBmsg.main # objj,trace
    
    import v_DLafterSPcall
    objj['v']["$after call"] = v_DLafterSPcall.main # objj,trace
    
    import v_DLtestSPmsg
    objj['v']["$test msg"] = v_DLtestSPmsg.main # objj,trace
    
    import v_EQEQFoo
    objj['v']["==Foo"] = v_EQEQFoo.main # objj,trace
    
    import v_UBUBask
    objj['v']["__ask"] = v_UBUBask.main # objj,trace
    
    import v_UBUBcallend
    objj['v']["__callend"] = v_UBUBcallend.main # objj,trace
    
    import v_DLitsSPfoo
    objj['v']["$its foo"] = v_DLitsSPfoo.main # objj,trace
    
    import v_EQEQChoo
    objj['v']["==Choo"] = v_EQEQChoo.main # objj,trace
    
    return(retbox)
  # end def init_pd3tst
  
  def testbed(self,objj,trace):
    ans = self.pd3tst_init(objj,trace)
    return(ans)
  # end testbed

  # procedures 
  
  def pd3tst_proc60(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc60') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '60', 'yesCell': '61', 'noCell': '-99', 'op': '//7//61//'}
    # assume all verbs are tests
    ans = objj['v']["//7//61//"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 61
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc60 
  
  def pd3tst_proc61(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc61') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '61', 'yesCell': '62', 'noCell': '-99', 'op': '$after call'}
    # assume all verbs are tests
    ans = objj['v']["$after call"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 62
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc61 
  
  def pd3tst_proc62(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc62') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '62', 'yesCell': '-1', 'noCell': '-99', 'op': '__msg'}
    # assume all verbs are tests
    ans = objj['v']["__msg"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = -1
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc62 
  
  def pd3tst_proc24(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc24') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '24', 'yesCell': '30', 'noCell': '-99', 'op': '__msg'}
    # assume all verbs are tests
    ans = objj['v']["__msg"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 30
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc24 
  
  def pd3tst_proc20(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc20') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '20', 'yesCell': '21', 'noCell': '-99', 'op': '$unk'}
    # assume all verbs are tests
    ans = objj['v']["$unk"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 21
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc20 
  
  def pd3tst_proc21(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc21') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '21', 'yesCell': '22', 'noCell': '-99', 'op': '__!'}
    # assume all verbs are tests
    ans = objj['v']["__!"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 22
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc21 
  
  def pd3tst_proc22(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc22') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '22', 'yesCell': '13', 'noCell': '-99', 'op': '$done'}
    # assume all verbs are tests
    ans = objj['v']["$done"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 13
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc22 
  
  def pd3tst_proc23(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc23') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '23', 'yesCell': '24', 'noCell': '-99', 'op': '$test msg'}
    # assume all verbs are tests
    ans = objj['v']["$test msg"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 24
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc23 
  
  def pd3tst_proc3(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc3') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '3', 'yesCell': '5', 'noCell': '-99', 'op': '__ask'}
    # assume all verbs are tests
    ans = objj['v']["__ask"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 5
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc3 
  
  def pd3tst_proc2(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc2') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '2', 'yesCell': '3', 'noCell': '-99', 'op': '$hello'}
    # assume all verbs are tests
    ans = objj['v']["$hello"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 3
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc2 
  
  def pd3tst_proc5(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc5') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '5', 'yesCell': '6', 'noCell': '-99', 'op': '$box'}
    # assume all verbs are tests
    ans = objj['v']["$box"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 6
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc5 
  
  def pd3tst_proc7(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc7') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '7', 'yesCell': '8', 'noCell': '-99', 'op': '$box'}
    # assume all verbs are tests
    ans = objj['v']["$box"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 8
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc7 
  
  def pd3tst_proc6(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc6') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '6', 'yesCell': '60', 'noCell': '-99', 'op': '__write'}
    # assume all verbs are tests
    ans = objj['v']["__write"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 60
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc6 
  
  def pd3tst_proc9(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc9') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '9', 'yesCell': '10', 'noCell': '11', 'op': '==Choo'}
    # assume all verbs are tests
    ans = objj['v']["==Choo"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 10
    elif (ret == -1):
        NextPoint = 11
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc9 
  
  def pd3tst_proc8(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc8') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '8', 'yesCell': '9', 'noCell': '-99', 'op': '__att'}
    # assume all verbs are tests
    ans = objj['v']["__att"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 9
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc8 
  
  def pd3tst_proc11(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc11') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '11', 'yesCell': '12', 'noCell': '20', 'op': '==Foo'}
    # assume all verbs are tests
    ans = objj['v']["==Foo"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 12
    elif (ret == -1):
        NextPoint = 20
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc11 
  
  def pd3tst_proc10(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc10') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '10', 'yesCell': '23', 'noCell': '-99', 'op': 'clearNds'}
    # assume all verbs are tests
    ans = objj['v']["clearNds"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 23
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc10 
  
  def pd3tst_proc13(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc13') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '13', 'yesCell': '-100', 'noCell': '-99', 'op': '__msg'}
    # assume all verbs are tests
    ans = objj['v']["__msg"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = -100
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc13 
  
  def pd3tst_proc12(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc12') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '12', 'yesCell': '13', 'noCell': '-99', 'op': '$its foo'}
    # assume all verbs are tests
    ans = objj['v']["$its foo"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = 13
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc12 
  
  def pd3tst_proc30(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin pd3tst_proc30') 
    retbox = [0,objj,trace] # initilize by type
    # {'cell': '30', 'yesCell': '-1', 'noCell': '-99', 'op': '__callend'}
    # assume all verbs are tests
    ans = objj['v']["__callend"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = -1
    elif (ret == -1):
        NextPoint = -99
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def pd3tst_proc30 
  
  

  
  # helper definitions
  # use stump for navagation traceing
  def stump(self,objj,trace):
    retbox = [0,objj,trace] # initilize by type
    xx = raw_input("stump")
    ans = raw_input("pass/fail/goto 0/-1 or next ")
    retbox.append( int(ans) )
    return(retbox)
  #end stump
  
  def trace(self,msg,objj):
    x = raw_input(msg + "... ")
    while (x != ''):
		if (x.upper() == "DS"):
			print(objj['ds'].dump())
		elif (x.upper() == "PS"):
			print(objj['ps'].dump())
		elif (x.upper() == "ES"):
			print(objj['es'].dump())
		elif (x.upper() == "NDS"):
			print(objj['nds'].dump())
		elif (x.upper() == "OBJJ"):
			print(objj)
		else:
			x = ''
		#endif
		x = raw_input("... ")
    #wend
  #end trace
  
  # use dump for command line development
  def dump(self,objj,trace):
    return(objj)
  #end dump
  
# end class pd3tst
  