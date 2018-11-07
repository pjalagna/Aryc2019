
# file v_cleanup.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_cleanup")
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
#end v_cleanup
                       
    