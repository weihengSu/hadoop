#!/usr/bin/python
from operator import itemgetter
import sys
import math
import operator

worstBuildings = dict()



for line in sys.stdin:
    line = line.strip()
    words = line.split("\t") 
    tempDifference = words[0]
    building = words[1]
    if (building in worstBuildings):
	worstBuildings[building] += int(tempDifference)
    else:
	worstBuildings[building] = int(tempDifference)

sorted_buildings = sorted(worstBuildings.items(), key=operator.itemgetter(1))
i = 0

for tuple in sorted_buildings:
    print '%s\t%s' % (tuple[0],tuple[1])
 
