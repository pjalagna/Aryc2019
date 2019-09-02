
# file v_initSQClass.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_initSQClass")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    t = objj['ds'].pop()
    import SQClass
    objj['c']['fioi'] = SQClass.SQC(t)
    objj['v']['dbRead'] = objj['c']['fioi'].SQReadAll
    objj['v']['dbWrite'] = objj['c']['fioi'].SQX
    return(retbox)
#end v_initSQClass
