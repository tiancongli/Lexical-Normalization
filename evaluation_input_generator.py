#coding=utf-8
"""
filter the data in labelled-tokens.txt, and output the data which is needed to be normalized.
"""

__author__ = "Tiancong Li"

from util import dict_set, remain_same

if __name__ == "__main__":
    ret = {}
    with open('labelled-tokens.txt') as f:
        for line in f:
            line = line.strip()
            token, label, correct_word = line.split()
            if label != 'OOV' or remain_same(token):
                continue
    
            ret[token] = correct_word
    
    for k, v in ret.items():
        print k, v

