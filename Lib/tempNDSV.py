m = """
file tempNDS.py
pja 02-15-2020

tempNDS functions for basii
dott # .t display
t0 # t0 delete all entries
tbang # t! (v,n,,) write
tat # t@ (n,,v) read

"""
"""
    drb = p['sy']['pop']()
    p['sy']['push'](dra)
    p['sy']['push'](p['OK'])
"""
def main(p,m=m):
    p['package']['tempNDS'] = ''
    p['help']['tempNDS'] = m
    p['tempNDS'] = {}
    p['sy']['.t']= dott #(val,index,[],,[])
    p['help']['.t']= ".t (,,) display tempNDS)"
    p['sy']['t0']= t0 #(val,index,[],,[])
    p['help']['t0']= "t0 delete all entries in tempNDS"
    p['sy']['t!']= tbang #(val,index,[],,[])
    p['help']['t!']= "(v,n,,) write entry to tempNDS"
    p['sy']['t@']= tat #(val,index,[],,[])
    p['help']['t@']= "(n,,v) read entry from tempNDS"
    return(p)
#end main
def dott(p): # .t display
    print(p['tempNDS'])
    p['sy']['push'](p['OK'])
#
def t0(p): # t0 delete all entries
    p['tempNDS'] = {} 
    p['sy']['push'](p['OK'])
#
def tbang(p): # t! (v,n,,) write
    name = p['sy']['pop']()
    vval = p['sy']['pop']()
    p['tempNDS'][name] = vval
    p['sy']['push'](p['OK'])
#
    
def tat(p): # t@ (n,,v) read
    name = p['sy']['pop']()
    vval = p['tempNDS'][name]
    p['sy']['push'](vval)
    p['sy']['push'](p['OK'])
#
    
    
    
