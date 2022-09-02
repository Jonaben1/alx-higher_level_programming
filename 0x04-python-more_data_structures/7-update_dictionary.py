#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new = {}
    for x in a_dictionary:
        if x == key:
            new.update(key = value)
        else:
            new.update(key = value)
    return new
