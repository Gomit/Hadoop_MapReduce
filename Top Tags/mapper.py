#!/usr/bin/python

"""
Created on Mon Jan 18 17:02:43 2016

@author: merongoitom
"""

import sys
import csv

def mapper(stdin):
    reader = csv.reader(stdin, delimiter='\t')
    # Skip header.
    reader.next()
    
    for line in reader:

        node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score = line[0:10]

        if node_type == "question":
            tag_names=tag_names.split()
            for key in tag_names:
                print "{0}\t{1}".format(key,1)

if __name__ == "__main__":
    mapper(sys.stdin)
