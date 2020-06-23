#file pboxClass
class pbx:
     """
     doesn't work same instance of p{} in each
     
     """
     def __init__(self):
         import pbox
         self.px = pbox
         self.px.main('bmain')
         self.px.start()
    #
#