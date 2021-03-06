# prefix: ##- postfix: -##
##- template doVerb.init
##- (4) p['sy']['%sym%'] = vector
##- (4) p['help']['%sym%'] = "%desc%" -##
##- template doVerb.py:codespace 
##- (0) %code% -##
m = """
#file doVerb.py
pja 8-20-2020 added upper,lower
pja 6-26-2020 dumpNDS to .n
pja 6-11-2020 added trim
pja 4-30-2020 fixed pick
pja 4-28-2020 added lib#, changed l0 to lib0
pja 04-25-2020 added l0 clear lib
pja 04-23-2020 added tillNor, lib@, lib!
-------------- "find" fails if needle not found
pja 04-21-2020 added tillor
pja 04-12-2020 added .l,l@,l!,.l? and rwd
-------------- added loadCode w/ code + :: + name
-------------- added protected
pja 04-09-2020 added .r,r#,r<,r>
pja 04-07-2020 added cx
pja 03-30-2020 added @?, cleaned dumpNDS
pja 03-29-2020 set up for sections
pja 03-27-2020 fixed @++
pja 03-09-2020 added verb?
pja 03-06-2020 added c1 , woB , isnum?, Q?, T?, <Lt >Gt DT
---- fixed wword BUT won't take comments
pja 02-18-2020 added p['object'] see objectProfile.txt
pja 02-15-2020 edited packages
pja 02-10-2020 added package and packages verbs
pja 02-05-2020 added crlf verb
pja 01-31-2020 added ch0 verb
pja 01-30-2020 added word verb 
pja 01-08-2020 added inp verb
-------------- added .X verb
pja 12-29-2019 edited att==@ to return '' on nos
pja 12-27-2019 redid this header block
               added ?space after msg inverb ask
               added takeV - imports vector files
# pja 3/9/2018 - added swap, drop, elipsis, dup roll depth
# -------- integer math:  mdas pwr root mod @++ @-- @0
# -------- str:  cat, cats, len find split 
# pja 2/10/2018 - added ask
# pja 2/8/2018

"""

