#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    new.update({n: 2 * a_dictionary[n] for n in a_dictionary.values()})
    return new
