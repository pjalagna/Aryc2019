"""
file phase2.py
pja 06-29-2020

add to xsd ontology

"""
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
    contend1s = "select vtype,v1,v2,v18 from v20 where v1='masterPosition';"
    contend1 = pkg['db'].SQReadAll(contend1s)
    ## per
    for x in range(len(contend1)):
        ### get my.sequence,my.pickup, master.refid
        mySeqS = "select v2 from v20 where v18='%p1%' and v1='seq';"
        mySeqS = mySeqS.replace('%p1%',contend1[x][3])
        myseq = pkg['db'].SQReadAll(mySeqS)
        myPuS = "select v2 from v20 where v18='%p1%' and v1='pickup';"
        myPuS = myPuS.replace('%p1%',contend1[x][3])
        myPu = pkg['db'].SQReadAll(myPuS)
        mrefidS = "select v18 from v20 where v1='pickup' and v2='%p1%' ;"
        mrefidS = mrefidS.replace('%p1%',contend1[x][2])
        mrefid = pkg['db'].SQReadAll(mrefidS)
        #RELATEWrite(Name1, Value1, relateType,relateValue,Name2, Value2,refid,flags='')
        pkg['ontology']. RELATEWrite( "leadingPosition", contend1[x][2], "ChildSequence",myseq, "ChildPosition", myPu,mrefid,flags='')
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
    # get mPU , myTag, myValue
    # contender list of @ endpoint not element/complex/seq/choice and not w/ sequence
    sqep22 = "select v18 from v20 where v1='endpointRefid' and v18 not in (select v18 from v20 where v1='tag' and v2='element') and v18 not in (select v18 from v20 where v1='tag' and v2='complexType') and v18 not in (select v18 from v20 where v1='tag' and v2='sequnce') and v18 not in (select v18 from v20 where v1='tag' and v2='choice') and v18 not in (select v18 where v1='seq');" 
    ## per
    ### skip if previous == endpoint 
    ### relate elementPosition ,y*
    ###        has<my.tag.name>,''
    ###        id,(my.previous).id
    ### refid  refid(y*)
    ## /per
    #
    
