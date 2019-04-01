import fileinput
import glob
import string, sys

# print(type(fileinput.input(glob.glob("data/data01.txt"))))
print(fileinput.input(glob.glob("data/data01.txt")))

"""
for line in fileinput.input(glob.glob("data/data01.txt")):
	print(line)
	print(type(line))
    if fileinput.isfirstline(): # first in a file?
        sys.stderr.write("-- reading %s --\n" % fileinput.filename())
    sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))

"""
