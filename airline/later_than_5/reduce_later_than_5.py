#!/usr/bin/env python

from operator import itemgetter
import sys

current_airport = None
not_late_count = 0.0
late_count = 0.0
airport = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # parse the input we got from mapper.py
    airport, stat = line.split('\t', 1)
    
    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: airport) before it is passed to the reducer
    if current_airport == airport:
        if stat == "not_late":
            not_late_count += 1
        elif stat == "late":
            late_count += 1
        else:
            continue
    else:
        if current_airport:
            # write result to STDOUT
            print '%s\t%.2f%%' % (current_airport, late_count/(not_late_count + late_count)*100)
        if stat == "not_late":
            not_late_count, late_count = 1.0, 0.0
        elif stat == "late":
            not_late_count, late_count = 0.0, 1.0
        current_airport = airport


# do not forget to output the last airport if needed!
if current_airport == airport:
    print '%s\t%.2f%%' % (current_airport, late_count/(not_late_count + late_count)*100)

