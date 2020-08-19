"""
file onto2rdf.py
pja 7/25/2020


test as
import useLib
import useK2
import onto2rdf
onto2rdf.main(file+'.onto')

creates onto+.rdf outputfile
rdf: ( s o p ) ;
S: = name ;
P: = name ;
end:


use onto2rdf.main(input#onto#file)

"""
"""
notes
[infile]<- (inFile)
open [infile] viz onto
[outfile]<- [infile]+".rdf"
open [outfile]

#[pickup]<- ATNseek('pickup')
#per[m]
## refid<-seek(pickup,[m])[4]
## [attributes]<- seek('ANT','','',"refid",refid)
## [relates]<- seek('RELATE','','','','','','',"refid",refid)
## r1='refid' r2=refid , rpred="@"
## rdfPred = "@"+refid
## rdfPred "r1@r2" #> rpx
##// per[K]-[attributes]
##// per[Q]-[relates]
#/per[m]



## per[K]
    #### s1=[attribute[K]][0]
    #### v1=[attribute[K]][1]
    #### p1 = "="
    #### rdfPred "s1=v1" 
    #### write RDF: ( ( s1 "=" v1 ) rdfPred ( REFID  = refid ) ) ;
## /per[K]

##// per[Q]-[relates]
# v1,v2,v3,v4,v5,v6,refid
RDF: (
( v1 = v2 )
( v3 .:. v4 )
( v5 = v6 )
) ;
RDF: ( * to 
( REFID = refid )
) ;
"""
def init():
    global nds,pkg
    import useLib
    import useOnto
    #open [infile] viz onto
    import OntologyClass
    pkg['onto'] = OntologyClass.Ontology(nds['inFile'])
    #[outfile]<- [infile]+".rdf"
    nds['outfile'] = nds['inFile']+'.rdf'
    # see rdfScriptFormat.txt
    # open [outfile]
    nds['fout'] = open(nds['outfile'],'w')
    nds["thing"] = {}
    nds["pred"]={}
    nds["edge"] = {} # format [from::to]='' unique edges
#end init

def main(ontoFileName):
    """
    
    """
    global nds,pkg
    nds = {}
    pkg = {}
    nds['inFile'] = ontoFileName
    init()
    #[pickup]<- seek('pickup')
    nds['pickupList'] = pkg['onto'].ATNSeek('pickup')
    nds['relateList'] = pkg['onto'].RELATESeek()
    perAk()
    per_Bm()
    per_Cp()
    #write end:
    #close outfile
    nds['fout'].write("END:")
    nds['fout'].close()
#main
    
    
def per_Bm():
    print('Bm begin')
    for m in range(1,len(nds["attributes"])+1):
        ## per[K]
        s1=nds["attributes"][m-1][1]
        v1=nds["attributes"][m-1][2]
        ref = nds["attributes"][m-1][18]
        fnB(s1,v1,ref)
        ## /per[m]
    #end for
    print('Bm end')
#perK
def perAk():
    #per[m] len(nds['pickupList'])
    print('Ak begin')
    for k in range(1,len(nds['pickupList'])+1):
       ## refid<-seek(pickup,[m])[4]
       nds['refid'] = nds['pickupList'][k-1][4]
       ## [attributes]<- seek('ANT','','',"refid",refid)
       nds['attributes'] = pkg['onto'].ATNSeek('','','refid',nds['refid'])
       ## r1='refid' r2=refid 
       nds['r1'] = 'Refid'
       nds['r2'] = nds['pickupList'][k-1][4]
       ## rdfPred = "@"+refid
       nds['rpred'] = "@"+ nds['pickupList'][k-1][4] 
    #endfor
    print('Ak end')
#/per[m]


def fnB(sn,sv,ref):
    """
    create rdf statements 
    """
    fnB1("refid",'-',"refid@"+ref)
    fnB1("refid@"+ref,'-',sn+"@"+sv)
    fnB1("refid@"+ref,'-',sn+"@"+sv+"!"+ref)
    fnB1(sn,'-',sn+"@"+sv)
#
def fnB1(sn,pn,on):
    """
    output RDF statements
    """
    s1= """
RDF: ( "%s%" "%p%" "%o%" ) ;
    """
    s1 = s1.replace ('%s%',sn)
    s1 = s1.replace ('%p%',pn)
    s1 = s1.replace ('%o%',on)
    print("s1=("+s1+")")
    nds['fout'].write(s1)
#fnB1
def per_Cp():
    """
    per relate of refid[a]
    v1->v1@v2
    v5->v5@v6!v3@v4
    node: v3@v4 refid=.z.
    fnB(v1,v2,ref)
    fnB(v5,v6,ref)
    v1->v2!v3@v4
    """
    global nds,pkg
    print("Cp begin")
    nds['relateList'] = pkg['onto'].RELATESeek()
    print(len(nds['relateList']))
    for p in range(1,len(nds['relateList'])+1):
        ref = nds['relateList'][p-1][18]
        v1 = nds['relateList'][p-1][1]
        v2 = nds['relateList'][p-1][2]
        v3 = nds['relateList'][p-1][3]
        v4 = nds['relateList'][p-1][4]
        v5 = nds['relateList'][p-1][5]
        v6 = nds['relateList'][p-1][6]
        fnB1(v1,'-',str(v1+"@"+v2))
        fnB1(v5,str(v3+"@"+v4),str(v5+"@"+v6))
        nds['fout'].write("\nNAME: " + str(v3+"@"+v4) + ' ;')
        fnB(v1,v2,ref)
        fnB(v5,v6,ref)
        fnB1(v1,str(v3+"@"+v4),v2)#v1->v2!v3@v4
    #/per
    print('Cp end')
#/perCp
        
        
    
    
