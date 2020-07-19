"""
file yedRep2.py
useage: yedRep2.main(ontoFile,outfile)

"""
"""
1- init
2- plist[pickup#] 
   ; register.set(len(plist+5))
   ; set ctl3=0 , ctl3Max=len(plist)
   ; ctl5 = 0 ; ctl5Max = len(plist)
   ; nds['xplist'] =[]
   3- per ctl3++; <>ctlMax==>4 else==> 5
      4- (pickup#[ctl3-1]) --> xplist[pickup,rplus()] 
      ; ==>3
         
         5 per ctl5++ <>ctlMax==> 6 else==>7
            6 (xplist[pickup]) --> profile_record[]
               ==>5
              7 ctl8 = 0; ctl8Max=len(profile)
                ftsw write head ==> 8
                8 per ctl8++ <>max==>9 else==>10
                   9 profile_record[] ==> graphATN(refid,v1,v2),register[]
                   ==> 8
                     10 write tail ==> 11
                       11 'done'
--


"""
"""
import yedRep2
yedRep2.main('t1.xsd.onto','pja1.txt','step')

pkg = yedRep2.pkg
nds = yedRep2.nds
"""
#support
def init(fn,outfile,trace):
    global pkg,nds
    nds['fn'] = fn
    nds['outfile'] = outfile
    nds['trace'] = trace
    import useLib
    import useOnto
    import OntologyClass
    pkg['og'] = OntologyClass.Ontology(fn,trace)
    import xlate
    pkg['xlate'] =xlate.setx()
    import useXS
    import registerClass
    pkg['register'] = registerClass.register()
    pkg['out'] = open(outfile,'w')
    import graphTemplates
    pkg['gt'] = graphTemplates
    return(2)
#init

def logg(txt):
    #prints txt if nds['logg'] is =="ON"
    global nds
    if (nds['trace'] == 'on'):
        print("log: " + txt)
    #endif
    if (nds['trace'] == 'step'):
        raw_input("? log: " + txt)
    #endif
#logg

def main(fn,outfile,trace=''):
    """
    usage main(fileName,outfile,trace='')
    
    """
    """
import yedRep2
yedRep2.main('t1.xsd.onto','pjaFile.txt','step')
    
    
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
            ctl = init(fn,outfile,trace) # 
    
    
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
    """  2- plist[pickup#] 
    ; register.set(len(plist+5))  
    ; ctl3 = -1 ctl3Max= len(plist)
    ; ctl5 = -1 ctl5Max= len(plist)
    ; nds['xplist'] =[]
    """
    global pkg,nds 
    plist1 = pkg['og'].ATNSeek('pickup') 
    lp = len(plist1)
    nds['lp'] = lp
    nds["plist"] = []
    for mm in range(lp):
        nds["plist"].append(plist1[mm][2])
    #end for 
    pkg['register'].set(lp+5)
    nds['ctl3'] = -1
    nds['ctl3Max'] = lp
    nds['ctl5'] = -1
    nds['ctl5Max'] = lp
    nds['xplist'] =[]
    return(3)
#end proc2

    
            
def proc3():
    """  3- per ctl3++ <>max==>4 else==> 11  """
    global pkg,nds
    nds['ctl3'] = nds['ctl3']+1
    if (nds['ctl3']==nds['ctl3Max']) :
        ret = 11
    else:
        ret = 4
    #end if
    return(ret)
#end proc3

    
            
def proc4():
    """  4- (pickup#[ctl3-1]) ==> xplist[pickup,rplus()]
          ==> 3  """
    global pkg,nds
    
    p4a = nds['plist'][nds['ctl3']-1] 
    nds['xplist'].append([p4a,pkg['register'].plus()])
    return(3)
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
    """  desc  """
    global pkg,nds  
    return(7+1)
#end proc7

    
            
def proc8():
    """  desc  """
    global pkg,nds  
    return(8+1)
#end proc8

    
            
def proc9():
    """  desc  """
    global pkg,nds  
    return(9+1)
#end proc9

    
            
def proc10():
    """  desc  """
    global pkg,nds  
    return(10+1)
#end proc10


def proc11():
    """  done  """
    global pkg,nds
    print("DONE")  
    return(-1)
#end proc10
