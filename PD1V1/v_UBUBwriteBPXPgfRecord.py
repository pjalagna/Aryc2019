
# file v_writeBPXPgfRecord.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_writeBPXPgfRecord")
    #endif
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    objj['c']['DBE']['dbn'].WriteRecord('k1','BPX' ,[ 'pgfName' ,  objj['nds'].att('pgfName') ,  'cn' ,  objj['nds'].att('cn') ,  'vn' , objj['nds'].att('vn') , 'elementName' ,  objj['nds'].att('cwd1') , 'elementType' , 'P' , '\0' ] )
    return(retbox)
#end v_writeBPXPgfRecord
                       
    