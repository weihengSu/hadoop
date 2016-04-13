#!/usr/bin/python
import sys
import math

#targetTemp = 0
#actualTemp = 0
#tempDifference = 0
for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
#    print '%s\t%s' % (words[2],words[3])
    try:
        targetTemp = int(words[2])
        actualTemp = int(words[3])
    except ValueError:
        continue
    tempDifference = int(math.fabs(targetTemp - actualTemp))
#    if len(words) >=7:
#        targetTemp = int(words[2])
#        actualTemp = int(words[3])
#        tempDiff = math.fabs(targetTemp-actualTemp)
#        system = words[4]
    print '%d\t%s' % (tempDifference, words[4]) 
