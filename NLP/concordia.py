"""
file concordia.py
pja 07/11/2020

takes in a sentence (text till ".")
and returns array of words in 
concordance: 
A simple list words, with indications to enable the inquirer to find the context of the document where the words occur.

"""
"""
notes
document -< context -< paragraph -< sentence -< words
(contextType,contextRefid)("collector",#)-- 
("paragraph",#),
("sentence",#),
("phrase",phrase),
("phraseOrder",#)

add to ontology of xsd the concordia per context:
-tag, 
-attributeName, 
-attributeValue

add to xml ontology

Home vs home? == case 
-- not now 
not one vs just one
-- not now

output 
word or ordered phrase , 
sentence number in paragraph, 
word number in sentence
documentName
"""

def ListOfWords(sentence):
    """
    returns words in order
    """
    final = [] # full collection of word lists
    final2 = [] # parallel list of word positions (0:)
    #clean sentence
    sentence = sentence.replace('.','')
    sentence = sentence.replace(',','')
    sentence = sentence.replace('!','')
    sentence = sentence.replace('?','')
    sentence = sentence.replace('"','')
    sentence = sentence.replace("'",'')
    #collect wds to v[]
    v = sentence.split(' ')
    n = len(v)
    print('begin')
    ans = [] 
    for I in range(1,2**n):
		print("I="+str(I)+":")
		ans = [] # word list
		ans2 = [] # position list 
		k = -1
		i = I
		# binary conversion of I
		while(i <> 0):
			k = k +1
			r = i - ((i/2)*2 )
			print("r="+str(r)+":")
			if (r==1):
			   print("k="+str(k)+":")
			   print(v[k]) 
			   ans.append(v[k])
			   ans2.append(k)
			i = i/2
		#wend
		print(ans)
		final.append(ans)
		final2.append(ans2)
	#endfor I
    return(final,final2)
#end concordia
