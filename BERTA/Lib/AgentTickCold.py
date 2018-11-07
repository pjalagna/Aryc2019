# filename: AgentTickCold.py
# pja 06-02-2017 orig
nop = """ test
# set profile
profile = {}
# record death location
profile['deathTable'] = 'Tick'
profile['deathCol'] = 'C'
profile['deathMark'] = 'die'

# record active location
profile['Table'] = 'tick'
profile['col'] = 'C'
profile['mark'] = 'TCold'

profile['status'] = 'not running'

AgentTickCold.main(profile)
# set tick.C == 'TCold'
# set tick.C == "die"
"""
#print(nop)
def main():
    """ prototype """
    import time
    print('==========agent begin')
    # (C)
    ctlC = 0
    while (ctlC == 0):
        """ if asked to die then die """
        m0 = SQget(profile['deathTable'],profile['deathCol'])
        if (m0 == profile['deathMark']):
            print("==========Agent asked to die")
            profile['status'] = 'to die'
            ctlC = -1 # break
        elif (m0 == profile['mark']):
            print("==========Agent asked to do work")
            profile['status'] = 'do work'
            ctlC = -2 # break
        else:
            print("==========Agent will sleep - (" + time.asctime() + ")")
            time.sleep(5) # seconds
            ctlC = 0 # loop
    #wend
    return(profile)
#end agentHead
            
        
        
        
        
        
        
        
def TCold():
    """ set agent """
    # set profile
    profile = {}
    # record death location
    profile['database'] = 'berta1'
    profile['deathTable'] = 'Tick'
    profile['deathCol'] = 'C'
    profile['deathMark'] = 'die'

    # record active location
    profile['Table'] = 'tick'
    profile['col'] = 'C'
    profile['mark'] = 'TCold'

    profile['status'] = 'not running'
    # import agentHead
    m = agentHead.main(profile)
    print('profile at return=' + m.__str__() + ")")
#end TCold

def findSet():
    """ find working set of bundles """      
	# clear(bq1)
	SQClearQ("bq1")
	# clear(bq2)
	SQClearQ("bq2")
	# clear(bq3)
	SQClearQ("bq3")
	# collect all bundles with cold=on 
	m1 = SQgetWhere('b',"bid", "b.cold='on'") 
	# -> //bq1//
	SQWriteListQ('bq1',m1)
	#(A)
	ctlA = 0
	while (ctlA ==0):
                """ x """
                # from bb get children of bq1 */
                # getIn(b.child,b.parent,in(bq1)) -> bq2 
                # if nof ==>  goto (B)
                m2 = SQgetIn('bb','b.child','b.parent','bq1')
                if (len(m2) == 0):
                    ctlA = -1 # if nof ==> goto (B)
                else:
                    """ x """
                    # m2 -> bq2
                    SQMoveListQ(m2,'bq2')
                    # move bq1 to final NOTE: move not copy*/
                    SQMoveQ("bq1","bq3") # -> //bq3//
                    # move bq2 (child) to become parents */
                    SQMoveQ("bq2","bq1") # -> //bq1//
                #endif
            #wend # Goto (A)
            #(B) 
            #Set tick.C = TRule1
            SQWriteT('tick','tick.C','TRule1')
            # sleep 
            st = 15 # test 15 sec, prod 1/100 sec==0.0100
            time.sleep(st)
        #wend #goto (C)
    #endif
    print("Agent dead")
#end main

#SQClearQ("bq1")
#SQget('tick','tick.C')
#SQgetWhere('b',"bid", "b.cold='on'") 
#SQWriteListQ('bq1',m1)
#SQgetIn('bb','b.child','b.parent','bq1')
#SQMoveListQ(m2,'bq2')
#SQMoveQ("bq1","bq3")
#SQWriteT('tick','tick.C','TRule1')




