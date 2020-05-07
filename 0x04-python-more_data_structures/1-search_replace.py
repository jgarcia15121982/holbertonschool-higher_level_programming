#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_b = my_list.copy()
    for i in range(len(list_b)):
        if list_b[i] == search:
            list_b[i] = replace
    return list_b
