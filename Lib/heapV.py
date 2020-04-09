m= """
# file name heapV.py
pja 1-30-2020
heap rtns for basii with help entries

# heapInit - ready/reset heap
# .h dump heap to display
# (#,,) h^ allots # slots to heap
# (,,) hx removes current slots from heap
# (v,#,,) h! writes v to heap[h[0]-#]
# (#,,v) h@ reads heap[h[0]-#]
"""
"""
test as 
import bbox
bbox.main('bmain')
bbox.start()
push 
heapV
takeV
heapInit
push 
5
h^
push "fox"
push "3"
h!
push "3"
h@
.h


fn = p['sy']['pop']()
p['sy']['push'](p['OK'])
"""
def main(p,m=m):
    p['package']['heapV'] = ''
    p['help']['heapV'] = m
    p['sy']['.h'] = doth # .h dump heap to display
    p['help']['.h'] = "doth # .h dump heap to display"
    p['sy']['h^'] = hup # (#,,) h^ allots # slots to heap
    p['help']['h^'] = "hup # (#,,) h^ allots # slots to heap"
    p['sy']['hx'] = hx # (,,) hx removes current slots from heap
    p['help']['hx'] = "hx # (,,) hx removes current slots from heap"
    p['sy']['h!'] = hbang # (v,#,,) h! writes v to heap[h[0]-#]
    p['help']['h!'] = "hbang # (v,#,,) h! writes v to heap[h[0]-#]"
    p['sy']['h@'] = hat # (#,,v) h@ reads heap[h[0]-#]
    p['help']['h@'] = "hat # (#,,v) h@ reads heap[h[0]-#]"
    p['sy']['heapInit'] = heapInit # heapInit - ready/reset heap
    p['help']['heapInit'] = "heapInit # heapInit - ready/reset heap"
    return(p)
#end main
def doth(p):
    print('==heap==')
    print(p['heap'].__str__())
    print('==end heap==')
    p['sy']['push'](p['OK'])
#end doth

def hup(p):
    ns = p['sy']['pop']()
    n = int(ns)
    for j in range(n):
        p['heap'].append(0)
    #end for
    f = p['heap'][0]
    p['heap'].append(f)
    p['heap'][0] = len(p['heap'])-1
    p['sy']['push'](p['OK'])
#end hup
def hx(p):
    n = p['heap'][p['heap'][0]]
    cc = p['heap'][0] - n
    for j in range(cc):
        p['heap'].pop()
    #end for
    p['heap'][0] = n
    p['sy']['push'](p['OK'])
#end hx

def hbang(p): # (v,#,,) h! writes v to heap[h[0]-#]
    i = int(p['sy']['pop']())
    v = p['sy']['pop']()
    m = int(p['heap'][0]-i)
    p['heap'][m]=v
    p['sy']['push'](p['OK'])
#end h!
def hat(p):
    # (#,,v) h@ reads heap[h[0]-#]
    fn = int(p['sy']['pop']())
    m = p['heap'][0]-fn
    v = p['heap'][m]
    p['sy']['push'](v)
    p['sy']['push'](p['OK'])
#end h@
def heapInit(p):
    p['heap'] = [0]
    p['sy']['push'](p['OK'])
#end heapInit