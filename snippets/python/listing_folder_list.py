######################################

import os

os.listdir(path)

# For reference and more os functions look here:
# Python 2 docs: https://docs.python.org/2/library/os.html#os.listdir
# Python 3 docs: https://docs.python.org/3/library/os.html#os.listdir

######################################

import os

for filename in os.listdir("C:\\temp"):
    print  filename
    
######################################

import os

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

######################################
# For files in current working directory without specifying a path

# Python 2.7:
import os
os.listdir(os.getcwd())

# Python 3.x:
import os
os.listdir()

######################################

