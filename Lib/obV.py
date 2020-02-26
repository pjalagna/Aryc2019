m = """
file obV.py
pja 02-24-2020 added object.revcall 
-- format listname=>objectName gets object name from listname
pja 02-22-2020
object package for basii

.ob dump p['object']
getOb p['object'] onto stack to use arV 
"""
def main(p,m=m):
    p['package']['obV'] = ''
    p['help']['obV'] = m
    p['object']={}
    p['object']['revcall'] = {}
    p['sy']['.ob']= dotOb #(val,index,[],,[])
    p['help']['.ob']= "(,,) display p['object']"
    p['sy']['getOb']= getOb #(val,index,[],,[])
    p['help']['getOb']= "(,,{ob}) stack p['object']"
    return(p)
#
def dotOb(p):
    print(p['object'])
    p['sy']['push'](p['OK'])
#
def getOb(p):
    p['sy']['push'](p['object'])
    p['sy']['push'](p['OK'])
#


    
    