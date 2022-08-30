#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]
    if sentence == ' ':
        y = None
    return x, y
