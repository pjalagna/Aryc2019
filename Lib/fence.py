"""
file fence.py
pja 04-08-2020 

clips a string from front mark to end mark exclusive
returns an array:
-- first position of found front marker
--- if front marker not found position 0 is used
--- if end marker is not found length is used
-- clipped string [1]
-- status in [2]
--- 0 =ok
--- 1 = front marker defaulted
--- 2 = back marker defaulted
--- 3 = both markers defaulted 
test as
import fence
jj = 'once upon a time '
a = fence.fence(jj,'n',' ')
-- (2, 'ce', 0) jj[2]='c'
b = fence.fence(jj,'n',' ',a[0])
-- (9, '', 0) jj[9:] =' a time ' 
c = fence.fence(jj,'n',' ',a[0]+1)
-- (9, '', 0)
d = fence.fence(jj,'n',' ',b[0]+1)
-- (0, 'once', 1) note status=1

"""
def fence(strin,fmark,bmark,foff=0):
    status = 0
    try:
        fo = strin.index(fmark,foff)
        fo = fo+len(fmark)
    except:
        fo = 0
        status = status + 1
    finally:
        nop = 1
    #
    try:
        bo = strin.index(bmark,fo)
    except:
        bo = len(strin)
        status = status + 2
    finally:
        nop = 1
    #
    ans = strin[fo:bo]
    return(fo,ans,status)
#