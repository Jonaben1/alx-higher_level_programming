#!/bin/bash/python3
"""
Define a peak-finding algorithm
"""


def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integer
    """
    if list_of_integers == []:
        return None
    leng = len(list_of_integers)
    if leng == 1:
        return list_of_integers[0]
    elif leng == 2:
        return max(list_of_integers)
    mid = int(leng / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
