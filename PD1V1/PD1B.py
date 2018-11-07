# copy # file PD1Builder.py
# notes
# if "__" op and v__op exists -->  copy for package
#                  and v__op not exist -->  new for package
# if "=="op --> buildEQEQ 
# if "//" op --> build callbox
# if "$op --> build lit 
# otherwise op --> build vector
# pja 7-7-2013 added output path 
#------------------ "_" = UB
#------------------ "\" = BS
# pja 7-17-2013 added out path to call boxes
# ----------------- added manifest file
# ------------------ added "[" = OX
# ------------------- "]" = CX
# pja 9-21-2013 added project name to callbox to avoid collisions of merged projects
# ===============================================================
def main(rec):
    """ format rec.cell , .yesCell, {.noCell} , .op """
    # ask output path
    global outpath
    outpath = raw_input("output path/? ")
    versionn = 'PD1B v.7-17-2013 1300'
    print(versionn)
    global loggAr
    loggAr = [] # logging array for manifest report
    d3q = '"""'
    import PDTemplates # structure # 0919 changed name to PDTemplates
    tt = PDTemplates.main() # local copies # 0919
    print("template version " + tt['version'].__str__())
    import time
    ptime = time.ctime()
    import shutil # copy functions
    # set 0 level sections
    section5 = tt['sec5']
    # read project name
    pname = rec['project'] # class
    fina = rec['fina'] # original point diagram file
    # assemble level 1 sections
    # 1
    section1 = tt['sec1']
    section1 = section1.replace('%class%',pname)
    section1 = section1.replace('%3q%',d3q)
    section1 = section1.replace('%time%',ptime)
    section1 = section1.replace('%fina%',fina)
    # 3
    section3 = tt['sec3']
    section3 = section3.replace('%class%',pname) # 0919 added testbed to PDTemplates
    # 3a
    section3a = tt['sec3a']
    section3a = section3a.replace('%class%',pname)
    # 6
    section6 = tt['sec6']
    section6 = section6.replace('%class%',pname)
    # set level 2 sections
    section2 = ''
    section4 = ''
    for df in rec.keys():
        print('rec=df',rec[df].__str__())
        if (df == 'project'):
            rd = -1 # nop
        elif (df == 'fina'):
            rd = -1 # nop
        elif (df.upper() == 'ENDCALL'):
            rd = -1
        else:
            tx = int(rec[df]['cell'])
            print('tx=',tx)
            if (0 < tx ):
                # 2 cell
                t2 = tt['sec2']
                t2 = t2.replace('%cell%',rec[df]['cell'])
                t2 = t2.replace('%class%',pname)
                section2 = section2 + t2
                # 4 rec class cell yesCell noCell op
                t4 = tt['sec4']
                t4 = t4.replace('%rec%',rec[df].__str__())
                t4 = t4.replace('%class%',pname)
                t4 = t4.replace('%cell%',rec[df]['cell'])
                t4 = t4.replace('%yesCell%',rec[df]['yesCell'])
                t4 = t4.replace('%verb%',rec[df]['op'])
                t4 = t4.replace('%noCell%',rec[df]['noCell'])
                section4 = section4 + t4
            #endif
        #endif
    #end for
    # add vectors
    section3 = section3 + '\n'
    jf = {}
    for af in rec.keys():
        try:
            px = rec[af]['op']
        except:
            xx = -1 # nop
        else:
            # convert nonalpha verb tokens
            verbt = rec[af]['op']
            verbt = verbt.replace('/','SL')
            verbt = verbt.replace("\x5C",'BS')
            verbt = verbt.replace(':','CL')
            verbt = verbt.replace('.','DT')
            verbt = verbt.replace(' ','SP')
            verbt = verbt.replace('=','EQ')
            verbt = verbt.replace('"','QT')
            verbt = verbt.replace('<','LT')
            verbt = verbt.replace('[','OX')
            verbt = verbt.replace(']','CX')
            verbt = verbt.replace('!','BG')
            verbt = verbt.replace('>','GT')
            verbt = verbt.replace('@','AT')
            verbt = verbt.replace('$','DL')
            verbt = verbt.replace('#','PN')
            verbt = verbt.replace('%','PC')
            verbt = verbt.replace('*','AS')
            verbt = verbt.replace('+','PL')
            verbt = verbt.replace('-','NG')
            verbt = verbt.replace('?','HK')
            verbt = verbt.replace('(','OP')
            verbt = verbt.replace(')','CP')
            verbt = verbt.replace('_','UB')
            verbt = verbt.replace(',','CM')
            verbt = verbt.replace(';','SI')
            jf[ rec[af]['op']] = {}
            jf[ rec[af]['op']]['op'] = rec[af]['op']
            jf[ rec[af]['op']]['verbt'] = verbt
            # discover if this is a callbox verb or test
            tcc = 0
            try:
            	mx = verbt.index('SLSL') 
            	if (mx == 0):
            	    tcc = 1
            	#endif
            except:
                tcc = 0
            finally:
                nop = 0
            #end try
            jcc = tcc
            try:
            	mx = verbt.index('DL') 
            	if (mx == 0):
            	    tcc = tcc + 2
            	#endif
            except:
                tcc = jcc
            finally:
                nop = 0
            #end try
            jcc = tcc
            try:
            	mx = verbt.index('EQEQ') 
            	if (mx == 0):
            	    tcc = tcc + 4
            	#endif
            except:
                tcc = jcc
            finally:
                nop = 0
            #end try
            jcc = tcc
            try:
            	mx = verbt.index('UBUB') 
            	if (mx == 0):
            	    tcc = tcc + 8
            	#endif
            except:
                tcc = jcc
            finally:
                nop = 0
            #end try
            if (tcc == 1):
            	makeCallbox(tt,verbt,rec[af]['op'],pname) # if SLSL *9-21-13
            	loggAr.append ("Callbox - " + pname + "_" + verbt ) # * 9-21-13
            elif (tcc == 2 ):
                makeLit(tt,verbt,rec[af]['op']) # if DL
                loggAr.append ("Literal - " + verbt )
            elif (tcc == 4 ):
                makeEQEQ(tt,verbt,rec[af]['op']) # if ==op
                loggAr.append ("EQEQ - " + verbt )
            elif (tcc == 8 ):
                makeVector(tt,verbt)
            else:
                makeVector(tt,verbt)
            #endif
    #end for
    for jfc in jf.keys():
        section3b = tt['sec3b']
        section3b = section3b.replace('%verb%',jf[jfc]['op'])
        # * 9 21 13
        if (jf[jfc]['verbt'][:4]  == "SLSL" ) : # callbox * 9-21-13
            section3b = section3b.replace('%verbt%',pname + '_' + jf[jfc]['verbt']) # call box has projectName_verbT #* 9-21-13
        else:
            section3b = section3b.replace('%verbt%',jf[jfc]['verbt'])
        #endif # * 9-21-13
        section3 = section3 + section3b
    #end for
            
    #             
    # open outfile
    outf = open(outpath + pname + '.py','w')
    # write sections to file
    outf.write(section1)
    outf.write(section2)
    outf.write(section3)
    outf.write(section3a)
    outf.write(section4)
    outf.write(section5)
    outf.write(section6)
    outf.close()
    # write manifest
    outm = open(outpath + "Manifest_" + pname + '.txt','w')
    loggAr = sorted(loggAr)
    for a in loggAr:
        outm.write(a + '\n')
    #end for
    outm.close()
