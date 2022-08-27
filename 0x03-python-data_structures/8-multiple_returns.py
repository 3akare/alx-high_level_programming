#!/usr/bin/python3
def multiple_returns(sentence):
    Len = len(sentence)
    First = sentence[:1]
    return Len, First

print(multiple_returns("Hello world"))