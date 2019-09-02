# file simpleVectorStk

def main(objj):
    """ uses simpleStk \n
        places class in objj['c']
        places each method in objj['s'] \n
        usage like  objj['s'].pushdat(xx)
    """
    objj['ds'] = {} # data stack
    objj['ps'] = {} # program (return) stack
    import simpleStk
    objj['ds'] = simpleStk.Stk()
    objj['ps'] = simpleStk.Stk()
    objj['c']['Stk'] = simpleStk
    return(objj)
#end main
    
    
