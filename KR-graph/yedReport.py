"""
file yedReport.py
usage yedReport.main(ontologyFile)
prints to std - cut and paste for final
"""
"""
test as
import yedReport
yedReport.main('KR-Ontology.graphml.onto','on')
yedReport.main('KR-Ontology.graphml.onto','off')
"""
def main(fn,trace=''):
    """
    usage main(fileName)
    renders to ontology fileName.onto
    """
    global nds,pkg
    nds = {}
    pkg = {}
    nds['trace'] = trace
    # umbrella ctl
    ctl = 1
    while (0 < ctl):
        logg('head: ctl=('+ctl.__str__() +')')
        logg('nds')
        logg(str(nds))
        logg('/nds')
        logg(' ')
        if (ctl == 1): #
            ctl = init(fn,trace) # 
    
    
        elif (ctl == 2): #
            logg(proc2.__doc__)
            ctl = proc2() #
    
        elif (ctl == 3): #
            logg(proc3.__doc__)
            ctl = proc3() #
    
        elif (ctl == 4): #
            logg(proc4.__doc__)
            ctl = proc4() #
    
        elif (ctl == 5): #
            logg(proc5.__doc__)
            ctl = proc5() #
    
        elif (ctl == 6): #
            logg(proc6.__doc__)
            ctl = proc6() #
    
        elif (ctl == 7): #
            logg(proc7.__doc__)
            ctl = proc7() #
    
        elif (ctl == 8): #
            logg(proc8.__doc__)
            ctl = proc8() #
    
        elif (ctl == 9): #
            logg(proc9.__doc__)
            ctl = proc9() #
    
        elif (ctl == 10): #
            logg(proc10.__doc__)
            ctl = proc10() #
    
        elif (ctl == 11): #
            logg(proc11.__doc__)
            ctl = proc11() #
    
        else:
            print('error ctl ('+ctl.__str__()+')')
            ctl = -1
        #endif
    #wend
#main
    
def proc2():
    """  step1 - list of <node contenders to s1
    set xx1=1 xx1Max len(s1)+1
    ==> 3  """
    global pkg,nds     
    s1s = "select v2 from v20 where v1='pickup' and v18 in ( select v18 from v20 where v1='tag' and v2='node')"
    nds['s1'] = pkg['db'].SQReadAll(s1s)
    nds['xx1'] = 1
    nds['xx1Max'] = len(nds['s1'])+1
    return(3)
#end proc2
           
def proc3():
    """  step3
    test xx1 == xx1Max==> -1
    n - get node pu[xxi] 
    set pu
    print n n node-id
    ==> 7  """
    global pkg,nds    
    if (nds['xx1'] == nds['xx1Max']):
        ans = -1
    else:
        nds['pu'] = nds['s1'][nds["xx1"]-1][0]
        #set pu = pickup[xxi]
        #get node pu[xxi] 
        nodeids = "select v2 from v20 where v1='id' and v18 in (select v18 from v20 where v1='pickup' and v2='%s1x%')"
        nodeids = nodeids.replace('%s1x%',nds['s1'][nds["xx1"]-1][0])
        nds["nodeid"] = pkg['db'].SQReadAll(nodeids)[0][0]
        #print n n node-id
        print(' ') # line space
        print(' ') # line space 
        print('node id=(' + nds["nodeid"]+")")
        ans = 7
    #endif
    return(ans)
#end proc3
           
def proc4():
    """  desc  """
    global pkg,nds     
    return(4+1)
#end proc4
           
def proc5():
    """  desc  """
    global pkg,nds     
    return(5+1)
#end proc5

    
            
def proc6():
    """  desc  """
    global pkg,nds     
    return(6+1)
#end proc6

    
            
def proc7():
    """  setp 7
    advance pu
    has tag? n==> 8
    y
    tag=</node? y==> 9
    n
    ==>10  """
    global pkg,nds    
    #advance pu
    nds['pu'] = int(nds['pu']) + 1
    ## get tag
    gtags = "select v2 from v20 where v1='tag' and     v18 in (select v18 from v20 where v1='pickup' and v2='%pu%')"
    gtags = gtags.replace('%pu%',str(nds['pu']))
    nds["gtag"] = pkg['db'].SQReadAll(gtags)
    #has tag?
    if (len(nds["gtag"])==0):
        logg('no tag')
        ans = 8
    elif (nds["gtag"][0][0]=='/node'):
        logg('=/node')
        ans = 9
    else:
        ans = 10
    #endif len-tag
    return(ans)
