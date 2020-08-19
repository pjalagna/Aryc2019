"""
// p9
if xsd // phase2

"""
"""
test as
file='pja1.xsd'
import callXML2Onto
callXML2Onto.main(file)

"""
def main(file):
    import useLib
    import useXS
    import p9
    p9.fresh(file)
    p9.main(file,'on')
#