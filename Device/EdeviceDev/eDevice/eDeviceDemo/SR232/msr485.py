# file msr485.py
# pja - 10-30-17 changed name to reflect protocol
"""
 in rs 485 all nodes are addressed and daisy chained in a circle
 - registration must tell each node 
 a) who is next in their linkage
 b) their node id
- there is no master slave protocol
-- all nodes start out as masters (set cts on 0000)
--- on reception look at <iam>ToAddress.txt
---- if address is me process and respond to <iam>FromAddress.txt
------ IE set addresses ToAddress <= FromAddress ; iam => FromAddress 
------- send
-- to send a message 
""" 
# pja - 11-17-12 added os.chmod to register. opens all files for read/write
#--- will this break on windows?
#pja 11-3-13 edited for eDevice demo
#--- register - skipped chmod
#------- 
#--- listenOnce needed local iam to add "In"
#----- deleted need for output to saved file
#----- changed logic for mailed file (sender data ready; status = 1110; now accepts data sets status to 0000 and then to 1000
# -- listenStart now returns af# file sr232.py
# pja - 11-17-12 added os.chmod to register. opens all files for read/write
#--- will this break on windows?
#pja 11-3-13 edited for eDevice demo
#--- register - skipped chmod
#------- 
#--- listenOnce needed local iam to add "In"
#----- deleted need for output to saved file
#----- changed logic for mailed file (sender data ready; status = 1110; now accepts data sets status to 0000 and then to 1000
# -- listenStart now returns after receiving data
# -- send - now returns status 0=not sent 1=sent
import time # sleep function
def logg(tx,item):
	print("log-----",tx,item)
#end logg
def listenOnce(iams):
   """ stepped listener for time shattered transfer \n
       returns status and data if any
   """
   data = '' # default
   iam = iams + 'In'
   ans = 0
   m = getStatus(iam)
   print('m is(' + m + ")")
   if ( m == '0000' ):
      setFile(iam + 'cts.txt','1')
   elif ( m == '1110'): # mailed 
      fin = open(iam+"data.txt",'r')
      fd = fin.readlines()
      fin.close()
      data = fd.__str__()
      # set status to 0000
      setFile(iam + 'cts.txt','0') # clear to send (receiver)
      setFile(iam + 'rts.txt','0') # request to send (sender)
      setFile(iam + 'dr.txt','0') # data ready (sender)
      setFile(iam + 'da.txt','0') # data acquired (receiver)
      # set status to 1000
      setFile(iam + 'cts.txt','1') # clear to send (receiver)
      setFile(iam + 'rts.txt','0') # request to send (sender)
      setFile(iam + 'dr.txt','0') # data ready (sender)
      setFile(iam + 'da.txt','0') # data acquired (receiver)
   elif ( m == '1101'):
      setFile(iam+'data.txt','')
   elif ( m == '1001'):
      setFile(iam+'cts.txt','0')
   elif ( m == '0001'):
      setFile(iam+'da.txt','0')
      ans = 1
   else:
      ans = 2 # no data 
   #endif
   return(ans,data)
#end listenOnce

def listenStart(channelName,toc):
   """ listenStart is a rs232 agent \n
       rvc-cts==++++++++++++++===++++
       snd-rts====++++++++++===
       snd-data
       snd-dr =======+++++++====
       rcv-da =========+++++===
   """
   if toc == 0:
      ltoc = 50000 # forever
   else:
      ltoc = toc
   #end if
   iam = channelName + "In"
   c = 1
   while (c == 1) :
      a = listenOnce(channelName)
      if (len(a[1]) != 0):
         c = -1
      else:
         time.sleep(ltoc)
      #endif
   # wend
   return(a)
# end def lsiten start

def getStatus(iam):
   fhcts = open(iam + 'cts.txt','r')
   cts = fhcts.read()
   fhcts.close()
   fhrts = open(iam + 'rts.txt','r')
   rts = fhrts.read()
   fhrts.close()
   fhdr = open(iam + 'dr.txt','r')
   dr = fhdr.read()
   fhdr.close()
   fhda = open(iam + 'da.txt','r')
   da = fhda.read()
   fhda.close()
   print("status = (" + cts + rts + dr + da + ")")
   return(cts + rts + dr + da)
# end status
   
