#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return None
    dic_list = list(a_dictionary.values())
    largest = dic_list[0]
    for v in a_dictionary.values():
        if v > largest:
            largest = v
    for k, v in a_dictionary.items():
        if v == largest:
            return k
