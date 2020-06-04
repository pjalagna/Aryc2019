"""
file OntologyClass.py
pja 6/2/2020 added doc 
pja 5/29/2020 redo format
pja 5/26/2020 

see .help() for more
"""

"""
test as
import useLib
import OntologyClass
og1 = OntologyClass.Ontology("TestdbName.Onto",'on')


og1.GUid('abc')
og1.GUid('abc')

import SQClass
dbx = SQClass.SQC("TestdbName.Onto")
sqx1 = 'select * from v20;'
dbx.SQReadAll(sqx1)

"""
# private functions
def timestamp():
    global gti
    ans = "X"
    a2 = gti.time()*100000
    ans = ans + str(int(a2))
    logg('timestamp=('+ ans +')')
    return(ans)
#timestamp

def help():
    ans = """
    ontology object
    data:
        none all held on sqlite database init(name)+".Onto"
    signals:
    help()/HELP() this message
    GUid(element) 
    returns an element that is unique. if the parameter was unique it is returned intact (and stored in the guid table). if the parameter was already known what is returned will have an added timestamp. this same will be stored.
    
    VAR       name,value,flags=''
    THING     name,value
    PREDICATE name,value
    ATN       name1,value1,name2,value2,flags=''
    RELATE    name1,value1,relateType,relateValue,name2,value2
    RDF       SubjectName, SubjectValue, PredicateName, PredicateValue, ObjectName, ObjectValue
    
    
    """
    return(ans)
#help
global logg
def logg(txt):
    global gt
    if (gt == 'on'):
        print(txt)
    #endif
#logg
def createDatabase(db):
    """
    creates GUID and v20 tables
    GUID ( element, primary key(element))
    V20 (VIX,  v1--v19 VType, primary key(VIX))
    """
    #--- guid table
    sqg = "create table GUID ( element, primary key(element));"
    db.SQX(sqg)
    #--- insert 0 this is tested for table existance
    sqgi = "insert into GUID (element) values ('0');"
    db.SQX(sqgi)
    #--- v20 table
    sqv = " create table V20 (VIX,  v1 , v2 , v3 , v4 , v5 ,v6 , v7 , v8, v9 , v10, v11 , v12 , v13 , v14 , v15, v16, v17, v18, v19, VType, primary key(VIX))"
    db.SQX(sqv)
    global logg,gt
    logg('database created')
