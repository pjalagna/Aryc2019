# file name SQClass.py
class SQC:
    """ DAO type class for i/f with sqlite databases """
    def __init__(self,dbna):
        """ connect and remember name """
        import sqlite3
        self.dh = sqlite3.Connection(dbna)
        self.cursor = self.dh.cursor()
        self.dbna = dbna
    # end def init
    def SQClose(self):
        self.cursor.close()
        self.dh.close
    # end def
    def hasRecords(self,dt):
        """ rets yes or no """
        mx = dt.__str__()
        # # print ('dt(' + mx.__str__() + ")")
        if ( mx.__str__() == "None"):
            ans = "no"
        else:
            ans = 'yes'
        #end if
        return(ans)
    # end def hasRecords
    def SQX(self, stmt):
        """ executes sql commands return is ?? """
        self.cursor = self.dh.cursor()
        self.drec = self.cursor.execute(stmt)
        self.dh.commit()
        ans = self.drec
        return(ans)
    # end def sqx
    def SQRead1(self,stmt):
        """ -- """
        self.cursor = self.dh.cursor()
        self.drec = self.cursor.execute(stmt)
        dt = self.drec.fetchone()
        self.cursor.close()
        return(dt)
    # end def SQRead1
    def SQReadFirst(self,stmt):
        """ -- """
        self.cursor = self.dh.cursor()
        self.drec = self.cursor.execute(stmt)
        dt = self.drec.fetchone()
        # check type of dt if nonetype close cursor
        return(dt.__str__())
    # end def SQReadFirst
    def SQReadNext(self):
        """ = """
        dt = self.drec.fetchone()
        # check type of dt if nonetype close cursor
        return(dt.__str__())
    # end def SQReadNext
    def SQReadAll(self,stmt):
        """ -- """
        self.cursor = self.dh.cursor()
        self.drec = self.cursor.execute(stmt)
        dt = self.drec.fetchall()
        self.cursor.close()
        return(dt)
    # end def SQReadAll
# end class
