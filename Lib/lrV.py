"""
file lrV.py
adds lr,ln arrays to p
verbs .lr,lr#,lr!,lr@ .ln,ln#,ln!,ln@
"""
def main(p):
    """
    for takeV
    """
    import lrV
    p['package']['lrV'] = lrV
    p['help']['lrV'] = lrV.__doc__
    p['ln'] = [] # list of names
    p['lr'] = [] # list of programs
    p['sy']['.lr']= dotlr
    p['help']['.lr']= 'display lr array'
    p['sy']['.ln']= dotln
    p['help']['.ln']= 'display ln array'
    p['sy']['lr!']= lrbang
    p['help']['lr!']= 'lr! (x,,) append to lr'
    p['sy']['ln!']= lnbang
    p['help']['ln!']= 'ln! (x,,) append to lr'
    p['sy']['lr@']= lratt
    p['help']['lr@']= 'lr@ (,,x) get from lr'
    p['sy']['ln@']= lnatt
    p['help']['ln@']= 'ln@ (,,x) get from ln'
    p['sy']['ln#']= lnpound
    p['help']['ln#']= 'ln# (,,x) depth of ln'
    p['sy']['lr#']= lrpound
    p['help']['lr#']= 'lr# (,,x) depth of lr'
    p['sy']['lrz']= lrz
    p['help']['lrz']= 'clears lr array'
    p['sy']['lnz']= lnz
    p['help']['lnz']= 'clears ln array'
    return(p)
#
def lnz(p):
    """
    zero ln array
    """
    p['ln'] = []
    p['sy']['push'](p['OK'])
#
def lrz(p):
    """
    zero lr array
    """
    p['lr'] = []
    p['sy']['push'](p['OK'])
#
def dotlr(p):
    print('[lr]')
    print(p["lr"])
    print('/[lr]')
    p['sy']['push'](p['OK'])
#
def dotln(p):
    print('[ln]')
    print(p["ln"])
    print('/[ln]')
    p['sy']['push'](p['OK'])
#
def lnpound(p):
    p['sy']['push'](str(len(p['ln'])))
    p['sy']['push'](p['OK'])
#
def lrpound(p):
    p['sy']['push'](str(len(p['lr'])))
    p['sy']['push'](p['OK'])
#
def lrbang(p):
    """
    into lr
    """
    p['lr'].append(p['sy']['pop']())
    p['sy']['push'](p['OK'])
#
def lnbang(p):
    """
    into ln
    """
    p['ln'].append(p['sy']['pop']())
    p['sy']['push'](p['OK'])
#
def lratt(p):
    """
    from lr
    """
    p['sy']['push'](p['lr'].pop())
    p['sy']['push'](p['OK'])
#
def lnatt(p):
    """
    from lr
    """
    p['sy']['push'](p['ln'].pop())
    p['sy']['push'](p['OK'])
#
#end lrV
    

