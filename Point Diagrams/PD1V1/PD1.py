# file PD1.py
# turing-church point graph reader
# pja 02-27-2015 - split main into main, main2
# pja 02-20-2015 added code for PHPPDX
""" test
import PD1
rec = PD1.main()
pd2Test.txt
proj,j = PD1.PHPPDX(rec)
fh = open("_"+proj+'.html','w')
fh.write(j)
fh.close()
"""
# composes records for work engine
# bnf  keys "litteral token" ; <<variable token>> [repeating group]; {optional group} ; $subTopic ; .=end of  topic; 
# $begin::
# "<project>"  <<projectname>>  "</project>" $cellLoop .
# $cellLoop::
#  [  ?-="@endend"  <<cellnum>>  $oploop ] /* repeat till @endend */
# $opLoop::
#  <<op>> "--" {"-"}">" cellnum2 {x,//} ]+
#                                                      //calledCell//returnCell// --> returnCell
#                        calledCell ... statements --> nn endCall --> -90 x 
#     cellA.cellB =no side of cellA -->
#    .endend
#
# record format cell,op,yesCell,NoCell
#
# pja 4/30/12 original
# pja 5/1/12 added default noCell to record
# pja 7/27/12 added comments logic
# pja ------- renamed file to PD1.py
# pja 10-17-2012 added validation of cell must be num or "endCall"
# ---------------return is reserved word
def PHPPDX(rec):
    """ returns a string in PHP PDX format ##point-cell=(( c-v ,+ ));; """
    j = """ <html><HEAD><title> %proj% </title></HEAD>
                  <BODY>
                  ::screenName-%proj%;;
        """
    lrec = sorted(rec.keys()) # ease of work
    for m in lrec:
        print('m=',m)
        if (m == 'fina'):
            nop = -1
        elif (m == 'project'):
            proj = rec[m]
        else:
            cl = rec[m]['cell']
            clx = int(cl)
            if (1 < clx):
                yc = rec[m]['yesCell']
                nc = rec[m]['noCell']
                op = rec[m]['op']
                print('rec ',cl,yc,nc,op)
                j = j +   "##point-"+cl+"=(( cell = "+cl+ " ,"
                j = j +   " yesCell = " + yc + " , "
                j = j +   " noCell = " + nc + " , "
                # check op
                if (rec[m]['op'][0] == "$"):
                    # litteral
                    j = j +   " op = " + '"' + rec[m]['op'][1:] + '" ));; \n'
                else:
                    j = j +   " op = " + rec[m]['op'] + ' ));; \n'
                #endif
            else:
                nop = -1
            #endif
        #endif
    #end for
    j = j + '</BODY></HTML>'
    j = j.replace('%proj%',proj)
    return(proj,j)
#end PHPPDX
        
def main():
     # ask file name
    fina = raw_input("Script file name? ")
    rec = main2(fina)
    return(rec)
#end main
def main2(fina):
    global rec
    rec = {}
    versionn = "PD v.2012.10.17"
    print("PD1 version: " , versionn) # tell me the version
    rec['fina'] = fina # save file name
    fh = open(fina,'r')
    import fioiClass
    k = fioiClass.fio(fina)
    # read till <project>
    c = 0
    while (c == 0):
        m = getword(k)
        if (m.upper() == '<PROJECT>'):
            c = -1
        #endif
        print('point loop1.a ')
    #wend
    pjna = getword(k)
    rec['project'] = pjna
    # read till </project>
    c = 0
    while (c == 0):
        m = getword(k)
        if (m.upper() == '</PROJECT>'):
            c = -1
        #endif
        print('point loop1.b ' + pjna )
    #wend
    loop1(k)
    print("point 1 ")
    return(rec)
# end main2

def loop1(k):
    # get cellnum // loop2 tail .
    # or cell.cell fill no side // loop2 tail.
    # or /* comment text */
    # or @endend
    global rec
    c = 0
    while(c==0):
        tt = getword(k)
        print('point loop1.1 ' + tt)
        p = 0
        try:
            zx = tt.index('.')
        except ValueError:
            p = -1
        finally:
            yx2 = 1 # nop
        #end try
        print('point loop1.c ' + p.__str__())
        if (p == 0 ):
            # cell.cell
            mo = tt.index('.')
            c1 = tt[0:mo]
            print ('c1=(' + c1 + ")")
            c2 = tt[mo+1:]
            print ('c2=(' + c2 + ")")
            print('rec et' + rec.__str__())
            print('rec-c1-a' + rec[c1].__str__())
            # write no side
            rec[c1]['noCell'] = c2
            print('rec-c1(' + c1 + ")(" + rec[c1].__str__() + ")")
            print('rec-c1-b' + rec[c1].__str__())
            # reset tt
            tt = c2
            newrec(tt)
            loop2(k,tt)
        elif (tt == '/*'):
            while (tt != "*/"):
                tt = getword(k)
                print("/*="+tt)
            #wend
        elif (tt.upper() == "@ENDEND"):
            c = -1
        else:
            # test id cell is num or "ret" abort otherwise
            testCell(tt)
            newrec(tt)
            loop2(k,tt)
        #endif
    #wend
# end loop1
def loop2(k,tt):
    # get [op --> cellnum2 {x,//} ]+
    # or /* -- */
    global rec
    c = 0
    while (c==0):
        op = getword(k)
        print('point loop2.a ' + op )
        if (op.upper() == "X"):
            print('do x')
            c = -1
            ans = rec
        elif (op == "//"):
            print('do //')
            c = -1
            ans = rec
        elif (op == '/*'):
            print('do comment')
            while (op != '*/'):
                op = getword(k)
                print("/*=" + op)
            #wend
        else:
            print('do rec')
            testOp(op) # op can not be numeric
            arow = getword(k)
            print("arow=" + arow)
            newcell = getword(k)
            testCell(newcell)
            rec[tt]['op'] = op
            rec[tt]['yesCell'] = newcell
            rec[tt]['noCell'] = '-99' # default
            print("rectt--------", rec[tt])
            print('point loop2.1 ' + rec[tt].__str__())
            tt = newcell
            newrec(tt)
        #endif
    #wend
# end loop2

def getword(k):
    ans = k.fpword()
    print('getword=(' + ans.__str__() + ")")
    return(ans[1])
#end getword

def newrec(k):
    """ if rec[k] does not exist create it """
    global rec
    try:
        sx = rec[k]
    except KeyError:
        rec[k] = {}
        rec[k]['cell'] = k
#end newrec
def testCell(cno):
    if (cno.upper() == 'ENDCALL'):
        ans = -1 # folderall
    elif (cno.upper() == "@ENDEND"):
        ans = -1
    else:
        try:
            ans = float(cno) # will fail if not num
        
        except:
            print("cell " + cno.__str__() + " MUST be numeric [ bad op? endCall? ]- failure to follow")
            m = 12/0 # fails
        else:
            x = 1 # nop
        finally:
            x = 1 # nop
        #end try
    #endif
#end testCell
def testOp(op):
    try:
        j = float(op)
    except:
        x = 1 # nop
    else:
        print('op (' + op + ') can NOT be numeric [preceeding x ?]- failure to follow')
        m = 12/0 #fails
    finally:
        x = 1 # nop
    #end try
# end testOp
    
    
                  
