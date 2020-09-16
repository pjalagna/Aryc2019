"""
registerV object process for parser registers
use in pbox "registerV" takeV
SetRegister NewRegister
dumpRegister
"""
def main(p):
    import registerClass
    try:
        j == p['class']
        p['class']['register']= registerClass
    except:
        p['class']= {} # first use
        p['class']['register']= registerClass
    finally:
        nop = 1
    #end try
    p['sy']['newRegister']= NewRegister
    p['help']['newRegister'] = "assigns new register"
    p['sy']['SetRegister']= SetRegister
    p['help']['SetRegister'] = "(value,name,rn,) into register"
    p['v']['rn'] = 1 # init
    return (p)
# main
def NewRegister(p):
    rn = p['nds']['rn']# rn = nds[rn]
    p['v']["rn"] = rn+1
    p['v']['rg'+str(rn)] = p['class']['register'].register(rn)
    p['sy']['push'](rn)
    p['sy']['push'](p['OK'])
# new
def SetRegister(p):
    # (value,name,rn,,)
    rn = p['sy']['pop']()
    na = p['sy']['pop']()
    val = p['sy']['pop']()
    le = p['v']['rg'+str(rn)]
    le.at[name]=val
    p['sy']['push'](p['OK'])
#
def dumpRegister(p):
    # (rn,,) prints contents
