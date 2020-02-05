"""
file SioV.py
pja 02-04-2020

interface for SioiClass to basii

Sioi(self):
Sioo(self):
setiox(self,ioxin):
getiox(self)
setSStr(self,strin):
getSStr(self):
Still(self,targetCH):
Stillor(self,targetCHS):
Swhite(self):
Sctill(self,targetCH):
Sctillor(self,targetCHS):
Sword(self):
Spback(self,struct):


tn = p['sy']['pop']()
p['sy']['push']( str )
p['sy']['push'](p['OK']) 
"""
def main(p):
    import SioiClass
    p['sy']['SIO'] = SioiClass.Sio()
    p['sy']['Sioi']= Sioi 
    p['help']['Sioi']= "(str,,ch) ch at iox "
    p['sy']['Sioo']= Sioo 
    p['help']['Sioi']= "( ,, ) resets iox-- "
    p['sy']['setiox']= setiox 
    p['help']['setiox']= "( #,, ) inserts iox "
    p['sy']['getiox']= getiox 
    p['help']['getiox']= "( ,,# ) reterives iox "
    p['sy']['getSStr']= getSStr 
    p['help']['getSStr']= "( ,, str)reterives working string "
    p['sy']['setSStr']= setSStr 
    p['help']['setSStr']= "( str ,, ) sets working str "
    
    p['sy']['Sword']= Sword 
    p['help']['Sword']= "(,,[s]) word from working string "
    p['sy']['Spback']= Spback 
    p['help']['Spback']= "([s],,) adjusts working string "
    return(p)
# 

def Sioo(p):
    p['sy']['SIO'].Sioo()
    p['sy']['push'](p['OK'])
# 
def Sioi(p):
    ans = p['sy']['SIO'].Sioi()
    p['sy']['push']( ans )
    p['sy']['push'](p['OK'])
#
def setiox(p):
    ioxin = p['sy']['pop']()
    p['sy']['SIO'].setiox(int(ioxin))
    p['sy']['push'](p['OK'])
#
def getiox(p):
    ans = p['sy']['SIO'].getiox()
    p['sy']['push']( ans.__str__() )
    p['sy']['push'](p['OK'])
#

def setSStr(p):
    SStr = p['sy']['pop']()
    # set iox to 0
    p['sy']['SIO'].iox = 0
    p['sy']['SIO'].setSStr(SStr)
    p['sy']['push'](p['OK'])
#
def getSStr(p):
    ans = p['sy']['SIO'].getSStr()
    p['sy']['push']( ans )
    p['sy']['push'](p['OK'])
#
def Sword(p):
    ans = p['sy']['SIO'].Sword()
    p['sy']['push']( ans )
    p['sy']['push'](p['OK'])
#
"""
Spback(self,struct):"""
def Spback(p):
    Strct = p['sy']['pop']()
    p['sy']['SIO'].Spback(Strct)
    p['sy']['push'](p['OK'])
#
    