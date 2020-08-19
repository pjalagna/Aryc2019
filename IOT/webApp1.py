#python webApp1.py
import urllib
import time
def agent():
    """
    polls web site for changes
    to mox.txt
    """
    # get current state
    link = "https://aryc.000webhostapp.com/IOT/mox.txt"
    f = urllib.urlopen(link)
#==== read
    myfile = f.read()
    f.close()
    time.sleep(10)
    # get after sleep
    link = "https://aryc.000webhostapp.com/IOT/mox.txt"
    f = urllib.urlopen(link)
    amyfile = f.read()
    if (amyfile <> myfile):
        print("changed")
        print(amyfile)
    #endif
#end agent



