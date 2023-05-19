#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        upper = 0
        lower = 0
        for i in my_list:
            upper += (i[0] * i[1])
            lower += (i[1])
        return (upper/lower)
    return 0
