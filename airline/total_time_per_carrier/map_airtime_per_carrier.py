#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    carrier = words[1].strip('\"')
    airtime = words[-3]
    try:
        airtime_hr = round(float(airtime)/60, 2)
    except ValueError:
        continue
    print '%s\t%s' % (carrier, airtime_hr)

