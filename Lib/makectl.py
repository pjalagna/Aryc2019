def x3q():
    ans = '"' + '"' + '"'
    return(ans)
#end x3q

def makectl(inp,desc):
    ans1 = """
        elif (ctl == %x%): #
            logg(proc%x%.__doc__)
            ctl = proc%x%() #
    """
    ans2 = """
            
def proc%x%():
    %3q% %desc% %3q%
    global pkg,nds  
    return(%x%+1)
#end proc%x%

    """
    ans1 = ans1.replace ('%x%',str(inp))
    ans1 = ans1.replace ('%3q%',x3q())
    ans1 = ans1.replace ('%desc%',desc)
    ans2 = ans2.replace ('%x%',str(inp))
    ans2 = ans2.replace ('%3q%',x3q())
    ans2 = ans2.replace ('%desc%',desc)
    return(ans1,ans2)
#end makectl

def makeset(low,high):
    finaltest = makeHead()
    finalProcs = ""
    for x in range(low,high+1):
        ans1,ans2 = makectl(x,' desc ')
        finaltest = finaltest + ans1
        finalProcs = finalProcs + ans2
    #end for
    
    return(finaltest+makeTail(),finalProcs)
#end makeset

def makeHead():
    ans1 = """
#support
def logg(txt):
    #prints txt if nds['logg'] is =="ON"
    global nds
    if (nds['trace'] == 'on'):
        print("log: " + txt)
    #endif
#logg

def main(fn,trace=''):
    %3q%
    usage main(fileName)
    renders to ontology fileName.onto
    %3q%
    global nds,pkg
    nds = {}
    pkg = {}
    nds = getnds()
    pkg = getpkg
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
    
    """
    ans1 = ans1.replace ('%3q%',x3q())
    return(ans1)
#makeHead

def makeTail():
    ans1 = """
        else:
            print('error ctl ('+ctl.__str__()+')')
            ctl = -1
        #endif
    #wend
#main
    
    """
    return(ans1)
#end makeTail

    
        
        
        