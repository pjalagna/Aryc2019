"""
file callRDF2Graph.py

"""
"""
test as
file='pja1.xsd'
import callRDF2Graph
callRDF2Graph.main(file)

"""
def main(file):
    import useLib
    import useRDF
    import RDFRead
    thing,predicate,edge,nodes = RDFRead.main(file+'.onto.rdf')
    print("thing")
    print(thing)
    print("/thing")
    
    print("predicate")
    print(predicate)
    print("/predicate")
    
    print("edge")
    print(edge)
    print("/edge")
    
    print("nodes")
    print(nodes)
    print("/nodes")
    import makeGraph
    outFile = file+'.onto.rdf.graphml'
    array = [thing,predicate,edge,nodes]
    makeGraph.mkG(outFile,array)
#
    