def looptill(inFile,valChr, maxCtr):
   """ loops till infile read has value returns ok/nok """
   i = 1
   c = 1
   while c == 1:
      i = i + 1
      if i == maxCtr :
         c = -1 # kill loop on max
      # end if
      # open infile
      fh = open(inFile,'r')
      # read contents
      ans = fh.read()
      # if contents = valchr end loop on -2
      if ans == valChr :
         c = -2
      else:
         fh.close()
         #---------------print ('bef sleep' )
         time.sleep(.2)
         #--------------print ('\n aft sleep')
      # end if
   # wend
   fh.close()
   # if good end ans = ok else nok
   if c == -2 :
      ans = 'ok'
   else:
      ans = 'nok'
   #end if
   return (ans)
# end def looptill
def setFile(fin,vval):
   """ sets file to vval """
   print('file is ' + fin + ' vval is ' + vval )
   fna = fin
   fh = open(fna,'w')
   fh.write(vval)
   fh.close()
   time.sleep(.01) # doevents
# end def setfile
def bidLock(lockFileName):
   """ bid for and lock a token access file """
   # see if file is already locked
   fh = open(lockFileName,'r')
   a1 = fh.readline()
   a2 = fh.readline()
   a3 = fh.readline()
   # is a3 (lock time) + 15 minutes < now
# end def bidLock
def sniff(channel, ctr):
   """ displays status of rs232 files \n
       give channel, loop counter
   """
   lctr = ctr
   while lctr != 0:
      #
      lctr = lctr -1
      iam = channel + "In"
      fh1cts = open(iam + "cts.txt",'r')
      cts = fh1cts.read()
      fh1cts.close()
      fh1rts = open(iam + "rts.txt",'r')
      rts = fh1rts.read()
      fh1rts.close()
      fh1dr = open(iam + "dr.txt",'r')
      dr = fh1dr.read()
      fh1dr.close()
      fh1da = open(iam + "da.txt",'r')
      da = fh1da.read()
      fh1da.close()
      print ("(In(" + lctr.__str__() + "))" + cts + "." + rts + "." + dr + "." + da + "." + "\n")
      time.sleep(.2)
   # wend
# end def
def send(channel,msg):
   """ send message if it can \n
       returns status 0 nnot sent 1=sent
   """
   status = 0 # default
   mm = 100 # idle loop count
   iam = channel + "In"
   c = 1
   while (c==1):
      m = getStatus(iam)
      if (m=='1000'):
         setFile(iam + 'rts.txt','1')
      elif (m=='1100'):
         omsg = '\n\n<t>' + time.asctime() + '</t> \n <msg>' + msg + "</msg>"
         setFile(iam +"data.txt",omsg)
         print('data sent to outfile (' + omsg + ")")
         status = 1 #sent
         setFile(iam + 'dr.txt','1')
      elif (m=='1111'):
         setFile(iam + 'dr.txt','0')
      elif (m=='1101'):
         setFile(iam + 'rts.txt','0')
      elif (m=='0001'):
         c = 0 # break
      elif (m=='0000'):
         mm = mm -1
         if (mm == 0):
            c = -42 # break on idle timeount
         #endif
      elif (m=='1110'):
         mm = mm -1
         if (mm == 0):
            c = -46 # break on busy timeount
         #endif
      elif (m=='1001'):
         mm = mm -1
         if (mm == 0):
            c = -48 # break on busy timeount
         #endif
      elif (m[0]=='0'): # if cts drops drop rts and dr
         setFile(iam + 'dr.txt','0')
         setFile(iam + 'rts.txt','0')
      else:
         x = 1 # nop
      #endif
   #wend
   return(status)
#end send
   

def listenOnce(iams):
   """ stepped listener for time shattered transfer \n
       returns status and data if any
   """
   data = '' # default
   iam = iams + 'In'
   ans = 0
   m = getStatus(iam)
   print('Listen status is(' + m + ")")
   if ( m == '0000' ):
      setFile(iam + 'cts.txt','1')
   elif ( m == '1110'): # mailed 
      fin = open(iam+"data.txt",'r')
      fd = fin.readlines()
      fin.close()
      data = fd.__str__()
      # set status to 0000
      setFile(iam + 'cts.txt','0') # clear to send (receiver)
      setFile(iam + 'rts.txt','0') # request to send (sender)
      setFile(iam + 'dr.txt','0') # data ready (sender)
      setFile(iam + 'da.txt','0') # data acquired (receiver)
      # set status to 1000
      setFile(iam + 'cts.txt','1') # clear to send (receiver)
      setFile(iam + 'rts.txt','0') # request to send (sender)
      setFile(iam + 'dr.txt','0') # data ready (sender)
      setFile(iam + 'da.txt','0') # data acquired (receiver)
   elif ( m == '1101'):
      setFile(iam+'data.txt','')
   elif ( m == '1001'):
      setFile(iam+'cts.txt','0')
   elif ( m == '0001'):
      setFile(iam+'da.txt','0')
      ans = 1
   else:
      ans = 2
   #endif
   return(ans,data)
