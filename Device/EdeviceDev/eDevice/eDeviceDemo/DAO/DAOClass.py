# file DAOClass.py
class DAO:
    def __init__(self,dbName):
        import SQClass
        self.dbName = dbName
        self.sq = SQClass.SQC(dbName)
    #end init

    def getDbName(self):
        return(self.dbName)
    #end getDBName
    
    def prep(self):
        """ prepares database for TCVR records """
        sq1 = 'create table TCVR ( ID, T, C, V, R , primary key ( ID ) ) ;'
        sq2 = 'create table IDX ( ID , A , primary key(A) ) ; '
        self.sq.SQX(sq1)
        self.sq.SQX(sq2)
        sq3 = "insert into IDX VALUES ( 1 , 'A' ) ; "
        self.sq.SQX(sq3)
    #end prep
        
    def close(self):
        self.sq.SQClose()
        self.sq = "no database connected"
    #end close
        
    def writeTCVR(self, ix,T,C,V,R):
        # see if record exists (exempt ix) if yes skip
        # get new ix if ix=0
        if ( ix ==0):
            ix = self.NextID()
        else:
            nop = -1 # nop
        #endif
        # insert statement
        sqw = 'insert into TCVR VALUES ('
        sqw += ix.__str__() + ' , '
        sqw += " '" + T.__str__() + "' , "
        sqw += " '" + C.__str__() + "' , "
        sqw += " '" + V.__str__() + "' , "
        sqw += " '" + R.__str__() + "' "
        sqw += ' ) ; '
        self.sq.SQX(sqw)
    #end writeTCVR
 

    def getID(self):
        sq1 = "select id from IDX where A = 'A' ; "
        v1 = self.sq.SQRead1(sq1)
        ans = float(v1[0])
        return(ans)
    #end getID
    
    def NextID(self):
        v1 = self.getID()
        v2 = v1 + 1
        sq2 = 'update IDX  set ID = ' + v2.__str__() + " , A = 'A'  ; "
        self.sq.SQX(sq2)
        return(v1)
    #end nextID

    def queryTCVR(self, M , T , C, V, R ):
        """ returns article (M) for values of TCVR """
        # select stmt
        sqs = 'select ' + M + ' from TCVR '
        wh = 'where'
        if (T != ""):
            if (wh == 'where'):
                sqs += ' where '
                wh = ' , and '
            #endif
            sqs += " T = '" + T.__str__() + "' "
        #endif
        if (C != ""):
            if (wh == 'where'):
                sqs += ' where '
                wh = ' , and '
            #endif
            sqs += " C = '" + C.__str__() + "' "
        #endif
        if (V != ""):
            if (wh == 'where'):
                sqs += ' where '
                wh = ' , and '
            #endif
            sqs += " V = '" + V.__str__() + "' "
        #endif
        if (R != ""):
            if (wh == 'where'):
                sqs += ' where '
                wh = ' , and '
            #endif
            sqs += " R = '" + R.__str__() + "' "
        #endif
        sqs += ' ; '
        ans = self.sq.SQReadAll(sqs)
        return(ans)
    #end queryTCVR
    

        

        
        
        
    
        
        
