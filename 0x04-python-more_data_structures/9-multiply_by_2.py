#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    new.update((x, y*2) for x, y in a_dictionary.items())
    for x, y in new.items():
        print("{}: {}".format(x, y))
