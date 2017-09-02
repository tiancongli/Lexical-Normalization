#coding=utf-8

"""
This python file defines the functions which help to improve the perfomance of the system.
"""

__author__ = "Tiancong Li"

dictionary = [line.strip() for line in open('dict.txt').readlines()]
dict_set = set(dictionary)

start_dict = {}
for item in dictionary:
    s = item[0]
    if s not in start_dict:
        start_dict[s] = set([])
    start_dict[s].add(item)

def change_before_norm(token):
    """
    Make changes to token before the normalization
    """
    token = ''.join([token[i] for i in range(len(token)-2) if not (token[i+2] == token[i] and token[i+1]== token[i])]+[token[-2:]])
    token = token.replace("0", "o")
    token = token.replace("2", "to")
    token = token.replace("4", "for")
    token = token.replace("-", "")
    return token

def change_after_norm(token):
    """
    Make changes to token after the normalization
    """
    if token.endswith("in"):
        token = token + "g"
    token = token.replace("q", "g")
    if token.endswith("z"):
        token = token[:-1] + "s"
    if token.startswith("de"):
        token = "the" + token[2:] 

    return token

def remain_same(token):
    """
    The preprocessing part, which judge whether the token should be returned as its original form.
    """
    if token in dict_set or "__" in token or token.startswith('@') or token.startswith('#') or token.startswith('http'):
        return True
    return False







