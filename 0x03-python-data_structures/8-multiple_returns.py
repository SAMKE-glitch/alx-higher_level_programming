#!/usr/bin/python3

def multiple_returns(sentence):
    for i in sentence:
        return len(sentence), sentence[0]
