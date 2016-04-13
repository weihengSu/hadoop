#!/usr/bin/python
from operator import itemgetter
import sys
import math
import operator


worstSystems = dict()

for line in sys.stdin:
    line = line.strip()
    words = line.split("\t") 
    tempDifference = words[0]
    system = words[1]
    if (system in worstSystems):
	worstSystems[system] += int(tempDifference)
    else:
	worstSystems[system] = int(tempDifference)

sorted_system = sorted(worstSystems.items(), key=operator.itemgetter(1))

i = 0
for tuple in sorted_system:
#    if i in range(0,5):
    print '%s\t%s' % (tuple[0],tuple[1])
