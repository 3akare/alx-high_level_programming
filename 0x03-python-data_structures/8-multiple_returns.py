#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    Len = len(sentence)
    First = sentence[:1]
    return Len, First
