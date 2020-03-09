m = """
file TRCV.py
pja 03-06-2020 dropped need for IXX table use genX
-- added delete before write if TCVR existed
pja 03-06-2020 changed name to TRCV 
--  because that's the way you load it in basii
pja 03-05-2020

needs gennV, SQV, arV
standards:
TCVR - TCVR-1990 amended thru 2020
Basii - Basii-1980 amended thru 2020
SQSQ - transformation security 1990

TRCV+ TRCVPlus initilize database with table TCVR
TRCV0 TRCV0 (,,) drop all data in TCVR 
TRCV! TRCVWrite (T,R,C,V,,) into table
TRCV@ TRCVSeek (T,R,C,V,,ans) any or all may be blank chart
"""

"""
test as
p = {}
p['package'] = {}
p['help'] = {}
p['sy'] = {}
import TRCV
p = TRCV.main(p)

or

import useLib
import bbox
bbox.main('bmain')
bbox.start()

"pjadb.db"
"SQV"
takeV

"TRCV"
takeV

"gennV"
takeV
push
"arV"
takeV


"cust"
"xabc"
"Fname"
"Paul"
TRCV!
push
cust
push
xabc
push
Fname
push
John
TRCV!
.s
push
cust
push
xabc
push
Fname
push
Billy
TRCV!
.s
push
cust
push
xabc2
push
Fname
push
Billy
TRCV!
.s





"""
def main( p , m = m ):
    p['package']['TRCV'] = ''
    p['help']['TRCV'] = m
    """
    -TRCV+ TRCVPlus initilize database with tables TCVR
    -TRCV0 TRCV0 (,,) drop all data in TCVR 
    - TRCV! TRCVWrite (T,R,C,V,,) into table
TRCV@ TRCVSeek (T,R,C,V,,ans) any or all may be blank chart
    """
    p['sy']['TRCV+'] = TRCVPlus
    p['help']['TRCV+'] = 'initilize database with table TCVR'
    p['sy']['TRCV0'] = TRCVPlus
    p['help']['TRCV0'] = 'TRCV0 (,,) drop all data in TCVR'
    p['sy']['TRCV!'] = TRCVWrite
    p['help']['TRCV!'] = 'TRCV! (T,R,C,V,,) into table'
    p['sy']['TRCV@'] = TRCVseek
    p['help']['TRCV@'] = """ TRCV@ (T,R,C,V,,ans) 
any input may be ''
conditions returned are:
0 none => [t] == tables in database 
1 r => [t] == tables using r (side-car, etc)
2 v => [c] ** == no conflict w/ meta 
4 c => [v] == domain of c
6 cv => [r] == indexes where c=v
8 t => [r] == indexes of t
9 tr => [c] == structure of t at r
12 tc => [r] ** == no conflict w/ meta
13 tcr => v == value of c at r in t
14 tcv => [r] == indexes where c=v in t
15 tcvr => tcvr/0 == existence test
    """
    return(p)
#end main

