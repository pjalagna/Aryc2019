# filename: AgentHead.py
# pja 06-02-2017 orig
nop = """ test
profile = AgentHead.setProfile() # test profile
m = AgentHead.main(profile)
# m returns if profile database.table.col == mark or deathMark
# set Tick.C == 'fool' # agent will sleep
# set tick.C == 'TCold' # agent status == do work
# set tick.C == "die"   # agent statu == die

"""
#print(nop)
def main(profile):
    """ prototype """
    import time
    import SQClass
    db = SQClass.SQC(profile['database'])
    print('agent begin')
    # (C)
    ctlC = 0
    while (ctlC == 0):
        """ if asked to die then die """
        m0 = db.SQget(profile['deathTable'],profile['deathCol'])
        if (m0 == profile['deathMark']):
            print("==========" + profile['mark'] + " Agent asked to die")
            profile['status'] = 'to die'
            ctlC = -1 # break
        elif (m0 == profile['mark']):
            print("==========" + profile['mark'] + " Agent asked to do work")
            profile['status'] = 'do work'
            ctlC = -2 # break
        else:
            print("==========" + profile['mark'] + " Agent will sleep - (" + time.asctime() + ")")
            time.sleep(5) # seconds
            ctlC = 0 # loop
    #wend
    return(profile)
#end agentHead
""" help/test  routines """
def KillAgent():
    """ set Tick.C == die """
    import SQClass
    db = SQClass.SQC('berta1.db')
    db.SQX("update Tick set C = 'die' ;")
#end KillAgent
def SetAgent(mark):
    """ set Tick.C == die """
    import SQClass
    db = SQClass.SQC('berta1.db')
    db.SQX("update Tick set C = '" + mark + "' ;")
#end SetAgent
def setProfile():
	profile = {}
	# record death location
	profile['database'] = 'berta1.db'
	profile['deathTable'] = 'Tick'
	profile['deathCol'] = 'C'
	profile['deathMark'] = 'die'

	# record active location
	profile['Table'] = 'tick'
	profile['col'] = 'C'
	profile['mark'] = 'TCold'

	profile['status'] = 'not running'
	return(profile)
# enddef setProfile



