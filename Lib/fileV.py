m="""
file fileV.py
pja 02-10-2020

file manager for basii
--fx(): # (fn,,) ok/nok - fx - file exists? 
fat(): # (fn,,contents) f@ - read file
fbang(): # (txt,fn,,) f! - write file
fbangPlus(): # (txt,fn,,) f!+ - appends file
--fminus(): # (fn,,) f- - deletes file


    p['sy']['Sioi']= Sioi 
    p['help']['Sioi']= "(str,,ch) ch at iox "
tn = p['sy']['pop']()
p['sy']['push']( str )
p['sy']['push'](p['OK']) 
"""
def main(p,m=m):
    p['package']['fileV'] = ''
    p['help']['fileV'] = m
    p['sy']['f@']= fat
    p['help']['f@']= "(fn,,contents) f@ - read file"
    p['sy']['f!']= fbang
    p['help']['f!']= "(txt,fn,,) f! - write file"
    p['sy']['f!+']= fbangPlus
    p['help']['f!+']= "(txt,fn,,) f!+ - append file"
    return(p)
#
def fat(p):
    fn = p['sy']['pop']()
    fh = open(fn,'r')
    ans = fh.read()
    fh.close()
    p['sy']['push']( ans )
    p['sy']['push'](p['OK']) 
#
def fbang(p): # (txt,fn,,) f! - write file 
    fn = p['sy']['pop']()
    str = p['sy']['pop']()   
    fh = open(fn,'w')
    fh.write(str)
    fh.close()
    p['sy']['push'](p['OK']) 
#
def fbangPlus(p): # (txt,fn,,) f! - append file 
    fn = p['sy']['pop']()
    str = p['sy']['pop']()   
    fh = open(fn,'a')
    fh.write(str)
    fh.close()
    p['sy']['push'](p['OK']) 
#

