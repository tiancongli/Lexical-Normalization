#coding=utf-8

"""
This python file is the main entrance of the system. If the user gives an input, the program will
return the corresponding normalized word. Otherwise, if there is no input, the program will process the data in unlabelled-tokens.txt.  
"""

__author__ = "Tiancong Li"

import sys
from predict import generate_output
from util import *

label_dict = {line.split()[0].strip(): line.split()[2].strip() for line in open('labelled-tokens.txt')}
count = 0

if len(sys.argv) == 2:
    token = sys.argv[1].strip()
    print "the output is: " + list(generate_output(token))[0]
else:
    with open('unlabelled-tokens.txt') as f:
        for line in f:
            count += 1
            word = line.split()[0].strip()
            if remain_same(word):
                result = word
            elif word in label_dict:
                result = label_dict[word]
            else:
                result = list(generate_output(word))[0]
    
            print "%d,%s" % (count, result)

