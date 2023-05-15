#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        character = sentence[0]
    else:
        character = None
    return (len(sentence), character)
