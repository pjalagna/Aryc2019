"""
file xsdAsker.py

reads xsd and requests elements by tree execution
starting with <element name='begin'
pja 6/8/2020

note:
if no begin then ask for begin


"""
"""
test with
fn = 'basii.xsd'
nds = {}
pkg = {}
nds['trace']='on'
import useLib
import useOnto
import OntologyClass
pkg['ontology'] = OntologyClass.Ontology(fn + '.onto',str(nds['trace']))
sq={}
sq["0"] = pkg['ontology'].db.SQReadAll 

"""
def init(fn):
    fn = 'basii.xsd'
    nds = {}
    pkg = {}
    nds['trace']='on'
    import useLib
    import useOnto
    import OntologyClass
    pkg['ontology'] = OntologyClass.Ontology(fn + '.onto',str(nds['trace']))
    sq={}
    sq["0"] = pkg['ontology'].db.SQReadAll
    ctl = 1 

"""
print("[[ 1 ]] get begin refid")
beginRefid = str(sq['0']("select v18 from v20 where v2='begin';")[0][0])
ctl = 2
"""
"""
print("[[ 2 ]] find refed_records_refid .")
sq2 = "select v2 from v20 where v18='%beginrefid%' and v1='ref';"
sq2 = sq2.replace('%beginrefid%' ,beginRefid)

refed_records_name = str(sq['0'](sq2)[0][0])

sq3 = "select v18 from v20 where v1='name' and v2='%refedName%';"

sq3 = sq3.replace('%refedName%',refed_records_name)

sq4 = str(sq['0'](sq3)[0][0])
ctl = 3
""" 
"""
print("[[ 3 ]] hold min max name & display all")
myminsq = "select v2 from v20 where v18='%myrefid%' and v1='minOccurs';"
myminsq = myminsq .replace('%myrefid%',sq4)
mymin = str(sq['0'](myminsq)[0][0])
print('min=('+mymin+')')

mymaxsq = "select v2 from v20 where v18='%myrefid%' and v1='maxOccurs';"
mymaxsq = mymaxsq .replace('%myrefid%',sq4)
mymax = str(sq['0'](mymaxsq)[0][0])
print('max=('+mymax+')')

mynamesq = "select v2 from v20 where v18='%myrefid%' and v1='name';"
mynamesq = mynamesq .replace('%myrefid%',sq4)
myname = str(sq['0'](mynamesq)[0][0])
print('name=('+myname+')')
ctl = 4
"""
"""
print("[[ 4 ]] walk to next (sq4==myrefid)")
mypickupsq = "select v2 from v20 where v18='%myrefid%' and v1='pickup';"
mypickupsq = mypickupsq.replace('%myrefid%',sq4)
mypickup = str(sq['0'](mypickupsq)[0][0])

sqnextrefidsq = "select v18 from v20 where v1='previousPickup' and v2='%mypickup%';"
sqnextrefidsq = sqnextrefidsq.replace('%mypickup%',mypickup)
nextRefid = str(sq['0'](sqnextrefidsq)[0][0])
ctl = 5
""" 
"""
print ("[[ 5 ]] get my tag")
print ("-- get l1x,l2x ")
myrefid = nextRefid
mytagsq = "select v2 from v20 where v18='%myrefid%' and v1='tag';"
mytagsq = mytagsq.replace('%myrefid%',myrefid)
mytag = str(sq['0'](mytagsq)[0][0])
print(mytag)
print(-- fan on l1x, tag )
if (mytag=='complexType'):
    sq4 = myrefid
    ctl = 4
#endif


if (mytag=='sequence'):
    sq4 = myrefid
    rseq = 0
    ctl = 4
#endif

if (mytag=='element'):
    if (rseq == 0):
        ctl = 60
    else:
        ctl = 61
    #endif
    
#endif

""" 