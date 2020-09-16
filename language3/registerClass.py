"""
register class
test as 

import registerClass
r1 = registerClass.register(number)

usage: with RegisterManager
getRegister, putRegister, initRegisterManager
getRegisterChain, putRegisterChain

"""
class register:
    def __init__(self,rn):
        self.at = {}
        self.at['registerNumber'] = rn
        self.at['isString'] = 0 #initially no
        self.at['isNumber'] = 0
        self.at['isString'] = 0
        self.at['isLabel'] = 0
        self.at['isArray'] = 0
        self.at['hasUrinaryMinus'] = 0
        self.at['contents'] = 0
    #
#end register class

