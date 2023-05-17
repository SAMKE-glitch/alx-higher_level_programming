#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = set(my_list)
    total_sum = 0
    for i in new_list:
        total_sum += i
    return total_sum
