#!/usr/bin/python

import sys, csv
reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

def mapper(stdin):
    for line in reader:
        
        node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score = line[0:10]

        hour=added_at[11:13]
        print "{0}\t{1}".format(author_id, hour)

if __name__ == "__main__":
    mapper(sys.stdin)
