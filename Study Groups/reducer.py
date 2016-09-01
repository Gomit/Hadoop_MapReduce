#!/usr/bin/python
"""
Created on Sun Aug 21 18:52:42 2016

@author: merongoitom
"""
import sys, csv

def reducer(reader):

    oldKey = None
    IDs = []

    for line in reader:
        data = line.strip().split('\t')

        if len(data) != 2:
            continue

        thisKey, thisID = data

        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, IDs)
            IDs = []

        oldKey = thisKey
        IDs.append(thisID)

    if oldKey != None:
        print "{0}\t{1}".format(oldKey, IDs)

if __name__ == "__main__":
    reducer(sys.stdin)

