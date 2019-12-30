"""
file smartRDFX1.py
facade for smartRDFX

pja 12-27-2019

test as
import smartRDFX1
p = smartRDFX1.main('script file')

"""
def main(scriptFile):
    import smartRDFX
    smartRDFX.main('RDFMain')
    p = smartRDFX.getp()
    
    # add other vector files
    p = smartRDFX.datPush('')
    p = smartRDFX.take(p,'fioiP')
    print(p)
#end main

