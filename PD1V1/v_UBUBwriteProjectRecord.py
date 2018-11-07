
# file v_writeProjectRecord.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_writeProjectRecord")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    pj = objj['nds'].att('project')
    # write project record 
    objj['c']['DBE']['dbn'].WriteRecord( 'k1','Project', ['mark' , 'a', 'ProjectName' , pj , '\0' ])
    return(retbox)
#end v_writeProjectRecord
                       
    