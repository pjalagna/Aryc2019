# file simpleStk.py
class Stk:
   def __init__(self):
      """ simple stack class simpleStk.Stk() --  push pop dots depth pick """
      self.ix = 0
      self.ar = []
   # end def
   def depth(self):
      ans = self.ar.__len__()
      return(ans)
   # end def
   def push(self,datum):
      self.ix = self.ix + 1
      self.ar.append( datum )
   # end def\
   def pop(self):
      ans = self.ar.pop()
      self.ix = self.ix - 1
      return(ans)
   # end def
   def dots(self):
      c = 0
      for i in self.ar:
         c = c + 1
         print("(",c,")=(",i,")")
      # end for
   # end def
   def pick(self):
      ix = int(self.pop())  * -1 # reverse pick from eos
      self.push( self.ar[ix])
   # end def pick
   def dump(self):
      """ returns XML string with contents of stack """
      import random
      id1 = random.randint(1,300)
      ans = "<Stack ID='" + id1.__str__() + "'> \n"
      ans += "    <StackVals> \n"
      c = 0
      for i in self.ar:
         c = c + 1
         ans += "    <Val ix='" + c.__str__() + "' Contents='" + i.__str__() + "'/> \n"
      # end for
      ans += "    </StackVals> \n"
      ans += "    <StackID ID='" + id1.__str__() + "'/> \n"
      ans += "</Stack>"
      return(ans)
   # end def
      
