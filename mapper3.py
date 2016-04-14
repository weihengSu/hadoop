#!/usr/bin/python
import sys
import math


for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    list = ["9","10","11","12","13","14","15","16"]
    try:
        target = words[1]
        if (target[0] in list or target[0:2] in list):
          #  if (int(words[1][0:1]) > 9):
            actualTemp = words[3]
            time = words[1]
            print '%s\t%s\t%s' % (time, actualTemp,words[6]) 
    except ValueError:
        continue
 #   tempDifference = int(math.fabs(targetTemp - actualTemp))
 #   print '%s\t%s\t%s' % (tempDifference, words[6]) 
