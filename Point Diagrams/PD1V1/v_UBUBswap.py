
# file v__swap.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v__swap")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    x1 = objj['ds'].pop()
    x2 = objj['ds'].pop()
    objj['ds'].push(x1)
    objj['ds'].push(x2)
    return(retbox)
#end v__swap
                       
    