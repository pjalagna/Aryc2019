class strnum() :
# lud 1/31/2013 changed str2num from int to float
	def str2num(self, inum) :
                # convert
                ans = float(inum)
		return( ans )                                                           
	# end str2num

	def num2str(self, inss) :
	   resp = inss.__str__()
	   return (resp)
	# end num2str
# end class strnum
