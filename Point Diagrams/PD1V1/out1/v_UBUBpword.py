
# file v_UBUBpword.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_pword")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    c = 0
    while (c==0):
        m = objj['c']['fioi'].fpword()
        if (m[1] == "/*"):
            # comment
            while (m[1] != "*/"):
                    m = objj['c']['fioi'].fpword()
            #wend
            ## repeat
        else:
            # push this word
            objj['ds'].push(m[1])
            # post all info
            objj['nds'].bang('cwd0',m[0].__str__())
            objj['nds'].bang('cwd1',m[1].__str__())
            objj['nds'].bang('cwd2',m[2].__str__())
            c = -1 #break
        #endif  
	#wend
    if(trace == 1):
        xx = raw_input("pword ("+m.__str__() +")")
    #endif
    return(retbox)
#end v_pword
                       
    