#end proc7

    
            
def proc8():
    """  step 8
    has backValue? n==> 7
    print(backValue)
    ==> 7  """
    global pkg,nds 
    #test for backckvalue
    bvs = "select v2 from v20 where v1='backValue' and     v18 in (select v18 from v20 where v1='pickup' and v2='%pu%')"
    bvs = bvs.replace('%pu%',str(nds["pu"]))
    bv = pkg['db'].SQReadAll(bvs)
    if (len(bv)<>0):
        print('()-data note:')
        bvst = bv[0][0].replace('[CDATA[','')
        bvst = pkg['wrap'](bvst,40)
        for df in range(len(bvst)):
            print(bvst[df])
        #end for
    else:
        nop = 1
    #endif bv    
    return(7)
#end proc8

    
            
def proc9():
    """  step 9
    advance xxi
    ==> 3  """
    global pkg,nds
    nds['xx1'] = int(nds['xx1']) +1   
    return(3)
#end proc9

    
            
def proc10():
    """  step 10
    gtag = nodeLable? n==>7
    has configuration? 
    n has value?
    --y print value
    ==>7
    configuration for name?
    y print entity name ==> 7
    n configuration for attr?
    --y print attributes ==> 7
    --n ==> 7
      """
    global pkg,nds 
    #gtag = nodeLable? n==>9
    #has configuration? n==>9
    #configuration for name?
    #y print entity name ==> 9
    #n configuration for attr?
    #--y print attributes ==> 9
    #--n ==> 9
    #/n
    logg(nds['gtag'][0][0])
    if (nds['gtag'][0][0]<>'y:NodeLabel'):
        logg('not NodeLabel')
        ret = 7
    else:
        #has configuration? n==>9
        confs = "select v2 from v20 where v1='configuration' and v18 in (select v18 from v20 where v1='pickup' and v2='%pu%')"
        confs = confs.replace('%pu%',str(nds['pu']))
        confg = pkg['db'].SQReadAll(confs)
        if (len(confg)==0):
            logg('no config')
            vsts = "select v2 from v20 where v1='value' and v18 in (select v18 from v20 where v1='pickup' and v2='%pu%')"
            vsts = vsts.replace('%pu%',str(nds['pu']))
            vstg = pkg['db'].SQReadAll(vsts)
            if (len(vstg)<>0):
                vstg = pkg['SQout'](vstg[0][0])
                print("::"+vstg)
            #endif vstg
            ret = 7
        else:
            ret = 7
            confg = confg[0][0]
            nf = confg.find("label.name")
            logg('nf=('+ str(nf)+')')
            ns = confg.find("label.attributes")
            logg('ns=('+ str(ns)+')')
            if (-1 < nf ):
                #get val as entity name
                cval = "select v2 from v20 where v1='value' and     v18 in (select v18 from v20 where v1='pickup' and v2='%pu%')"
                cval = cval.replace('%pu%',str(nds["pu"]))
                cvals = pkg['db'].SQReadAll(cval)[0][0]
                ans = pkg['SQout'](cvals)
                print("()- entityName: " + ans)
            elif (-1 < ns):
                # case3 config==attr print val as attributes
                #get val as entity name
                cval = "select v2 from v20 where v1='value' and     v18 in (select v18 from v20 where v1='pickup' and v2='%pu%')"
                cval = cval.replace('%pu%',str(nds["pu"]))
                cvals = pkg['db'].SQReadAll(cval)[0][0]
                ans = pkg['SQout'](cvals)
                print("()- Attributes: ")
                print(ans)
            else:
                ret = 7
            #endif ns,nf
        #endif len-confg
    
        
    return(ret)
#end proc10


## support ##
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
    import textwrap
    pkg['wrap']=textwrap.wrap #txt,size
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
    return(2)
#

    


