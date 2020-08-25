import os
arr = os.listdir(".")
print("Current dir")
print(os.getcwd())
print("Current dir listing")
print(arr)

import sys
print("program arguments")
print(sys.argv)

from extfunc import *

otherfunction("test")
