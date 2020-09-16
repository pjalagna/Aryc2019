"""
connector1.py
adds connections to ontology using child element 
adds the child's 
tagname,tagValue,and refid to parent refid
(IE a referent marker)
useful for XML and  XSD
"""
"""
test as

import connector1
connector1.main('StratML.xsd','on')
note uses the name of the xml file NOT the ontology.

debug
pkg = connector1.pkg
nds = connector1.nds

"""
nds = {}
pkg = {}
def logg(txt):
    """
    prints txt if nds['logg'] is =="ON"
    """
    global nds
    if (nds['trace'] == 'on'):
        print("log: " + txt)
    #endif
#logg
def getnds():
    global nds
    return(nds)
#
def getpkg():
    global pkg
    return(pkg)
#
def init(fn,trace=''):
    global nds,pkg
    print('initilizing')
    nds['trace'] = trace
    nds['file'] = fn
    import useLib
    import gennV
    pkg['genX'] = gennV.gennX
    import fioiClass
    pkg['fioi'] = fioiClass.fio(fn)
    import useOnto
    import SQSQ # encryption for protection 
    pkg['SQin'] = SQSQ.SQin
    pkg['SQout'] = SQSQ.SQout
    import OntologyClass
    pkg['ontology'] = OntologyClass.Ontology(fn + '.onto',str(nds['trace']))
    #preset modes
    nds['sequenceMode'] = 0
    nds['chooseMode'] = 0
    #pickup position
    nds['pu'] = 0
    nds['prevPu'] = 0
    # parent list
    nds['parent'] = [] # logical parent list
    nds['parent'].append(0)
    #attr
    nds['attr'] = {}
    #first
    nds['first']=''
    return(2)
#init

def main(ontofile,trace=''):
    """
    db1 = ontoFile
    for all provenance sq1
    -- if len < 2 skip
    -- else
    ---- vtype = 'RELATE' 
    ----v1 pickip[max-1]::tagname" // childs tagname
    ----v2 pickip[max-1]::value // tagValue 
    ---------- already SQ protected
    ----v3 "Role"
    ----v4 'Role:refid'
    ----v5 'refid'
    ----v6 pickup[max-1]::refid // child refid
    ---- v18 = pickup[max]::refid // parentRefid
    """
    global nds,pkg
    nds = {}
    pkg = {}
    nds = getnds()
    pkg = getpkg()
    nds['trace'] = trace
    # umbrella ctl
    ctl = 1
    while (0 < ctl):
        logg('head: ctl=('+ctl.__str__() +')')
        if (ctl == 1): #
            ctl = init(ontofile,trace) # "
        elif (ctl == 2): #
            logg(proc2.__doc__)
            ctl = proc2() # "
        else:
            print('error ctl ('+ctl.__str__()+')')
            ctl = -1
        #endif
    #wend
#main

def proc2():
    """
    connect tagname-1 to refid
    """
    global nds,pkg
    sq1 = """
select v2 from v20
where v1 = 'provenance'
and v18 not in (
select v18 from v20
where 
v1 = 'l1x'
and v2 = '</'
)
and v18 not in (
select v18 from v20
where 
v1 = 'l2x'
and v2 = '/>'
)
;
"""
    forall = pkg['ontology'].db.SQReadAll(sq1)
    for fx in range(1,len(forall)+1):
        # split into array
        a= forall[fx-1][0].split("[")
        a2 = a[1].split("]")
        a3 = a2[0].split(',')
        logg('a3=('+str(a3)+')')
        # rule 1 if len(forall[fx]) > 2 skip
        if (len(a3)<= 1 ):
            logg('len(a3)<= 1')
        elif (int(a3[len(a3)-2])==0) :
            logg("int(a3[len(a3)-2])==0") # rule 2 if max-1 == 0 skip
        else:
            fxmax = int(a3[len(a3)-1])
            fxmx = int(a3[len(a3)-2])
            role = v1v2v1('pickup', str(fxmax), 'tag') 
            rval = v1v2v1('pickup', str(fxmax),'value')
            refidM = v1v2v1('pickup', str(fxmax),'refid')
            refidMe = v1v2v1('pickup', str(fxmx), 'refid') 
            pkg['ontology'].RELATEWrite( role,rval,'Role','refid','refid',refidM,refidMe)
        #endif
    #endfor
    ctl=-1
    return(ctl)
#proc2
def v1v2v1(v1a,v2,v1b):
    global nds,pkg
    sqsx = """ select v2 from v20
    where v1 = 'v1b'
and v18 in
( select v18 from v20
where v1='v1a'
and v2 = 'v2v'
)
order by v18 ;"""
    sqsx = sqsx.replace('v1b',v1b)
    sqsx = sqsx.replace('v1a',v1a)
    sqsx = sqsx.replace('v2v',v2)
    ans = pkg['ontology'].db.SQReadAll(sqsx)
    logg('v1v2v1:ans('+ str(ans) +')')
    if (len(ans)==0):
        ans = ''
    else:
        ans = ans[0][0]
    #endif
    return(ans)
#end

    