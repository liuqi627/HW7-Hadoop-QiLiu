#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    dep_airport = words[3].strip('"')
    crs_dep_time = words[9].strip('"')
    dep_time = words[10].strip('"')
    delay = 0
    
    try:
        delay = int(dep_time) - int(crs_dep_time)
    except ValueError:
        pass
    if delay > 5:
        print '%s\t%s' % (dep_airport, "late")
    else:
        print '%s\t%s' % (dep_airport, "not_late")

