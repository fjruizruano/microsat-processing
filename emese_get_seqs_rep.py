#!/usr/bin/python

import sys

data = open(sys.argv[1]).readlines()
out = open(sys.argv[1]+".list","w")

for line in data:
	name = ""
	line = line.split(";")
	if int(line[1]) > 0:
		name = name + line[0] 
		for num in range(0,int(line[1])):
			name = name + "_" + line[3+(3*num)] + "-" + line[3+(3*num)+2]
		out.write(name+"\n")
out.close()