#end listenOnce

def listenStart(channelName,toc):
   """ listenStart is a rs232 agent \n
       rvc-cts==++++++++++++++===++++
       snd-rts====++++++++++===
       snd-data
       snd-dr =======+++++++====
       rcv-da =========+++++===
   """
   if toc == 0:
      ltoc = 50000 # forever
   else:
      ltoc = toc
   #end if
   iam = channelName + "In"
   c = 1
   while (c == 1) :
      a = listenOnce(channelName)
      if (len(a[1]) != 0):
         c = -1
      else:
         time.sleep(ltoc)
      #endif
   # wend
   return(a)
# end def lsiten start

def getStatus(iam):
   fhcts = open(iam + 'cts.txt','r')
   cts = fhcts.read()
   fhcts.close()
   fhrts = open(iam + 'rts.txt','r')
   rts = fhrts.read()
   fhrts.close()
   fhdr = open(iam + 'dr.txt','r')
   dr = fhdr.read()
   fhdr.close()
   fhda = open(iam + 'da.txt','r')
   da = fhda.read()
   fhda.close()
   print("status = [ch]" +'[' + iam + '](' + cts + rts + dr + da + ")")
   return(cts + rts + dr + da)
# end status
   
def looptill(inFile,valChr, maxCtr):
   """ loops till infile read has value returns ok/nok """
   i = 1
   c = 1
   while c == 1:
      i = i + 1
      if i == maxCtr :
         c = -1 # kill loop on max
      # end if
      # open infile
      fh = open(inFile,'r')
      # read contents
      ans = fh.read()
      # if contents = valchr end loop on -2
      if ans == valChr :
         c = -2
      else:
         fh.close()
         #---------------print ('bef sleep' )
         time.sleep(.2)
         #--------------print ('\n aft sleep')
      # end if
   # wend
   fh.close()
   # if good end ans = ok else nok
   if c == -2 :
      ans = 'ok'
   else:
      ans = 'nok'
   #end if
   return (ans)
# end def looptill
def registerChannel(channelName,linkChannel):  
   """ sets files in place """
   # import os # skipped PJA 11-3-13
   iam = channelName + "In"
   setFile(iam + 'cts.txt','0') # clear to send (receiver)
   setFile(iam + 'rts.txt','0') # request to send (sender)
   setFile(iam + 'data.txt','0') # data transfer file
   setFile(iam + 'dr.txt','0') # data ready (sender)
   setFile(iam + 'da.txt','0') # data acquired (receiver)
   setFile(iam + 'sts.txt','s') # status (sender/receiver)
   setFile(iam + '485Link.txt',linkChannel) # daisy chain 
   # os.chmod(iam+"*",0777) # open for read/write by anybody # skipped PJA 11-3-13
   # write blanks to channle output file
   # setFile('./out/' + channelName + '.txt','') # skipped PJA 11-3-13
# end def registerChannel
def setFile(fin,vval):
   """ sets file to vval """
   print('file is ' + fin + ' vval is ' + vval )
   fna = fin
   fh = open(fna,'w')
   fh.write(vval)
   fh.close()
   time.sleep(.01) # doevents
# end def setfile

def sniff(channel, ctr):
   """ displays status of rs232 files \n
       give channel, loop counter
   """
   lctr = ctr
   while lctr != 0:
      #
      lctr = lctr -1
      iam = channel + "In"
      cts = getFile(iam + "cts.txt")
      fh1rts = open(iam + "rts.txt",'r')
      rts = fh1rts.read()
      fh1rts.close()
      fh1dr = open(iam + "dr.txt",'r')
      dr = fh1dr.read()
      fh1dr.close()
      fh1da = open(iam + "da.txt",'r')
      da = fh1da.read()
      fh1da.close()
      fhLink = open(iam + '485Link.txt','r')
      Link = fhLink.read()
      fhLink.close()
      print ("(In(" + lctr.__str__() + "))" + cts + "." + rts + "." + dr + "." + da + "." + "Link==" + Link + "\n")
      time.sleep(.2)
   # wend
