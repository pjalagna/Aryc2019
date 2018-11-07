
# file v_SLSL80SLSL74SLSL.py 
def main(objj,trace):
    if(trace == 1):
        xx = raw_input("begin v_SLSL80SLSL74SLSL")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    # ps push return cell
    objj['ps'].push(74)
    # set goto cell
    retbox[0] = 80
    return(retbox)
#end v_SLSL80SLSL74SLSL

