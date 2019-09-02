
# file v_UBUBinitLib.py 
def main(objj,trace):
    """ edit date 6-3-13 """
    local = {} # local architecture ; dies with action
    local['ds'] = []
    local['nds'] = {}
    if(trace == 1):
        xx = raw_input("begin v_initLib")
    retbox = [0,objj,trace] # init by type
    # set status to retbox[0] = 0 ok -1 ng or #
    retbox[0] = 0 # default is ok
    # process work goes here
    # get project name
    fn = objj['nds'].att('project')
    fn = fn + '.db'
    # clear db file
    fh = open(fn,'w') # drops file
    fh.close()
    #new here
    objj['nds'].bang('MyName','sq')
    objj['nds'].bang('DBName',fn)
    import DBEClass
    objj['c']['DBE'] = {}
    objj['c']['DBE']['dbn'] = DBEClass.DBE()
    objj['c']['DBE']['dbn'].DBConnect(fn ,'ddi')
    objj['c']['DBE']['dbn'].DBMakeInstance('ddi','k1')
    objj['c']['DBE']['dbn'].PrepDB('k1')
    # write tables ===
    objj['c']['DBE']['dbn'].CreateTable('k1','BPX', [ 'pgfName' , 'cn' , 'vn' , 'elementName' , 'elementType' , '\0' ] , [ 'pgfName' , 'cn' , 'vn' ,  '\0' ])
    objj['c']['DBE']['dbn'].CreateTable('k1','SFile',[ 'mark' , 'FileName' , '\0' ],['mark' , '\0'])
    objj['c']['DBE']['dbn'].CreateTable('k1','Project',[ 'mark' , 'ProjectName' , '\0' ],['mark' , '\0'])
    return(retbox)
#end v_initLib
                       
    
