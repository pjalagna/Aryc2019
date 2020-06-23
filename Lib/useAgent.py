"""#file useAgent.py
usage: keep in lib
import useLib then
import useAgent

sets up use of ..Agent files
"""
import os
M = os.getcwd() # my path
os.chdir('/Users/PJA/GitHub/Aryc/Agent/') 
D = os.getcwd() # lib path 
import sys
sys.path.append(D)
os.chdir(M) # back into my own directory

