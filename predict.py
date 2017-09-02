#coding=utf-8

"""
This python file contains the main function of predicting the normalized forms of tokens.
"""

__author__ = "Tiancong Li"

from algorithms import *
from util import *

candidates = None

def combination(token):
    """
    The combination of normalization methods, which is made up of Soundex, edit distance,
    and ngram. Users could change the combination to see different outputs.
    """
    # get the dictionary subset which starts with the same letter as the token
    input_set = start_dict.get(token[0], [])
    # normalizing
    candidates_sound = calc_soundex(token, 5, source=input_set) 
    candidates = calc_distance_by_thres(token, 1, _type=LEVEN, source=input_set)
    candidates = candidates| candidates_sound
    candidates = calc_distance_by_thres(token, 0.5, _type=NGRAM, source=candidates)
    return candidates

    
def generate_output(original):
    """
    original: the original token input

    Return
    candidates: the predicted candidates of the input
    """
    # change the data before normalizatin
    token = change_before_norm(original)
    # normalization
    candidates = combination(token)

    if not candidates:
        # if no output is produced, make some changes to the token
        token = change_after_norm(token)
        # normalization
        candidates = combination(token)

    if len(candidates) > 1:
        # if multiple outputs, reduce them by ngram
        candidates = calc_distance_by_thres(token, 0.7, _type=NGRAM, source=candidates)

    if not candidates:
        # if no outputs, use the original token as output, with a little change
        token = original
        if token.endswith("in"):
            token = token + "g"
        candidates = set([token])

    return candidates


