#file svc1serviceBox
def main(ffile): 
    """ service for dev1 records """
    # get <msg> v </msg>
    fo = ffile.index('<msg>')
    bo = ffile.index('</msg>')
    fo = fo + 5
    vs = ffile[fo:bo]
    # ans = v + 12
    v = float(vs) + 12
    # send to hub viz "whereishub.txt"
    fx = open('hubaddrdisp.txt', 'r')
    fx1 = fx.readline()
    fx1 = fx1[:-1]
    ans = ffile + '<svc1> ' + v.__str__() + ' </svc1>' 
    import sr232
    sr232.send(fx1, ans )
    print('dev1serviceBox test' , ans )
    x = raw_input('?? ..')
#end main