def init(p,m=m):
    # load symbol table with all preset verbs
    #       symbol   verb
    p['object'] = {} # set up object profile see ObjectProfile.txt
    p['help']={} #set up help array
    p['package']={} #set up package array
    p['package']['doVerb'] = m
    p['sy']['packages'] = packages
    p['help']['packages'] = "(,,) displays installed packages "
    p['sy']['package'] = package
    p['help']['packages'] = "(name,,) displays installed packages help"
    p['sy']['help?'] = helphook
    p['sy']['.n'] = ndsOut
    p['sy']['verbs'] = vocab
    p['sy']['takeV'] = takeV
    p['sy']['msg'] = msg
    p['sy']['='] = eq
    p['sy']['<>'] = neq
    p['sy']['!'] = bang
    p['sy']['@'] = att
    p['sy']['depth'] = depth
    p['sy']['ask'] = ask
    p['sy']['inp'] = inp
    p['sy']['tail.'] = tail
    p['sy']['drop'] = drop
    p['sy']['drops'] = drops
    p['sy']['swap'] = swap
    p['sy']['dup'] = dup
    p['sy']['roll'] = roll
    p['sy']['...'] = elipsis
    p['sy']['cat'] = cat
    p['sy']['cats'] = cats
    p['sy']['word'] = wword
    p['sy']['len'] = length
    p['sy']['+'] = mplus
    p['sy']['-'] = mminus
    p['sy']['/'] = mdiv
    p['sy']['*'] = mmul
    p['sy']['**'] = mpwr
    p['sy']['-**'] = mroot
    p['sy']['mod'] = mmod
    p['sy']['++'] = mplusplus
    p['sy']['--'] = mminusminus
    p['sy']['@++'] = mattplusplus
    p['sy']['@--'] = mattminusminus
    p['sy']['@0'] = mattzero
    p['sy']['find'] = find
    p['sy']['split'] = split
    p['sy']['.X'] = dox
    p['help']['help?'] = "(name,,) displays help about name"
    p['sy']['verb?'] = verbHook
    p['help']['verb?'] = "(name,,) ok if names exists as verb nok if not"
    p['help']['.n'] = "displays NDS"
    p['help']['verbs'] = "(,,) lists current verbs alphabetically "
    p['help']['takeV'] = "({options},name,,) imports V files"
    p['help']['msg'] = "(txt,,) displays txt"
    p['help']['='] = "(op1,op2,,) sets ok if op1=op2"
    p['help']['<>'] = "(op1,op2,,) sets ok if op1 != op2"
    p['help']['!'] = "(v,name,,) stores into NDS [name] = v "
    p['help']['@'] = "(name,,v) retrives v from NDS[name]"
    p['help']['depth'] = "(,,c) count of elements in data stack"
    p['help']['ask'] = "(txt,,ans) enquires of keyboard "
    p['help']['inp'] = "(,,ans) input from keyboard"
    p['help']['tail.'] = "tail recursion at specified paragraph"
    p['help']['drop'] = "(m,,) removes curent TOS of data stack"
    p['help']['drops'] = "([m],,) removes ALL data on stack"
    p['help']['swap'] = "(a,b,,a,b) reverses 2 topmost elements"
    p['help']['dup'] = "(a,,a,a) duplicates"
    p['help']['roll'] = "(a,b,c,,c,b,a)"
    p['help']['...'] = " continues to next clause"
    p['help']['cat'] = "(a,b,,ab) concatenate "
    p['help']['cats'] = "(a,b,,a b) concatenate with space"
    p['help']['word'] = "(txt,,rest,w) splits txt at space "
    p['help']['len'] = "length of TOS onto TOS"
    p['help']['+'] = "(a,b,,a+b) addition"
    p['help']['-'] = "(a,b,,a-b) subtraction"
    p['help']['/'] = "(a,b,,a/b) subtraction"
    p['help']['*'] = "(a,b,,a*b) subtraction"
    p['help']['**'] = "(a,b,,a**b) power"
    p['help']['-**'] = "(16,2,,4) inverse root"
    p['help']['mod'] = "(a,b,,a mod b) modulous"
    p['help']['++'] = "(a,,a+1) increment"
    p['help']['--'] = "(a,,a-1) decrement"
    p['help']['@++'] = "(a,,) contents of NDS[a] incremented"
    p['help']['@--'] = "(a,,) contents of NDS[a] decremented"
    p['help']['@0'] = "(addr,,) NDS[addr] = 0 "
    p['help']['find'] = "(needle,haystack,,position/-1) "
    p['help']['split'] = "(haystack,needle,,first,middle,last)"
    p['help']['.X'] = "(name,,) executes verb named "
    p['sy']['ch0'] = chzero
    p['help']['ch0'] = "(,,x0) charicter 0 to data stack"
    p['sy']['crlf'] = crlf
    p['help']['crlf'] = "(,,crlf) adds newline to stack"
    p['sy']['c1'] = c1
    p['help']['c1'] = "(word,,first) extracts first charicter from word"
    p['sy']['woB'] = woB
    p['help']['woB'] = "(QuotedWord,,word) removes quotes "
    p['sy']['isnum?'] = isnumHook
    p['help']['isnum?'] = "(x,,) fails if x not digits"
    p['sy']['Q?'] = QHook
    p['help']['Q?'] = "(x,,) fails if x not double quote charicter"
    p['sy']['T?'] = THook
    p['help']['T?'] = "(x,,) fails if x not single quote charicter"
    p['sy']['P?'] = PHook
    p['help']['P?'] = "(x,,) fails if x not period charicter"
    p['sy']['SEMI?'] = SEMIHook
    p['help']['SEMI?'] = "(x,,) fails if x not semicolon charicter"
    p['sy']['<'] = LT
    p['help']['<'] = "(a,b,,) a < b test fails if not"
    p['sy']['>'] = GT
    p['help']['>'] = "(a,b,,) a > b test fails if not"
    p['sy']['DT'] = DT
    p['help']['DT'] = "DT (,,timeStamp) "
    ##- doverb.py:init 4 -##
    p['sy']['cut'] = cut
    p['help']['cut'] = "cut string at pos (haystack,pos,,front,middle,last) "
    p['sy']['@?'] = atHook
    p['help']['@?'] = "(target,,0,nds names that contain target) "
    p['sy']['replace'] = SReplace
    p['help']['replace'] = "(haystack,needle,repStr,,replacedString) "
    p['sy']['pick'] = pick
    p['help']['pick'] = "(#,,#thItem) "
    p['sy']['cx'] = cx
    p['help']['cx'] = "cx (str,#,,str[#th] or nok ) "
    p['sy']['r<'] = rin
    p['help']['r<'] = "r< (str,,) into r stack"
    p['sy']['r>'] = rout
    p['help']['r>'] = "r< (,,str) from r stack or nok"
    p['sy']['r#'] = rpound
    p['help']['r#'] = "r# (,,str) depth of r stack"
    p['sy']['.r'] = rdump
    p['help']['.r'] = ".r (,,) dump of r stack"
    p['sy']['.l'] = dotl
    p['help']['.l'] = ".l (,,) dump of lib "
    p['sy']['.l?'] = dotlhook
    p['help']['.l?'] = ".l? (,,) list of lib names "
    p['sy']['l!'] = lbang
    p['help']['l!'] = "l! (code,name,,) enters code to lib "
    p['sy']['l@'] = latt
    p['help']['l@'] = "l@ (name,,code) get code from lib  can fail"
    p['sy']['loadCode'] = lloadCode
    p['help']['loadCode'] = " (basiiCode,,) into Lib"
    p['sy']['rwd'] = rwd
    p['help']['rwd'] = "rwd (,,word of r)"
    p['sy']['protected'] = protected
    p['help']['protected'] = "protected (cmd,,) system safe ok/nok"
    p['sy']['tillor'] = tillor
    p['help']['tillor'] = "(str,ctr,strList,,ctr') till in list ok/nok"
    p['sy']['tillNor'] = tillNor
    p['help']['tillNor'] = "(str,ctrName,strList,,str') till not in list ok/nok"
    p['sy']['lib@'] = libatt
    p['help']['lib@'] = '(r,c,,v) from lib ok/nok'
    p['sy']['lib!'] = libbang
    p['help']['lib!'] = '(r,c,v,,) into lib'
    p['sy']['lib0'] = libzero
    p['help']['lib0'] = 'reset lib'
    p['sy']['lib#'] = libkeys
    p['help']['lib#'] = 'list all cells'
    p['sy']['slice'] = slice
    p['help']['slice'] = '(bo,fo,str,,str[fo:bo])'
    p['sy']['trim'] = trimv
    p['help']['trim'] = '(str,,str) removes white space front and back'
    p['sy']['upper'] = upperV
    p['help']['upper'] = '(str,,str) converts to upper case '
    p['sy']['lower'] = lowerV
    p['help']['lower'] = '(str,,str) converts to lower case '
    return(p)
