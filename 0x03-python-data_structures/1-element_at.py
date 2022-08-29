#!/usr/bin/python3
def element_at(my_list, idx):
    new = list(my_list)
    for idx, y in enumerate(new):
        new[idx] = y
        if idx < len(my_list):
            return None
        if idx < 0:
            return None
        return new

