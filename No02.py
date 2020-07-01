from ctypes import *

#load the shared object file
forb  = CDLL('./forb.so')

#Find sum of integers
import time 
l=time.time()
forb.main()
g=time.time()
print(g-l)
