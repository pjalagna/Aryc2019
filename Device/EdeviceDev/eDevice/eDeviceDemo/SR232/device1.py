# file device1.py
"""
pickup station for device1 info
"""

def dev1():
	import msr485 # transputer station
	# get info -- tested here as a getfile 
	fh = open('dev1.txt','r')
	dx = fh.readlines()
	fh.close
	if (dx.__len__() == 0 ):
		To,From,Msg,Time = msr485.unpack(dx)
		From = 'Dev1'
		msg2send = msr485.pack(To,From,Msg)
		stat,msgBack = msr485.sr485(To,Msg,'Dev1')