#!/usr/bin/python
"""
Created on Sun Aug 21 18:52:42 2016

@author: merongoitom
"""
import sys, csv

def reducer(reader):

    tag_count = 0
    prev_tag = None
    top_10 = []

    for line in reader:
        data=line.strip().split('\t')
        if len(data) != 2:
            continue

        tag,count = data
        #if current_tag is None or tag != current_tag:
        #    if not current_tag is None:
        if prev_tag != None and prev_tag != tag:
            top_10 = add_record(prev_tag, tag_count, top_10)
            tag_count = 0
        
        prev_tag = tag
        tag_count+=int(count)

    top_10 = add_record(prev_tag, tag_count, top_10)
 
    for tag, tag_count in top_10:
       print "{0}\t{1}".format(tag, tag_count)

def add_record(tag, tag_count, top_10):
    """sort tags based on values"""
    if len(top_10) < 10 or tag_count > top_10[9][1]:
        top_10.append([tag, tag_count])
        top_10.sort(key=lambda k: k[1], reverse=True)
        top_10 = top_10[:10]
    return top_10

if __name__ == "__main__":
    reducer(sys.stdin)

