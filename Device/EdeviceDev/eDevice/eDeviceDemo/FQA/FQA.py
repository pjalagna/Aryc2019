def FQagent(loc,serviceBox):
    """ 
          pja 11-9-13 tested
          pja - 11-5-13
          File Queue Agent off of loc \n
          serviceBox is a pointer to the service.main
    """
    import os
    import time
    sleepLong = 10 # test = 10 real = 500
    sleepShort = 2 # 
    c = 1
    while (c==1):
        # get the list of files from iamin to ldir
        ldir = os.listdir(loc)
        # if len=0
        if(len(ldir) == 0): #-1
            ## sleep long
            print("sleepLong")
            time.sleep(sleepLong)
        else:
            #per rec == note single thread loop (spawn for bees)
            for f in range(len(ldir)):
                # open file
                fh = open(loc + ldir[f],'r')
                # readit
                li = fh.read() # all into string
                # close it
                fh.close()
                serviceBox(li)
                # delete file
                os.remove(loc + ldir[f])
            #endfor
            print('sleepShort')
            time.sleep(sleepShort)
        #endif - 1
    #wend
#end FQagent
