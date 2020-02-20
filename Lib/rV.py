# file name rV.py 
"""
pja 1-30-2020
r register rtns for basii with help

rzero # r0 - ready/reset r p['r'] = []
dotr # .r dump r to display
rat # r@ (,,vr) r[0] to dat p['r'][0]
rbang # r! (s,,) dat to r[0]
rin # r< append to r (v,,) p['r'].append(v)
rout # r> pop from r (,,r[0] with destroy ) p['r'].pop()
"""
"""
test as 
import bbox
bbox.main('bmain')
bbox.start()
push 
rV
takeV



fn = p['sy']['pop']()
p['sy']['push'](p['OK'])
"""
def main(p,m):
    p['package']['rV'] = ''
    p['help']['rV'] = m
	p['sy']['r0'] = rzero # ready/reset r register
	p['help']['r0'] = "rzero # ready/reset r register"
	p['sy']['.r'] = dotr # (,,) display r register contents
	p['help']['.r'] = "dotr # (,,) display r contents"
	p['sy']['r<'] = rin # (v,,) appends v to r
	p['help']['r<'] = "rin # (v,,) appends v to r"
	p['sy']['r>'] = rout # (,,r[last]) r[last] to dat w/ destroy
	p['help']['r>'] = "rout # (,,r[last]) r[last] to dat w/ destroy"
	p['sy']['r@'] = rat # (,,v) r[last] to dat
	p['help']['r@'] = "rat # (,,v) r[last] to dat"
	p['sy']['r!'] = rbang # (v,,) r[last] <- dat
	p['help']['r!'] = "rbang # (v,,) r[last] <- dat"
	return(p)
#end main
def rbang(p): # (v,,) r[last] <- dat
    fn = p['sy']['pop']()
    p['r'][len(p['r'])-1] = fn
    p['sy']['push'](p['OK'])
#end r!
def rat(p): # (,,v) r[last] to dat
    m = p['r'][len(p['r'])-1]
    p['sy']['push'](m)
    p['sy']['push'](p['OK'])
#end rat
def rout(p): # (,,r[last]) r[last] to dat w/ destroy
    m = p['r'].pop(len(p['r'])-1)
    p['sy']['push'](m)
    p['sy']['push'](p['OK'])
#end rout
def rin(p): # (v,,) appends v to r
    v= p['sy']['pop']()
    p['r'].append(v)
    p['sy']['push'](p['OK'])
#end rin
def rzero(p): # ready/reset r register
    p['r']=[]
    p['sy']['push'](p['OK'])
#end rzero
def dotr(p): # (,,) display r register contents
    print('===r===')
    m = p['r'].__str__()
    print(m)
    print('===end r===')
    p['sy']['push'](p['OK'])
#end dotr