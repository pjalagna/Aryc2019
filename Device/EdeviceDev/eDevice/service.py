def main(li):
    """  demo service for eDevice \n
           all services MUST be of format <name>.main \n
           each service can independently have as many parameters as it needs
    """
    import os
	# try look for <cmd>
	try:
		k = li.index('<cmd>')
	except:
		k = -1
	finally:
		nop = -1
	#end try
	if (k==-1): # device message
		# create qml to service
		qf = '<qfrom> hubaddr </qfrom>'
		qcmd = '<cmd> service </cmd>'
		# add the msg from input
		fo = li.index('<msg>')
		bo = li.index('</msg>')
		qmsg = li[fo:bo+len('</msg>')]
		# do work
		print(qf+qcmd+qmsg) # test
	else:
		# do cmd (sendToDisplay)
		qf = '<qfrom> hubaddr </qfrom>'
		qcmd = '<cmd> display </cmd>'
		# add the msg from input
		fo = li.index('<msg>')
		bo = li.index('</msg>')
		qmsg = li[fo:bo+len('</msg>')]
		# do work
		print(qf+qcmd+qmsg) # test
		# delete file
		os.remove(iamin + ldir[f])
	#endif
#main