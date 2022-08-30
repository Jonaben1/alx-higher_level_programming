#!/usr/bin/python3
def no_c(my_string):
    res = str(my_string)
    for i in res:
        if i == 'c' or i == 'C':
            continue
        return i
