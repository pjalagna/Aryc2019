
# file v_writeBPXRecord.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_writeBPXRecord")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    # if lit element adjust name, set lit type
    gg = objj['nds'].att('cwd1')
    if (gg[0] == "'"): # if tick
        ff = gg[1 : -1] # all but the ticks
        ff2 = "L"
    else:  # else use name, type = simple
        ff = gg
        ff2= "V"
    #endif
    objj['c']['DBE']['dbn'].WriteRecord('k1','BPX', [ 'pgfName' ,  objj['nds'].att('pgfName') ,  'cn' ,  objj['nds'].att('cn') ,  'vn' , objj['nds'].att('vn') , 'elementName' ,  ff  , 'elementType' , ff2 , '\0' ])
    return(retbox)
#end v_writeBPXRecord
                       
    