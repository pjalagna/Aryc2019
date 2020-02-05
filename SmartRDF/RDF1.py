"""
file RDF1.py

pja 01-27-2020

test as
import RDF1
d = RDF1
RDF = d.RDFInit()
RDF = d.SPO(RDF,'thing','has','kitty')
RDF = d.SPO(RDF,'thing','has','James')
RDF = d.SPO(RDF,'thing','has','Ippolito')
RDF = d.SPO(RDF,'thing','has','Vinchenza')
RDF = d.SPO(RDF,'predicate','gets','is')
RDF = d.SPO(RDF,'predicate','gets','child')
# add family
RDF = d.SPO(RDF,'kitty','child','fortunata')
RDF = d.SPO(RDF,'James','child','fortunata')
RDF = d.SPO(RDF,'fortunata-of-kitty','is','marie')
RDF = d.SPO(RDF,"Ippolito",'child','Giovanni')
RDF = d.SPO(RDF,'Vinchenza','child','Giovanni')
RDF = d.SPO(RDF,'Giovanni-of-Ippolito','is','john')
RDF = d.SPO(RDF,'marie','child','Cathy')
RDF = d.SPO(RDF,'john','child','Cathy')
RDF = d.SPO(RDF,'Cathy-of-marie','child','joe')
RDF = d.SPO(RDF,'joe','is','BigJoe')
RDF = d.SPO(RDF,'Cathy-of-marie','child','anthony')
RDF = d.SPO(RDF,'Cathy-of-marie','child','matt')
RDF = d.SPO(RDF,'marie','child','Vicky')
RDF = d.SPO(RDF,'john','child','Vicky')
RDF = d.SPO(RDF,'marie','child','Paul')
RDF = d.SPO(RDF,'john','child','Paul')
# add GGpa
RDF = d.SPO(RDF,'thing','has','Giovanni')
RDF = d.SPO(RDF,'Giovanni','child','Ippolito')

"""
"""
rules on predicates
"is" 
- must record on object the object is subject - ie dual points; 
- parent of object is parent of subject

'marries' eg paul marries joan 
- puts agent on predicate "child" to insert other partner
-- eg (marie child cathy) also creates (john child cathy)
- what do we do with kitty's 3 husbands?

"""
def RDFInit():
    RDF = {}
    RDF['thing'] = {}
    RDF['predicate']={}
    RDF['predicate']['has'] = {}
    RDF['predicate']['gets'] = ''
    RDF['predicate']['parent'] = ''
    RDF['thing']['thing'] = {}
    RDF['thing']['predicate'] = ''
    return(RDF)
#end RDFInit

def SPO(RDF,subject,predicate,object):
    # subject must exist or be "predicate"
    try:
        sm = RDF['thing'].keys()
        if (-1 < sm.index(subject)):
            ts = 1
        else:
            ts = -1
        #endif
    except:
        ts = -1
        print('subject does not exist ' + subject )
    finally:
        nop = 1
    #end try
    print('ts='+ts.__str__())
    nop =1
    
    # predicate must exist
    try:
        p = RDF['predicate'].keys() 
        if (-1 < p.index(predicate)):
            print('pr 1 ')
            tp = 1
        else:
            print('pr 2 ')
            tp = -1
        #endif
    except:
        tp = -1
        print('predicate does not exist ' + predicate )
    finally:
        nop = 1
    #end try
    print('tp='+tp.__str__())
    nop = 1
    #1= exception predicate gets <object>
    if (ts+tp == 2):
        if (subject =='predicate' and predicate == 'gets'):
            RDF['predicate'][object]=''
        else:
            #disambiguate object before entry
            ## if thing-object exists
            ### change current record parent-object to parent-object-of-parent
            #### cathy child matt to cathy child matt-of-cathy
            ### change thing[subject] record
            ### change new object to subject-predicate-object-of-subject
            #### allan child matt new object matt-of-allen
            
            try:
                te = RDF['thing'][object]
                tee = 1
            except:
                tee = -1
            finally:
                nop =1
            #end try
            nop = 1
            if (tee == 1):
                #diambiguate and change object
                pa = RDF[object]['parent'].keys()[0]
                pa = pa.__str__()
                c1o = object + '-of-' + pa 
                # replace old rec of object with c1o object
                RDF[c1o] = RDF[object]
                RDF['thing'].pop(object)
                RDF['thing'][c1o]=''
                RDF.pop(object)
                object = object + '-of-' + subject
            #endif
            try:
                om = RDF['thing'].keys()
                if (-1 < om.index(object)):
                    to = 1
                else:
                    to = -1
                #endif
            except:
                to = -1
                # print('object does not exist ' + object )
            finally:
                nop = 1
            #end try
            print('to='+to.__str__())
            nop =1
            
            #if new object [object]={},[object]['parent']={}
            if (to != 1 ):
                print('p 2 ')
                RDF[object] = {}
            #endif
            print('p 3 ')
            # if object has no parent create {}
            try:
                op = RDF[object]['parent']
                ope = 1
            except:
                ope = -1
            finally:
                nop = 1
            #endtry
            nop = 1
            if (ope != 1):
                RDF[object]['parent']={}
            #endif
            RDF[object]['parent'][subject]='' #2 write object parent
            # if subject[predicate] is new create
            try:
                sp = RDF[subject][predicate]
            except:
                RDF[subject][predicate] = {}
            finally:
                nop = 1
            #end try
            nop = 1
            RDF[subject][predicate][object]=''#2= write [s][p][o] = ''
            RDF['thing'][object]=''
        #endif
    #endif
    return(RDF)
#end SPO