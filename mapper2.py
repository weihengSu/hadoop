#!/usr/bin/python
import sys
import math


for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    try:
        targetTemp = int(words[2])
        actualTemp = int(words[3])
    except ValueError:
        continue
    tempDifference = int(math.fabs(targetTemp - actualTemp))
    print '%d\t%s' % (tempDifference, words[6]) 
