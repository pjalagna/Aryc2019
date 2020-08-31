""" StkV: verbs ( $new $push, $pop, $depth, $swap, $drop, $drops, $dropn, $spy, $pick, $.s $dump) """
m = """ StkV: verbs ( $push, $pop, $depth, $swap, $drop, $drops, $dropn, $spy, $pick, $.s $dump) """


def main(p,m=m):
    import StkClass
    p['package']['StkV'] = StkClass
    p['help']['StkV'] = m
    p['sy']['$new'] = newStack
    p['help']['$new'] = "(na,,) creates new stack"
    p['sy']['$.s'] = ddots
    p['help']['$.s'] = "(na,,) displays stack"
    p['sy']['$push'] = dpush
    p['help']['$push'] = "(data,na,,) adds to stack"
    p['sy']['$pop'] = dpop
    p['help']['$pop'] = "(na,,data) gets tos stack"
    p['sy']['$depth'] = ddepth
    p['help']['$depth'] = "(na,,count) size stack"
    p['sy']['$dup'] = ddup
    p['help']['$dup'] = "(val,na,,) dup on stack"
    p['sy']['$swap'] = dswap
    p['help']['$swap'] = "(na,,) swaps on stack"
    #drop
    p['sy']['$drop'] = ddrop
    p['help']['$drop'] = "(na,,) drop tos on stack"
    #drops
    p['sy']['$drops'] = ddrops
    p['help']['$drops'] = "(na,,) drop all on stack"
    #pick
    p['sy']['$pick'] = dpick
    p['help']['$pick'] = "(#,na,,nth) from stack"
    return(p)
# main
def dpick(p):
    p1 = p['sy']['pop']() # na
    p2 = p['sy']['pop']() # #
    # push onto stack
    p['package'][p1].push(p2)
    ans = p['package'][p1].pick()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
def ddrop(p):
    p1 = p['sy']['pop']()
    p['package'][p1].drop()
    p['sy']['push'](p['OK'])
#
def ddrops(p):
    p1 = p['sy']['pop']()
    p['package'][p1].dropx()
    p['sy']['push'](p['OK'])
#
def dswap(p):
    p1 = p['sy']['pop']()
    p['package'][p1].swap()
    p['sy']['push'](p['OK'])
#
def ddup(p):
    p1 = p['sy']['pop']()
    p['package'][p1].dup()
    p['sy']['push'](p['OK'])
#
def ddepth(p):
    p1 = p['sy']['pop']()
    p2 = p['package'][p1].depth()
    p['sy']['push'](p2)
    p['sy']['push'](p['OK'])
#
def newStack(p):
    p1 = p['sy']['pop']()
    p['package'][p1] = p['package']['StkV'].Stks(p1)
    p['sy']['push'](p['OK'])
#
def ddots(p):
    p1 = p['sy']['pop']()
    print(p['package'][p1].dots())
    p['sy']['push'](p['OK'])
#
def dpush(p):
    p1 = p['sy']['pop']() # stk na
    p2 = p['sy']['pop']() # data
    p['package'][p1].push(p2)
    p['sy']['push'](p['OK'])
#
def dpop(p):
    p1 = p['sy']['pop']() # stk na
    ans = p['package'][p1].pop()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#