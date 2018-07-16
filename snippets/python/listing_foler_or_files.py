######################################
import os
os.listdir("somedirectory")

######################################

import glob
txtfiles = []
for file in glob.glob("*.txt"):
    txtfiles.append(file)
    
######################################

import os.path
listOfFiles = [f for f in os.listdir() if os.path.isfile(f)]
print(listOfFiles)

> output

['a simple game.py', 'data.txt', 'decorator.py']


######################################

import pathlib

>>> flist = []
>>> for p in pathlib.Path('.').iterdir():
...  if p.is_file():
...   print(p)
...   flist.append(p)
...
error.PNG
exemaker.bat
guiprova.mp3
setup.py
speak_gui2.py
thumb.PNG

######################################
### get all file list from all sub folder

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

######################################

