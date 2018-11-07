# file srRcvClass.py
# pja 11-5-13
#
import threading
class srRcv:
    """ sets up a sr232 receiver for given channel """
    def __init__(self,channel):
        """ -- """
        threading.Thread.__init__(self)
        self.channel = channel
        import sr232
        self.sr232 = sr232
    #end init
    def run(self):
        thread = self.sr232.listenStart(self.channel,5)
    #end run
#end Rev
