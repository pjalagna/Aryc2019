m= """
file genn.py
create uid
pja 01-10-2020
use with takeV verb in basii
"""
"""
test as
p = {}
p['package'] = {}
p['help'] = {}
p['sy'] = {}
import gennV
p = gennV.main(p)


"""
def main( p , v=m ):
    p['package']['gennV'] = ''
    p['help']['gennV'] = v
    p['sy']['genX'] = genX
    p['help']['genX'] = 'genX (,,gen#) generates a UID'
    return(p)
#end main
def genX(p):
    import time
    j = "X" + time.time().__str__()
    # push j
    p['sy']['push'](j)
    # push ok
    p['sy']['push'](p['OK'])
#end genn
