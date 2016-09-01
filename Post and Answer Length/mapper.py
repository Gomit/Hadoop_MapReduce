#!/usr/bin/python

"""
Created on Mon Jan 18 17:02:43 2016

@author: merongoitom
"""

import csv, sys


def mapper(stdin):
    reader = csv.reader(stdin, delimiter='\t')
    reader.next()
    
    question={}
    answer={}

    for line in reader:

        node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score = line[0:10]
            
        body_len=len(body)
        question_id=str(abs_parent_id)
    	
        #Inser {key:value} pairs into 'question' and 'answer'
        if node_type=="question":
            question[node_id]=body_len
        elif node_type=="answer":
            if not question_id in answer:
                answer[question_id]=[body_len]
            else:
                answer[question_id].append(body_len)
    
    for key in question:
        if not key in answer:
            print "{0}\t{1}\t{2}".format(int(key),int(question[key]),"0")
        else:
            for value in answer[key]:
                print "{0}\t{1}\t{2}".format(int(key),int(question[key]),int(value))

if __name__ == "__main__":
    mapper(sys.stdin)
