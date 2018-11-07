# file name CreBerta.py version 2-04-2017
# creates all files for BERTA
# pja - 02-22-2017 added dataDict table 
# pja - 02-20-2017 added desc fields 
# pja - 2-04-2017 org
""" test as 
import CreBerta
"""

""" miller of BERTA 
in all cases xID is the same as <name>
where name must be one continious (no spaces,tabs or line breaks) converted to camelCase by convention.
"""

import SQClass
db=SQClass.SQC('berta')

""" type 1 tables """

"""
dataDict (( TableName, ColName ) desc , isNum, isKey, isFK, RefTable, RefCol )
"""
sq = """ create table dataDict ( TableName , ColName , desc , isNum, isKey, isFK, RefTable, RefCol, primary key ( TableName,ColName) ); """
db.SQX(sq)

"""
/* berta BPX table */
berta (( ParagraphName, ClauseNo, Sequence ) VerbType, VerbName, Literal )
"""
sq = """ create table berta ( ParagraphName, ClauseNo, Sequence , VerbType, VerbName, Literal , primary key ( ParagraphName, ClauseNo, Sequence ) );"""
db.SQX(sq)
sq=""" insert into dataDict ( 'berta' , 'ParagraphName' , 'see BPX definition' , '', 'isKey' , '' ,'', '' ); """
db.SQX(sq)
sq=""" insert into dataDict ( 'berta' , 'ClauseNo' , 'see BPX definition' , 'isNum', 'isKey' , '' ,'', '' ); """
db.SQX(sq)
sq=""" insert into dataDict ( 'berta' , 'Sequence' , 'see BPX definition' , 'isNum', 'isKey' , '' ,'', '' ); """
db.SQX(sq)
sq=""" insert into dataDict ( 'berta' , 'VerbType' , 'data switch L (for Litteral) or V (for Verb)' , '', '' , '' ,'', '' ); """
db.SQX(sq)
""" 
/* process BPX table */
process (( paragraphName, ClauseNo, Sequence ) VerbType, VerbName, Literal )
"""
sq = """ create table process ( paragraphName, ClauseNo, Sequence , VerbType, VerbName, Literal , primary key ( paragraphName, ClauseNo, Sequence ) ); """
db.SQX(seq)



""" sticky ((usr,na) vval ) """
sq = """ create table sticky ( usr , na , vval , primary key (usr,na) );"""
db.SQX(seq)

""" bundle ((bid) cold,ready ) """
seq = """create table bundle ( bid , cold, ready, primary key(bid));"""
db.SQX(seq)

""" rule ((rid) ) """
seq = """ create table rule (rid, desc, primary key(rid) ) ; """
db.SQX(seq)

""" test ((tid) V1Type, OP1Type, V2Type, OP2Type, V3Type ) """
seq = """ create table test (tid , desc , V1Type, OP1Type, V2Type, OP2Type, V3Type, primary key(tid) ) ;  """
db.SQX(seq)

""" action (( aid ) actionType ) """
seq = """ create table action (aid, primary key(aid) ) ; """
db.SQX(seq)

""" event ((eid ) ) """
seq = """ create table event (eid, primary key(eid) ) ; """
db.SQX(seq)


""" litPool (( lid ) ) """
seq = """ create table litPool (lid, primary key(lid) ) ; """
db.SQX(seq)

""" end type 1 tables """
"""
bundle --< br >-- rule
br (( bidFK, ridFK ) ) """
sq = """ create table br ( bidFK , ridFK , 
FOREIGN KEY(bidFK) REFERENCES bundle(bid)
FOREIGN KEY(ridFK) REFERENCES rule(rid)
);"""
db.SQX(sq)
"""
rule --< rts >-- test
rts ((ridFK,tidFK ) seq )
test --< testV1litType >-- litPool
testV1litType ((tidFK, V1Type="Lit",lidFK) ) """
sq = """ create table testV1litType ( tidFK , V1Type, lidFK , 
FOREIGN KEY(tidFK) REFERENCES test(tid)
FOREIGN KEY(lidFK) REFERENCES litPool(lid)
);"""
db.SQX(sq)
"""
test --< testV1EventType >-- Event
testV1EventType ((tidFK, V1Type="Event",eidFK) ) """
sq = """ create table testV1EventType ( tidFK , V1Type, eidFK , 
FOREIGN KEY(tidFK) REFERENCES test(tid)
FOREIGN KEY(eidFK) REFERENCES event(eid)
);"""
db.SQX(sq)
"""
test --< testV1RuleType >-- rule
testV1RuleType ((tidFK, V1Type="Rule",ridFK) )"""
sq = """ create table testV1RuleType ( tidFK , V1Type, ridFK , 
FOREIGN KEY(tidFK) REFERENCES test(tid)
FOREIGN KEY(ridFK) REFERENCES rule(rid)
);"""
db.SQX(sq)
"""
truthtable ((ridFK,tidFK,seq) ynVal )
/* (rid,tid) is unique */
rule --< truthTable >-- test
rule --< actionTable >-- action
--- ac = [truthtable] from tid[1] to tid[max] at each index
actionTable (( ridFK,aidFK,seq) ) 
/* transfer table to select aid on rid and index */
/* (rid,aid) is unique */
action --< actionTypePreProcess >-- process
actionTypePreProcess ((aidFK,pidFK ) )
action --< actionTypeBundleClose >-- Bundle
actionTypeBundleClose (( aidFK,bidFK ) )
action --< actionTypeBundleOpen >-- Bundle
actionTypeBundleOpen (( aidFK,bidFK ) )
action --< actionTypePostProcess >-- process
actionTypePostProcess ((aidFK,pidFK ) )
event --< eventBPX
eventBPX ((eidFK, clause, verbIndex) verb )
process --< processBPX
processBPX ((pidFK, clause, verbIndex) verb )
bundleQue (( bidFK,seq )
ruleQue (( ridFK,seq )
testQue (( tidFK,seq )
eventQue (( eidFK,seq )
""" 
""" end FK tables """
db.SQClose()
print (" done ")
