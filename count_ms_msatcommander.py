#!/usr/bin/python

# It counts the number of repetition per motif found
# in a MsatCommander's output

import sys

try:
    file = sys.argv[1]
except:
    file = raw_input("Introduce MsatCommander\'s output: ")

data = open(file).readlines()

di = {}

for i in data[0:-2]:
    ms = i.split()
    if ms[1] != "No":
        ms = ms[1]
        ms = ms.split("^")
        look = ms[0] in di
        if look == True:
            di[ms[0]] += int(ms[1])
        else:
            di[ms[0]] = int(ms[1])

w = open(file + ".counts" ,"w")

for el in di:
    motif = el
    rep = str(di[motif])
    w.write("%s\t%s\n" % (motif, rep))
