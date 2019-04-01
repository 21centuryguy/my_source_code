import fileinput
import sys

for line in fileinput.input("data/data01.txt"):
    sys.stdout.write("-> ")
    sys.stdout.write(line)
