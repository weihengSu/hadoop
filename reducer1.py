#!/usr/bin/python
from operator import itemgetter
import sys
import math
import operator
#date = None
#time = None
#targetTemp = 0
#actualTemp = 0
#tempDifference = None
#system = None
#systemAge = None
#buildingId = None

#worstSystems = {}
worstSystems = dict()
#worstBuildings = dict()
#worstSystemLists = []
#worstBuildingLists = []


for line in sys.stdin:
    line = line.strip()
    words = line.split("\t") 
#    targetTemp = words[0]
#    actualTemp = words[1]
    tempDifference = words[0]
    system = words[1]


#    date = line[0]
#    time = line[1]
#    targetTemp = line[2]
#    actualTemp = line[3]
#    system = line[4]
#    systemAge = line[5]
#    buildingId = line[6]

#    try:
#        targetTemp = int(targetTemp)
#        actualTemp = int(actualTemp)
#        tempDifference = int(math.fabs(targetTemp-actualTemp))
#	actualTemp = int(actualTemp)
#    except ValueError:
#	continue



    if (system in worstSystems):
#	tempDifference = math.fabs(targetTemp - actualTemp)
	worstSystems[system] += int(tempDifference)
    else:
	worstSystems[system] = int(tempDifference)
#for system in worstSystems.keys():
#    sum_temp = sum(worstSystems[system])
#    worstSystems[system] = sum_temp
#    print '%s\t%s' % (tempDifference, syste)
 #   if (buildingId in worstBuildings.keys()):
#	tempDifference = math.fabs(targetTemp - actualTemp)
#	worstBuildings[buildingId] += tempDifference
 #   else:
#	worstBuildings[buildingId] = tempDifference
sorted_system = sorted(worstSystems.items(), key=operator.itemgetter(1))
#sorted_building = sorted(worstBuildings.items(), key=operator.itemgetter(1))
i = 0
#j = 0
for tuple in sorted_system:
#    if i in range(0,5):
    print '%s\t%s' % (tuple[0],tuple[1])
#    else:
#       break
#for tuple in sorted_building:
#    if j in range(0,5):
#	print(tuple)
#    else:
#	break			
#for key,value in worstSystems.iteritems():
#    print '%s\t%s' % (key,value) 
