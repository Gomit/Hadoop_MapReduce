#!/usr/bin/python

import sys

def reducer(reader):
    hour_count=[0]*24
    oldkey=None

    for line in sys.stdin:
        data=line.strip().split('\t')

        if len(data) != 2:
            continue

        thiskey,thisHour = data

        if oldkey != None and oldkey != thiskey:
            for hour,count in enumerate(hour_count):
                if count==max(hour_count):
                    print "{0}\t{1}".format(oldkey,hour)
            hour_count=[0]*24

        hour_count[int(thisHour)]+=1
        oldkey = thiskey

    if oldkey != None:
        for hour,count in enumerate(hour_count):
            if count==max(hour_count):
                print "{0}\t{1}".format(oldkey,hour)

if __name__ == "__main__":
    reducer(sys.stdin)
