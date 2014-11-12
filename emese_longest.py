#!/usr/bin/python

import sys
import numpy as np

try:
	file = sys.argv[1]
except:
	file = raw_input("Introduce *.seq file: ")

data = open(file).readlines()

full_list = []
out_dict = {}

out = open(file + ".out", "w")

for line in data:
	line = line.split(";")
	nrep = int(line[1])
	if nrep > 0:
		while nrep > 0:
			motif = line[3*nrep]
			repetitions = int(line[(3*nrep)+2])
			full_list.append(repetitions)
			look = motif in out_dict
			if look == True:
				out_dict[motif].append(repetitions)
			elif look == False:
				out_dict[motif] = [repetitions]
			nrep -= 1

maximum = max(full_list)

header = ["len_motif\tmotif"] 
for n in range(1,maximum+1):
	header.append(str(n))
header.append("\n")
out.write("\t".join(header))

for el in out_dict:
	histo = np.histogram(out_dict[el], bins=range(1,maximum+2))
	li = histo[0]
	li.tolist()
	out.write(str(len(el)) + "\t" + el + "\t" + "\t".join("%s" % num for num in li) + "\n")

out.close()
