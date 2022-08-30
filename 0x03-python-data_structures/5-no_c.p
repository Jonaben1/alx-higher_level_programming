#!/usr/bin/python3
def no_c(my_string):
    res = str(my_string)
    for i in range(res):
        if i == 'c' or i == 'C':
            res = res.pop(i)
        return res
