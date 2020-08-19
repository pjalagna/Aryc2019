"""
file callXSD2Onto
// p9
if xsd // phase2

"""
"""
test as
file = 'pja1.xsd'
import callXSD2Onto
callXSD2Onto.main(file)

"""
def main(file):
    import useLib
    import useXS
    import p9
    p9.fresh(file)
    p9.main(file,'on')
    #and phase 2
    import phase2
    phase2.main(file+'.onto')
#