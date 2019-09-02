
# file v__AT.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v__AT")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    j = objj['ds'].pop()
    ans = objj['nds'].att(j)
    objj['ds'].push(ans)
    return(retbox)
#end v__AT
                       
    