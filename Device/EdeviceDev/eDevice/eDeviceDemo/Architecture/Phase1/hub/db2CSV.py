# file db2CSV.py
def main(dbName):
    """ converts TCVR file into out.csv """
    import DAOClass
    d = DAOClass.DAO(dbName)
    a = d.queryTCVR("*",'','','','')
    # open and write header
    fh = open('out.csv','w') # open and clear
    fh.write ('ID,T,C,V,R \n')
    for rx in range(len(a)):
        ls = ''
        for cx in range(len(a[0])):
            if (cx ==0):
                ls += a[rx][cx].__str__()
            else:
                ls += ' , ' + a[rx][cx].__str__()
            #endif
        #end for cx
        ls += '\n'
        fh.write(ls)
    #endfor rx
    fh.close()
    print("file out.csv created ")
#end main
    

    
    
    
