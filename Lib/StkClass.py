class Stks() :
   """ Stack Class: actions ( push, pop, depth, swap, drop, dropx, dropn, spy, pick, .s dump trace) """
   # Stk Class 
   # =====================================================
   # 2/2/9	pja	original
   # 2/9/9 pja amended
   # 2/10/09 pja dropx
   # 2/10/09 pja trace switch
   # 2/10/09 pja added x.str2num 
   # =====================================================
   # supporting imports
   import StrnumClass
   x = StrnumClass.strnum()
   # variables
   sdata = [] # stack data strings
   scount= 0 # depth count
   sname = ""
   strace = 1 
   # actions
   # __init___
   def __init__(self, na):
      self.sdata = []
      self.scount = 0
      self.sname = na
      self.strace = 0 # default is off
   # sin
   def push(self, x) :
      if (self.strace == 1 ) :
          print ("trace=push.." + self.sname)
      self.sdata.append(x)
      self.scount = self.scount + 1
   # dup
   def dup(self):
      if (self.strace == 1 ) :
          print ("trace=dup.." + self.sname)
      m = self.pop()
      self.push(m)
      self.push(m)
   # sout
   def pop(self):
      if (self.strace == 1 ) :
          print ("trace=pop.." + self.sname)
      self.scount = self.scount - 1
      return(self.sdata.pop())
   # depth
   def depth(self):
      if (self.strace == 1 ) :
          print ("trace=depth.." + self.sname)
      return(self.scount)
   # swap
   def swap(self) :
       if (self.strace == 1 ) :
           print ("trace=swap.." + self.sname) 
       m = self.pop()
       v = self.pop()
       print ("test m=" + m + " v=" + v + "..")
       self.push(m)
       self.push(v)
   # drop
   def drop(self) :
       if (self.strace == 1 ) :
           print ("trace=drop.." + self.sname)
       m = self.pop()
   # dropx
   def dropx(self) :
       if (self.strace == 1 ) :
           print ("trace=dropx.." + self.sname)
       self.sdata = []
       self.scount = 0
   # dropn
   # spy
   def spy(self) :
         if (self.strace == 1 ) :
             print ("trace=spy.." + self.sname)
         return(self.sdata[0])
   # pick
   def pick(self):
       if (self.strace == 1 ) :
             print ("trace=pick.." + self.sname)
       # get number off stack
       m = self.pop()
       mi = self.x.str2num(m)
       print ('mi=',mi)
       # 0,1 mean dup
       if (mi == 0) :
          self.dup()
       elif (mi == 1):
          self.dup()
       else:
          # else tos-pick -> push
          dj = self.sdata[self.scount - mi]
          self.push(dj)
   # end def pick
       
   # dots #display to developer
   def dots(self) :
         return(self.sdata) 
   # dumps # xml dump to caller
   def dumps(self) :
       fc = 0
       ans = "<" + self.sname + ">"
       for sd in self.sdata :
          fc = fc +1
          ans = ans + '<Pos id="' + self.x.num2str(fc) + '">"' + sd + '"</Pos> '
       ans = ans + "</" + self.sname + ">"
       return (ans)
   # trace
   def trace(self, x) :
       strace = x # 0/1 1= on
# end class Stks