#end main

def makeVector(tt,verbt):
    # if vector file does not exist write out the base code 
    # if it does exist write a copy for the package
    import shutil
    global outpath
    global loggAr
    try:
        fv = open('v_'+verbt+'.py','r')
        cc = 1 # exists
    except:
        cc = -1 # not xists 
    finally:
        nop = -1
    #end try
    if (cc == 1):
        print('open-r' + verbt )
        # exists so copy for package
        print("copy of " + verbt)
        shutil.copy('v_'+verbt+'.py' , outpath + 'v_' + verbt + '.py' )
        loggAr.append("Known verb " + verbt )
    else:
        print("new vector for (" + verbt + ")")
        loggAr.append("NEW verb " + verbt )
        # write base file from template
        print('open-w1')
        m = outpath + 'v_'+ verbt + '.py'
        print('test','m=',m)
        fv = open(m,'w')
        print('open-w2')
        lv = tt['vector']
        lv = lv.replace('%vector%',verbt)
        # print("test",'lv=',lv)
        fv.write(lv)
    #endif
	fv.close()
	print('close')
# end makeVector

def makeLit(tt,verbt,Strin):
    global outpath
    # write out the base code
    print("LitBox for (" + verbt + ")")
    # write base file from template
    fv = open(outpath + 'v_'+verbt+'.py','w')
    print('open-w')
    lv = tt['Lit']
    lv = lv.replace('%vector%',verbt)
    lv = lv.replace('%Lit%',Strin[1:]) # $xxx
    # print("test",'lv=',lv)
    fv.write(lv)
    fv.close()
    print('close')
# end makeLit

# eq for EQxx vectors (%vector%, %vval%)
def makeEQEQ(tt,verbt,orgVerb):
    global outpath
    print("eqeq for " + orgVerb)
    # remove == from op 
    vv = orgVerb[2:]
    # exception is space
    if (vv == 'space'):
        vv = ' '
    #endif
    fv = open(outpath + 'v_'+ verbt +'.py','w')
    print('open-w')
    lv = tt['eq']
    lv = lv.replace('%vector%',verbt)
    lv = lv.replace('%vval%',vv) # $xxx
    print("test",'lv=',lv)
    fv.write(lv)
    fv.close()
    print('close')
#end makeEQEQ

def makeCallbox(tt,verbt,orgVerb,projectName): # *-9-21-13
    global outpath
    # if vector file does not exist write out the base code
    print("CallBox for (" + verbt + ")")
    b1 = orgVerb[2:]
    b2 = b1[b1.index('//')+2 :] 
    b3 = b1[:b1.index('//')]
    fv = open(outpath + 'v_' + projectName+ "_" + verbt+ '.py' , 'w') # * 9 21 13 
    print('open-w')
    # get returnCell
    returnCell = int(b2[:-2]) 
    # get gotoCell
    gotoCell = int(b3)
    lv = tt['callbox']
    lv = lv.replace('%vector%',verbt)
    lv = lv.replace('%project%',projectName) # * 9-21-13
    lv = lv.replace('%returnCell%',returnCell.__str__())
    lv = lv.replace('%gotoCell%',gotoCell.__str__())
    print("test",'lv=',lv)
    fv.write(lv)
    fv.close()
    print('close')
# end makeCallbox

    
