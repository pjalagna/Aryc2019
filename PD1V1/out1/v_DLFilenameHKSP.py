
# file v_DLFilenameHKSP.py as a literal ($op)
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_DLFilenameHKSP , Filename?  ")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    objj['ds'].push("Filename? ")
    return(retbox)
#end v_DLFilenameHKSP (Filename? )
                       
    