m = """
# file fioiV.py
pja 04-07-2020 fiox@
pja 03-31-2020 added fctillor, fwhite
pja 01-30-2020 added help entries
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
def main(p,m=m):
    p['package']['fioiV'] = ''
    p['help']['fioiV'] = m
    """ p is architecture array """
    # set up class in sy-fioC using filename on datastack
    # all Pverbs come off class
    import fioiClass
    PFN = p['sy']['pop']() # file name on stack
    p['sy']['fioC'] = fioiClass.fio(PFN)
    p['help']['fioC'] = "fioiClass.fio(PFN)"
    # need facades for all class bound verbs
    # fioiV:main 4  # sections mark
    p['sy']['fioi'] = fioiP
    p['help']['fioi'] = "(,,c(iox)) from file PFN"
    p['sy']['fioo'] = fiooP
    p['help']['fioo'] = "(,,) PFN iox is decremented"
    p['sy']['fpword'] = fpwordP
    p['help']['fpword'] = "(,,word) from PFN at iox"
    p['sy']['ftlc'] = ftlP
    p['help']['ftlc'] = "fctl file-till-char (CHX,,stringTillCHX) from PFN at iox"
    #fioxSet(self,pos)
    p['sy']['fback'] = fback
    p['help']['fback'] = "fback (,,) resets fiox from last pword at fiox"
    p['sy']['fctillor'] = Vfctillor
    p['help']['fctillor'] = "(stringOfTargets,,) collects till one of target"
    p['sy']['fwhite'] = Vwhite
    p['help']['fwhite'] = "(,,) skips space line tabs and comments in file"
    p['sy']['f0'] = fzero
    p['help']['f0'] = "(,,) rewind file"
    p['sy']['fiox@'] = fioxAt
    p['help']['fiox@'] = "(,,fiox) get current file position"
    return (p)
#end main
# fioiV:codespace 0 # sections mark
def fioxAt(p):
    ans = p['sy']['fioC'].fioxGet()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
def fzero(p):
    p['sy']['fioC'].fioxSet(0)
    p['sy']['push'](p['OK'])
#

def Vwhite(p):
    p['sy']['fioC'].fwhite()
    p['sy']['push'](p['OK'])
#
def Vfctillor(p):
    target = p['sy']['pop']()
    ans = p['sy']['fioC'].fctillor(target)
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
    
def fback(p):
    #get pos from NDS
    p['sy']['push']('FPWSP')
    p['sy']['@'](p)
    p['sy']['pop']()
    pos = p['sy']['pop']()
    posi = int(pos)
    p['sy']['fioC'].fioxSet(posi)
    #push ok
    p['sy']['push'](p['OK'])
#end ftlP
def ftlP(p):
    #get target
    targetCH = p['sy']['pop']()
    ans = p['sy']['fioC'].fctill(targetCH)
    p['sy']['push'](ans)
    #push ok
    p['sy']['push'](p['OK'])
#end ftlP
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