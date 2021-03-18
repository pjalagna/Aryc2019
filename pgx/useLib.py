"""#file useLib.py
usage: copy to each subdir
import first
sets up use of ..Lib files
"""
import os
M = os.getcwd() # my path
os.chdir('/Users/paul/Documents/GitHub/Aryc2019/Lib/') 
D = os.getcwd() # lib path 
import sys
sys.path.append(D)
os.chdir(M) # back into my own directory

