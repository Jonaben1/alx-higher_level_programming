#!/usr/bin/python3
def best_score(a_dictionary):
    a = [i for i in a_dictionary if i is not None]
    out = [None] * 3 if len(a) == 0 else max(a)
    return out
