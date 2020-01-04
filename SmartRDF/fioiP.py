# file fioiP.py
"""
pja 01-02-2020 added fioo
pja 12-28-2019 edited fpword ! command added ok to stack
pja 12-27-2019 edited main for datastack pickup of filename
pja 02-11-2018 orig
vector sets fioi verbs for basiiP protocol

I: requires parse file name on data stack
-- as per datPush protocol
O: returns new architecture array with inclusions

note: all symbols and subroutine names must be unique within architecture p

not all signals of the class have been added. those beginning with "--" have
--fioi , 
--fioo ,
--fpword 
get/set iox, 
flookup , 
fwhite, 
ftill,  
fctill, 
ftillor
"""
# fioi , fioo , get/set iox, flookup , fwhite, ftill,  fctill, ftillor
def main(p):
    """ p is architecture array """
    # set up class in sy-fioC using filename on datastack
    # all Pverbs come off class
    import fioiClass
    PFN = p['sy']['pop']() # file name on stack
    p['sy']['fioC'] = fioiClass.fio(PFN)
    # need facades for all class bound verbs
    p['sy']['fioi'] = fioiP
    p['sy']['fioo'] = fiooP
    p['sy']['fpword'] = fpwordP
    return (p)
#end main
def fioiP(p):
    ans = p['sy']['fioC'].fioi()
    # push ans
    p['sy']['push'](ans)
    #push ok
    p['sy']['push'](p['OK'])
#end fioiP
def fiooP(p):
    """ push back character counter """
    p['sy']['fioC'].fioo()
    p['sy']['push'](p['OK'])
#end fiooP

def fpwordP(p):
    ans = p['sy']['fioC'].fpword()
    # ans is startPos,word,endpos,type
    # store FPWSP
    p['sy']['push'](ans[0])
    p['sy']['push']('FPWSP')
    p['sy']['!'](p)
    p['sy']['pop']() #drop
    # store FPWD
    p['sy']['push'](ans[1])
    p['sy']['push']('FPWD')
    p['sy']['!'](p)
    p['sy']['pop']() #drop
    # store FPWEP
    p['sy']['push'](ans[2])
    p['sy']['push']('FPWEP')
    p['sy']['!'](p)
    p['sy']['pop']() #drop
    # store FPWT
    p['sy']['push'](ans[3])
    p['sy']['push']('FPWT')
    p['sy']['!'](p)
    p['sy']['pop']() #drop
    # push word
    p['sy']['push'](ans[1])
    #push ok
    p['sy']['push'](p['OK'])
#end fpwordP