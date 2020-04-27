m= """ file pd2020V.py
pja 4-27-2020 fixed overwrite
pja 4-26-2020 PDC error overwrites former cell info
pja 4-25-2020

point diagram compiler (PDC) and execution (PDX) framework
format 
a) cell [[ verbs ]] --> yescell etc
b) cell [[ verbs ]] .
c) -- calling cells
-- verb = call/routineCell/returncell
-- verb = "endcall" continues at return cell
-- calls are stackable 
"""
def pdinit(p):
    from pd2020V import ckcell
    from pd2020V import setop
    from pd2020V import pdword
    from pd2020V import getop
    from pd2020V import pdlibBang
    p['sy']['push'](p['OK'])
#
def main(p,m=m):
    p['sy']['PDC'] = pdc
    p['help']['PDC'] = '(script,,) sets lib with code'
    p['sy']['PDX'] = pdx
    p['help']['PDX'] = '(startcell,,x) executes point diagram stored by PDC into lib'
    p['sy']['PDInit'] = pdinit
    p['help']['PDInit'] = '(,,) init for PDC PDX '
    return(p)
#
def pdc(p):
    global script
    # get script
    script = p['sy']['pop']()
    # get trace
    p['sy']['push']('trace')
    p['sy']['@'](p)
    p['sy']['pop']() #ok
    trace = p['sy']['pop']()
    #umbrella
    uctl = 1
    while(uctl <> 0):
        if (trace == 'step'):
            raw_input('uctl is(' + uctl.__str__() + ')')
        #endif
        if (uctl == 0):
            uctl = 0
        elif (uctl == 1):
            m1 = pdword(p)
            if (trace == 'step'):
                print('----m1 is(' + m1.__str__() + ')')
            #endif
            if (m1 == 'end'):
                uctl = 0 #end
            else:
                uctl = 3
            #
        elif (uctl == 3):
            cell = ckcell(m1,p,trace)
            if (trace == 'step'):
                print('cell is(' + cell.__str__() + ')')
            #endif
            uctl = 4
        elif (uctl == 4):
            #store cell --> 5
            #cell 'cell' cell pdlib! 
            pdlibBang(cell,'cell',cell,p,trace)
            uctl = 5
        elif (uctl == 5):
            m5 = pdword(p)
            if (m5 == '[['):
                seq = 1
                uctl = 8
            elif (m5 == '.'):
                uctl = 1
            else:
                raw_input('expected "[[" in script(' + script +") will exit")
                exit
            #endif
        elif (uctl == 8):
            #pdword =]]->10 , setop seq++ ->8
            m8 = pdword(p)
            if (trace == 'step'):
                print('m8 is(' + m8.__str__() + ')')
            #endif
            if (m8 == "]]"):
                uctl = 10
            else:
                #setop seq++ ->8
                setop(cell,seq,m8,p)
                seq = seq + 1
                uctl = 8
            #endif
        elif (uctl == 10):
            m10  = pdword(p)
            if (trace == 'step'):
                print('m10 is(' + m10.__str__() + ')')
            #endif
            if (m10 == '.'):
                uctl = 1
            else:
                #word,save-yescell,cell=yescell -> 4
                m10a = pdword(p)
                pdlibBang(cell,'yescell', m10a, p, trace)
                cell = m10a
                if (trace == 'step'):
                    print('cell is(' + cell.__str__() + ')')
            #endif
                uctl = 4
            #endif
        else:
            raw_input('uctl unknown(' + uctl + ') will exit')
            exit
        #endif
    #wend
    p['sy']['push'](p['OK'])
