"""
file genn.py
create uid
pja 01-10-2020
use with takeV verb in basii
"""
def main(p):
    p['sy']['genx'] = genx
    return(p)
#end main
def genx(p):
    import time
    j = "X" + time.time().__str__()
    # push j
    p['sy']['push'](j)
    # push ok
    p['sy']['push'](p['OK'])
#end genn
