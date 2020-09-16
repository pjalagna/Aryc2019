"""#file useXS.py
usage: copy to each subdir
import first
sets up use of ..Ontology files
"""
import os
M = os.getcwd() # my path
os.chdir('/Users/PJA/GitHub/Aryc/XMLParse') 
D = os.getcwd() # lib path 
import sys
sys.path.append(D)
os.chdir(M) # back into my own directory
