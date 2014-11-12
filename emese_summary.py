#!/usr/bin/python
# in vim you must run this comands before run this script:
# :%s/\r/\r/g
# :%s/A\n;/A;/g
# :%s/C\n;/C;/g
# :%s/G\n;/G;/g
# :%s/T\n;/T;/g

file = raw_input("Emese' software seq file: ")

file = open(file).readlines()

dictio = {}

for line in file:

	line = line[:-1]
	line = line.split(";")
	for elem in range(0,len(line)-1):
		if elem%3 == 0 and elem > 1:
			look = line[elem] in dictio
			motif = line[elem]
			count = line[elem+2]
			if look == True:
				dictio[motif][1] +=  int(count)
				dictio[motif][2] +=  1
			elif look == False:
				dictio[motif] = [len(motif), int(count), 1]

out = open("output.txt", "w")

for cosa in dictio:
	len_motif = dictio[cosa][0]
	count = dictio[cosa][1]
	loci = dictio[cosa][2]

	out.write("%s\t%s\t%s\t%s\n" % (str(len_motif), cosa, str(count), str(loci)))

out.close()

