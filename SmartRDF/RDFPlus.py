"""/* file RDFPlus.basii
pja 01-21-2020

format
init 
things{}
predicates {}
RDF "stmt" {subject {predicate{object}}}
subject
(subject predicate object)
"""

RDF = {}
RDF['thing'] = {}
RDF['predicate'] = {}
RDF['event'] = {}
RDF['action'] = {}
RDF['stmt'] = {}

RDF['thing']['thing'] = ''
RDF['predicate']['has'] = ''
RDF['predicate']['gets'] = ''

def records(RDFType, subject,predicate,object):
    global RDF
    erc = 0
    if (RDFType == 0): #  simple spo
        # exception predicate gets <<object>>
        # event gets <<object>>
        # action gets <<object>>
        if (subject =='predicate' and predicate == 'gets'):
            RDFWrite(erc, subject,predicate,object)
        else:
            erc = 1 
            # does subject exist erc= erc * 2
			try:
				m = RDF['thing'][subject]
			except:
				erc= erc * 2
			finally:
				print('subject erc' + erc.__str__())
		
			# does predicate exist erc= *3
			try:
				m = RDF['predicate'][predicate]
			except:
				erc = erc * 3
			finally:
				print('predicate erc' + erc.__str__())
			# end tests
			# record if erc ==0 mod gives errors
			if (erc.__mod__(2) == 0):
				print('subject does not exist')
			if (erc.__mod__(3) == 0):
				print('predicate does not exist')
			if (erc ==1):
				RDFWrite(erc, subject,predicate,object)
			#endif
		#endif
	#endif
#end records

def RDFWrite(erc, subject,predicate,object):
    global (RDF)
    if (erc==1):
		# if rdf[stmt][subject] exists use it else create it
		try:
		   m = RDF['stmt'][subject]
		except:
			RDF['stmt'][subject] = {}
			print('new subject')
		finally: 
			nop = 1
		#end 
		try:
		   m = RDF['stmt'][subject][predicate]
		except:
			RDF['stmt'][subject][predicate] = {}
			print('new predicate')
		finally: 
			nop = 1
		#end 
		try:
		   m = RDF['stmt'][subject][predicate][object]
		except:
			RDF['stmt'][subject][predicate][object] = ''
			print('new object')
		finally: 
			nop = 1
		#end
		#add object to things if new
		try:
			m = RDF['thing'][object]
		except:
			RDF['thing'][object]=''
		finally:
			nop = -1
		#end
	elif (erc==0): # predicate gets <<object>>
	    # new predicate
	    #add object to things if new
		try:
			m = RDF['predicate'][object]
		except:
			RDF['predicate'][object]=''
		finally:
			nop = -1
		#end
	#endif
#end RDFWrite
     
"""
RDF01 :-
[[ 1 ]] VWord ... .
[[ 2 ]] dup ==( drop complexSubject RDF02 tail. .
[[ 3 ]] "subject" ! RDF02 tail. .
;
complexSubject :-
[[ 1 ]] VWord "ssubject" ! 

     


"""  
