
# file v_UBUBBG.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v__BG")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    addr = objj['ds'].pop()
    vval = objj['ds'].pop()
    objj['nds'].bang(addr,vval)
    return(retbox)
#end v__BG
                       
    
