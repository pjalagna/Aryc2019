
# file v_initfioi.py 
def main(objj,trace):
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_initfioi")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
	j = objj['ds'].pop() # filename
	import fioiClass
	objj['c']['fioi'] = fioiClass.fio(j)
	objj['v']['ioi'] = objj['c']['fioi'].fioi
	objj['v']['ioo'] = objj['c']['fioi'].fioo
    return(retbox)
#end v_initfioi
                       
    