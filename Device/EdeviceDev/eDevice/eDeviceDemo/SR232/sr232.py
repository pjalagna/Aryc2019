# file sr232.py
# pja - 11-17-12 added #os.chmod to register. opens all files for read/write
#--- will this break on windows?
# pja 11-5 fixed for linux
#-- chmod
#-- write 
# pja 11-9-13 added channelName to iam
# ----------- redid register channel made channel subdir, eliminated out file
import time # sleep function
import os
def version():
   print("""
# pja - 11-17-12 added #os.chmod to register. opens all files for read/write
#--- will this break on windows?
# pja 11-5 fixed for linux
#-- chmod
#-- write 
# pja 11-9-13 added channelName to iam
# ----------- redid register channel made channel subdir, eliminated out file
pja 11-9-13 major rewrite
---- removed looptill - not implemented
---- removed 
         """)

def listenOnce(iam):
   """ stepped listener for time shattered transfer \n
       iam is location of device files
   """
   ans = 0
   m = getStatus(iam)
   print('m is(' + m + ")")
   if ( m == '0000' ):
      setFile(iam + '/cts.txt','1')
   elif ( m == '1110'):
      fin = open(iam+"/data.txt",'r')
      fd = fin.readlines()
      fin.close()
      fout = iam + '/in/c'+time.time().__str__()
      fout = fout.replace('.','x')
      fout = fout + '.txt'
      fh = open(fout,'w')
      fh.write(fd.__str__())
      fh.close()
      setFile(iam+'/da.txt','1')
   elif ( m == '1101'):
      setFile(iam+'/data.txt','')
   elif ( m == '1001'):
      setFile(iam+'/cts.txt','0')
   elif ( m == '0001'):
      setFile(iam+'/da.txt','0')
      ans = 1
   else:
      ans = 2
   #endif
   return(ans)
#end listenOnce

def listenStart(loc,toc):
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
   iam = loc
   c = 1
   while (c == 1) :
      a = listenOnce(iam)
      time.sleep(ltoc)
   # wend
# end def lsiten start

def getStatus(iam):
   fhcts = open(iam + '/cts.txt','r')
   cts = fhcts.read()
   fhcts.close()
   fhrts = open(iam + '/rts.txt','r')
   rts = fhrts.read()
   fhrts.close()
   fhdr = open(iam + '/dr.txt','r')
   dr = fhdr.read()
   fhdr.close()
   fhda = open(iam + '/da.txt','r')
   da = fhda.read()
   fhda.close()
   print("status = (" + cts + rts + dr + da + ")")
   return(cts + rts + dr + da)
# end status
   

def registerChannel(channelName):
   """ sets files in place """
   import os
   loc = os.getcwd() # this dir
   iam = loc + '/' + channelName + '/' 
   os.mkdir(iam)
   # go to iam
   os.chdir(iam)
   setFile(iam + 'cts.txt','0') # clear to send (receiver)
   #os.chmod(iam + 'cts.txt',777)
   setFile(iam + 'rts.txt','0') # request to send (sender)
   #os.chmod(iam + 'rts.txt',777)
   setFile(iam + 'data.txt','0') # data transfer file
   #os.chmod(iam + 'data.txt',777)
   setFile(iam + 'dr.txt','0') # data ready (sender)
   #os.chmod(iam + 'dr.txt',777)
   setFile(iam + 'da.txt','0') # data acquired (receiver)
   #os.chmod(iam + 'da.txt',777)
   setFile(iam + 'sts.txt','s') # status (sender/receiver)
   # create in folder
   os.mkdir(iam + 'In')
   # go to original loc
   os.chdir(loc)
   #os.chmod(iam + 'sts.txt',777)
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

def sniff(loc, ctr):
   """ displays status of rs232 files \n
       give channel, loop counter
   """
   lctr = ctr
   while lctr != 0:
      #
      lctr = lctr -1
      iam = loc
      fh1cts = open(iam + "/cts.txt",'r')
      cts = fh1cts.read()
      fh1cts.close()
      fh1rts = open(iam + "/rts.txt",'r')
      rts = fh1rts.read()
      fh1rts.close()
      fh1dr = open(iam + "/dr.txt",'r')
      dr = fh1dr.read()
      fh1dr.close()
      fh1da = open(iam + "/da.txt",'r')
      da = fh1da.read()
      fh1da.close()
      print ("(In(" + lctr.__str__() + "))" + cts + "." + rts + "." + dr + "." + da + "." + "\n")
      time.sleep(.2)
   # wend
# end def

def send(loc,msg):
   mm = 100 # idle loop count
   iam = loc
   c = 1
   while (c==1):
      m = getStatus(iam)
      if (m=='1000'):
         setFile(iam + '/rts.txt','1')
      elif (m=='1100'):
         omsg = '\n\n<t>' + time.asctime() + '</t> \n <msg>' + msg + "</msg>"
         setFile(iam +"/data.txt",omsg)
         print('data sent to outfile (' + omsg + ")")
         setFile(iam + '/dr.txt','1')
      elif (m=='1111'):
         setFile(iam + '/dr.txt','0')
      elif (m=='1101'):
         setFile(iam + '/rts.txt','0')
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
         setFile(iam + '/dr.txt','0')
         setFile(iam + '/rts.txt','0')
      else:
         x = 1 # nop
      #endif
   #wend
#end send
   
   
