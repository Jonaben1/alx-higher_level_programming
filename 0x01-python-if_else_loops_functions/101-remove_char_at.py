#!/usr/bin/python3
def remove_char_at(str, n):
    # Characters before the n-th indexed
    # is stored in a variable a

    a = str[: n]

    # Characters after the nth indexed
    # is stored in a variable b

    b = str[n + 1:]

    # Returning string after removing
    # nth indexed character.

    return (a + b)
