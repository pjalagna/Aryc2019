# file tword.py
"""
tokenizer for strings
pja - 4/9/2014 - org

test
import tword
fh = open('f2.txt', 'r')
strin = fh.read()
fh.close()
r = tword.white(strin)
w,r = tword.tword(r)
w,r = tword.ctill(r,';') # doesn't return ';'


"""
def white(strin):
    c = 0
    ii = 0
    while (c==0):
        if (strin.__len__() < ii):
            c = -1
        elif (strin[ii]== ' '):
            c = 0
            ii = ii + 1
        elif (strin[ii] == '/' and strin[ii+1] == "*"):
            ii = strin.index('*/') + 2
            c = 0
        elif (strin[ii] == '\n'):
            c = 0
            ii = ii + 1
        elif (strin[ii] == '\t'):
            c = 0
            ii = ii + 1
        else:
            c = 1 # stop if not found
        #end if
    #wend
    if ( c == -1): # eol
        ans = '\03' # nok
    else:
        ans = strin[ii:]
    #endif
    return(ans)
#white
def ctill(strin,marks):
    # does NOT return ending mark
    c = 0
    mark = minmark(strin,marks) # symbol of first mark
    if (mark == '\03'):
        c = -1 # no marks found
    else:
        ii = strin.index(mark)
    #endif
   
    if ( c == -1): # eol
        ans = ['\03',''] # nok
    else:
        ans = [strin[0:ii], strin[ii+1:] ]
    #endif
    return(ans)
#white
def tword(strin):
    rest = white(strin)
    if (rest[0] == '"'):
        bo = reat.index('"')
        w = rest[:bo]
        r = rest[bo+1:]
        ans = []
        ans.append(w)
        ans.append(r)
    else:
        ans = ctill(rest," \n\t")
    #endif
    return(ans)
#end tword
def minmark(strin,marks):
    mm = strin.__len__() + 1
    tt = mm
    for i in marks:
        try:
            j = strin.index(i)
            if (j < mm):
                mm = j
                ansx = i
            #endif
        except:
            nop = 1
        finally:
            nop = 1
        #end try
    #end for
    if (j == tt): # no marks found
        ans = '\03' # nok
    else:
        ans = j
    #endif
    return(ansx)
#end minmark
def find(strin,mark):
    try:
        fo = strin.index(mark)
        ans = fo
    except:
        ans = -1
    finally:
        nop = 1
    #end try
    return(ans)
#end find

        
    
