"""
file 	.py
reads x.RDF and creates return[thing[],predicate[],edge[],node[]]

pja 7/28/2020 added lastnode pickup for subject
pja 7/27/2020
file = "pja1.xsd"
import useLib
import useRDF
import RDFRead
thing,predicate,edge,nodes = RDFRead.main(file+'.onto.rdf')

"""
def main(inFile):
    """
    inFile -> res[thing[],predicate[],edge[],node[]]
    """
    global nds,pkg
    nds = {}
    pkg = {}
    nds["thing"]={}
    nds["predicate"]={}
    nds["edge"]={}
    nds['node']={}
    nds['inFile'] = inFile
    init()
    loop1()
    return(nds["thing"],nds["predicate"],nds["edge"],nds['node'])
#end main
def init():
    global nds,pkg
    import useLib
    # open input file with fio
    import fioiClass
    pkg['in'] = fioiClass.fio(nds['inFile'])
    nds['register'] = 2 #all nodes start at 2
#
def loop1():
    global nds,pkg
    counter = 0
    ctl1 = 0
    while (ctl1==0):
        print("loop1"+str(counter))
        counter = counter+1
        j =getwd()
        j = j.upper()
        j=j.rstrip(' \n\t')
        j=j.lstrip(' \n\t')
        print("j=("+j+")")
        if (j=="RDF:"):
            doRDF()
            nop = getwd() #;
        elif (j=="PRED:"):
            cP()
            nop = getwd() #;
        elif (j=="NAME:"):
            cS()
            nop = getwd() #;
        elif(j=='END:'):
            print("DONE")
            ctl1=-2
        elif(j=='@EOFEOF'):
            print("DONE")
            ctl1=-2
        else:
            print("unknown marker ("+j+")"  )
            ctl1=-1
        #endif
    #wend
    return()
#/loop1
def cedges(rx,ry,rz) :
    print('cedges') 
    mx = regPlus()
    nds['lastnode'] = str(mx)
    nds['edge'][mx]=str(rx)+":"+str(rz)+"!"+str(ry)
    print('edge '+str(mx)+"="+str(rx)+":"+str(rz)+"!"+str(ry))
    #nds['node'][str(mx)] = str(ry)
    #print('node'+str(mx)+'='+str(ry)	)
    #print('edge mx=('+str(mx)+')')
    return(mx)
#/cedges
def getwd():
    s = pkg['in'].fpword()[1]
    s = s.rstrip(' \n\t')
    s = s.lstrip(' \n\t')
    print("\nword")
    print(s)
    print("/word\n")
    return(s)
#
def doRDF():
    global nds,pkg
    print('doRDF')
    t =getwd() 
    if (t=="("):
        rx = cS()
        ry = cP()
        rz = cS()
        cedges(rx,ry,rz)
        ##raw_input('1-here')
        nop = getwd() #)
    elif (t[1].upper == 'S'):
        #=
        cS()
        nop = getwd() #;
        #raw_input('2-here')
    elif (t[1].upper == 'P'):
        cP()
        nop = getwd() #;
        #raw_input('3-here')
    else:
        print("unknown format RDF: " + t[1] )
    #endif
#doRDF
def regPlus():
    global nds,pkg
    a = nds['register']
    nds['register'] = nds['register'] + 1
    print('register a=('+str(a)+')')
    return(a)
#regPlus

def cS():
    global nds,pkg
    
    ts =getwd()
    print('cS ts('+ts+')')
    if (ts == "("):
        nds["rx"] = cS()
        nds["ry"] = cP()
        nds["rz"] = cS()
        nds["mx"] = cedges(nds["rx"],nds["ry"],nds["rz"])
        #raw_input('4-here')
        nop =getwd() #)
        a = nds["mx"]
    elif (ts=='$'): # lastnode
        a = nds['lastnode']
    else:
        #test ts[1] if unique to thing gen ix
        try:
            a = nds['thing'][ts]
        except:
            #see if its a predicate 
            j = yesPredicate(ts)
            if (j==-1):
                nds['thing'][ts] = regPlus()
                a = nds['thing'][ts]
            else:
                a = j
            #endif
        finally:
            nop = 1
        #end try
    #endif
    print('cs a=('+str(a)+')')
    print('end cS')
    return(a)
#/cS
def yesPredicate(ts):
    try:
        a = nds['predicate'][ts]
    except:
        a = -1
    finally:
        nop = 1
    #endtry
    return(a)
#/yesPredicate

def cP():
    global nds,pkg
    ts =getwd()
    print('cP ts('+ts+')')
    if (ts == "("):
        nds["rx"] = cS()
        nds["ry"] = cP()
        nds["rz"] = cS()
        nds["mx"] = cedges(nds["rx"],nds["ry"],nds["rz"])
        #raw_input('5-here')
        nop =getwd() #)
        a = nds["mx"]
    else:
        #test ts[1] if unique to thing gen ix
        try:
            a = nds['predicate'][ts]
        except:
            nds['predicate'][ts] = regPlus()
            a = nds['predicate'][ts]
        finally:
            nop = 1
        #end try
    #endif
    print('cp a=('+str(a)+')')
    print('end cP')
    return(a)
#/cP