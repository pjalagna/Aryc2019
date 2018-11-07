# file unpack
def xml1(target,string,startPos):
    """ type1 - unpacks simple xml statements <x> text </x> \n
         no attributes, no subsections \n
         returns text if <x> exists otherwise \3
    """
    fos = "<" + target + ">"
    bos = "</" + target + ">"
    try:
        fo = string.index(fos,startPos)
        e = 0
    except:
        e = -1
    finally:
        nop = -1
    #end try
    if(e==0):
        bo = string.index(bos,fo)
        fop = fo + len(target) + 2
        ans = string[fop:bo]
    else:
        ans = '\3'
    #end if
    return(ans)
#end xml1

    
