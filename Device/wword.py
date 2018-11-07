def wword (ret,arc,ptrace):
    """ basii wword  \n
        ((string,,rest,word)) and resp=0 or resp=1 ((string,,))
    """
    strin = arc[1].pop()
    if len(strin)==0:
        ans1=''
        ans2=''
    else:
	    # white
	    i = 0
	    c = 0
	    while c == 0:
	    	print 'i=(',i,")"
	        if len(strin) != i:
	                if strin[i] == " ":
	                    i = i+1
	                elif strin[i] == chr(10):
	                    i = i+1
	                elif strin[i] == chr(13):
	                    i = i+1
	                else:
	                    c = -1
	                #endif
	        else:
	            c = -2
	        #endif
	    # wend
	    fo = i
	    if strin[0] == '"':
	        # collect all of the text between the quotes
	        bo = strin.find('"',fo+1) + 1
	        
	    else:
	        bo = strin.find(' ',fo+1)
	        if bo == -1:
	            bo = len(strin)
	        # endif
	    # endif
	    ans1 = strin[fo:bo]
	    ans2 = strin[bo+1:]
	    if ptrace == 1:
	        print "fo=(",fo,")"
	        print "bo=(",bo,")"
	        print "ans1=(",ans1,")"
	        print "ans2=(",ans2,")"
	    #endif ptrace
	#endif
    # push results rest,ans1 if len else resp=1
    if len(ans1) != 0:
        arc[1].push(ans2)
        arc[1].push(ans1)
        ans = [0]
    else:
        ans = [1]
    #endif
    return(ans)
# end def wword
        
