#coding=utf-8

"""
This file contains the distance and similarity algorithms,
including edit distance, ngram and soundex.
"""

__author__ = "Tiancong Li"

import sys
import fuzzy
import editdistance
from ngram import NGram

from util import dictionary

GLOBAL = 0
LOCAL = 1
LEVEN = 2
NGRAM = 3

DISTANCE_SET = set([LEVEN])

def init_matrix(rows, colums):
    matrix = []
    for r in range(rows):
        matrix.append([])
        for c in range(colums):
            matrix[r].append(0)
    return matrix

def matrix_maxvalue(matrix):
    ret = 0
    for row in matrix:
        for colum in row:
            if colum > ret:
                ret = colum
    return ret

def calc_by_local_edit(word1, word2):
    """
    Calculate the local edit distance of two words
    """
    match = 1
    deletion = -1
    insertion = -1
    replace = -1

    word1_len = len(word1)
    word2_len = len(word2)

    matrix = init_matrix(word2_len + 1, word1_len + 1)

    for j in range(1, word2_len + 1):
        for k in range(1, word1_len + 1):
            matrix[j][k] = max(0, 
                    matrix[j][k-1] + deletion,
                    matrix[j-1][k] + insertion,
                    matrix[j-1][k-1] + (match if word1[k-1] == word2[j-1] else replace))
    return matrix_maxvalue(matrix)

def calc_by_global_edit(word1, word2):
    """
    Calculate the global edit distance of two words
    """
    match = 1
    deletion = -1
    insertion = -1
    replace = -1

    word1_len = len(word1)
    word2_len = len(word2)

    matrix = init_matrix(word2_len + 1, word1_len + 1)

    for j in range(1, word2_len + 1):
        matrix[j][0] = j * insertion
    for k in range(1, word1_len + 1):
        matrix[0][k] = k * deletion

    for j in range(1, word2_len + 1):
        for k in range(1, word1_len + 1):
            matrix[j][k] = max( 
                    matrix[j][k-1] + deletion,
                    matrix[j-1][k] + insertion,
                    matrix[j-1][k-1] + (match if word1[k-1] == word2[j-1] else replace))
    return matrix[word2_len][word1_len]


def calc_distance(string, _type=LEVEN, source=dictionary):
    """
    The main entrance of calculating the distance.
    string: the token needed to be processed.
    _type:  different algorithms like ngram, local distance, etc.
    source: the vocabulary set, which is used when process the token.
    """
    if len(source) == 1:
        return source
    ret = {}
    init_score = float('inf') if _type in DISTANCE_SET else 0
    if _type == LEVEN:
        edit_distance = editdistance.eval
    elif _type == GLOBAL:
        edit_distance = calc_by_global_edit
    elif _type == LOCAL:
        edit_distance = calc_by_local_edit
    else:
        edit_distance = NGram.compare
    for word in source:
        score = edit_distance(string, word)
        if score not in ret:
            ret[score] = []
        ret[score].append(word)
        if _type in DISTANCE_SET:
            if score < init_score:
                init_score = score
        else:
            if score > init_score:
                init_score = score
    candidates = ret.get(init_score, [])
    return set(candidates)


def calc_distance_by_thres(string, threshold, _type=LEVEN, source=dictionary):
    """
    An alternative of "calc_distance".
    By using this function, an threshold is given.
    The return candidates are the words within the threshold,
    instead of the ones with smallest distance.
    """
    if len(source) == 1:
        return source
    candidates = set([])
    if _type == LEVEN:
        edit_distance = editdistance.eval
    elif _type == GLOBAL:
        edit_distance = calc_by_global_edit
    elif _type == LOCAL:
        edit_distance = calc_by_local_edit
    else:
        edit_distance = NGram.compare
    for word in source:
        score = edit_distance(string, word)
        if _type in DISTANCE_SET:
            if score <= threshold:
                candidates.add(word)
        else:
            if score >= threshold:
                candidates.add(word)

    return candidates

def calc_soundex(string, length, source=dictionary):
    """
    Soundex method
    string: the token.
    length: the length which the algorithm will use when comparing tokens.
    source: vocabulary set.
    """
    candidates = set([])
    soundex = fuzzy.Soundex(length)
    standard = soundex(string)
    for word in source:
        if soundex(word) == standard:
            candidates.add(word)
    return candidates

