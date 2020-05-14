"""
file csv2.py
pja 5/7/2020 

convert csv files into:
SPO 3-point snowflake array
ProAr 6 point snowflake array
returns (SPO,ProAr)

test as

import useLib
import csv2
box = csv2.main()

"""


import spoRtns
spoRtns.spoInit()
spoPlus = spoRtns.spoPlus
import ProfileRtns
global profileRtns
profileRtns = ProfileRtns
def getspo():
    global SPO
    return(spoRtns.getspo())
#
def main():
    global profileRtns
    profileRtns.ProfileInit()
    fn = raw_input('csv filename? ')
    fh = open(fn,'r')
    l1 = fh.readline()
    ca1 = l1.split(',')
    # best KRI in ca1
    KRID = bestKRI(ca1)
    ri = 0 # row number
    cx = 1
    while (cx == 1 ):
        print('')
        r1 = fh.readline()
        if (r1 == ''):
            cx = -1
        else:
            ri = ri +1
            r11 = r1.split(',')
            KRID = int(KRID)
            if (KRID == -1):
                kri = 'KRI:' + "ROW" + ':' + ri.__str__()
            else:
                kri = 'KRI:' + ca1[KRID] + ':' + r11[KRID]
            #endif krid
            spoPlus("ROW",ri.__str__(),kri)
            profileRtns.ProfilePlus("ROW",ri.__str__(),"KRI","*",kri)
            spoPlus("ATN", "(" + 'row::'+ri.__str__()+")" ,kri )
            profileRtns.ProfilePlus("ATN","(" + 'row::'+ri.__str__()+")","KRI","*",kri)
            spoPlus(kri, "ATN", "(" + 'row::'+ri.__str__()+")" )
            profileRtns.ProfilePlus("KRI", kri, "ATN" ,'row', ri.__str__() )
            s = 0
            for m in r11:
                m = m.rstrip(' \t\r\n')
                m = m.lstrip(' \t\r\n')
                if (m <> ''):
                    spoPlus("NAME" , m , kri )  
                    profileRtns.ProfilePlus("NAME",m,"KRI","*",kri)
                    spoPlus(ca1[s],m,kri)
                    profileRtns.ProfilePlus("COL", ca1[s], "CELL@KRI" ,m,kri)
                    spoPlus(m,ca1[s],kri)
                    profileRtns.ProfilePlus("CELL", m, "COL@KRI" ,ca1[s],kri)
                    spoPlus(kri,ca1[s],m)
                    profileRtns.ProfilePlus('KRI',kri,"COL@CELL", ca1[s],m)
                    spoPlus(kri,"ATN", "(" + ca1[s] + "::" +m +")")
                    profileRtns.ProfilePlus("KRI",kri,"ATN",ca1[s],m)
                    print('KRI:' + ca1[KRID] + ':' + r11[KRID] + ' row' + ri.__str__() + ' ' + ca1[s] + ' ' + m)
                #endif m
                s = s + 1
            #
        #endif r1
    #wend

    fh.close()
    return(getspo(),profileRtns.getProAr())
#end main

def bestKRI(ca1):
    KRID = 'unknown'
    look = 0
    attr = {}
    for s in range(len(ca1)-1):
        p = ca1[s]
        t = p.find(':')
        if (t <> -1):
            p = p[t+1:]
        else:
            nop =1
        #endif
        attr[p]=s
    #endfor
    print('attr')
    print(attr)
    print('/attr')
    try:
        if (look == 0):
            jk = attr['IDENTIFIER'] 
            KRID = jk
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['ID'] 
            KRID = jk
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['NAME']
            KRID = jk
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    try:
        if (look == 0):
            jk = attr['ROW'] 
            KRID=-1
            look = 1
    except:
        nop = 1
    finally:
        nop = 1
    #endtry
    print('KRID=' + KRID.__str__())
    return(KRID)
#

