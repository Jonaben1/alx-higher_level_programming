#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    x = set(set_1)
    y = set(set_2)
    return x ^ y
