# file name SQV.py 
"""
pja 01-30-2020 added help stmts
pja 1-3-2020
SQV - vector usage 
p['sy']['SQC'](dbname,,)
p['sy']['SQget'](c,tl,,result)
p['sy']["SQClose"](,,)
p['sy']['SQX'](stmt,,)
p['sy']['SQRead1'](sql,,dt)
p['sy']['SQReadFirst'](sql,,dt)
p['sy']['SQReadNext'](,,)
p['sy']['SQReadAll'](sql,,dt

test as 
import smartRDFX
smartRDFX.main('RDFMain')
p = smartRDFX.getp()
p['sy']['push']('trial.db')
g = smartRDFX.take(p,'SQV')
# create table
sql = "create table if not exists TCVR ( ix , T , C , V , R, primary key(ix));"
p['sy']['push'](sql)
p['sy']['.si'](p)
p['sy']['SQX'](p)
p['sy']['.si'](p)


"""
def main(p):
    import SQClass
    # pop dbfilename
    fn = p['sy']['pop']()
    p['sy']['SQC'] = SQClass.SQC(fn)
    p['help']['SQC'] = "SQClass.SQC(fn)"
    p['sy']['SQget'] = sqgetp #(c,tl,,result)
    p['help']['SQget'] = "sqgetp #(c,tl,,result)"
    p['sy']["SQClose"] = sqclosep #(,,)
    p['help']["SQClose"] = "sqclosep #(,,)"
    p['sy']['SQX'] = sqxp  #(stmt,,)
    p['help']['SQX'] = "sqxp  #(stmt,,)"
    p['sy']['SQRead1'] = sqread1p #(sql,,dt)
    p['help']['SQRead1'] = "sqread1p #(sql,,dt)"
    p['sy']['SQReadFirst'] = sqreadfirstp #(sql,,dt)
    p['help']['SQReadFirst'] = "sqreadfirstp #(sql,,dt)"
    p['sy']['SQReadNext'] = sqreadnextp # (,,dt)
    p['help']['SQReadNext'] = "sqreadnextp # (,,dt)"
    p['sy']['SQReadAll'] = sqreadallp #(sql,,dt)
    p['help']['SQReadAll'] = "sqreadallp #(sql,,dt)"
    p['sy']['SQWrite'] = sqwritep # (0,[cv],,)
    p['help']['SQWrite'] = "sqwritep # (0,[cv],,)"
    return(p)
#end main
def sqwritep(p):
    """  (0,[cv],tn,,)
         create insert stmt from [cv]
         insert into tn ( [c],+ ) values ( [v],+ ); 
    """
    # test look at stack before process
    p['sy']['.si'](p) # debug call
    pc = ""
    pv = ""
    tn = p['sy']['pop']() # table name
    pa = 'insert into ' + tn 
    m = p['sy']['pop']()
    while (m != "0"):
        pc = pc + ' ' + "'" + m +  "'" + ','
        pvx = p['sy']['pop']()
        pv = pv + ' ' + "'" + pvx +  "'" + ','
        m = p['sy']['pop']()
        print('sqwrite m=(' + m + ')')
    #wend
    # remove last comma
    pc = pc[:-1]
    pv = pv[:-1]
    pa = pa + "(" + pc + ") values (" + pv + " );"
    print("pa=(" + pa + ")")
    ax = p['sy']['SQC'].SQX(pa)
    p['sy']['push'](p['OK'])
#end sqwritep

def sqreadnextp(p):
    #(sql,,dt)
    stmt = p['sy']['pop']()
    ans = p['sy']['SQC'].SQRead1(stmt)
    # push ans
    p['sy']['push'](ans)
    #push ok
    p['sy']['push'](p['OK'])
#end sqread1p
    
def sqreadallp(p):
    #(sql,,dt)
    stmt = p['sy']['pop']()
    ans = p['sy']['SQC'].SQReadAll(stmt)
    # push ans
    p['sy']['push'](ans)
    #push ok
    p['sy']['push'](p['OK'])
#end sqreadallp
    
def sqreadfirstp(p):
    #(sql,,dt)
    stmt = p['sy']['pop']()
    ans = p['sy']['SQC'].SQReadFirst(stmt)
    # push ans
    p['sy']['push'](ans)
    #push ok
    p['sy']['push'](p['OK'])
#end sqreadfirstp

def sqread1p(p):
    #(sql,,dt)
    stmt = p['sy']['pop']()
    ans = p['sy']['SQC'].SQRead1(stmt)
    # push ans
    p['sy']['push'](ans)
    #push ok
    p['sy']['push'](p['OK'])
#end sqread1p
    
def sqxp(p):
    #(stmt,,)
    stmt = p['sy']['pop']()
    ans = p['sy']['SQC'].SQX(stmt)
    #push ok
    p['sy']['push'](p['OK'])
#end sqxp

def sqclosep(p):
    #(,,)
    ans = p['sy']['SQC'].SQClose()
    #push ok
    p['sy']['push'](p['OK'])
#end sqclosep

def sqgetp(p):
    #(c,tl,,result)
    T = p['sy']['pop']() 
    C = p['sy']['pop']()
    ans = p['sy']['SQC'].SQget(T,C)
    # push ans
    p['sy']['push'](ans)
    #push ok
    p['sy']['push'](p['OK'])
#end sqgetp
  
