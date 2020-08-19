"""
file makeGraph.py
pja 7/30/2020 reads [thing[],predicate[],edge[],node[]]
pja 7/18/2020
test1 = first make
"""
"""
test as 
file = 'pja1.xsd'
import makeGraph
outFile = file+'.onto.rdf.graphml'
Iarray = [thing,predicate,edge,nodes]
makeGraph.mkG(outFile,Iarray)


"""
def init():
    global nds,pkg,graphTemplates,fh
    pkg = {}
    import useLib
    import graphTemplates
    pkg["fout"] = open(nds["outfile"],'w')
    pkg["fout"].write(graphTemplates.head)
#

def mkG(outFile,Iarray):
    """
    make yed graph from thing,pred,edge,node
    """
    global nds,pkg,graphTemplates,fh
    nds = {}
    nds['outfile'] = outFile
    nds['iarray']=Iarray
    init()
    per(0)#thing
    per(1)#pred
    perNode()#node
    perEdge()   
    pkg["fout"].write(graphTemplates.tailT)
    pkg["fout"].close()
    print('mkG DONE')
#end mkG
def per(ix):
    """
    make a node for each thing
    """
    global graphTemplates,nds,pkg
    for t in range(1,len(nds['iarray'][ix])+1):
        na = nds['iarray'][ix].keys()[t-1]
        #protect na from < and >
        pna = na
        pna = pna.replace("<","Z-")
        pna = pna.replace(">","-Z")
        rnt = graphTemplates.refidT
        rnt = rnt.replace("%refid%",str(pna))
        rnt = rnt.replace("%refidNode%",'n'+str(nds['iarray'][ix][na]))
        print('na=('+pna+')@reg=('+ str(nds['iarray'][ix][na])+')')
        pkg["fout"].write(rnt)
    #endfor
#per



def perNode():
    """
    make a node for each node
    """
    global graphTemplates,nds,pkg
    for t in range(1,len(nds['iarray'][3])+1):
        na = nds['iarray'][3].keys()[t-1]
        #protect na from < and >
        pna = na
        pna = pna.replace("<","Z-")
        pna = pna.replace(">","-Z")
        rnt = graphTemplates.refidT
        rnt = rnt.replace("%refid%",str(''))
        rnt = rnt.replace("%refidNode%",'n'+str(pna))
        print('na=('+pna+')@reg=('+ str(pna)+')')
        pkg["fout"].write(rnt)
    #endfor
#perNode

def perEdge():
    """
    edge format ([from:to]=str)
    """
    global graphTemplates,nds,pkg
    # reverse predicates for text
    rpred = {}
    for rp in range(1,len(nds['iarray'][1])+1):
        k = nds['iarray'][1].keys()[rp-1]
        v = nds['iarray'][1][k]
        rpred[str(v)] = str(k)
    for t in range(1,len(nds['iarray'][2])+1):
        fxa = nds['iarray'][2].keys()[t-1]
        xa = nds['iarray'][2][fxa]
        fo = xa.find(":")
        mo = xa.find("!")
        fr = xa[0:fo]
        tt = xa[fo+1:mo]
        tp = xa[mo+1:]
        edge = graphTemplates.edgeT
        edge = edge.replace("%edg%",'e'+str(fxa))
        edge = edge.replace("%srcNode%",'n'+str(fr))
        edge = edge.replace("%objNode%",'n'+str(tt))
        edge = edge.replace("%text%",str(rpred[tp]))
        print('\nxa=('+xa+')')
        print('fr=('+str(fr)+')')
        print('tt=('+str(tt)+')')
        print('txt='+str(rpred[tp]))
        print('reg=('+str(fxa)+')')
        pkg["fout"].write(edge)
    #endfor
#end edge
#support  


    
    
    
    
    
    
    