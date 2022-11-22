import json
import sys

# This is a toy Python script that reads in a text file
# and outputs everything in upper case to a new file, called
# upper.txt

file_name = sys.argv[1]
fd = open(file_name)
out_fd = open("upper.txt", "w")
for line in fd:
    out_fd.write(line.upper())

fd.close()
out_fd.close()