#
def pdx(p):
    # get trace
    p['sy']['push']('trace')
    p['sy']['@'](p)
    p['sy']['pop']() #ok
    trace = p['sy']['pop']()
    #(cell,,x)
    cell = p['sy']['pop']()
    seq = 1
    pctl = 1
    while(0 < int(pctl)):
        if (trace == 'step'):
            print('cell is(' + cell.__str__() + ')')
            print('seq is(' + seq.__str__() + ')')
            raw_input('pctl is(' + pctl.__str__() + ')')
        #endif
        if (int(cell) < 0):
            pctl = cell
        elif (pctl == 1):
            status,mpdx = getop(cell,seq,p)
            if (trace == 'step'):
			    print('----mpdx is(' + mpdx.__str__() + ')')
			    print('----status is(' + status.__str__() + ')')
			#endif 
            if (status <> 0 ): # fail-> yescell #if-1
                try:
                    cell = p['l'][cell]['yescell']
                except:
                    cell = -99
                finally:
                    nop = 1
                #endytry
                seq = 1
                pctl = 1
            else: #if-1
				if (mpdx[0] == '"'):
					p['sy']['push'](mpdx[1:-1]) 
					seq = seq +1 
					pctl = 1
				elif (mpdx[0] == "'"):
					p['sy']['push'](mpdx[1:-1]) 
					seq = seq +1 
					pctl = 1
				else:
					pctl = 2 #n->p2
				#endif
			#endif-1
        elif (pctl == 2):
            pxstatus = 0
            #p2 mpdx has 'call'?
            try:
                jj = mpdx.index('call/')
                pctl = 5 # y -> p5;
                pxstatus = 1 
            except:
                nop =1
            finally:
                nop = 1
            #
            #has 'endcall'?->p6
            try:
                jj = mpdx.index('endcall')
                pctl = 6 # 
                pxstatus = 2 
            except:
                nop =1
            finally:
                nop = 1
            #
            if (pxstatus == 0): 
                pctl = 3 # no->p3
            #endif
        elif (pctl == 3):
            #p3 .x pass -> p1 
            #fail-> cell = nocell ->p1
            try:
                p['sy'][mpdx](p)
                st = p['sy']['pop']()
                if (trace == 'step'):
                    raw_input('3-st is(' + st.__str__() + ')')
                #endif
                if (st == p['OK']):
                    seq = seq + 1
                    pctl = 1
                else:
                    cell = p['l'][cell]['nocell']
                    seq = 1
                    pctl = 1
                #endif
            except:
                #cell = nocell seq = 1
                cell = p['l'][cell]['nocell']
                seq = 1
                pctl = 1
            finally:
                nop =1
            #endtry
        elif (pctl == 5):   
            #p5 call/box/ret split at '/' 
            # cell = box, r< = ret -> p1
            x,cell,ret = mpdx.split('/')
            p['r'].append(ret)
            seq = 1
            pctl = 1
        elif (pctl == 6):
            #p6 cell = r> -> p1
            cell = p['r'].pop()
            seq = 1
            pctl = 1
        else:
            if (trace == 'step'):
                    print('PDX done')
                #endif
        #endif
    p['sy']['push'](p['OK'])
#
           
# private rtns           
def ckcell(m1,p,trace): # (m1,,cell) sets nocell -> cell
    if (trace == 'step'):
        print('ckcell-m1 is(' + m1.__str__() + ')')
    #endif
    st = 0
    try:
        mc = m1.index('.')
        op1 = m1[0:mc]
        op2 = m1[mc+1:]
        cell = op2
        st = 1
    except:
        cell = m1
        st = 0
    finally:
        nop = 1
    #endtry
    if (st == 1):
        #set nocell
        pdlibBang(op1 ,'nocell', op2 ,p,trace)
    #
    return(cell)
#
def pdword(p):
    # remove word from script 
    global script
    # push script x word pop ok
    p['sy']['push'](script)
    p['sy']['word'](p)
    p['sy']['pop']() # ok
    wd = p['sy']['pop']()
    script = p['sy']['pop']()
    return(wd)
#
def setop(cell,seq,val,p):
    # get lib
    l = p['l']
    try:
        m= l[cell]
    except:
        l[cell] = {}
    finally:
        nop = 0
    #endtry
    try:
        m= l[cell]['op']
    except:
        l[cell]['op'] = {}
    finally:
        nop = 0
    #endtry
    l[cell]['op'][seq]=val
#

def getop(cell,seq,p): 
    try: 
        ans =  p['l'][cell]['op'][seq]
        status = 0
    except:
        ans = ''
        status = -1
    finally:
        nop = 1
    #endtry
    return(status,ans)
#
def pdlibBang(op1 ,name, op2 ,p,trace):
    if (trace == 'step'):
        print('pdlibBang(op1 is(' + op1.__str__() + ')')
        print('pdlibBang(name is(' + name.__str__() + ')')
        print('pdlibBang(op2 is(' + op2.__str__() + ')')
    #endif
    # p['l'][op1][name] = op2
    # get lib
    l = p['l']
    try:
        m= l[op1]
    except:
        l[op1] = {}
    finally:
        nop = 0
    #endtry
    try:
        m= l[op1][name]
        l[op1][name] = op2 # rewrite
    except:
        l[op1][name] = op2
    finally:
        nop = 0
    #endtry
#
"""
test as 
import useLib
import bbox
bbox.main('bmain')
bbox.start('step')
'pd2020V'
takeV
PDInit
l0
{{
2 [[ "0" "e" ! ]] --> 4 .
4 [[ 'test 2' msg "e" @ "0" <> ]] --> 5 .
4.6 [[ 'at 6' msg "1" "e" ! ]] -----> 4 .
5 [[ 'at 5' msg call/200/-99 ]] .
200 [[ 'here at 200' msg endcall ]] .
end 

}}
PDC
2
PDX





"""