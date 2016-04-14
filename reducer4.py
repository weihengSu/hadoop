#!/usr/bin/python
from operator import itemgetter
import sys
import math
import operator
import collections
worstBuildings = {}
#timePointsForEachBuilding = {}


for line in sys.stdin:
    line = line.strip()
    words = line.split("\t") 
    time = words[0]
    temp = words[1]
    building = words[2]
    if (building in worstBuildings):
	worstBuildings[building][0] += int(temp)
        timePoint = (time, temp)
        worstBuildings[building].append(timePoint)
    else:
	worstBuildings.setdefault(building,[]).append(int(temp))

sorted_buildings = sorted(worstBuildings.items(), key=operator.itemgetter(1))
#i = 0

b = worstBuildings.items()
b.sort(key = itemgetter(1), reverse=True)

#print b
for tuple in b:
    print '%s\t%s' % (tuple[0],tuple[1])
#    print(tuple) 
#print(sorted_buildings)



