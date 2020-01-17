"""
file arV.py
pja 01-10-2020

array functions for basii

"""
def main(p):
    p['sy']['ARHelp'] = ARHelp
    return(p)
#end main
def ARHelp(p):
    ans = """
    array functions for basii
    .ARHelp this file
    .ARD ([],,depth)
    ARRead ([],#,,[0])
    ARAdd ([],v,,[]) # append v to []
    ARVWrite (0,v,+,,[]) # enumerated list from v
    ARDWrite (0,[c,v],,{}) #dictionary gen from cv
    ARRecWrite (0,[recn,0,[cv]],,[[]])
    """
    print(ans)
    p['sy']['push'](p['OK'])
#end ARHelp