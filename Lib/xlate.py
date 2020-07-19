"""
file xlate.py
pja 7/18/2020
establishes a translation array
usage 
import xlate
a = xlate.setx()
a.x("a",'hay')
a.r('a')==> 'hay'
a.r('hay')==>'a'
"""
class setx:
    def __init__(self):
        self.arx = {}
    #
    def x(self,a,b):
        self.arx[a] = b
        self.arx[b] = a
    #
    def r(self,op):
        return(self.arx[op])
    #
#end xlate