#create database
class Ontology:
    def VARWrite(self,name1,value1,flags=''):
        """
        VARWrite(self,name1,value1,flags='')
        """
        vix = timestamp()
        # reserve record
        sq1 = "insert into v20 (VIX) values ('%vix%') ;"
        sq1 = sq1.replace('%vix%',vix)
        self.db.SQX(sq1)
        sop = ''
        sop = """
UPDATE v20 
SET 
VType = 'VAR',
v1 = '%name1%',
v2 = '%value1%',
v19 = '%flags%'
WHERE
    VIX = '%vix%' ;
        """
        sop = sop.replace('%vix%',vix)
        sop = sop.replace('%name1%',name1)
        sop = sop.replace('%value1%',value1)
        sop = sop.replace('%flags%',flags)
        logg('VARWrite (' +sop+ ')')
        self.db.SQX(sop)
    #OperationWrite
    
    def VARSeek(self,name1='',value1=''):
        """
        VARSeek(self,name1='',value1='')
        """
        sqs = "select * from v20 where VType = 'VAR' "
        if (name1 <> ''):
           sqs = sqs + ' and ' + 'v1 =' + "'" + name1 + "'" 
        #endif
        if (value1 <> ''):
           sqs = sqs + ' and ' + 'v2 =' + "'" + value1 + "'" 
        #endif
        sqs = sqs + ';'
        logg('rdfseek sq=('+ sqs + ')')
        ans = self.db.SQReadAll(sqs)
        return(ans)
    #VARSeek
        
        
        
    def __init__(self,dbFilename,trace=''):
        global logg,gt,gti
        self.trace = trace
        gt = self.trace
        logg('here at init')
        import time
        self.t = time
        gti = self.t
        #set __doc__ help
        self.__doc__ = help()
        #open/ create database
        import SQClass
        self.db = SQClass.SQC(dbFilename)
        # if no tables then create tables
        try:
            m = self.db.SQReadAll('select * from GUID;')
        except:
            createDatabase(self.db)
        finally:
            nop = 1
        #endtry
    #init
    def GUid(self,element):
        """
        GUID verifies an id or creates a new id if id exists
        """
        sg = "select * from GUID where element = '"+element+"' ;"
        m = self.db.SQReadAll(sg)
        ans = ''
        # if element is new add element to table return element
        if (len(m) == 0):
            #new
            ans = element
            #new record
            gi = "insert into GUID (element) values ('%element%') ;"
            gi = gi.replace('%element%',element)
            logg("GUID gi=(" + gi + ")")
            self.db.SQX(gi)
        else: # else exists add timestamp overwrite
            ans = element + ':-:' + timestamp()
            #overwrite record
            gu = "update GUID set element = '"+ans+"' where element = '" + element + "';"
            logg("GUID gu=(" + gu + ")")
            self.db.SQX(gu)
        #endif
        return(ans)
    #GUID
        
    def RDFWrite(self,SubjectName, SubjectValue, PredicateName, PredicateValue, ObjectName, ObjectValue):
        """
        RDFWrite(self,SubjectName, SubjectValue, PredicateName, PredicateValue, ObjectName, ObjectValue)
        """
        vix = timestamp()
        # reserve record
        sq1 = "insert into v20 (VIX) values ('%vix%') ;"
        sq1 = sq1.replace('%vix%',vix)
        self.db.SQX(sq1)
        sqRDF = """
UPDATE v20 
SET 
VType = 'RDF',
v1 = '%SubjectName%', 
v2 = '%SubjectValue%', 
v3 = '%PredicateName%', 
v4 = '%PredicateValue%', 
v5 = '%ObjectName%', 
v6 = '%ObjectValue%'

WHERE
    VIX = '%vix%' ;
        """
        #replace markers
        sqRDF = sqRDF.replace('%vix%',vix)
        #SubjectName, SubjectValue, PredicateName, PredicateValue, ObjectName, ObjectValue
        sqRDF = sqRDF.replace('%SubjectName%',SubjectName)
        sqRDF = sqRDF.replace('%SubjectValue%',SubjectValue)
        sqRDF = sqRDF.replace('%PredicateName%',PredicateName)
        sqRDF = sqRDF.replace('%PredicateValue%',PredicateValue)
        sqRDF = sqRDF.replace('%ObjectName%',ObjectName)
        sqRDF = sqRDF.replace('%ObjectValue%',ObjectValue)
        logg('RDFWrite (' +sqRDF+ ')')
        self.db.SQX(sqRDF)
    #RDFWrite
    def RDFSeek(self,SubjectName='', SubjectValue='', PredicateName='', PredicateValue='', ObjectName='', ObjectValue=''):
        """
        RDFSeek(self,SubjectName='', SubjectValue='', PredicateName='', PredicateValue='', ObjectName='', ObjectValue='')
        """
        sqs = "select * from v20 where VType = 'RDF' "
        if (SubjectName <> ''):
           sqs = sqs + ' and ' + 'v1 =' + "'" + SubjectName + "'" 
        #endif
        if (SubjectValue <> ''):
           sqs = sqs + ' and ' + 'v2 =' + "'" + SubjectValue + "'" 
        #endif
        if (PredicateName <> ''):
           sqs = sqs + ' and ' + 'v3 =' + "'" + PredicateName + "'" 
        #endif
        if (PredicateValue <> ''):
           sqs = sqs + ' and ' + 'v4 =' + "'" + PredicateValue + "'" 
        #endif
        if (ObjectName <> ''):
           sqs = sqs + ' and ' + 'v5 =' + "'" + ObjectName + "'" 
        #endif
        if (ObjectValue <> ''):
           sqs = sqs + ' and ' + 'v6 =' + "'" + ObjectValue + "'" 
        #endif
        sqs = sqs + ';'
        logg('rdfseek sq=('+ sqs + ')')
        ans = self.db.SQReadAll(sqs)
        return(ans)
    #RDFSeek
    #ATN
    def ATNWrite(self,name1,value1,name2,value2,flags=''):
        """
        ATNWrite(self,name1,value1,name2,value2,flags='')
        """
        vix = timestamp()
        # reserve record
        sq1 = "insert into v20 (VIX) values ('%vix%') ;"
        sq1 = sq1.replace('%vix%',vix)
        self.db.SQX(sq1)
        sqFact = """
        UPDATE v20 
        SET 
        VType = 'ATN',
        v1 = '%name1%',
        v2 = '%value1%',
        v3 = '%name2%',
        v4 = '%value2%',
        v19 = '%flags%'
        WHERE
            VIX = '%vix%' ;
        """
        
        sqFact = sqFact.replace('%vix%',vix)
        sqFact = sqFact.replace('%name1%',name1)
        sqFact = sqFact.replace('%value1%',value1)
        sqFact = sqFact.replace('%name2%',name2)
        sqFact = sqFact.replace('%value2%',value2)
        sqFact = sqFact.replace('%flags%',flags)
        logg('ATNWrite sq=(' + sqFact + ')')
        self.db.SQX(sqFact)
    #ATNWrite
    def ATNSeek(self,name1='',value1='',name2='',value2='',flags=''):
        """
        ATNSeek(self,name1='',value1='',name2='',value2='',flags='')
        """
        sqs = "select * from v20 where VType = 'ATN' "
        if (name1 <> ''):
           sqs = sqs + ' and ' + 'v1 =' + "'" + name1 + "'" 
        #endif
        if (value1 <> ''):
           sqs = sqs + ' and ' + 'v2 =' + "'" + value1 + "'" 
        #endif
        if (name2 <> ''):
           sqs = sqs + ' and ' + 'v3 =' + "'" + name2 + "'" 
        #endif
        if (value2 <> ''):
           sqs = sqs + ' and ' + 'v4 =' + "'" + value2 + "'" 
        #endif
        if (flags <> ''):
           sqs = sqs + ' and ' + 'v19 =' + "'" + flags + "'" 
        #endif
        sqs = sqs + ';'
        ans = self.db.SQReadAll(sqs)
        return(ans)
    #ATNSeek
    
    #Relate
    def RELATEWrite(self, Name1, Value1, relateType,relateValue,Name2, Value2,flags=''):
        """
        RELATEWrite(self, Name1, Value1, relateType,relateValue,Name2, Value2,flags='')
        """
        vix = timestamp()
        # reserve record
        sq1 = "insert into v20 (VIX) values ('%vix%') ;"
        sq1 = sq1.replace('%vix%',vix)
        self.db.SQX(sq1)
        sqFact = """
        UPDATE v20 
        SET 
        VType = 'RELATE',
        v1 = '%Name1%',
        v2 = '%Value1%',
        v3 = '%relateType%',
        v4 = '%relateValue%',
        v5 = '%Name2%',
        v6 = '%Value2%',
        v19 = '%flags%'
        WHERE
            VIX = '%vix%' ;
        """
        
        sqFact = sqFact.replace('%vix%',vix)
        sqFact = sqFact.replace('%Name1%',Name1)
        sqFact = sqFact.replace('%Value1%',Value1)
        sqFact = sqFact.replace('%relateType%',relateType)
        sqFact = sqFact.replace('%relateValue',relateValue)
        sqFact = sqFact.replace('%Name2%',Name2)
        sqFact = sqFact.replace('%Value2%',Value2)
        sqFact = sqFact.replace('%flags%',flags)
        logg('ATNWrite sq=(' + sqFact + ')')
        self.db.SQX(sqFact)
    #RELATEWrite
    def RELATESeek(self, Name1='', Value1='', relateType='',relateValue='',Name2='', Value2='',flags=''):
        """
        RELATESeek(self, Name1='', Value1='', relateType='',relateValue='',Name2='', Value2='',flags='')
        """
        #factTrack, UICI, lnName, nsName, Name, lnValue, nsValue, Value
        sqs = "select * from v20 where VType = 'RELATE' "
        if (Name1 <> ''):
           sqs = sqs + ' and ' + 'v1 =' + "'" + Name1 + "'" 
        #endif
        if (Value1 <> ''):
           sqs = sqs + ' and ' + 'v2 =' + "'" + Value1 + "'" 
        #endif
        if (relateType <> ''):
           sqs = sqs + ' and ' + 'v3 =' + "'" + relateType + "'" 
        #endif
        if (relateValue <> ''):
           sqs = sqs + ' and ' + 'v4 =' + "'" + relateValue + "'" 
        #endif
        if (Name2 <> ''):
           sqs = sqs + ' and ' + 'v5 =' + "'" + Name2 + "'" 
        #endif
        if (Value2 <> ''):
           sqs = sqs + ' and ' + 'v6 =' + "'" + Value2 + "'" 
        #endif
        if (flags <> ''):
           sqs = sqs + ' and ' + 'v19 =' + "'" + flags + "'" 
        #endif
        sqs = sqs + ';'
        ans = self.db.SQReadAll(sqs)
        return(ans)
    #ATNSeek
    
    #BPX
    #BERTA
#end class
    