#end init
##- doverb.py:codespace 0 -##
def upperV(p):
    str = p['sy']['pop']()
    ans = str.upper()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
def lowerV(p):
    str = p['sy']['pop']()
    ans = str.lower()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
def trimv(p):
    str = p['sy']['pop']() 
    ans = trim(str)
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
def trim(str):
    str = str.lstrip(' \t\r\n')
    str = str.rstrip(' \t\r\n')
    return(str)
#
    
def libkeys(p):
    print(p['l'].keys())
    p['sy']['push'](p['OK'])
#
def slice(p):
    #'(bo,fo,str,,str[fo:bo])'
    str = p['sy']['pop']()
    fo = p['sy']['pop']()
    bo = p['sy']['pop']()
    fo = int(fo)
    bo = int(bo)
    try:
        ans = str[fo:bo]
        p['sy']['push'](ans)
        p['sy']['push'](p['OK'])
    except:
        p['sy']['push'](p['NOK'])
    finally:
        nop = 1
    #
#
def libzero(p):
    # clear lib
    p['l'] = {}
    p['sy']['push'](p['OK'])
#
def libbang(p): # (r,c,v,,)
    v = p['sy']['pop']()
    c = p['sy']['pop']()
    r = p['sy']['pop']()
    try:
        x = p['l'][r]
    except:
        p['l'][r]={}
    finally:
        nop = 0
    #
    try:
        x = p['l'][r][c]
        p['l'][r][c] = v
    except:
        p['l'][r][c]=v
    finally:
        nop = 1
    #
    p['sy']['push'](p['OK'])
#
def libatt(p):
    c = p['sy']['pop']()
    r = p['sy']['pop']()
    try:
        ans = p['l'][r][c]
        p['sy']['push'](ans)
        p['sy']['push'](p['OK'])
    except:
        p['sy']['push'](p['NOK'])
    finally:
        nop =0
    #
