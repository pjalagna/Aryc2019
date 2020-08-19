"""
file RDFEntry.py
pja 7/19/2020

"""
"""
test as
import RDFEntry
res = RDFEntry.main()
res = RDFEntry.batch(fileName)
RDFEntry.makeGraph(res,"pja1RDF.graphml")
"""
def main():
	
    ctl = 0
    while(ctl==0):
        j = raw_input('?> ')
        if (j.lower() == 'end'):
            ctl = -1
        elif (j.lower()== 'name:'):
            n = raw_input(j+"? ")
            try:
                a = thing[n]
                print('exists')
            except:
                pred[n] = t.plus()
                print('assigned '+str(pred[n]))
            finally:
                nop = 1
            #end try
        elif (j.lower()== 'predicate:'):
            n = raw_input(j+"? ")
            try:
                a = pred[n]
                print('exists')
            except:
                pred[n] = t.plus()
                print('assigned '+str(pred[n]))
            finally:
                nop = 1
            #end try
        elif (j.lower()=='rdf:'):
            six = getSubject()
            pix = getPred()
            oix = getObj()
            record.append([six,pix,oix])
        else:
            print('unknown command ' + str(j))
        #endif
    #wend
    return(thing,pred,collect,record)
#end
def getSubject():
    global thing,pred,collect,record,t
    n = raw_input("subject? ")
    if (n=="("):
        a = getCollect()
    else:
        try:
            a = thing[n]
            print('exists')
        except:
            thing[n] = t.plus()
            print('assigned '+str(thing[n]))
            a = thing[n]
        finally:
            nop = 1
        #end try 
    #endif
    return(a)
#end getSubject 
def getObj():
    global thing,pred,collect,record,t
    n = raw_input("Object? ")
    if (n=="("):
       a = getCollect()
    else:
        try:
            a = thing[n]
            print('exists')
        except:
            thing[n] = t.plus()
            print('assigned '+str(thing[n]))
            a = thing[n]
        finally:
            nop = 1
        #end try 
    #endif
    return(a)
#end getObj 
def getPred():
    global thing,pred,collect,record,t
    n = raw_input("predicate? ")
    if (n=="("):
        a = getCollect()
    else:
        try:
            a = pred[n]
            print('exists')
        except:
            pred[n] = t.plus()
            print('assigned '+str(pred[n]))
            a = pred[n]
        finally:
            nop = 1
        #end try 
    #endif
    return(a)
#end getPred 
def getCollect():
    global thing,pred,collect,record,t
    six = getSubject()
    pix = getPred()
    oix = getObj()
    cx = "::"+str(six)+"::"+str(pix)+"::"+str(oix)
    #compound exists?
    try:
        a = collect[cx]
        print("exists")
    except:
        collect[cx] = t.plus()
        print('assigned '+str(collect[cx]))
        a = collect[cx]
    finally:
        nop = 1
    #end try
    return(a)
#end getCollect

def makeGraph(res,outfile):
    # res [0]thing [1]pred [2]collect [3]record
    import SPOTemplate_graphml
    fh = open(outfile,'w')
    #write head
    fh.write(SPOTemplate_graphml.headT)
    #write node for each thing
    print('process things')
    for nn in res[0]:
        nna = nn
        nox = res[0][nn]
        nod = SPOTemplate_graphml.nodeT
        nod = nod.replace('%node%',str(nox))
        nod = nod.replace("%nodeContent%",str(nna))
        fh.write(nod)
    #endfor
    #write center for each predicate
    print('process predicates')
    for nn in res[1]:
        nna = nn
        nox = res[1][nn]
        cox = SPOTemplate_graphml.centerT
        cox = cox.replace('%node%',str(nox))
        cox = cox.replace('%c%',str(nna))
        fh.write(cox)
    #
    #endfor
    print('process collection')
    for tt in res[2]:
        #write center for each collect
        cx = res[2][tt]
        cox = SPOTemplate_graphml.centerT
        cox = cox.replace('%node%',str(cx))
        cox = cox.replace('%c%',str(tt))
        fh.write(cox)
        #write edge for each collect to nodes in collect
        xc = tt
        xv = xc.split("::")
        for j in range(1,len(xv)):
            #write edge for each collect to nodes in collect
            #xv[j] - target cx src
            edg = SPOTemplate_graphml.edgeT
            edg = edg.replace('%edge%',str(t.plus()))
            edg = edg.replace('%src%',str(cx))
            edg = edg.replace('%targ%',str(xv[j]))
            edg = edg.replace('%aro-data%',"")
            fh.write(edg)
    #endfor
    #write edge for each record
    for mm in res[3]:
        tg = mm
        s = tg[0]
        p = tg[1]
        o = tg[2]
        #write edge s->p
        edg = SPOTemplate_graphml.edgeT
        edg = edg.replace('%edge%',str(t.plus()))
        edg = edg.replace('%src%',str(s))
        edg = edg.replace('%targ%',str(p))
        edg = edg.replace('%aro-data%',"")
        fh.write(edg)
        #write edge p->o
        edg = SPOTemplate_graphml.edgeT
        edg = edg.replace('%edge%',str(t.plus()))
        edg = edg.replace('%src%',str(p))
        edg = edg.replace('%targ%',str(o))
        edg = edg.replace('%aro-data%',"")
        fh.write(edg)
    #end for
    #write tail
    fh.write(SPOTemplate_graphml.tailT)
    #close outfile
    fh.close()
    print("outfile "+ outfile+"done")
#end makeGraph

def getline(txt=''):
    global thing,pred,collect,record,t,fb
    sd = fb.readline()
    sd = sd.rstrip('\n\t ')
    sd = sd.lstrip('\n\t ')
    return(sd)
#

