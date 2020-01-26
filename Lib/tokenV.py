# file name tokenV.py 
"""
pja 1-25-2020

true LALR(n) parser

    sets p['token']=[] for record hold
p['token'][0] is stack ix
p['token'][#]={frontpos,token,backpos} from fio fpword

    sets vectors for basii doVerb
getToken == fpword 
token    == put curent token on d-stack
putback  == reset fiox before current token; erase p['token'][#] record

    assumes fioi vectors are installed EG install fioi first

test as 
test file contents:
one two three
/test

import bbox
bbox.main('bboxMain')
push "testFile.txt"
push "fioV"
takeV
push "tokenV" 
takeV
getToken
.s // no entry on stack //
token
.s // (,,one)
token
.s // (one,,one,one)
getToken
token
.s // (one,one,,one,one,two)
putback
getToken
token
.s // (,,)


handy statements
push and pop
stmt = p['sy']['pop']()
p['sy']['push'](p['OK'])
"""
def main(p):
    p['token'] = [] // record hold
    p['token'][0] = 0
    
    p['sy']['getToken'] = getToken #(,,)
    p['sy']["token"] = token #(,,token) and p['token'][#] record
    p['sy']['putback'] = putback #(,,) and reset of fiox, p['token'][#] record

    return(p)
#end main
