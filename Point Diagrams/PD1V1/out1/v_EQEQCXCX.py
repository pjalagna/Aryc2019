
# file v_EQEQCXCX.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_EQEQCXCX")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    t = objj['ds'].pop()
    if (t == "]]"):
        retbox[0] = 0 # ok
    else:
        objj['ds'].push(t)
        retbox[0] = -1
    #endif
    return(retbox)
#end v_EQEQCXCX
                       
    