# end lib@
def tillor(p):
    #rint('needs work')
    #"(workStr,ctr,strList,,ctr')  ok/nok"
    strList = p['sy']['pop']()
    ctr = p['sy']['pop']()
    workStr = p['sy']['pop']()
    # -- 
    ctr = int(ctr) -1
    ctrStart = ctr
    if (ctr < len(workStr)):
        sw = 0
        while(sw == 0):
            ctr=ctr+1
            sw = 0
            #rint("work[ctr]=(" + workStr[ctr] + ")")
            for m in range(strList.__len__()):
                j = workStr[ctr]
                #rint("l-sl[m]=(" + strList[m] + ")")
                if (j == strList[m]):
                    sw = 1 #break
                #endif
                #rint("l-sw=(" + sw.__str__() + ")")
            #endfor
            #rint("sw=(" + sw.__str__() + ")")
        #wend
        p['sy']['push'](ctr)
        p['sy']['push'](p['OK'])
        # return(ctr) # test
    else:
        #push nok
        p['sy']['push'](p['NOK'])
#end tillor
def tillNor(p):
    #rint('needs work')
    #"(workStr,ctr,strList,,ctr')  ok/nok"
    strList = p['sy']['pop']()
    ctr = p['sy']['pop']()
    workStr = p['sy']['pop']()
    # -- 
    ctr = int(ctr) -1
    if (ctr < len(workStr)):
        sw = 0
        while(sw == 0):
            ctr=ctr+1
            sw = 0
            #rint("work[ctr]=(" + workStr[ctr] + ")")
            k = 0
            for m in range(strList.__len__()):
                j = workStr[ctr]
                #rint("l-sl[m]=(" + strList[m] + ")")
                if (j <> strList[m]):
                    k = k+1
                #endif
                #rint("l-sw=(" + sw.__str__() + ")")
            #endfor
            if (k == len(strList)):
                sw = 1 #break
            #endif
            #rint("sw=(" + sw.__str__() + ")")
        #wend
        p['sy']['push'](ctr)
        p['sy']['push'](p['OK'])
        # return(ctr) # test
    else:
        #push nok
        p['sy']['push'](p['NOK'])
#end tillNor
def protected(p):
    # (cmd,,) ok/nok
    cmd = p['sy']['pop']()
    try:
        p['sy'][cmd](p)
        ss = 0
    except:
        ss = -1
    finally:
        nop = 1
    #
    if (ss == 0):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #
#
    
