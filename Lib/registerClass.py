"""
#file registerClass.py
# usage 
# import registerClass
manage an integer series

"""
#file registerClass.py
# usage 
# import registerClass
# r1 = registerClass.register()
# r1.plus()
# 
class register:
    def __init__(self):
        self.holder=0
    #init
    def set(self,num):
        self.holder = num
    #
    def get(self):
       return(self.holder)
    #
    def plus(self):
        self.holder = self.holder + 1
        return(self.holder)
    #
#end register class
        
        