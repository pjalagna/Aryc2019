m="""
file fenceV.py
pja 04-08-2020 

a takeV file
adds verb fence (str,fmark,bmark,offset,,clip,fpos) ok/nok
"""
def main(p,m=m):
    # import 
    import fence
    # set package and package help
    p['package']['fenceV'] = fence
    p['help']['fenceV'] = m
    # set symbol and help
    p['sy']['fence']= fenceP 
    p['help']['fence']= "fence (str,fmark,bmark,offset,,[a]) a=clip,fpos if ok else nok"
    return(p)
#
# converters for code
def fenceP(p):
    #get paras str,fmark,bmark,offset
    offset = p['sy']['pop']()
    bmark = p['sy']['pop']()
    fmark = p['sy']['pop']()
    strin = p['sy']['pop']()
    #proc
    ##po--("strin=(" + strin.__str__() + ")")
    ##po--("fmark=(" + fmark.__str__() + ")")
    ##po--("bmark=(" + bmark.__str__() + ")")
    ##po--("offset=(" + offset.__str__() + ")")
    res = p['package']['fenceV'].fence(strin,fmark,bmark,int(offset))
    # if status not 0 nok else clip,fpos
    ##po--("res=(" + res.__str__() + ")")
    if (res[2] <> 0):
        p['sy']['push'](p['NOK'])
    else:
        p['sy']['push'](res[1]) # clip
        p['sy']['push'](res[0]) # fpos
        p['sy']['push'](p['OK'])
    #
#end fenceV