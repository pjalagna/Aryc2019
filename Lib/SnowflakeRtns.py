"""
file SSnowflakeRtns.py

pja 5/12/2020 added snowflake2csv
pja 5/7/2020

routines to write 6-point snowflake arrays into ProAr
see snowflakeDatabase.txt for formats

test as
import useLib
import SnowflakeRtns
SnowflakeRtns.ProfileInit()
atv = 't1'
atn = 'marker'
kri = 'box1'
SnowflakeRtns.ProfilePlus("ATN",atn,atv,"KRI",kri)
SnowflakeRtns.ProfilePlus("KRI",kri,"ATN",atn,atv)
SnowflakeRtns.ProfilePlus("UID",kri)
# dup test

SnowflakeRtns.ProfilePlus("KRI",kri,"ATN",atn,atv)
kri = 'box2'
atn = 'b1b'
atv= '32'
SnowflakeRtns.ProfilePlus("KRI",kri,"ATN",atn,atv)
SnowflakeRtns.ProfilePlus("ATN",atn,atv,"KRI",kri)
SnowflakeRtns.ProfilePlus("UID",kri)
kri = 'dd1'
atv = '33'
SnowflakeRtns.ProfilePlus("KRI",kri,"ATN",atn,atv)
SnowflakeRtns.ProfilePlus("ATN",atn,atv,"KRI",kri)
SnowflakeRtns.ProfilePlus("UID",kri)

m = SnowflakeRtns.getProAr()
SnowflakeRtns.dispProAr(m)

"""
global snowflakeRtns
import SnowflakeRtns
snowflakeRtns = SnowflakeRtns

def getds():
    import time
    ds = time.time().__str__()
    return(ds)
#
def ProfileInit():
    global ProAr
    ProAr = {} # [type][typeValue][structure][name][value][duplicateKB]
#


def ProfilePlus(type,typeValue,structure='',name='',value='',ds=''):
    global ProAr,snowflakeRtns
    import time
    #does type exist?
    print('profile',type,typeValue,structure,name,value,ds )
    try:
        tx = ProAr[type]
    except:
        ProAr[type] = {}
    finally:
        nop =1
    #
    #does ProAr[typeject][typeValue] exist?
    try:
        tx = ProAr[type][typeValue]
    except:
        ProAr[type][typeValue] = {}
    finally:
        nop =1
    #
    #does ProAr[typeject][typeValue][structure] exist?
    try:
        tx = ProAr[type][typeValue][structure]
    except:
        ProAr[type][typeValue][structure] = {}
    finally:
        nop =1
    #
    #does ProAr[typeject][typeValue][structure][name] exist?
    try:
        tx = ProAr[type][typeValue][structure][name]
    except:
        ProAr[type][typeValue][structure][name] = {}
    finally:
        nop =1
    #
    #does ProAr[typeject][typeValue][structure][name][value] exist?
    try:
        tx = ProAr[type][typeValue][structure][name][value]
    except:
        ProAr[type][typeValue][structure][name][value] = {}
    finally:
        nop =1
    #
    #does ProAr[typeject][typeValue][structure][name][value][ds] exist?
    try:
        tx = ProAr[type][typeValue][structure][name][value][ds]
        doagain = 1
    except:
        ProAr[type][typeValue][structure][name][value][ds] = ''
        doagain = 0
    finally:
        nop =1
    #
    if (doagain == 1):
        ds = time.time().__str__()
        print("duplicate breaker("+ ds + ")")
        SnowflakeRtns.ProfilePlus( type, typeValue, structure, name, value, ds )
    #endif    
#end ProfilePlus 

def getProAr():
    global ProAr
    return(ProAr)
#
def getPRec(type,typeValue='',structure='',name='',value='',ds=''):
    global ProAr
    ans = ProAr[type]
    if (typeValue <> ''):
        try:
            ans = ProAr[type][typeValue]
        except:
            ans = -1
        finally:
            nop = 1
        #endtry
    #
    if (structure <> ''):
        
        try:
            ans = ProAr[type][typeValue][structure]
        except:
            ans = -1
        finally:
            nop = 1
        #endtry
    #
    if (name <> ''):
        
        try:
            ans = ProAr[type][typeValue][structure][name]
        except:
            ans = -1
        finally:
            nop = 1
        #endtry
        
    #
    if (value <> ''):
        
        try:
            ans = ProAr[type][typeValue][structure][name][value][ds]
        except:
            ans = -1
        finally:
            nop = 1
        #endtry
    #
    return(ans)
