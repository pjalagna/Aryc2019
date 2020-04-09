## xsdParse.py
def parta():
spo = {}
' parent pop push rewrite '
parent = []
parent.append('')
pix = 0

foff = 0
soff = 0
skip = 1
fh = open('Strat.xsd','r')
xsdin = fh.read()
fh.close()

foff,r = fence(xsdin,"<",">",foff)
#loop a
while ( skip == 1):
    skip = 0
    if (r[0] == "?"):
        skip = 1
    #
    if (r[0] == "!"):
        skip = 1
    #
    if (r[0] == '/'):
        skip = 2
    #  
    if (foff == 0):
        skip = -1
    #endif
    if (skip == 0):
        soff,sd = fence(xsdin,">","<",foff-1)
        # r has sp if1
        ## yes
            # na = [0:sp]
            # doatt
            # bestid
            # spoAtt
            # // b
            skip = 1
        ## no
            # att na = r
            # att kri = r
            # spoAtt
            # // b
            skip = 1
        #endif
    #endif if1
    foff,r = fence(xsdin,"<",">",foff)
    if (skip == 2):
        soff,sd = fence(xsdin,">","<",foff-1)
        na = r[1:] #w/o /
        # last parent check
        ## yes
            # parent pop
            skip = 1
        ## no
            raw_input('point 57')
        #endif
#wend
#end parta
def partb():
    # t white(sd)
    # t has text
    ## yes
        # spo as att text=sd
    ## no
        nop = 1
    #endif
    #parent+ na:kri
    # spo(parent,child,na:kri)
#end partb


# get the chain   
foff,r = fence(xsdin,"<","</",foff)

# check name
n1 = r[0:r.index(' ')]
# if fails n1 = r

# has :
n2 = n1.index(':')
# if fails n2 = 0
na = n1[n2+1:]
# == element?
## yes
doatt
bestid
## no
##endif




#doatt
af = 0
af,ad = fence(r,' ','=',af)
# till af ==0
af1,ad2 = fence(r,'=',' ',af)
#ad = atName
#ad1 = val in quotes
af,ad = fence(r,' ','=',af)
# end till



