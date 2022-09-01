#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = {keys: val for keys, val in a_dictionary.items() if key != key}
    return new_dict
