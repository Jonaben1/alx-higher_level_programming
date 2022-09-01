#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary.items(), key=lambda x: x[1])
    for key, value in new.items():
        print("{}: {}".format(key, value))
