class strnum() :
	def str2num(self, inum) :
	# converts string to num
		ans = 0
		ctl = 0
		for m in inum : # msd first
		   # print ('m=',m)
		   # process while a number
		   if (m=='1') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 1
		   elif (m == '2') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 2 
		   elif (m == '3') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 3
		   elif (m == '4') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 4
		   elif (m == '5') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 5
		   elif (m == '6') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 6
		   elif (m == '7') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 7
		   elif (m == '8') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 8
		   elif (m == '9') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 9
		   elif (m == '0') :
		      ctl = ctl + 1
		      ans = (ans * 10) + 0
		   else:
		      ctl = 0
		# print ("ans=",ans ) 
		return( ans )                                                           
	# end str2num

	def num2str(self, inss) :
	   resp = inss.__str__()
	   return (resp)
	# end num2str
# end class strnum
