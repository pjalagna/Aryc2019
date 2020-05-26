"""
file p7xRtns.py
pja 5/14/2020

read routines for p7 generated arrays

"""
def p7clean0(atn):
    #cleans key[0] p7 atn 
    ans = jj[atn].keys()[0].__str__()
    return(ans)
#
def p7KRecord(mx,krid):
    ans = mx['KRID'][krid]['ATN']
    return(ans)
#
def p7First(mx):
    """pu = getPU() from first"""
    tpu =mx['KRID'][mx['FIRST'].keys()[0]]['ATN']['pickup'].keys()[0]
    tkrid = mx['ATN']['pickup'][tpu]['KRID'].keys()[0]
    return(tkrid)
#
def p7Next(mx,tpu): #=> krid/-1
    try:
        tpu = mx['previousPU'][tpu]['ATN']['pickup'].keys()[0]
        tkrid = mx['ATN']['pickup'][tpu]['KRID'].keys()[0]
        mx['KRID'][tkrid]['ATN']
    except:
        tkrid = -1
    finally:
        nop = 1
    #endtry
    return(tkrid)
#