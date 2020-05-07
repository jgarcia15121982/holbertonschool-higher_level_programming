#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    list_b = set(my_list)
    for i in list_b:
        sum = sum + i
    return sum
