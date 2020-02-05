# file name libV.py 
"""
pja 1-30-2020
library rtns for basii

lzero # l0 (,,) sets/resets library
lbang # l! (code,name,,) lib[name] = code
libat # l@ (name,,code) gets code from lib['name']
dotlib # .l (,,) display lib names
lminus # l- (name,,) drops name in library

test as 
import bbox
bbox.main('bmain')
bbox.start()
push 
libV
takeV

fn = p['sy']['pop']()
p['sy']['push'](p['OK'])
"""
def main(p):
	p['sy']['l0'] = lzero # l0 (,,) sets/resets library
	p['help']['l0'] = "(,,) sets/resets library"
	
	p['sy']['l!'] = lbang # l! (code,name,,) lib[name] = code
	p['help']['l!'] = "l! (code,name,,) lib[name] = code"
	
	p['sy']['l@'] = libat # l@ (name,,code) code from lib['name']
	p['help']['l@'] = "l@ (name,,code) code from lib['name']"
	
	p['sy']['.l'] = dotlib # .l display names
	p['help']['.l'] =  ".l display names"
	p['sy']['l-'] = lminus # (name,,) drops name from library
	p['help']['l-'] =  "(name,,) drops name from library"
	return(p)
#end main
def lminus(p): # l- (name,,) drops name in library
    na = p['sy']['pop']()
    p['lib'].pop(na)
    p['sy']['push'](p['OK'])
#end l-
def dotlib(p): # .l display names
    ans = p['lib'].keys()
    ans.sort()
    anss = ans.__str__()
    print('=== lib names ===')
    print(anss)
    print('=== end lib names ===')
    p['sy']['push'](p['OK'])
#end .l
def libat(p):  # l@ (name,,code) code from lib['name']
    na = p['sy']['pop']()
    ans = p['lib'][na]
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#end l@
def lbang(p): # l! (code,name,,) lib[name] = code
    na = p['sy']['pop']()
    code = p['sy']['pop']()
    p['lib'][na]=code
    p['sy']['push'](p['OK'])
#end l!

def lzero(p): # l0 (,,) sets/resets library
    p['lib'] = {}
    p['sy']['push'](p['OK'])
#end l0

