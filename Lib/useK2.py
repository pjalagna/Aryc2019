"""#file useK2.py
usage: copy Lib
import first
sets up use of ..K2 files
"""
import os
M = os.getcwd() # my path
os.chdir('/Users/PJA/GitHub/Aryc/KR-graph/KR2') 
D = os.getcwd() # lib path 
import sys
sys.path.append(D)
os.chdir(M) # back into my own directory
