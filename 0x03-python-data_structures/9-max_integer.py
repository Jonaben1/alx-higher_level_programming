#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = my_list[0]
    for num in my_list:
        if my_list == []:
            return None
        elif num > biggest:
            biggest = num
    return biggest
