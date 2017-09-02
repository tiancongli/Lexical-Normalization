#coding=utf-8

"""
This python file uses the output of evaluation_input_generator.py, and normalize the 
data. At the end, it compares the outputs with the labelled correct forms.
"""

__author__ = "Tiancong Li"

import time
from predict import generate_output
from util import *

precision = [0.0, 0.0]
recall = [0.0, 0.0]
accuracy = [0.0, 0.0]

now = time.time()
num = 0

with open('filtered_input.txt') as f:
    for line in f:
        line = line.strip()
        num += 1
        original, intended = line.split()

        # generate candidates
        candidates = generate_output(original)

        # print the log of the evaluation metrics
        input_set = start_dict.get(original[0], [])
        recall[1] += 1
        accuracy[1] += 1
        precision[1] += len(candidates)
        print "Set: %d" % len(input_set)
        print "Cans: %d" % len(candidates)
        print "Line: %d" % num 
        print "Misspelled Word: %s" % original
        print "Correct Word: %s" % intended
        if len(candidates) < 10:
            print "Candidates: %s" % str(candidates)
        if intended in candidates:
            print "match"
            precision[0] += 1
            recall[0] += 1
            if intended == list(candidates)[0]:
                accuracy[0] += 1
        else:
            print "not match"


        print "******************************************\n"


if precision[1]:
    print 'precision: %.4f%%, recall: %.4f%%, accu: %.4f%%' % (100 * precision[0]/precision[1], 100 * recall[0]/recall[1], 100 * accuracy[0]/accuracy[1])

print 'time used %.2f' % (time.time() - now)
