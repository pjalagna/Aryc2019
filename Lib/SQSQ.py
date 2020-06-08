"""
file SQSQ.py
 
pja 6/7/2020 added quote protection
pja 12-26-2019 cloned from SQSQ.php

test as
import SQSQ
m = SQSQ.SQin('his snoring zzz was #%!@#$%^&*()')
print('m=(' + m + ')' )
print('back=' + SQSQ.SQout(m))

"""

def SQin(ins) :
    endans = ''
    for x in ins:
        ans = x
        if (x=='z') : 
           ans  = 'zzz'
        if (x=='*') : 
           ans  = 'zsz'
        if (x=='"') : 
           ans  = 'zdqz'
        if (x=="'") : 
           ans  = 'zsqz'
        if (x=='^') : 
           ans  = 'zuz'
        if (x=='&') : 
           ans  = 'zaz'
        if (x==';') : 
           ans  = 'zscoz'
        if (x==',') : 
           ans  = 'zcmz'
        if (x=='!') : 
           ans  = 'zbz'
        if (x=='@') : 
           ans  = 'zatz'
        if (x=='#') : 
           ans  = 'zhz'
        if (x=='$') : 
           ans  = 'zdlz'
        if (x=='%') : 
           ans  = 'zpnz'
        if (x=='=') : 
           ans  = 'zeqz'
        if (x=='+') : 
           ans  = 'zplz'
        if (x=='[') : 
           ans  = 'zobz'
        if (x==']') : 
           ans  = 'zcbz'
        if (x=='{') : 
           ans  = 'zobrz'
        if (x=='}') : 
           ans  = 'zcbrz'
        if (x=='<') : 
           ans  = 'zgtz'
        if (x=='>') : 
           ans  = 'zcltz'
        if (x=='.') : 
           ans  = 'zpz'
        if (x=='?') : 
           ans  = 'zqz'
        if (x==',') : 
           ans  = 'zcmz'
        if (x=='-') : 
           ans  = 'zdsz'
        if (x=='(') : 
           ans  = 'zopz'
        if (x==')') : 
           ans  = 'zcpz'
        if (x=='/') : 
           ans  = 'zslz'
        endans = endans + ans
    # end for
    return (endans)
#end SQin
    
def SQout(ins) :
	x = ins
	x = x.replace('zsz','*')
	x = x.replace('zsqz',"'")
	x = x.replace('zdqz','"')
	x = x.replace('zaz','&')
	x = x.replace('zsz','*')
	x = x.replace('zscoz',';')
	x = x.replace('zcmz',',')
	x = x.replace('zbz','!')
	x = x.replace('zatz','@')
	x = x.replace('zhz','#')
	x = x.replace('zdlz','$')
	x = x.replace('zpnz','%')
	x = x.replace('zeqz','=')
	x = x.replace('zplz','+')
	x = x.replace('zobz','[') 
	x = x.replace('zcbz',']')
	x = x.replace('zobrz','{')
	x = x.replace('zcbrz','}')
	x = x.replace('zgtz','<')
	x = x.replace('zltz','>')
	x = x.replace('zpz','.')
	x = x.replace('zqz','?')
	x = x.replace('zdsz','-')
	x = x.replace('zopz','(')
	x = x.replace('zcpz',')')
	x = x.replace('zslz','/')
	x = x.replace('zuz','^')
	x = x.replace('zzz','z')
	return (x)
#end SQout