def  TRCVseek(T,R,C,V):
    V = p['sy']['pop']()
    C = p['sy']['pop']()
    R = p['sy']['pop']()
    T = p['sy']['pop']()
    #tcvr = 8421
    Tsp = 0
    if (T!=''):
       Tsp = Tsp+8
    #endif 
    if (C!=''):
       Tsp = Tsp+4
    #endif 
    if (V!=''):
       Tsp = Tsp+2
    #endif 
    if (R!=''):
       Tsp = Tsp+1
    #endif
    print('TRCVSeek Tsp=(' + Tsp +')')
    if (Tsp==0):    #
        # 0 none => [t] == tables in database 
        Tsq = 'select distinct(T) from TCVR;'
    #endif
    if (Tsp==1):
        # 1 r => [t] == tables using r (side-car, etc)
        Tsq = "select distinct(T) from TCVR where R ='" + R + "' ;" 
    #endif
    if (Tsp==2):
        # 2 v => [c] ** == no conflict w/ meta == where used
        Tsq = "'" + V + "' ;"
    #endif       
    if (Tsp==4):
        # 4 c => [v] == domain of c
        Tsq = "select distinct(V) from TCVR where C = '" + C + "' ;"
    #endif       
    if (Tsp==6):
        #6 cv => [r] == indexes where c=v
        Tsq = "select distinct(R) from TCVR where C = '" + C + "' and  V = '" + V + "'  ; ";
    #endif             
    if (Tsp==9):
        #9  tr => [c] == structure of t at r
        Tsq = "select distinct(C) from TCVR where T = '" + T + "' and R = '" + R + "' ;"
    #endif       
    if (Tsp==12):
        #12  tc => [r] ** == no conflict w/ meta where used
        Tsq = "select distinct(R) from TCVR where T = '" + T + "' and C = '" + C + "' ;"
    #endif       
    if (Tsp==13):
        #13 tcr => v == value of c at r in t
        Tsq = "select V from TCVR where T = '" + T + "' and C = '" + C + "' and R = '" + R + "' ;"
    #endif       
    if (Tsp==14):
        #14 tcv => [r] == indexes where c=v in t
        Tsq = "select distinct(R) from TCVR where T = '" + T + "' and C = '" + C + "' and V = '" + V + "' ;"
    #endif       
    if (Tsp==15):
        #15 tcvr => 1/0 == existence test
        Tsq = "select count(*) from TCVR where T = '" + T + "' and C = '" + C + "' and V = '" + V + "' and R = '" + R + "' ;"
    #endif       
    print('TRCV@ select=(' + Tsq +')')
    # push
    p['sy']['push'](Tsq)
    # readall
    p['sy']['SQReadAll'](p)
    p['sy']['pop']() #ok
    p['sy']['push'](p['OK'])
#end TRCVSeek

def TRCVWrite(p):
    # (T,R,C,V,,)
    V = p['sy']['pop']()
    C = p['sy']['pop']()
    R = p['sy']['pop']()
    T = p['sy']['pop']()
    # see if this exists y-delete + add;  no-write
    Tans2 = 'select V from TCVR ' 
    Tans2 += " where T = '" + T + "'"
    Tans2 += " and C = '" + C + "'"
    Tans2 += " and R = '" + R + "';"
    print('TRCV! select=('+ Tans2 +')')
    p['sy']['push'](Tans2)
    p['sy']['SQReadAll'](p)
    p['sy']['pop']() # ok
    # test
    tst = p['sy']['pop']()
    if (tst.__len__()!=0):
        #if exists delete first DELETE FROM tableWHERE search_condition;
        Tans22 = "DELETE FROM TCVR "
        Tans22 += " where T = '" + T + "'"
        Tans22 += " and C = '" + C + "'"
        Tans22 += " and R = '" + R + "';"
        print('TRCV! delete=('+ Tans22 +')')
        p['sy']['push'](Tans22)
        # sqx
        p['sy']['SQX'](p)
        p['sy']['pop']()
        tst='' # fake test for insert
    #endif
    if (tst.__len__()==0):
        # nof then insert
        p['sy']['genX'](p)
        p['sy']['pop']()
        ix = p['sy']['pop']()
        Tic = "insert into TCVR  values ("
        Tic += "'" + ix + "',"
        Tic += "'" + T + "',"
        Tic += "'" + C + "',"
        Tic += "'" + V + "',"
        Tic += "'" + R + "' );"
        print('TRCV! insert=('+ Tic +')')
        p['sy']['push'](Tic)
        # sqx
        p['sy']['SQX'](p)
        p['sy']['pop']()
    #endif
    p['sy']['push'](p['OK']) # ok
# end TRCVWrite

def TRCV0(p):
    p['sy']['push']("Truncate TABLE TCVR ;")
    p['sy']['SQX'](p)
    p['sy']['pop']()
    p['sy']['push'](p['OK'])
# end TRCV0

def TRCVPlus(p):
	p['sy']['push']("""create table if not exists TCVR ( IXX numeric(12), T varchar(1000) , C varchar(1000), V varchar(10000), R varchar(1000) , primary key (IXX) ) ;""")
	p['sy']['SQX'](p)
	p['sy']['pop']()
	p['sy']['push'](p['OK'])
#end TCVRPlus
