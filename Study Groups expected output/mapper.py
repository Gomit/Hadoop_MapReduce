#!/usr/bin/python

"""
Created on Mon Jan 18 17:02:43 2016

@author: merongoitom
"""

import sys, csv
reader = csv.reader(sys.stdin, delimiter='\t')

def mapper(stdin):
    for line in reader:
 
        node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score = line[0:10]
        
        if node_type == "question":
            print "{0}\t{1}".format(node_id,author_id)
        else:
            print "{0}\t{1}".format(abs_parent_id,author_id)
 
if __name__ == "__main__":
    mapper(sys.stdin)
