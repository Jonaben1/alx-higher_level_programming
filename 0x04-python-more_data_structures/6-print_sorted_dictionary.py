#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = {}
    sorted_keys = sorted(a_dictionary, key=a_dictionary.get)
    for w in sorted_keys:
        new[w] = a_dictionary[w]
    for key, value in new.items():
        print("{}: {}".format(key, value))
