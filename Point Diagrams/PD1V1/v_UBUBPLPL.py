
# file v_UBUBPLPL.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_cnPLPL")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    cns = objj['ds'].pop()
    cn = int(cns) + 1
    objj['ds'].push(cn.__str__())
    return(retbox)
#end v_UBUBPLPL
                       
    
