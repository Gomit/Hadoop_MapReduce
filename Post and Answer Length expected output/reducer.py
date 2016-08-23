#!/usr/bin/python
"""
Created on Sun Aug 21 18:52:42 2016

@author: merongoitom
"""

import csv, sys

def reducer(stdin):

    count=0
    tot_len=0
    oldKey=None
    oldQue=None
    
    for line in stdin:
        data = line.strip().split('\t')
        	 
        if len(data) != 3:
            continue

        thisKey,thisQue,thisAns=data
 
        if oldKey != None and oldKey != thisKey:
            avg_len=tot_len/float(count)
            print "{0}\t{1}\t{2}".format(oldKey,oldQue,avg_len)
            tot_len=0
            count=0
        	
        oldKey=thisKey
        oldQue=thisQue
        count+=1
        tot_len+=int(thisAns)
    
    if oldKey != None:
        avg_len=tot_len/float(count)
        print "{0}\t{1}\t{2}".format(oldKey,oldQue,avg_len)

if __name__ == "__main__":
    reducer(sys.stdin)
