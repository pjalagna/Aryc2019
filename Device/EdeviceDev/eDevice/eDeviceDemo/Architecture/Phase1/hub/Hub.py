# file Hub.py
# pja 11-9-13 added <channelName>service.py as called file
#------------ added /in<channelName>/ as input area name
def main(channelName):
    """  pja 11-5-13
         Hub calls File Queue Agent off of <here>/in \n
        for demo proc is fixed otherwise it would be moose
        thread needs one argument so (nop)
    """
    import os
    service = __import__(channelName +  "serviceBox")
    serviceBox = service.main # no parens
    iam = os.getcwd()
    loc = iam + '/' + channelName + '/In/'
    import FQA
    FQA.FQagent(loc,serviceBox)
#end main


                
            
        
    
