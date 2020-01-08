"""
file SLV.py
pja 01-05-2026

single list (vector)
behaviors are
main(p) sets sy vectors
SLVoriginate (p)
SLVcreate(name,,)
SLVadd(name,elementName,value,,)
SLVRead(name,elementName,,)
SLVReadAll(name,,)
"""
def main(p):
    p['sy']['logg']('SLV main')
    p['sy']['SLVoriginate'] = SLVoriginate
    return(p)
#end main
def SLVoriginate(p):
    p['sy']['logg']('SLVoriginate')
    p['SLV']={}
    return(p)
#end SLVoriginate
