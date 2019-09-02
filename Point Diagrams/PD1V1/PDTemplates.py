# file = PDTemplates.py
# lud 7-17-2013 1400
# pja 7.27.12 added logic to sec4 to allow rtns to set NextPoint
# ------------- allows call and return
# pja 8.7.12 added dump routine to deliver objj to command line
# ------------- fixed as cell 10000 can be called during development
# pja 9/3/12 added objj ['c'] class store
# ----------- changed return from vectors to be retbox format
# pja 9-19-12 added testbed, changed init to have return
# pja 9-19-12 renamed file to PDTemplates
# pja 10-17-20112 fixed objj['s'] to point to stack
# pja 1-31-2013 fixed init 'c' order
# pja 2-1-2013 added callbox for //call//return operators
# pja 3-18-2013 changed simpson to correct Turing-Church
# -------------- added local architecture to verb call
# pja 3-29-13 0108 added trace call  to main ,  trace def to ??
# pja 5-19-2013 2000 added Lit template to push $ op
# pja 5-23-2013 0320 fixed def trace
# ===============added version for LUD
#================bug in vector
# pja 6-19-2013 added ES (environment stack)
# pja 7-17-2013 fixed eq
#pja 9-21-2013 added project name to callbox to avoid collisions with merged projects.
def main():
    temps = {}
    temps['version'] = '05-23-2013 0411'
    temps['sec1'] = """
class %class%Class ():
  %3q% all the code below was generated by The Turing-Church point Builder program (V2.05.01 of AlagnaRythms Inc (Aryc) 2011 
      on %time% \n
      From the point diagram file %fina%
  %3q%

  def main(self,objj,trace):
    retbox = [0,objj,trace]
    objj['trace'] = self.trace
    if trace == 1:
        xx = objj['trace']( 'Begin %class%' , objj) 
    ctl = 1 # always begins at 1
    while 0 < ctl:
      if trace == 1:
        xx = objj['trace']  ( 'in loop -%class%.' + ctl.__str__() ,objj )
      if ctl == 1:
        xx = self.%class%_init(objj,trace)
        ctl = 2 # init always leads to 2
      elif ctl == 10000: # dump fixed as cell 10000
        retbox = self.dump(objj,trace)
        ctl = retbox[0]
      """
    temps['sec2'] = """
      elif ctl == %cell%:
        retbox = self.%class%_proc%cell%(objj,trace) # always returns an array with [0]== status
        ctl = retbox[0]
      """
    temps['sec3'] = """
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

  def %class%_init(self,objj,trace):
    retbox = [0,objj,trace]
    if trace == 1:
      xx = raw_input ( 'begin %class%_init ')
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
    """
    temps['sec3b'] = """
    import v_%verbt%
    objj['v']["%verb%"] = v_%verbt%.main # objj,trace
    """
    temps['sec3a'] = """
    return(retbox)
  # end def init_%class%
  
  def testbed(self,objj,trace):
    ans = self.%class%_init(objj,trace)
    return(ans)
  # end testbed

  # procedures 
  """
    temps['sec4'] = """
  def %class%_proc%cell%(self,objj,trace):
    if trace == 1:
      xx = raw_input ( 'begin %class%_proc%cell%') 
    retbox = [0,objj,trace] # initilize by type
    # %rec%
    # assume all verbs are tests
    ans = objj['v']["%verb%"](objj,trace)
    ret = ans[0]
    objj = ans[1]
    trace = ans[2]
    if (ret == 0):
        NextPoint = %yesCell%
    elif (ret == -1):
        NextPoint = %noCell%
    else:
        NextPoint = ret
    #endif
    retbox[0]= NextPoint
    return(retbox)
  # end def %class%_proc%cell% 
  """
    temps['sec5'] = """
  

  
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
  """

    temps['sec6'] = """
# end class %class%
  """
    # vector (%vector%)
    temps['vector'] = """
# file v_%vector%.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_%vector%")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    if(trace == 1):
		x = raw_input("debug " + "... ")
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
				 print("unknown(", x , ")")
			#endif
			x = raw_input("debug " + "... ")
		#wend
	#endif
    return(retbox)
#end v_%vector%
                       
    """
    # eq for EQxx vectors (%vector%, %vval%)
    temps['eq'] = """
# file v_%vector%.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_%vector%")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    t = objj['ds'].pop()
    if (t == "%vval%"):
        retbox[0] = 0 # ok
    else:
        objj['ds'].push(t)
        retbox[0] = -1
    #endif
    return(retbox)
#end v_%vector%
                       
    """
    # work templates  assemble as work1 + @work lines + work2
    # work1(vector)
    temps['work1'] = """
# file v_%vector%.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_%vector%")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    """
    # work2(vector)
    temps['work2'] = """
    return(retbox)
#end v_%vector%
                       
    """
    
    temps['Lit'] = """
# file v_%vector%.py as a literal ($op)
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_%vector% , %Lit% ")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    objj['ds'].push("%Lit%")
    return(retbox)
#end v_%vector% (%Lit%)
                       
    """
       
    temps['callbox'] = """
# file v_%project%_%vector%.py 
def main(objj,trace):
    if(trace == 1):
        xx = raw_input("begin v_%project%_%vector%")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    # ps push return cell
    objj['ps'].push(%returnCell%)
    # set goto cell
    retbox[0] = %gotoCell%
    return(retbox)
#end v_%project%_%vector%

"""
    return(temps)