# end def
def send(channel,msg):
   """ send message if it can \n
       returns status
       
   """
   status = 0 # default
   mm = 100 # idle loop count
   iam = channel + "In"
   c = 1
   while (c==1):
      m = getStatus(iam)
      if (m=='1000'):
         setFile(iam + 'rts.txt','1')
      elif (m=='1100'):
         setFile(iam +"data.txt",msg)
         print('data sent to outfile (' + msg + ")")
         setFile(iam + 'dr.txt','1')
      elif (m=='1111'):
         setFile(iam + 'dr.txt','0')
      elif (m=='1101'):
         setFile(iam + 'rts.txt','0')
      elif (m=='0001'):
         c = 0 # break
      elif (m=='0000'):
         mm = mm -1
         if (mm == 0):
            c = -42 # break on idle timeount
         #endif
      elif (m=='1110'):
         mm = mm -1
         if (mm == 0):
            c = -46 # break on blocked timeount
         #endif
      elif (m=='1001'):
         mm = mm -1
         if (mm == 0):
            c = -48 # break on busy timeount
         #endif
      elif (m[0]=='0'): # if cts drops drop rts and dr
         setFile(iam + 'dr.txt','0')
         setFile(iam + 'rts.txt','0')
      else:
         x = 1 # nop
      #endif
   #wend
   return(c) # 
#end send
def sr485Node(To,msg2send,iam):
	""" lsitens and receeives on <iam> channel might send on Link (daisy chain)
	"""
	Lmsg2send = msg2send # local copy
	Link = getFile(iam + 'In485Link.txt')
	From = iam
	ctlB = 1
	while (ctlB == 1 ):
		if ( msg2send.__len__() == 0 ):
			stat,msgRcvd = listenOnce(iam)
			logg('stat=',stat)
			logg ('msg=',msgRcvd)
			if (stat == 2 ):
				ctlB = 1 # loop
			else:
				#get ToAddress 
				ToAddress,FromAddress,Data,Time = unpack(msgRcvd)
				logg('to=',ToAddress)
				if (ToAddress == iam):
					if (Data.__len__() != 0):
						ms = Data
						ctlB = -1 # break
					else:
						ctlB = 1 # loop
					#endif
				else: # not me = daisy
					logg('daisy Link=',Link)
					send(Link,pack(ToAddress,FromAddress,Data))
					ctlB = 1 # loop
				#endif
			#endif
		else: # msg to send
			msgOut = pack(To,iam,Lmsg2send)
			send(Link,msgOut)
			Lmsg2send = ''
			ctlB = 1 # loop
		#endif
	#wend
	return(ctlB,msgRcvd)
#end sr485Node
def getFile(fna):
	""" open read and close
	"""
	fhFna = open(fna,'r')
	ans = fhFna.read()
	fhFna.close()
	return(ans)
#end getFile
def pack(ToAddress,FromAddress,msg2send):
	""" pack to xml """
	ans = "<To>" + ToAddress + "</To>\n"
	ans = ans + "<From>" + FromAddress + "</From>\n"
	ans = ans + "<Msg>" + msg2send + "</Msg>\n"
	ans = ans + "<Time>" + time.asctime() + "</Time>"
	return(ans)
#end pack
def unpack(msg):
	""" xml msg """
	if (msg.__len__() ==0):
		To = "" 
	else:
		# get To
		fo = msg.find('<To>')
		fo = fo +4
		bo = msg.find('</To>')
		To = msg[fo:bo]
		# get From
		fo = msg.find('<From>')
		fo = fo +4
		bo = msg.find('</From>')
		From = msg[fo:bo]
		# get Msg
		fo = msg.find('<Msg>')
		fo = fo +4
		bo = msg.find('</Msg>')
		Msg = msg[fo:bo]
		# get Time
		fo = msg.find('<Time>')
		fo = fo +4
		bo = msg.find('</Time>')
		Time = msg[fo:bo]
		return(To,From,Msg,Time)
	#endif
#end unpack
	
	
    
"""
def test485(iam):
...
register 'master1 master2 master3' in a circle
...
msg2send = 'hello'
To = 'master1'
stat,msgdx = sr485node(To,msg2send,iam) 
"""
   
   
