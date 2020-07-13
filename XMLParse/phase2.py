"""
file phase2.py
pja 07-112-2020 attach contextID
pja 07-08-2020 attach attributes and 
--- enumerations to elements
--- also attached attribute documentation to attribute
pja 07-04-2020 ns: removal
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
    
    3- attach <attributes and enumerations to elements
    
    4- attach contextID for tagName, AttributeName, AttributeValue.
    """
    global pkg,nds
    # make contender list of any profile with master into contend1
    init(ontoFile,trace)
    contend1s = "select v1,v2,v3,v4,v5,v6,v18 from v20 where vtype='RELATE' and v1='masterPosition' and v3='SEQ';"
    contend1 = pkg['db'].SQReadAll(contend1s)
    ## per
    for x in range(1,len(contend1)+1):
        ### get masterpu, childSeq, master.refid
        logg('len contend1-x-1='+str(len(contend1[x-1])))
        masterpu = contend1[x-1][1]
        ChildSeq = contend1[x-1][3]
        mrefidS = "select v18 from v20 where v1='pickup' and v2='%p1%' ;"
        mrefidS = mrefidS.replace('%p1%',contend1[x-1][1])
        mrefid = pkg['db'].SQReadAll(mrefidS)[0][0]
        logg("mrefid="+mrefid)
        #RELATEWrite(Name1, Value1, relateType,relateValue,Name2, Value2,refid,flags='')
        pkg['ontology']. RELATEWrite( "leadingPosition", masterpu, "ChildSequence",ChildSeq, "ChildRefid", contend1[x-1][5],mrefid,flags='')
        logg('x='+str(x))
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
    logg('begin 2')
    # get contenders
    # contender list of @ endpoint not element/complex/seq/choice and not w/ sequence
    sqep22 = "select v18 from v20 where v1='endpointRefid' and v18 not in (select v18 from v20 where v1='tag' and v2='element') and v18 not in (select v18 from v20 where v1='tag' and v2='complexType') and v18 not in (select v18 from v20 where v1='tag' and v2='sequnce') and v18 not in (select v18 from v20 where v1='tag' and v2='choice') and v18 not in (select v18 where v1='seq');"
    sqepx =  pkg['db'].SQReadAll(sqep22)
    ## per
    for xi in range(1,len(sqepx)+1):
        #  myprev, myref=[xi-1]
        myprevSQ = "select v2 from v20 where v1='previousPickup'  and v18 = '%myref%'"
        myprevSQ = myprevSQ.replace('%myref%',sqepx[xi-1][0])
        myprev = pkg['db'].SQReadAll(myprevSQ)[0][0]
        logg("myprev="+myprev)
        ### skip if previous == endpoint 
        # get prev profile.endpoint
        sqppepSQ = "select v1,v2 from v20 where v1='endpointRefid' and V18 in(select v18 from v20 where v1='pickup' and v2='%myprev%');"
        sqppepSQ = sqppepSQ.replace('%myprev%',myprev)
        sqppep = pkg['db'].SQReadAll(sqppepSQ)
        logg("sqppep="+str(sqppep))
        if (len(sqppep)==0):
            # prev not endpoint so process
            # get prev-value via prevProfile
            prevValSQ = "select v2 from v20 where v1='value' and V18 in(select v18 from v20 where v1='pickup' and v2='%myprev%') ;"
            prevValSQ = prevValSQ.replace('%myprev%',myprev)
            # test preval for len(0)
            prevVal = pkg['db'].SQReadAll(prevValSQ)
            if (len(prevVal)<>0):
                prevVal = prevVal[0][0]
            else:
                prevVal = ''
            #endif
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
            for xp in range(1,len(myprovsp)+1):
                # is tag of pu = element/schema yes break
                xxp = len(myprovsp)-xp # from the back
                xptagSQ = "select v2 from v20 where v1='tag' and v18 in (select v18 from v20 where v1='pickup' and v2='%xpPu%') ;"
                xptagSQ = xptagSQ.replace('%xpPu%',myprovsp[xxp].strip(' '))
                xpTag = pkg['db'].SQReadAll(xptagSQ)[0][0]
                # remove ns:
                mo = xpTag.find(':')
                if (mo <> -1):
                   xpTag = xpTag[mo+1:]
                #endif
                logg("xpTag="+xpTag)
                xpRefidSQ = "select v2 from v20 where v1='refid' and v18 in (select v18 from v20 where v1='pickup' and v2='%xpPu%') ;"
                xpRefidSQ = xpRefidSQ.replace('%xpPu%',myprovsp[xxp].strip(' '))
                xpRefid = pkg['db'].SQReadAll(xpRefidSQ)[0][0]
                logg("xpRefid="+xpRefid)
                if (xpTag == 'schema'):
                    break
                elif (xpTag == 'element'):
                    break
                elif (xpTag == 'attribute'):
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
            pkg['ontology'].RELATEWrite( "elementPosition", elementPosition, "has",prevTag, "value", prevVal,xpRefid,flags='')
        #endif len-sqppep      
    ## /per end for xi
    #
    """
    3- attach attributes w/ emumerations to element
    3a- [refid] <- tagName 'enumeration' 
    -- per 
    ---- get-provenance
    ------ backwalk to element -> Erefid
    ------ backwalk to attribute -> atn
    ------ me.value -> EValue
    ------ relate 
    --------- "attributeName",atn
    --------- "AttributeEnumeration",''
    --------- "Enumeration",EValue
    --------- @ Erefid
    /3a
    3b [] <- tagname = 'Restriction'
    -- filter not l1x </
    -- per
    ---- get prov
    ------ backwalk to e -> Erefid
    ------ backwalk to restriction -> use,base
    ------ backwalk to attribute -> atn
    ------ relate 
    --------- "attributeName",atn
    --------- "use",''
    --------- "use",c-use
    --------- @ Erefid
    ------ relate 
    --------- "attributeName",atn
    --------- "base",''
    --------- "base",c-base
    --------- @ Erefid
    ------ relate 
    --------- "attributeName",atn
    --------- "attributeRefid",''
    --------- "refid",Arefid
    --------- @ Erefid
    -- /per
    """
    logg("begin 3a")
    """
    3a- [refid] <- tagName 'enumeration' 
    -- per 
    ---- get-provenance
    ------ backwalk to element -> Erefid
    ------ backwalk to attribute -> atn
    ------ me.value -> EValue
    ------ relate 
    --------- "attributeName",atn
    --------- "AttributeEnumeration",''
    --------- "Enumeration",EValue
    --------- @ Erefid
    """
    sq3 = "select v18 from v20 where v1='tagName' and v2='enumeration' ;"
    sq3x = pkg['db'].SQReadAll(sq3)
    #per
    for x3 in range(1,len(sq3x)+1):
        #backwalk to element,mypu -> Erefid
        Erefid = backwalk('element',sq3x[x3-1][0])
        #backwalk to attribute -> atn
        Arefid = backwalk('attribute',sq3x[x3-1][0])
        sq222 = "select v2 from v20 where v1='name' and v18 = '%myref%';"
        sq222 = sq222.replace('%myref%',Arefid)
        atn = pkg['db'].SQReadAll(sq222)[0][0]
        #me.value -> EValue
        sq227 = "select v2 from v20 where v1='value' and v18='%myref%' ;"
        sq227 = sq227.replace('%myref%',sq3x[x3-1][0])
        EValue = pkg['db'].SQReadAll(sq227)[0][0]
        #relate atn,atn,atemum,'',enum,eval
        pkg['ontology'].RELATEWrite("attributeName",atn, "attributeEnumeration",'',"enumeration",EValue,Erefid)
    #end for 3a
    logg('begin 3b')
    """
    3b [] <- tagname = 'Restriction'
    -- filter not l1x </
    -- per
    ---- get prov
    ------ backwalk to e -> Erefid
    ------ backwalk to restriction -> use,base
    ------ backwalk to attribute -> atn
    ------ relate 
    --------- "attributeName",atn
    --------- "use",''
    --------- "use",c-use
    --------- @ Erefid
    ------ relate 
    --------- "attributeName",atn
    --------- "base",''
    --------- "base",c-base
    --------- @ Erefid
    relate 
    --------- "attributeName",atn
    --------- "attributeRefid",''
    --------- "refid",Arefid
    --------- @ Erefid
    -- /per
    """
    #[] <- tagname = 'Restriction'
    rc = pkg['ontology'].RELATESeek('tagName','/restriction')
    for s258 in range(1,len(rc)+1):
        #backwalk element,sq256x[s258-1][0]-> Erefid
        Erefid = backwalk('element',rc[s258-1][18])
        #backwalk to restriction -> use,base
        Rrefid = backwalk('restriction',rc[s258-1][18])
        base = pkg['ontology'].ATNSeek('base','','','',Rrefid)[0][2]
            
        #backwalk to attribute -> atn
        Arefid = backwalk('attribute',rc[s258-1][18])
        atn = pkg['ontology'].ATNSeek('name','','','',Arefid)[0][2]
        use = pkg['ontology'].ATNSeek('use','','','',Arefid)[0][2]
            
        #relate-1 atn,use @ element
        pkg['ontology'].RELATEWrite( "attributeName",atn,"base",'',"base",base,Erefid)
        #relate-2 atn,base @ element
        pkg['ontology'].RELATEWrite( "attributeName",atn,"use",'',"use",use,Erefid)
        pkg['ontology'].RELATEWrite( "attributeName",atn,"attributeRefid",'',"refid",Arefid,Erefid)
    #endfor s258
    logg('begin 4')
    #attach contextID to refid
    #get list of all refid
    rLists = "select v18 from v20 where v1='pickup';"
    rlist = pkg['db'].SQReadAll(rLists)
    #per
    for i in range(1,len(rlist)+1):
        ## get plist[v1,v2] for rlist[i+1] for ATN
        psq = "select v1,v2 from v20 where vtype='ATN' and v18 ='%refid%';"
        psq = psq.replace('%refid%',rlist[i-1][0])
        plist = pkg['db'].SQReadAll(psq)
        ###per 
        for m in range(1,len(plist)+1):
            # v1,v2,refid
            ContextID( plist[m-1][0], plist[m-1][1], rlist[i-1][0])
        ###/per
        nop = 1
    #/per
    nop = 1
