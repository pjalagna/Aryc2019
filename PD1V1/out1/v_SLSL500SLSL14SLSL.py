
# file v_SLSL500SLSL14SLSL.py 
def main(objj,trace):
    if(trace == 1):
        xx = raw_input("begin v_SLSL500SLSL14SLSL")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    # ps push return cell
    objj['ps'].push(14)
    # set goto cell
    retbox[0] = 500
    return(retbox)
#end v_SLSL500SLSL14SLSL