#
def snowflake2csv(ar):
    ss = "v1,v2,v3,v4,v5,v6\n"
    s = 0
    for type in ar:
        for typeValue in ar[type]:
            for structure in ar[type][typeValue]:
                for name in ar[type][typeValue][structure]:
                    for value in ar[type][typeValue][structure][name]:
                        for ds in ar[type][typeValue][structure][name][value]:
                            s = s + 1
                            ss1 = type.__str__() + ',' + typeValue.__str__() + ',' + structure.__str__() + ',' + name.__str__() + ',' + value.__str__() + ',' + ds.__str__()
                            ss = ss + ss1 + '\n'
                        #endfor ds
                    #endfor val
                #endfor na
            #endfor struct
        #endfor typeval
    #endfor type
    return(ss)
#
def getPRecK(type,typeValue='',structure='',name='',value='',ds=''):
    global ProAr
    ans = ProAr[type].keys()
    if (typeValue <> ''):
        ans = ProAr[type][typeValue].keys()
    #
    if (structure <> ''):
        ans = ProAr[type][typeValue][structure].keys()
    #
    if (name <> ''):
        ans = ProAr[type][typeValue][structure][name].keys()
    #
    if (value <> ''):
        ans = ProAr[type][typeValue][structure][name][value].keys()
    #
    return(ans)
#
    
    
def dispProAr(ar):
    s = 0
    for type in ar:
        for typeValue in ar[type]:
            for structure in ar[type][typeValue]:
                for name in ar[type][typeValue][structure]:
                    for value in ar[type][typeValue][structure][name]:
                        for ds in ar[type][typeValue][structure][name][value]:
                            s = s + 1
                            print(s,type,typeValue,structure,name,value,ds)
                        #endfor ds
                    #endfor val
                #endfor na
            #endfor struct
        #endfor typeval
    #endfor type
#end dispProAr
def DBrecord(uniquesw,v1,v2,v3='',v4='',v5='',v6=''):
    """
    write DBrecord (uniquesw,v1-v6) => ok/nok on unique
    uniquesw 'replace' , 'both' , 'error=""'
                                   error == return nok don't insert
                          both == genx ds
             replace == update
    """
#
def DBInit(nsName):
    global SFdb
    import SQClass
    import os
    fp = os.getcwd()
    # create repository name from nsName
    dbFileName = fp + '/' + nsName + ".repos"
    #filename exist?
    if (os.path.exists(dbFileName) == True):
        ## y 
        SFdb = SQClass.SQC(dbFileName) # open
    else: ## n create and create table
        SFdb = SQClass.SQC(dbFileName) # create and open
        cre = """
 create table snowflake (
 rid not null 
 v1 not null,
 v2 null,
 v3 null,
 v4 null,
 v5 null,
 v6 null,
 primary key (rid)
);
    """
        SFdb.SQX(cre)
    #endif
      
#
def DBSeek(v1,v2='',v3='',v4='',v5='',v6=''):
    """
    lots of options
        thinking of stored scripts w/ parameters
        no scriptname == select * from ??
        OR follow array convention
        UID value
        ATN name value name value
        KRID value ATN name value
        name value name value
        
        atn name value krid kridv
        v1 = 'atn' and v2<>'' and v3='' => domain of v2
        v1 = 'atn' and v2<>'' and v3<>'' => keys of [v2]=v3
        krid val atn '' dominion of krid
    """
    sq = 'select %a% from snowflake'
#
"""

Notes convert to db

import SQClass
SFdb = SQClass.SQC(dbFileName)

create table snowflake (
 rid not null 
 v1 null,
 v2 null,
 v3 null,
 v4 null,
 v5 null,
 v6 null,
 fileNa null,
 ds  null,
 primary key (rid)
);

create table UIQ (rix not null, promary key (rix));

#use genx for index

insert into snowflake 
(v1,v2,v3,v4,v5) values
( 'ATN', 'local' , 'Name','GRID','Jhh11');

insert into snowflake 
(v1,v2) values
('GRID','answer');

sqSN = 'select * from snowflake;'
ans = db.SQReadAll(sqSN)





"""