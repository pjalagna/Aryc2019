"""
file makeGraph.py
test1 = first make
"""
"""
test as
import makeGraph
makeGraph.mkG('pja1.graphml')
makeGraph.main('pja1.graphml')

"""
def mkG(outfile,nin=100):
    """
    load outfile
    """
    global graphTemplates,fh
    import graphTemplates
    fh = open(outfile,'w')
    fh.write(graphTemplates.head)
    relateG1(
    "this is one"
    ,"this is two"
    ,"this is three"
    ,"this is four"
    ,"this is five"
    ,"this is six"
    ,"this is seven"
    ,nin*2)
    relateG1(
    "this is eight"
    ,"this is nine"
    ,"this is ten"
    ,"this is eleven"
    ,"this is twelve"
    ,"this is thirteen"
    ,"this is fourteen"
    ,nin*4)
    fh.write(graphTemplates.tailT)
    fh.close()
    print('mkG DONE')
#end mkG

def relateG1(v1,v2,v3,v4,v5,v6,refid,nin=100):
    #test2
    global graphTemplates,fh
    nreg = nin
    #refid
    rn = nreg
    rnt = graphTemplates.refidT
    rnt = rnt.replace("%refidNode%",'n'+str(rn))
    rnt = rnt.replace("%refid%",refid)
    fh.write(rnt)
    #
    nreg = nreg+1
    # center
    cn = nreg
    cnt = graphTemplates.centerT
    cnt = cnt.replace("%cent%",'n'+str(cn))
    fh.write(cnt)
    #
    nreg = nreg+1
    fh.write(Nv1v2(v1,v2,nreg))
    v1v2n = nreg
    nreg = nreg+1
    #v5v6

    fh.write(Nv1v2(v5,v6,nreg))
    v5v6n = nreg
    nreg = nreg + 1
    #predicateT predNode v3 v4
    prdn = nreg
    prdnt = graphTemplates.predicateT
    prdnt = prdnt.replace("%predNode%",'n'+str(prdn))
    prdnt = prdnt.replace("%v3%",v3)
    prdnt = prdnt.replace("%v4%",v4)
    fh.write(prdnt)
    # edgeT "%edg%" "%srcNode%" "%objNode%"
    fh.write(edgeN(nreg,rn,cn))
    nreg = nreg+1
    fh.write(edgeN(nreg,v1v2n,cn))
    nreg = nreg+1
    fh.write(edgeN(nreg,cn,v5v6n))
    nreg = nreg+1
    fh.write(edgeN(nreg,cn,prdn))
#end relateG
    
    
def main(outfile,nin=100):
    #test1
    global graphTemplates
    import graphTemplates
    fh = open(outfile,'w')
    # head
    fh.write(graphTemplates.head)
    nreg = nin
    #refid
    rn = nreg
    rnt = graphTemplates.refidT
    rnt = rnt.replace("%refidNode%",'n'+str(rn))
    fh.write(rnt)
    #
    nreg = nreg+1
    # center
    cn = nreg
    cnt = graphTemplates.centerT
    cnt = cnt.replace("%cent%",'n'+str(cn))
    fh.write(cnt)
    #
    nreg = nreg+1
    v1 = 'i am v1'
    v2 = 'i am v2'
    fh.write(Nv1v2(v1,v2,nreg))
    v1v2n = nreg
    nreg = nreg+1
    #v5v6
    v1 = 'i am v5'
    v2 = 'i am v6'
    fh.write(Nv1v2(v1,v2,nreg))
    v5v6n = nreg
    nreg = nreg + 1
    #predicateT predNode v3 v4
    prdn = nreg
    prdnt = graphTemplates.predicateT
    prdnt = prdnt.replace("%predNode%",'n'+str(prdn))
    prdnt = prdnt.replace("%v3%",'predv3')
    prdnt = prdnt.replace("%v4%",'predv4')
    fh.write(prdnt)
    # edgeT "%edg%" "%srcNode%" "%objNode%"
    fh.write(edgeN(nreg,rn,cn))
    nreg = nreg+1
    fh.write(edgeN(nreg,v1v2n,cn))
    nreg = nreg+1
    fh.write(edgeN(nreg,cn,v5v6n))
    nreg = nreg+1
    fh.write(edgeN(nreg,cn,prdn))
    fh.write(graphTemplates.tailT)
    fh.close()
#end main
    
    
    
    
    
    
#support  
def Nv1v2(v1,v2,nreg):
    """
    ret filled text
    """
    global graphTemplates
    v52t = graphTemplates.Nv1v2T
    v52t = v52t.replace("%Node%",'n'+str(nreg))
    v52t = v52t.replace("%v1%",v1)
    v52t = v52t.replace("%v2%",v2)
    return(v52t)
#end Nv1v2
def edgeN(nreg,src,targ):
    """
    ret string
    """
    global graphTemplates
    # edgeT "%edg%" "%srcNode%" "%objNode%"
    edge = graphTemplates.edgeT
    edge = edge.replace("%edg%",'e'+str(nreg))
    edge = edge.replace("%srcNode%",'n'+str(src))
    edge = edge.replace("%objNode%",'n'+str(targ))
    return(edge)
#end edgeN
    
    
    
    
    
    
    