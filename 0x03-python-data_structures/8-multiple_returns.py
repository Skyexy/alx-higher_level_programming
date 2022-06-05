#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if n == 0:
        i = None
    else:
        i = sentence[0]
    return (n, i)
