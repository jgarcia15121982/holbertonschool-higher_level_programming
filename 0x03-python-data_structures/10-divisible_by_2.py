#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result=[None] * len(my_list)
    for i in range(len(my_list)):
        list_result[i] =  bool(0) if (my_list[i] % 2 != 0) else bool(1)
    return list_result
