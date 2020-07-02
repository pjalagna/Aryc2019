"""
file phase2.py
pja 06-29-2020

add to xsd ontology
usage phase2.main(ontoFile,{trace='on'})
"""
"""
test as 
ontoFile = 't1.xsd.onto'
trace
"""
def logg(txt):
    """
    prints txt if nds['logg'] is =="ON"
    """
    global nds
    if (nds['trace'] == 'on'):
        print("log: " + txt)
    #endif
#logg

def init(ontoFile,trace='off'):
    global pkg,nds
    pkg = {}
    nds = {}
    nds['trace'] = trace
    import useLib
    import SQClass
    pkg['db'] = SQClass.SQC(ontoFile)
    import gennV
    pkg['genX'] = gennV.gennX
    import useOnto
    import SQSQ # encryption for protection 
    pkg['SQin'] = SQSQ.SQin
    pkg['SQout'] = SQSQ.SQout
    import OntologyClass
    pkg['ontology'] = OntologyClass.Ontology(ontoFile,str(nds['trace']))
#

def main(ontoFile,trace='off'):
    """
    useage - main(ontoFile,trace='off')
    1- add to "master" element a fwd reference to child in sequence ("leadingPosition"=mPU)("childSeq"=seq)("childRefid"=Childrefid) 
    refid of master==mRefid
    
    2- master reference to <documentation>value</documentation>
    @ endpoint not in sequence, 
    not in endpoint chain IE previous <> endpoint
    not of element/complex/sync/choice type IE tag<>..
    relate ("leadingPosition"=mPU)("hasytype"=<tagname>)("value"=value)
    refid of master
    
    """
    global pkg,nds
    # make contender list of any profile with master into contend1
    init(ontoFile,trace)
    contend1s = "select v1,v2,v3,v4,v5,v6,v18 from v20 where vtype='RELATE' and v1='masterPosition' and v3='SEQ';"
    contend1 = pkg['db'].SQReadAll(contend1s)
    ## per
    for x in range(len(contend1)-1):
        ### get masterpu, childSeq, master.refid
        masterpu = contend1[x][1]
        ChildSeq = contend1[x][3]
        mrefidS = "select v18 from v20 where v1='pickup' and v2='%p1%' ;"
        mrefidS = mrefidS.replace('%p1%',contend1[x][1])
        mrefid = pkg['db'].SQReadAll(mrefidS)[0][0]
        logg("mrefid="+mrefid)
        #RELATEWrite(Name1, Value1, relateType,relateValue,Name2, Value2,refid,flags='')
        pkg['ontology']. RELATEWrite( "leadingPosition", masterpu, "ChildSequence",ChildSeq, "ChildRefid", contend1[x][5],mrefid,flags='')
    ##/per
    #
    """
    2- master reference to <documentation>value</documentation>
    @ endpoint not in sequence, 
    not in endpoint chain IE previous <> endpoint
    not of element/complex/sync/choice type IE tag<>..
    relate ("leadingPosition"=mPU)("hasytype"=<tagname>)("value"=value)
    refid of master
    """
    # get contenders
    # contender list of @ endpoint not element/complex/seq/choice and not w/ sequence
    sqep22 = "select v18 from v20 where v1='endpointRefid' and v18 not in (select v18 from v20 where v1='tag' and v2='element') and v18 not in (select v18 from v20 where v1='tag' and v2='complexType') and v18 not in (select v18 from v20 where v1='tag' and v2='sequnce') and v18 not in (select v18 from v20 where v1='tag' and v2='choice') and v18 not in (select v18 where v1='seq');"
    sqepx =  pkg['db'].SQReadAll(sqep22)[0][0]
    ## per
    for xi in range(len(sqepx)):
        #  myprev, myref=[xi]
        myprevSQ = "select v2 from v20 where v1='previousPickup'  and v18 = '%myref%'"
        myprevSQ = myprevSQ.replace('%myref%',sqepx[xi][0])
        myprev = pkg['db'].SQReadAll(myprevSQ)[0][0]
        logg("myprev="+myprev)
        ### skip if previous == endpoint 
        # get prev profile.endpoint
        sqppepSQ = "select v1,v2 from v20 where v1='endpointRefid' and V18 in(select v18 from v20 where v1='pickup' and v2='%myprev%');"
        sqppepSQ = sqppepSQ.replace('%myprev%',myprev)
        sqppep = pkg['db'].SQReadAll(sqppepSQ)[0][0]
        logg("sqppep="+sqppep)
        if (len(sqppep)==0):
            # prev not endpoint so process
            # get prev-value via prevProfile
            prevValSQ = "select v2 from v20 where v1='value' and V18 in(select v18 from v20 where v1='pickup' and v2='%myprev%') ;"
            prevValSQ = prevValSQ.replace('%myprev%',myprev)
            prevVal = pkg['db'].SQReadAll(prevValSQ)[0][0]
            logg("prevVal="+prevVal)
            prevTagSQ = "select v2 from v20 where v1='tag' and V18 in(select v18 from v20 where v1='pickup' and v2='%myprev%') ;"
            prevTagSQ = prevTagSQ.replace('%myprev%',myprev)
            prevTag = pkg['db'].SQReadAll(prevTagSQ)[0][0]
            logg("prevTag="+prevTag)
            prevKRIDSQ =  "select v2 from v20 where v1='KRID' and V18 in(select v18 from v20 where v1='pickup' and v2='%myprev%') ;" 
            prevKRIDSQ = prevKRIDSQ.replace('%myprev%',myprev)
            prevKRID = pkg['db'].SQReadAll(prevKRIDSQ)[0][0]
            logg("prevKRID="+prevKRID)
            # find leading element y*
            myprovSQ = "select v2 from v20 where v1='provenance' and v18 ='%myref%' ;"
            myprovSQ = myprovSQ.replace('%myref%',sqepx[xi][0])
            myprov = pkg['db'].SQReadAll(myprovSQ)[0][0]
            logg("myprov="+myprov)
            myprovsp = myprov[1:-1].split(',')
            # from the back find first tag=element/schema
            for xp in range(len(myprovsp)):
                # is tag of pu = element/schema yes break
                xxp = len(myprovsp)-xp-1 # from the back
                xptagSQ = "select v2 from v20 where v1='tag' and v18 in (select v18 from v20 where v1='pickup' and v2='%xpPu%') ;"
                xptagSQ.replace('%xpPu%',myprovsp[xxp].strip(' '))
                xpTag = pkg['db'].SQReadAll(xptagSQ)[0][0]
                logg("xpTag="+xpTag)
                xpRefidSQ = "select v2 from v20 where v1='refid' and v18 in (select v18 from v20 where v1='pickup' and v2='%xpPu%') ;"
                xpRefidSQ = xpRefidSQ.replace('%xpPu%',myprovsp[xxp].strip(' '))
                xpRefid = pkg['db'].SQReadAll(xpRefidSQ)[0][0]
                logg("xpRefid="+xpRefid)
                if (xpTag == 'schema'):
                    break
                elif (xpTag == 'element'):
                    break
                else:
                    nop = 1
                #endif
            #end for xp
            elementPosition = myprovsp[xxp].strip(' ')
            logg("elementPosition="+elementPosition)
            myTagName = prevTag
            logg("myTagName="+myTagName)
            krid = prevKRID
            logg("krid="+krid)
            toRefid = xpRefid
            logg("toRefid="+toRefid)
            ### you have=doc value=xx
            pkg['ontology']. RELATEWrite( "elementPosition", elementPosition, "has",prevTag, "value", prevVal,xpRefid,flags='')
        #endif len-sqppep      
    ## /per end for xi
    #
#end main

    