#end main

#support
def ContextID(name,value,refid):
    """
    attach context=value,type=name,id to refid
    attach context=value,type=name,refid to blank
    attach context=name,type="name",id to refid
    attach context=name,type="name",refid to blank
    """
    CID = pkg['genX']()
    pkg['ontology'].RELATEWrite(
"context",value,"type",name,"ID",CID,refid)
    pkg['ontology'].RELATEWrite( "context",value,"type",name,"Refid",refid,'.z.')
    CID = pkg['genX']()
    pkg['ontology'].RELATEWrite(
"context",name,"type","designation","ID",CID,refid)
    pkg['ontology'].RELATEWrite( "context",name,"type","designation","Refid",refid,'.z.')
#end CID
def backwalk(ttype,ref18):
    """
    using provenance chain stop on ttype
    return -1 ttype not found OR
           refid of ttype
    """
    global pkg,nds
    # find leading type y*
    myprovSQ = "select v2 from v20 where v1='provenance' and v18 ='%myref%' ;"
    myprovSQ = myprovSQ.replace('%myref%',ref18)
    myprov = pkg['db'].SQReadAll(myprovSQ)[0][0]
    logg("myprov="+myprov)
    myprovsp = myprov[1:-1].split(',')
    # from the back find first tag=element/schema
    for xp in range(1,len(myprovsp)+1):
        # is tag of pu = element/schema yes break
        xxp = len(myprovsp)-xp # from the back
        xptagSQ = "select v2 from v20 where v1='tag' and v18 in (select v18 from v20 where v1='pickup' and v2='%xpPu%') ;"
        xptagSQ = xptagSQ.replace('%xpPu%',myprovsp[xxp].strip(' '))
        xpTag = pkg['db'].SQReadAll(xptagSQ)[0][0]
        # remove ns:
        mo = xpTag.find(':')
        if (mo <> -1):
            xpTag = xpTag[mo+1:]
        #endif
        logg("xpTag="+xpTag)
        xpRefidSQ = "select v2 from v20 where v1='refid' and v18 in (select v18 from v20 where v1='pickup' and v2='%xpPu%') ;"
        xpRefidSQ = xpRefidSQ.replace('%xpPu%',myprovsp[xxp].strip(' '))
        xpRefid = pkg['db'].SQReadAll(xpRefidSQ)[0][0]
        logg("xpRefid="+xpRefid)
        ttypesw = -1
        if (xpTag == ttype):
            ttypesw = 1
            break
        else:
            nop = 1
        #endif
    #end for xp
    if (ttypesw == -1):
        ans = -1
    else:
        ans = xpRefid
    #endif
    return(ans)
#/backwalk



    
