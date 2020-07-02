"""#file usePgx.py
sets up use of ..pgx files
mainly pbox
"""
import os
M = os.getcwd() # my path
os.chdir('/Users/PJA/GitHub/Aryc/pgx') 
D = os.getcwd() # lib path 
import sys
sys.path.append(D)
os.chdir(M) # back into my own directory

