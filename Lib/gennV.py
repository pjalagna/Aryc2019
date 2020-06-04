m= """
file genn.py
create uid
pja 6/1/2020 added gennx simple routine for simple use
pja 04-20-2020 changed time.time to asctime + clock
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
    """ vector init """
    p['package']['gennV'] = ''
    p['help']['gennV'] = v
    p['sy']['genX'] = genX
    p['help']['genX'] = 'genX (,,gen#) generates a UID'
    return(p)
#end main
def genX(p):
    """ vector routine """
    import time
    j = "X" + time.asctime() + time.clock().__str__() 
    j = j.replace(' ',"X")
    # push j
    p['sy']['push'](j)
    # push ok
    p['sy']['push'](p['OK'])
#end genn
def gennX():
    """ simple function returns GUID from time """
    import time
    j = "X" + time.asctime() + time.clock().__str__() 
    j = j.replace(' ',"X")
    return(j)
#gennX