def lloadCode(p):
    # 
    p['sy']['push']('def')
    p['sy']['push'](';')
    p['sy']['push']('0')
    p['sy']['fence'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['drop'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['word'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['push']('pgna')
    p['sy']['!'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['word'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['drop'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['push']('; :: ')
    p['sy']['cats'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['push']('pgna')
    p['sy']['@'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['cats'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['push']('code')
    p['sy']['!'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['push']('code')
    p['sy']['@'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['push']('pgna')
    p['sy']['@'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['l!'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['push'](p['OK'])
#
       
def rwd(p):
    # r> word swap r< .
    p['sy']['r>'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['word'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['swap'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['r<'](p)
    okb = p['sy']['pop']() # ok rtn
    p['sy']['push'](p['OK'])
#

def latt(p):
    #popname try(ans=p['l'][name]) ok pushans pushok. else push nok.
    name = p['sy']['pop']()
    try:
        ans=p['l'][name]
        ss = 0
    except:
        ss = -1
    finally:
        nop = 1
    #
    if (ss == 0):
        p['sy']['push'](ans)
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #
#
def lbang(p):
    #popcode,popname p['l'][name] = code, ok
    name = p['sy']['pop']()
    code = p['sy']['pop']()
    p['l'][name] = code
    p['sy']['push'](p['OK'])  
#
def dotl(p):
    #.l = print(p['l'].__str__()), ok
    print(p['l'].__str__())
    p['sy']['push'](p['OK'])
#
def dotlhook(p):
    #.l? = print(p['l'].keys()__str__()), ok
    print(p['l'].keys().__str__())
    p['sy']['push'](p['OK'])
#

def cx(p):
    # str,#,,str[#]or nok
    cc = p['sy']['pop']()
    cc = int(cc)
    strin = p['sy']['pop']()
    try:
        ans = strin[cc]
        anso = 'ok'
    except:
        anso = 'nok'
    finally:
        nop = 1
    #
    if (anso == 'ok'):
        p['sy']['push'](ans)
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #
#
def rdump(p):
    print(p['r'].__str__())
    p['sy']['push'](p['OK'])
#
def rpound(p):
    ans = len(p['r']).__str__()
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
# 
def rout(p):
    try:
        ans = p['r'].pop()
        ert = 1 # ok
    except:
        ert = -1
    finally:
        nop = 1
    #
    if (ert == 1):
        p['sy']['push'](ans)
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#rout
    
def rin(p):
    #(str,,)
    str = p['sy']['pop']()
    p['r'].append(str)
    p['sy']['push'](p['OK'])
#    
def pick(p):
    a=[]
    ctr = p['sy']['pop']()
    ctr = int(ctr)
    for x in range(ctr):
        a.append(p['sy']['pop']())
    #
    jj = a[len(a)-1]
    for xx in range(ctr):
        p['sy']['push'](a.pop())
    #
    p['sy']['push'](jj)
    
    p['sy']['push'](p['OK'])
#

def SReplace(p):
   repl = p['sy']['pop']()
   need = p['sy']['pop']()
   hays = p['sy']['pop']()
   ans = hays.replace(need,repl)
   p['sy']['push'](ans)
   p['sy']['push'](p['OK'])
#
def atHook(p):
    if (p['v']['trace'] == 'on'):
        print('@?')
    #endif
    tgt = p['sy']['pop']()
    m = p['v'].keys()
    m.sort()
    # push zero marker
    p['sy']['ch0'](p)
    p['sy']['pop']()
    for mx in m:
        try:
            d = mx.index(tgt)
            if (d==0):
                p['sy']['push'](mx)
            #endif
        except:
            nop = 1
        finally:
            nop = 1
        #end try
    #endfor
    p['sy']['push'](p['OK'])
#

def DT(p):
    import time
    p['sy']['push'](time.asctime())
    p['sy']['push'](p['OK'])
#
def LT(p):
    b = p['sy']['pop']()
    a = p['sy']['pop']()
    if (a < b ):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#
def GT(p):
    b = p['sy']['pop']()
    a = p['sy']['pop']()
    if (a > b ):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#
def PHook(p):
    """
    trap for '.' verb
    """
    x = p['sy']['pop']()
    if (x == '.'):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#    
def SEMIHook(p):
    """
    trap for ';' verb
    """
    x = p['sy']['pop']()
    if (x == ';'):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#    
def QHook(p):
    x = p['sy']['pop']()
    if (x == '"'):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#
def THook(p):
    x = p['sy']['pop']()
    if (x == "'"):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
# 
def isnumHook(p):
    x = p['sy']['pop']()
    if (x.isdigit() == True):
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#
def woB(p):
    x = p['sy']['pop']()
    ans = x[1:-1]
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
def c1(p):
    x = p['sy']['pop']()
    ans = x[0]
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
def drops(p):
    if (p['v']['trace'] == 'on'):
        print('drops')
    #endif
    p['sy']['depth'](p)
    x = p['sy']['pop']() #ok
    m = int(p['sy']['pop']()) # 
    for z in range(m):
        x = p['sy']['pop']()
    #endfor
    p['sy']['push'](p['OK'])
#

def package(p):
    na = p['sy']['pop']()
    print(p['help'][na])
    p['sy']['push'](p['OK'])
#end help?
def packages(p):
    m = p['package'].keys()
    m.sort()
    mm = m.__str__()
    nn = mm.replace(',','\n')
    print('=== packages ===')
    print(nn)
    print('=== end packages ===')
    p['sy']['push'](p['OK'])
#end vocab
def crlf(p):
    ans = """
"""
    p['sy']['push'](ans)
    p['sy']['push'](p['OK'])
#
def chzero(p):
    p['sy']['push'](chr(0))
    p['sy']['push'](p['OK'])
#end help?
def helphook(p):
    na = p['sy']['pop']()
    print(p['help'][na])
    p['sy']['push'](p['OK'])
#end help?
def verbHook(p):
    # (n,,) ok nok if exists
    na = p['sy']['pop']()
    m = p['sy'].keys()
    try:
        ans = m.index(na)
        p['sy']['push'](p['OK'])
    except:
        p['sy']['push'](p['NOK'])
    finally:
        nop = 1
    #
#
def vocab(p):
    m = p['sy'].keys()
    m.sort()
    mm = m.__str__()
    nn = mm.replace(',','\n')
    print('=== verbs ===')
    print(nn)
    print('=== end verbs ===')
    p['sy']['push'](p['OK'])
#end vocab
def wword(p): # (s,,rest,w)
    if (p['v']['trace'] == 'on'):
        print('wword')
    #endif
    f = p['sy']['pop']()
    local = f
    local = local.rstrip()
    local = local.lstrip()
    local = local + ' '
    try:
        sp = local.index(' ')
    except:
        sp = len(local)+1
    finally:
        nop = 1
    #
    try:
        sq = local.index('"')
    except:
        sq = len(local)+1
    finally:
        nop = 1
    #
    try:
        st = local.index("'")
    except:
        st = len(local)+1
    finally:
        nop = 1
    #
    fo = 0
    mm = min(sp,sq,st)
    if (sp == mm):
       bo = sp
       wd = local[fo:bo]
       rest = local[bo:-1]
    #
    if (sq == mm):
       fo = 1
       bo = local.index('"',sq+1)
       wd = '"' + local[fo:bo] + '"'
       rest = local[bo+1:-1]
    #
    if (st == mm):
       fo = 1
       bo = local.index("'",st+1)
       wd = "'" + local[fo:bo] + "'"
       rest = local[bo+1:-1]
    #
    wd = wd.rstrip()
    wd = wd.lstrip()
    p['sy']['push'](rest)
    p['sy']['push'](wd)
    p['sy']['push'](p['OK'])
#end wword
    
def ndsOut(p):
    if (p['v']['trace'] == 'on'):
        print('ndsOut')
    #endif
    print('begin nds dump \n')
    m = p['v'].keys()
    m.sort()
    for j in m:
        print(j+'=(' + p['v'][j].__str__() + ')')
    #endfor
    print('\n end nds dump \n')
    p['sy']['push'](p['OK'])
# end ndsOut

def dox(p):
    """ executes verb on stack """
    if (p['v']['trace'] == 'on'):
        print('.X')
    #endif
    m = p['sy']['pop']()
    p['sy'][m](p) 
    # verb adds ok/nok
#end dox

def takeV(p):
    # (vectorFile,,) add vectors to architecture 
    # get vectorfile
    VectorFile = p['sy']['pop']()
    # do wild import
    j = __import__( VectorFile ) # no .py extension
    # run x.main(p)
    p = j.main(p)
    p['sy']['push'](p['OK'])
#end takeV

def depth(p):
    if (p['v']['trace'] == 'on'):
        print('depth')
    #endif
    d = len(p['dat'])
    s1 = d.__str__()
    p['sy']['push'](s1)
    p['sy']['push'](p['OK'])
#end depth

def roll(p):
    if (p['v']['trace'] == 'on'):
        print('roll')
    #endif
    #(a,b,c,,c,b,a)
    mc = p['sy']['pop']()
    mb = p['sy']['pop']()
    ma = p['sy']['pop']()
    p['sy']['push'](mc)
    p['sy']['push'](mb)
    p['sy']['push'](ma)
    p['sy']['push'](p['OK'])
#end roll
def find(p):
    if (p['v']['trace'] == 'on'):
        print('find')
    #endif
    # (haystack,needle,, "pos"/ "-1" )
    needle = p['sy']['pop']()
    haystack = p['sy']['pop']()
    pos = haystack.find(needle)
    sp = pos.__str__()
    if (pos <> -1):
        p['sy']['push'](sp)
        p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#end find
def cut(p):
    if (p['v']['trace'] == 'on'):
        print('cut')
    #endif
    # (haystack,pos,,front,middle,last)
    poss = p['sy']['pop']()
    pos = int(poss)
    haystack = p['sy']['pop']()
    front = haystack[:pos]
    middle = haystack[pos]
    last = haystack[pos+1:]
    p['sy']['push'](front)
    p['sy']['push'](middle)
    p['sy']['push'](last)
    p['sy']['push'](p['OK'])
#end cut
    
def split(p):
    if (p['v']['trace'] == 'on'):
        print('split')
    #endif
    # (haystack,needle,,first,middle,last)
    needle = p['sy']['pop']()
    middle = needle
    haystack = p['sy']['pop']()
    posAR = haystack.split(needle) # [first,last]
    first = posAR[0].__str__()
    last = posAR[1].__str__()
    p['sy']['push'](first)
    p['sy']['push'](middle)
    p['sy']['push'](last)
    p['sy']['push'](p['OK'])
#end split

def mattzero(p):
    if (p['v']['trace'] == 'on'):
        print('@--')
    #endif
    # (add,) --> () v(addr) is v-1
    p['sy']['dup'](p)
    p['sy']['pop']() # ok rtn
    p['sy']['@'](p)
    p['sy']['pop']() # ok rtn
    s3 = "0"
    p['sy']['push'](s3) # (addr,val )
    p['sy']['swap'](p)     # val,addr
    p['sy']['pop']() # ok rtn
    p['sy']['!'](p)
    p['sy']['pop']() # ok rtn
    p['sy']['push'](p['OK'])
#end mattzero

def mattminusminus(p):
    if (p['v']['trace'] == 'on'):
        print('@--')
    #endif
    # (add,) --> () v(addr) is v-1
    # dup @ (n3) swap ! (n3)
    p['sy']['dup'](p)
    p['sy']['pop']() # ok rtn)
    p['sy']['@'](p)
    p['sy']['pop']() # ok rtn 
    m2 = p['sy']['pop']() # get val
    n2 = int(m2)
    n1 = 1
    n3 = n2 - n1
    s3 = n3.__str__()
    p['sy']['push'](s3) # (val )
    p['sy']['swap'](p)     # val,addr
    p['sy']['pop']() # ok rtn
    p['sy']['!'](p)
    p['sy']['pop']() # ok rtn
    p['sy']['push'](s3) # (val )
    p['sy']['push'](p['OK'])
#end mattminusminus
def mattplusplus(p):
    if (p['v']['trace'] == 'on'):
        print('@++')
    #endif
    # (add,,c++) --> () v(addr) is ++
    # dup dup @ 1 + swap ! @
    p['sy']['dup'](p)
    p['sy']['pop']()
    p['sy']['dup'](p)
    p['sy']['pop']()
    p['sy']['@'] (p)
    p['sy']['pop']()
    p['sy']['push']('1')
    p['sy']['+'] (p)
    p['sy']['pop']()
    p['sy']['swap'] (p)
    p['sy']['pop']()
    p['sy']['!'] (p)
    p['sy']['pop']()
    p['sy']['@'] (p)
    p['sy']['pop']()
    p['sy']['push'](p['OK'])
#end mattplusplus
    
def mminusminus(p):
    """ math plus """
    if (p['v']['trace'] == 'on'):
        print(' -- ')
    #endif
    m2 = p['sy']['pop']()
    n2 = int(m2)
    n1 = 1
    n3 = n1 - n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mminusminus
def mplusplus(p):
    """ math plus """
    if (p['v']['trace'] == 'on'):
        print(' ++ ')
    #endif
    m2 = p['sy']['pop']()
    n2 = int(m2)
    n1 = 1
    n3 = n1 + n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mplusplus
def mroot(p):
    """ math subtract """
    if (p['v']['trace'] == 'on'):
        print(' -** ')
    #endif
    # 16,2 -** -> 4
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 ** (n2 * -1)
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mroot
def mmod(p):
    """ math mod """
    if (p['v']['trace'] == 'on'):
        print('mod')
    #endif
    # 5,3 - --> 2 
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1.__mod__(n2)
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mmod
def mpwr(p):
    """ math subtract """
    if (p['v']['trace'] == 'on'):
        print(' ** ')
    #endif
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 ** n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mpwr
def mmul(p):
    """ math subtract """
    if (p['v']['trace'] == 'on'):
        print(' * ')
    #endif
    # 5,2 - --> 10
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 * n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mmul
def mdiv(p):
    """ math divide """
    if (p['v']['trace'] == 'on'):
        print(' int / ')
    #endif
    # 5,2 - --> 7
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 / n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mdiv
def mminus(p):
    """ math subtract """
    if (p['v']['trace'] == 'on'):
        print(' - ')
    #endif
    # 5,2 - --> 7
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 - n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mminus
def mplus(p):
    """ math plus """
    if (p['v']['trace'] == 'on'):
        print(' + ')
    #endif
    m2 = p['sy']['pop']()
    n2 = int(m2)
    m1 = p['sy']['pop']()
    n1 = int(m1)
    n3 = n1 + n2
    s3 = n3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end mplus
    
    
def length(p):
    if (p['v']['trace'] == 'on'):
        print('length')
    #endif
    m1 = p['sy']['pop']()
    m3 = len(m1)
    s3 = m3.__str__()
    p['sy']['push'](s3)
    p['sy']['push'](p['OK'])
#end length

def cats(p):
    if (p['v']['trace'] == 'on'):
        print('cats')
    #endif
    m1 = p['sy']['pop']()
    m2 = p['sy']['pop']()
    m3 = m2 + " " + m1
    p['sy']['push'](m3)
    p['sy']['push'](p['OK'])
#end cats
def cat(p):
    if (p['v']['trace'] == 'on'):
        print('cat')
    #endif
    m1 = p['sy']['pop']()
    m2 = p['sy']['pop']()
    m3 = m2 + m1
    p['sy']['push'](m3)
    p['sy']['push'](p['OK'])
#end cat

def dup(p):
    if (p['v']['trace'] == 'on'):
        print('dup')
    #endif
    m1 = p['sy']['pop']()
    p['sy']['push'](m1)
    p['sy']['push'](m1)
    p['sy']['push'](p['OK'])
#end dup

def swap(p):
    if (p['v']['trace'] == 'on'):
        print('swap')
    #endif
    m1 = p['sy']['pop']()
    m2 = p['sy']['pop']()
    p['sy']['push'](m1)
    p['sy']['push'](m2)
    p['sy']['push'](p['OK'])
#end swap

def drop(p):
    if (p['v']['trace'] == 'on'):
        print('drop')
    #endif
    m = p['sy']['pop']()
    p['sy']['push'](p['OK'])
#end drop

    
def elipsis(p):
    """ AKA fail """
    if (p['v']['trace'] == 'on'):
        print('...')
    #endif
    p['sy']['push'](p['NOK'])
#end elipsis.
def tail(p):
    """ does tail recursion """
    p['sy']['push']('tail.')
#end tail.
def ask(p):
    if (p['v']['trace'] == 'on'):
        print('ask')
    #endif
    m = p['sy']['pop']()
    j = raw_input(':'+m+'? ')
    # push answer
    p['sy']['push'](j)
    # push ok
    p['sy']['push'](p['OK'])
#end ask
def inp(p):
    # get input w/o question
    if (p['v']['trace'] == 'on'):
        print('inp')
    #endif
    j = raw_input()
    # push answer
    p['sy']['push'](j)
    # push ok
    p['sy']['push'](p['OK'])
#end ask
def msg(p):
    if (p['v']['trace'] == 'on'):
        print('msg')
    #endif
    m = p['sy']['pop']()
    print(m)
    p['sy']['push'](p['OK'])
#end msg
def bang(p):
    if (p['v']['trace'] == 'on'):
        print('bang')
    #endif
    # (val,addr)
    ad = p['sy']['pop']()
    vval = p['sy']['pop']()
    p['v'][ad] = vval
    p['sy']['push'](p['OK'])
#endif
def att(p):
    if (p['v']['trace'] == 'on'):
        print('att')
    #endif
    ad = p['sy']['pop']()
    try:
        p['sy']['push'](p['v'][ad])
    except:
        p['sy']['push']('')
    finally:
        p['sy']['push'](p['OK'])
    #end try
#end att
def eq(p):
    if (p['v']['trace'] == 'on'):
        print('eq')
    #endif
    op1 = p['sy']['pop']()
    op2 = p['sy']['pop']()
    if (op1 == op2):
       p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#end eq
def neq(p):
    if (p['v']['trace'] == 'on'):
        print('neq')
    #endif
    op1 = p['sy']['pop']()
    op2 = p['sy']['pop']()
    if (op1 != op2):
       p['sy']['push'](p['OK'])
    else:
        p['sy']['push'](p['NOK'])
    #endif
#end eq  
    
